---
name: dreaming-course-build-pptx
description: Assemble the final 16:9 PowerPoint from the professor-accepted current image set, render it, run structural and visual QA, and return the completed project to open-ended user collaboration.
---

# Stage 6 - Build PowerPoint and QA

Read `../../references/pipeline-contract.md` completely before acting.

## Preconditions

Require `dependencies_verified: true`, `blueprint_approved: true`, and `images_approved: true`. Use the exact `python_executable` recorded in `pipeline_state.json`. Read `04_images/image_manifest.md` and use its current-file mapping. Require exactly one current image for every blueprint slide, with no missing or duplicate slide mappings. Older revision files may remain in the folder but must not be inserted.

## Assemble

Use `python-pptx` with `lxml` support to create a 16:9 presentation with one full-bleed current image per slide in exact numerical order. Use `Pillow` to verify each source image's pixel dimensions and aspect ratio before placement. Do not crop away content, stretch images, add unreviewed text or graphics, or alter the selected images. Save the generated file as `05_output/final_deck.pptx`.

## QA

Read `../../references/powerpoint-rendering.md` completely and render the finished deck through the platform route recorded in `pipeline_state.json`: Windows uses `pywin32` COM; macOS uses Python `subprocess` with `/usr/bin/osascript` and AppleScript. Export `final_deck.pptx` to PDF, close and clean up the locally created PowerPoint instance, then use `PyMuPDF` to render every PDF page into `05_output/rendered_slides/`. On macOS, allow the already-approved Automation permission but do not use `System Events`, keystrokes, menus, mouse actions, `activate`, or computer use. Do not use a Codex PowerPoint/Presentations connector, Aspose, LibreOffice, Poppler, or a cloud service.

Inspect the rendered output, not only the PPTX object model. Use `python-pptx`/`lxml` for structural slide-count and relationship checks; `Pillow`, `numpy`, and `opencv-python` for aspect ratio, full-bleed placement, clipping, borders, blank or corrupt slides, and image artifacts; and PaddleOCR for spelling/exact-text evidence where reviewed slides contain text. Visually resolve OCR discrepancies and inspect continuity and alignment with the reviewed blueprint and image manifest.

Write `05_output/qa_report.md` with each check, evidence, result, and unresolved issue. Write `05_output/final_manifest.md` with slide-to-image mapping, hashes, Python executable, package/tool versions, local PowerPoint export method, review references, and output paths.

Fix assembly or rendering defects and rerun QA. If a defect requires changing image content, return to the user with the affected slide and proposed revision rather than silently replacing a reviewed image.

Set `pptx_built` to true after structural assembly succeeds and `final_qa_passed` to true only when all required checks pass. Return the final deck path, QA paths, counts, tools used, and limitations. This is the terminal pipeline stage: remain available for the user's open-ended follow-up questions or requested edits and do not spawn another agent automatically.
