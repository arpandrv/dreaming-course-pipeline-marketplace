#!/usr/bin/env python3
"""Check and optionally install the Dreaming Course Pipeline Python packages."""

from __future__ import annotations

import argparse
import importlib.util
from importlib import metadata
import json
import platform
import subprocess
import sys
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Dependency:
    package: str
    import_name: str
    purpose: str
    windows_only: bool = False
    minimum_major: int | None = None


DEPENDENCIES = (
    Dependency("python-pptx", "pptx", "Read PowerPoint files, extract notes, and build the final deck"),
    Dependency("lxml", "lxml", "Parse and validate Office Open XML"),
    Dependency("pywin32", "win32com", "Export PowerPoint through locally installed Microsoft PowerPoint", True),
    Dependency("PyMuPDF", "fitz", "Render PDF pages to images and inspect PDFs"),
    Dependency("Pillow", "PIL", "Inspect, resize, and composite images"),
    Dependency("numpy", "numpy", "Perform image-array checks"),
    Dependency("opencv-python", "cv2", "Preprocess images and run visual QA"),
    Dependency("paddleocr", "paddleocr", "OCR scanned pages and generated slide images"),
    Dependency("paddlepaddle>=3.0", "paddle", "Run PaddleOCR models", minimum_major=3),
    Dependency("python-docx", "docx", "Extract DOCX text and structure"),
    Dependency("openpyxl", "openpyxl", "Read Excel workbooks"),
    Dependency("pandas", "pandas", "Normalize and inspect tabular source data"),
    Dependency("beautifulsoup4", "bs4", "Parse HTML source documents"),
    Dependency("trafilatura", "trafilatura", "Extract clean main text from HTML"),
)


def applicable_dependencies() -> list[Dependency]:
    is_windows = platform.system() == "Windows"
    return [item for item in DEPENDENCIES if not item.windows_only or is_windows]


def is_available(import_name: str) -> bool:
    try:
        return importlib.util.find_spec(import_name) is not None
    except (ImportError, ModuleNotFoundError, ValueError):
        return False


def inspect() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for dependency in applicable_dependencies():
        result = asdict(dependency)
        result["installed"] = is_available(dependency.import_name)
        try:
            distribution_name = dependency.package.split(">=", 1)[0]
            result["version"] = metadata.version(distribution_name) if result["installed"] else None
        except metadata.PackageNotFoundError:
            result["version"] = None
        if result["installed"] and dependency.minimum_major is not None:
            try:
                installed_major = int(str(result["version"]).split(".", 1)[0])
                result["installed"] = installed_major >= dependency.minimum_major
            except (TypeError, ValueError):
                result["installed"] = False
        results.append(result)
    return results


def install(packages: list[str]) -> None:
    subprocess.run(
        [sys.executable, "-m", "pip", "install", *packages],
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--install-missing",
        action="store_true",
        help="Install only packages whose import cannot be found, then verify again.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    before = inspect()
    missing = [str(item["package"]) for item in before if not item["installed"]]

    install_error = None
    if args.install_missing and missing:
        try:
            install(missing)
        except subprocess.CalledProcessError as exc:
            install_error = f"pip exited with code {exc.returncode}"

    after = inspect()
    remaining = [str(item["package"]) for item in after if not item["installed"]]
    payload = {
        "python_executable": sys.executable,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "attempted_install": bool(args.install_missing and missing),
        "initially_missing": missing,
        "install_error": install_error,
        "dependencies": after,
        "remaining_missing": remaining,
        "ok": not remaining and install_error is None,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"Python: {payload['python_executable']} ({payload['python_version']})")
        for item in after:
            status = "OK" if item["installed"] else "MISSING"
            version = f" {item['version']}" if item["version"] else ""
            print(f"[{status}] {item['package']}{version}: {item['purpose']}")
        if install_error:
            print(f"Install error: {install_error}", file=sys.stderr)

    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
