---
name: dreaming-course-process
description: "Process course files with local headless command-line tools: render PowerPoint slides to images, extract only speaker notes, and hand verified outputs to blueprint design. Never use PowerPoint/Presentations connectors, computer use, or GUI automation."
---

# Stage 3 - Process Files

Read `../../references/pipeline-contract.md` completely before acting.

## Preconditions and fidelity

Require `source_copy_created: true` and `files_organized: true`. This is ingestion, not teaching design. Preserve source wording, order, structure, and page boundaries. Do not summarize, paraphrase, correct, interpret, or silently repair OCR. Mark uncertainty without guessing.

## Required local execution path

Run Stage 3 entirely against local project files with headless command-line tools. Do not request, enable, or invoke any built-in or external PowerPoint/Presentations app or connector, Microsoft PowerPoint application automation, computer use, GUI automation, browser automation, or cloud document service.

For PowerPoint rendering, use this order:

1. Load the bundled workspace dependency paths when that facility is available and use its local presentation-rendering utilities.
2. Otherwise use an already-installed LibreOffice executable in headless mode, with Python or shell orchestration as needed.
3. Use Python libraries or direct OOXML inspection for speaker-note extraction and validation. Do not claim that `python-pptx` itself visually renders slides.

Do not install software or ask the user for unrelated app/plugin permissions. If neither a bundled local renderer nor an installed headless LibreOffice executable is available, record the exact missing dependency in `processing_manifest.md`, leave `files_processed` false, and stop as a genuine blocker. Never fall back to an interactive application or computer use.

## Process by type

- **PowerPoint:** Render every slide at high quality into `02_processed/pptx/<deck-name>/slide_NNN.png` through the required local headless execution path above. Do not extract visible slide text. If speaker notes exist, extract them verbatim into a companion Markdown file with source filename and slide-number boundaries. If no notes exist, record that fact in the manifest without creating an empty notes artifact.
- **PDF:** Test for a usable text layer. Extract it directly when usable and apply OCR only to pages that need it. Preserve page boundaries and mark low-confidence or illegible regions.
- **DOC/DOCX:** Extract text and structure while preserving headings, lists, tables, captions, and document order.
- **Markdown:** Copy unchanged and verify byte equality.
- **Other types:** Copy unchanged and record whether each type was processed, copied only, unreadable, or unsupported.

Do not create a README file. Create only `02_processed/processing_manifest.md` for cross-format traceability, including every organized file, output paths, exact local command-line rendering method and executable/script path, processing method, OCR use, status, warnings, and errors.

Validate that every PowerPoint slide has exactly one rendered image, speaker notes are aligned to the correct slide, expected outputs are non-empty, and every organized file has a recorded outcome. Set `files_processed` to true only after validation and record the timestamp and manifest path.

## Automatic handoff

After successful processing, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-blueprint`. Include the absolute project root, verified state, processing manifest, rendered-deck paths, notes artifacts, processed course-material paths, warnings, and OCR uncertainties. Do not design the blueprint in this agent.
