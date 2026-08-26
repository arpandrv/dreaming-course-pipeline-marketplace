---
name: dreaming-course-build-pptx
description: Assemble the final 16:9 PowerPoint from the professor-accepted current image set, render it, run structural and visual QA, and return the completed project to open-ended user collaboration.
---

# Stage 6 - Build PowerPoint and QA

Read `../../references/pipeline-contract.md` completely before acting.

## Preconditions

Require `blueprint_approved: true` and `images_approved: true`. Read `04_images/image_manifest.md` and use its current-file mapping. Require exactly one current image for every blueprint slide, with no missing or duplicate slide mappings. Older revision files may remain in the folder but must not be inserted.

## Assemble

Create a 16:9 presentation with one full-bleed current image per slide in exact numerical order. Do not crop away content, stretch images, add unreviewed text or graphics, or alter the selected images. Save the generated file as `05_output/final_deck.pptx`.

## QA

Render every finished slide with LibreOffice or another reliable renderer into `05_output/rendered_slides/`. Inspect the rendered output, not only the PPTX object model, for slide count and order, aspect ratio, full-bleed placement, clipping, borders, blank or corrupt slides, text legibility and spelling, image artifacts, continuity, and alignment with the reviewed blueprint and image manifest. Parse or open the PPTX to verify structural validity.

Write `05_output/qa_report.md` with each check, evidence, result, and unresolved issue. Write `05_output/final_manifest.md` with slide-to-image mapping, hashes, build tool/version where available, review references, and output paths.

Fix assembly or rendering defects and rerun QA. If a defect requires changing image content, return to the user with the affected slide and proposed revision rather than silently replacing a reviewed image.

Set `pptx_built` to true after structural assembly succeeds and `final_qa_passed` to true only when all required checks pass. Return the final deck path, QA paths, counts, tools used, and limitations. This is the terminal pipeline stage: remain available for the user's open-ended follow-up questions or requested edits and do not spawn another agent automatically.
