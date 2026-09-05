---
name: dreaming-course-preflight
description: Verify or install Python and the complete local dependency stack before starting a new Dreaming Course Pipeline project, then hand verified execution to project setup.
---

# Stage 0 - Verify Runtime and Dependencies

Read `../../references/pipeline-contract.md` and `../../references/execution-permissions.md` completely before acting.

## Find or install Python

Do not create or modify the professor's project yet.

1. Prefer the Codex bundled workspace Python as a base interpreter when its dependency-path facility is available.
2. Otherwise locate a working Python 3 interpreter using platform-appropriate commands: `py -3` or `python` on Windows, and `python3` on macOS/Linux.
3. Verify the base interpreter with a harmless version command and record its absolute executable path and version.
4. If no usable Python 3 interpreter exists, install Python for the current user with the platform's standard package manager when available. Request outside-sandbox execution and required network/package-install access through the normal Codex permission mechanism; do not substitute a textual confirmation loop. On Windows, prefer the current-user Python 3.12 package through `winget`. On macOS, prefer an existing package manager such as Homebrew and Python 3.12; do not install Homebrew itself implicitly. Re-discover and verify Python after installation.
5. If automatic installation is unavailable or fails, stop with the exact attempted method and error. Do not start Stage 1.

## Select the pipeline environment

Do not install packages into Codex's bundled runtime or mutate another managed Python installation. Use a dedicated reusable virtual environment for the pipeline:

- Windows: `%LOCALAPPDATA%\DreamingCoursePipeline\venv`
- macOS/Linux: `${XDG_CACHE_HOME:-~/.cache}/dreaming-course-pipeline/venv`

If its Python executable already exists, verify and reuse it. Otherwise request outside-sandbox execution when the target path is outside the writable workspace, create the directory's parent, and run `<base-python> -m venv <venv-path>`. If the chosen base interpreter cannot create a venv, try another discovered Python interpreter before treating it as a Python-install blocker. From this point forward, `<python>` means the virtual environment's Python executable. Record both the base and pipeline interpreter paths.

## Verify and install the package set

Verify that `<python> -m pip --version` succeeds. If Python exists but pip does not, run `<python> -m ensurepip --upgrade`, then verify pip again. Resolve the bundled script relative to this `SKILL.md`, use its absolute path, and run:

```text
<python> <absolute-plugin-path>/scripts/check_dependencies.py --json
```

The authoritative package declaration is `../../requirements.txt`. The check covers `python-pptx`, `lxml`, `pywin32` on Windows only, `PyMuPDF`, `Pillow`, `numpy`, `opencv-python`, `paddleocr`, `paddlepaddle>=3.0`, `python-docx`, `openpyxl`, `pandas`, `beautifulsoup4`, and `trafilatura`. macOS does not install `pywin32`; its PowerPoint automation route uses the operating system's `osascript` executable.

If anything is missing, run the same script with `--install-missing --json` using the selected interpreter. Before running it, request outside-sandbox execution plus network/package-install permission when needed. Install only the missing packages; do not replace working packages or perform an unrelated full upgrade. Do not keep retrying a denied install inside the sandbox.

Run `<python> -m pip check`, then run the dependency script once more without `--install-missing`. Continue only when both commands succeed and `remaining_missing` is empty. Record the base Python, pipeline Python executable, Python version, package versions, initially missing packages, packages installed, and any warnings in the agent handoff.

## Verify the platform renderer

Read `../../references/powerpoint-rendering.md` and verify the matching platform route before Stage 1:

- **Windows:** require `sys.platform == "win32"` and the verified `pywin32` import. Request outside-sandbox execution before the first COM call; initialize COM with `pythoncom.CoInitialize()`, create an isolated PowerPoint instance with `DispatchEx`, query its version, clean it up in `finally`, and call `pythoncom.CoUninitialize()`. Treat a sandbox-only COM failure such as `0x80070520` as an execution-context error, not proof that PowerPoint is absent.
- **macOS:** require `sys.platform == "darwin"`, executable `/usr/bin/osascript` and `/usr/bin/sdef`, and locally installed Microsoft PowerPoint for Mac. Request outside-sandbox execution before resolving the application with `osascript -e 'id of application "Microsoft PowerPoint"'`. Perform one harmless AppleScript query such as requesting the PowerPoint version so macOS can request Automation permission. Retry once after the user grants the operating-system permission. If access is denied, stop before Stage 1.
- **Linux:** discover soffice or libreoffice, verify its version, and test headless PDF export with a disposable one-slide deck. If missing, install LibreOffice Impress and required fonts using the distribution package manager only through the normal approval mechanism. Verify exported PDF/page rendering before setup. No GUI or Microsoft PowerPoint is required.
- **Other operating systems:** report the unsupported renderer.

Record `operating_system`, `powerpoint_automation_method` as `pywin32-com`, `osascript-applescript` or `libreoffice-headless`, and the actual probe result/execution mode (outside sandbox for Office automation; permitted headless mode for Linux). If required outside-sandbox execution is unavailable or denied, report that exact permission blocker and do not start Stage 1. Headless Linux rendering may run sandboxed when its filesystem/process requirements are permitted. Linux may install LibreOffice through approved package-manager execution. Do not install Aspose, Tesseract, Poppler or any Codex presentation/computer-use plugin. PaddleOCR may download model data on its first real OCR invocation; request network permission at that point if the model is not already cached.

## Automatic handoff

After the final dependency and platform-renderer checks pass, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-setup-project`. Include the professor's selected source path or current working context, operating system, verified PowerPoint automation method, verified Python executable and version, all package results, and `dependency_preflight_passed: true`. Use the shared contract's local-continuation fallback only if delegation is unavailable.
