---
name: dreaming-course-generate-images
description: Illustrate only approved narrative insertions, inspect full story text and continuity, and revise selected images through professor review before deck assembly.
---

# Stage 5 — Illustrate, review and revise

Read ../../references/pipeline-contract.md and ../../references/teaching-story.md completely. Require blueprint_generated and blueprint_approved. Read the approved plan and prompts; use recorded Python for QA.

## Production boundary

Generate ONLY new insertion images, not original lecture slides. Use the available Codex image-generation capability and its applicable instructions. If unavailable, report the capability blocker; do not substitute quote cards or Python-drawn story art.

Send only exact On-slide story text, Character bible, Visual direction, aspect ratio and rendering constraints to generation. Do NOT send an entire blueprint section as print instructions: placement, narration, concept connection, IDs and review notes are metadata. Render the approved passage verbatim exactly once. Add no duplicated arrow text, unrequested checkmarks, extra characters or academic labels. Visual direction specifies composition, not extra captions.

Repeat complete character designs each time and use supported reference images for continuity. Keep setup narrative and the approved final bridge explicit. Use readable panels, captions and attributed speech bubbles, not scenery with a slogan.

Save slide_NNN.png in the single flat 04_images/ folder using insertion IDs. Inspect every candidate for complete text, readability, meaning, clipping, stable characters and prompt compliance. Use Pillow for dimensions, numpy/OpenCV for image checks and PaddleOCR as exact-text evidence; resolve OCR differences visually. Retry obvious technical failures only a bounded number of times, then report remaining issues. Never silently change approved wording.

Write image_manifest.md with insertion ID, anchor, full prompt reference, current filename, revisions and QA evidence. Set images_generated only after the required set exists and is inspected.

## Professor review and targeted revision

Show ordered insertions with placements and ask for changes or permission to build. Agent inspection is not approval.

For each requested change, open the current image, read its actual production prompt and feedback, revise only that prompt, synchronize image_prompts.md and insertion_plan.json, and recreate only that image. Preserve story text, narration, character identity and anchor unless the user requests a change. Save new_slide_NNN.png, then new1_slide_NNN.png, new2_slide_NNN.png, etc.; keep previous candidates. Inspect the revision, update the current-file pointer and ask again. Do not regenerate the whole sequence for one-image feedback or create extra review folders.

If content changes affect story/mapping, return those changes to blueprint review. Record clear build approval and timestamp in image_review.md, set images_approved true and hand off to dreaming-course-build-pptx with current mapping, anchors, source counts and accepted limitations.
