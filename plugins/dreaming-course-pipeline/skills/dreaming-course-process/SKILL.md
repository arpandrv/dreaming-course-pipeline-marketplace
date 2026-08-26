---
name: dreaming-course-process
description: "Process course files with the verified Python stack and platform-local PowerPoint automation on Windows or macOS, then hand verified outputs to blueprint design."
---

# Stage 3 - Process Files

Read `../../references/pipeline-contract.md`, `../../references/execution-permissions.md`, and `../../references/powerpoint-rendering.md` completely before acting.

## Preconditions and fidelity

Require `dependencies_verified: true`, `source_copy_created: true`, and `files_organized: true`. Use the exact `python_executable` recorded in `pipeline_state.json`. This is ingestion, not teaching design. Preserve source wording, order, structure, and page boundaries. Do not summarize, paraphrase, correct, interpret, or silently repair OCR. Mark uncertainty without guessing.

## Required local execution path

Run Stage 3 entirely against local project files with the Stage 0-verified Python stack. Do not request, enable, or invoke a Codex PowerPoint/Presentations connector, computer use, GUI clicking, browser automation, or cloud document service.

1. Use `python-pptx` and `lxml` to inspect the PPTX package and extract speaker notes. Do not claim that `python-pptx` visually renders slides.
2. Request outside-sandbox execution before any PowerPoint automation. On Windows, use `pywin32` COM with explicit `pythoncom.CoInitialize()`/`CoUninitialize()` and direct PowerPoint PNG export. On macOS, use Python `subprocess` with `/usr/bin/osascript` and AppleScript to export through locally installed Microsoft PowerPoint without GUI clicking.
3. On macOS, use `PyMuPDF` to render every exported PDF page to a high-resolution PNG in slide order. On both platforms, check the rendered-image count against the PPTX slide count before accepting the output.

The Windows COM and macOS AppleScript routes are approved local programmatic automation and must run through the outside-sandbox command mode described in the execution-permissions reference. The macOS route may launch PowerPoint and requires macOS Automation permission, but must not use `System Events`, keystrokes, menus, mouse actions, `activate`, computer use, or other visible app control. Do not install Aspose, LibreOffice, Poppler, Tesseract, or presentation plugins. If outside-sandbox execution is unavailable, PowerPoint is absent, platform automation is denied, or export fails, record the exact distinct blocker in `processing_manifest.md`, leave `files_processed` false, and stop. Do not manufacture approximate slides with `python-pptx` drawing primitives.

## Process by type

- **PowerPoint:** Use `python-pptx`/`lxml` for structure and notes. Render with the recorded outside-sandbox Windows `pywin32` direct-PNG route or macOS `osascript` PDF route followed by `PyMuPDF`. Save every rendered slide at high quality as `02_processed/pptx/<deck-name>/slide_NNN.png`. Do not extract visible slide text. If speaker notes exist, extract them verbatim into a companion Markdown file with source filename and slide-number boundaries. If no notes exist, record that fact without creating an empty notes artifact.
- **PDF:** Use `PyMuPDF` to test and extract a usable text layer while preserving page boundaries. For image-only or unusable pages, rasterize with `PyMuPDF`, preprocess only as needed with `Pillow`, `numpy`, and `opencv-python`, and OCR with `paddleocr` backed by `paddlepaddle`. Record OCR use and uncertainty page by page; never silently correct OCR.
- **DOCX:** Use `python-docx` to extract headings, paragraphs, lists, tables, captions, and document order. Treat legacy `.doc` as unsupported unless an already-available, explicitly approved local converter can produce a faithful intermediate; record the outcome rather than renaming it.
- **XLSX:** Use `openpyxl` to preserve workbook/sheet/cell structure and `pandas` only where a tabular view aids extraction or validation. Record formulas and displayed-value limitations.
- **HTML:** Use `trafilatura` for main-text extraction and `beautifulsoup4` for DOM structure or fallback extraction. Preserve the original HTML copy and record which method produced the processed text.
- **Raster images:** Inspect with `Pillow`; when textual extraction is relevant, preprocess with `numpy`/`opencv-python` and OCR with PaddleOCR. Preserve the original image and record confidence or illegibility.
- **Markdown:** Copy unchanged and verify byte equality.
- **Other types:** Copy unchanged and record whether each type was processed, copied only, unreadable, or unsupported.

Do not create a README file. Create only `02_processed/processing_manifest.md` for cross-format traceability, including every organized file, output paths, exact local command-line rendering method and executable/script path, processing method, OCR use, status, warnings, and errors.

Validate that every PowerPoint slide has exactly one rendered image, speaker notes are aligned to the correct slide, expected outputs are non-empty, and every organized file has a recorded outcome. Set `files_processed` to true only after validation and record the timestamp and manifest path.

## Automatic handoff

After successful processing, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-blueprint`. Include the absolute project root, verified state and Python executable, processing manifest, rendered-deck paths, notes artifacts, processed course-material paths, library/render methods used, warnings, and OCR uncertainties. Do not design the blueprint in this agent.
