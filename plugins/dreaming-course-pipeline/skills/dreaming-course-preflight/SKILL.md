---
name: dreaming-course-preflight
description: Verify or install Python and the complete local dependency stack before starting a new Dreaming Course Pipeline project, then hand verified execution to project setup.
---

# Stage 0 - Verify Runtime and Dependencies

Read `../../references/pipeline-contract.md` completely before acting.

## Find or install Python

Do not create or modify the professor's project yet.

1. Prefer the Codex bundled workspace Python as a base interpreter when its dependency-path facility is available.
2. Otherwise locate a working Python 3 interpreter using platform-appropriate commands: `py -3` or `python` on Windows, and `python3` on macOS.
3. Verify the base interpreter with a harmless version command and record its absolute executable path and version.
4. If no usable Python 3 interpreter exists, install Python for the current user with the platform's standard package manager when available. Request required system or network approval through the normal Codex permission mechanism; do not substitute a textual confirmation loop. On Windows, prefer the current-user Python 3.12 package through `winget`. On macOS, prefer an existing package manager such as Homebrew and Python 3.12; do not install Homebrew itself implicitly. Re-discover and verify Python after installation.
5. If automatic installation is unavailable or fails, stop with the exact attempted method and error. Do not start Stage 1.

## Select the pipeline environment

Do not install packages into Codex's bundled runtime or mutate another managed Python installation. Use a dedicated reusable virtual environment for the pipeline:

- Windows: `%LOCALAPPDATA%\DreamingCoursePipeline\venv`
- macOS/Linux: `${XDG_CACHE_HOME:-~/.cache}/dreaming-course-pipeline/venv`

If its Python executable already exists, verify and reuse it. Otherwise create the directory's parent and run `<base-python> -m venv <venv-path>`. If the chosen base interpreter cannot create a venv, try another discovered Python interpreter before treating it as a Python-install blocker. From this point forward, `<python>` means the virtual environment's Python executable. Record both the base and pipeline interpreter paths.

## Verify and install the package set

Verify that `<python> -m pip --version` succeeds. If Python exists but pip does not, run `<python> -m ensurepip --upgrade`, then verify pip again. Resolve the bundled script relative to this `SKILL.md`, use its absolute path, and run:

```text
<python> <absolute-plugin-path>/scripts/check_dependencies.py --json
```

The authoritative package declaration is `../../requirements.txt`. The check covers `python-pptx`, `lxml`, `pywin32` on Windows only, `PyMuPDF`, `Pillow`, `numpy`, `opencv-python`, `paddleocr`, `paddlepaddle>=3.0`, `python-docx`, `openpyxl`, `pandas`, `beautifulsoup4`, and `trafilatura`. macOS does not install `pywin32`; its PowerPoint automation route uses the operating system's `osascript` executable.

If anything is missing, run the same script with `--install-missing --json` using the selected interpreter. Allow the execution environment to request network or package-install permission when needed. Install only the missing packages; do not replace working packages or perform an unrelated full upgrade.

Run `<python> -m pip check`, then run the dependency script once more without `--install-missing`. Continue only when both commands succeed and `remaining_missing` is empty. Record the base Python, pipeline Python executable, Python version, package versions, initially missing packages, packages installed, and any warnings in the agent handoff.

## Verify the platform renderer

Read `../../references/powerpoint-rendering.md` and verify the matching platform route before Stage 1:

- **Windows:** require `sys.platform == "win32"`, the verified `pywin32` import, and a locally installed Microsoft PowerPoint COM registration.
- **macOS:** require `sys.platform == "darwin"`, executable `/usr/bin/osascript` and `/usr/bin/sdef`, and locally installed Microsoft PowerPoint for Mac. Resolve the application with `osascript -e 'id of application "Microsoft PowerPoint"'`. Perform one harmless AppleScript query such as requesting the PowerPoint version so macOS can request Automation permission. Retry once after the user grants the operating-system permission. If access is denied, stop before Stage 1.
- **Other operating systems:** stop as unsupported; do not select a different renderer automatically.

Record `operating_system` and `powerpoint_automation_method` as `pywin32-com` or `osascript-applescript`. Do not install Aspose, Tesseract, Poppler, LibreOffice, or any Codex presentation/computer-use plugin. PaddleOCR may download model data on its first real OCR invocation; request network permission at that point if the model is not already cached.

## Automatic handoff

After the final dependency and platform-renderer checks pass, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-setup-project`. Include the professor's selected source path or current working context, operating system, verified PowerPoint automation method, verified Python executable and version, all package results, and `dependency_preflight_passed: true`. Do not create the project in this agent.
