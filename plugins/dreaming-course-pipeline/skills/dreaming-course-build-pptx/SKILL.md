---
name: dreaming-course-build-pptx
description: Insert reviewed story slides into preserved teaching decks, retain original order and notes, render and verify the result, and deliver the final PowerPoint.
---

# Stage 6 — Insert story slides and verify

Read ../../references/pipeline-contract.md, ../../references/powerpoint-rendering.md and ../../references/execution-permissions.md completely.

Require dependencies_verified, blueprint_approved and images_approved. Read insertion_plan.json and image_manifest.md. Validate every anchor and one current image per insertion.

## Preserve the original lecture

For PPTX, open a copied original with python-pptx and add only reviewed image slides before their original targets. Preserve source slide objects, notes, masters, relationships and order: do not rebuild the lecture from screenshots. Record original slide identities BEFORE inserting so additions cannot shift later anchors.

Use a suitable blank layout and original deck dimensions. Preserve image aspect ratio without cropping; letterbox unobtrusively when ratios differ. Reorder added slides relative to original slide IDs/relationships; do not splice arbitrary XML across presentations. Verify round-trip fidelity because python-pptx cannot guarantee preservation of every Office feature. Report unsupported loss instead of claiming originals are intact.

Keep original notes unchanged. Set each inserted slide's notes to its approved Narration, including the final verbal academic handoff.

PDF lecture pages may be embedded unchanged as image slides; disclose they are not editable. For multiple PPTX inputs, default to one augmented deck per source to preserve dimensions/features. Combine only if the professor requests an order and a faithful supported merge is available; never silently flatten decks to simplify merging.

Save 05_output/final_deck.pptx for one source or named per-source outputs. Never overwrite original inputs or earlier delivered decks without authorization.

## QA and delivery

Render through the verified platform route. Require final count = original count + approved insertions per source. Verify anchors/order, no stale candidates, notes, aspect ratio and OOXML relationships. Compare final renders of original slides with pre-insertion renders using the same renderer/dimensions; visually resolve differences. Inspect insertions for complete text, continuity, readable scenes and explicit concept payoff. Pillow/numpy/OpenCV and OCR provide evidence, not a substitute for inspection.

Write qa_report.md and final_manifest.md with source hashes, original-to-final mapping, insertion/image hashes, notes checks, renderer/version and limitations. Fix assembly defects and rerun checks. Return image-content changes for professor review instead of silently altering accepted art.

Set pptx_built after assembly and final_qa_passed only after required checks pass. Deliver files and QA results with retained-editability limitations. End automatic routing and handle open-ended follow-up.
