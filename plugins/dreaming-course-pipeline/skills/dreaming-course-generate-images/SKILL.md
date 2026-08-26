---
name: dreaming-course-generate-images
description: Generate the complete slide-image set from the reviewed blueprint, revise individual images through an iterative professor review loop, then hand the accepted set to PowerPoint production.
---

# Stage 5 - Generate and Review Images

Read `../../references/pipeline-contract.md` completely before acting.

## Preconditions and generation

Require `dependencies_verified: true`, `blueprint_generated: true`, and `blueprint_approved: true`. Use the exact `python_executable` recorded in `pipeline_state.json` for local image QA. Read every slide entry and image prompt before generation.

Generate one complete 16:9 image per numbered slide, in order. Preserve recurring characters, settings, objects, colours, and visual language. Follow the reviewed composition, exact-text, accessibility, source, and exclusion instructions. Do not introduce culturally specific symbols, designs, ceremonies, places, people, or story elements that the blueprint does not support.

Save the initial candidates directly in the single flat folder `04_images/` as `slide_NNN.png`. Do not create `generated`, `approved`, or `superseded` subfolders.

Inspect each candidate at useful size for count, aspect ratio, exact text and spelling, clipping, artifacts, continuity, prompt compliance, cultural constraints, and blueprint alignment. Use `Pillow` for dimensions, colour mode, compositing, and contact sheets; `numpy` and `opencv-python` for blank-image, corruption, clipping, and visual-anomaly checks; and `paddleocr`/`paddlepaddle` to read generated on-image text when the blueprint requires exact wording. Compare OCR output with the required text, then visually inspect every discrepancy because OCR is evidence, not authority. Regenerate obvious technical failures before presenting the set. Create `04_images/image_manifest.md` with one row per slide containing the image-prompt reference, initial file, current file, revision history, inspection status, OCR/text check, and warnings. Set `images_generated` to true only when the complete set passes this technical inspection.

## Iterative professor review

Present the images in slide order with slide numbers and important warnings. Ask the professor what should change or whether Codex should proceed with the current set to PowerPoint creation.

For each requested image change:

1. Open and inspect the specific current image.
2. Read the professor's request and the exact image prompt used for that slide.
3. Update that slide's prompt in `03_blueprint/image_prompts.md`, preserving a concise change log.
4. Recreate only that image.
5. Keep every version in `04_images/`; never overwrite or move an earlier version.
6. Name the first revision `new_slide_NNN.png`, then `new1_slide_NNN.png`, `new2_slide_NNN.png`, and so on.
7. Re-run the Pillow/OpenCV/NumPy checks and OCR exact-text check where applicable, inspect the revision, update the manifest's `current file`, and ask the professor to review it.

Continue this loop until no further agent revisions are requested. Do not create a separate image-review skill or folder.

Use the contract's natural-language review semantics. Infer permission narrowly but do not demand a fixed phrase. Clear statements such as "go ahead and make the PPTX," "just do the damn thing," or "I'm alright; I'll fix it myself" may authorize use of the current manifest-selected images when context makes that meaning unambiguous. Ask one short clarification only when it is genuinely unclear whether the user wants a PPTX now or wants the pipeline to stop.

Record the user's wording, timestamp, and final current-file mapping in `04_images/image_review.md`; then set `images_approved` to true.

## Approved handoff

After approval, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-build-pptx`. Include the absolute project root, verified state, slide count, `image_manifest.md`, exact current file for every slide, and any accepted limitations. Do not assemble the PowerPoint in this agent.
