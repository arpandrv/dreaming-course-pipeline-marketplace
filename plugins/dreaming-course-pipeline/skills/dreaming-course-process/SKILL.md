---
name: dreaming-course-process
description: Render PowerPoint slides to images, extract only their speaker notes, faithfully process other source types, and hand the project to blueprint design in a fresh agent.
---

# Stage 3 - Process Files

Read `../../references/pipeline-contract.md` completely before acting.

## Preconditions and fidelity

Require `source_copy_created: true` and `files_organized: true`. This is ingestion, not teaching design. Preserve source wording, order, structure, and page boundaries. Do not summarize, paraphrase, correct, interpret, or silently repair OCR. Mark uncertainty without guessing.

## Process by type

- **PowerPoint:** Render every slide at high quality into `02_processed/pptx/<deck-name>/slide_NNN.png`. Do not extract visible slide text. If speaker notes exist, extract them verbatim into a companion Markdown file with source filename and slide-number boundaries. If no notes exist, record that fact in the manifest without creating an empty notes artifact.
- **PDF:** Test for a usable text layer. Extract it directly when usable and apply OCR only to pages that need it. Preserve page boundaries and mark low-confidence or illegible regions.
- **DOC/DOCX:** Extract text and structure while preserving headings, lists, tables, captions, and document order.
- **Markdown:** Copy unchanged and verify byte equality.
- **Other types:** Copy unchanged and record whether each type was processed, copied only, unreadable, or unsupported.

Do not create a README file. Create only `02_processed/processing_manifest.md` for cross-format traceability, including every organized file, output paths, processing method, OCR use, status, warnings, and errors.

Validate that every PowerPoint slide has exactly one rendered image, speaker notes are aligned to the correct slide, expected outputs are non-empty, and every organized file has a recorded outcome. Set `files_processed` to true only after validation and record the timestamp and manifest path.

## Automatic handoff

After successful processing, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-blueprint`. Include the absolute project root, verified state, processing manifest, rendered-deck paths, notes artifacts, processed course-material paths, warnings, and OCR uncertainties. Do not design the blueprint in this agent.
