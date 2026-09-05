---
name: dreaming-course-blueprint
description: Write and iteratively review complete teaching stories and insertion-only slide prompts grounded in processed course concepts, without redesigning original slides.
---

# Stage 4 — Story blueprint and professor review

Read ../../references/pipeline-contract.md and ../../references/teaching-story.md completely. Require verified dependencies and processed sources.

Inspect rendered teaching slides, extracted text, speaker notes and processing_manifest.md. Read the bundled story index and any selected story in full. Professors need not supply the library again; do not force a traditional story onto an unrelated concept.

## Design before illustration

Follow teaching-story.md: learning objective -> mechanism mapping/limitations -> full causal story -> illustrated frames -> explicit academic bridge. Default to one excellent sequence, typically 4–7 frames, expanding for readability. Do not rebuild every lecture slide or create decorative quote introductions. Show named characters, a goal, failed attempt, concrete consequence, changed approach and resolution. The slides' dialogue/narration must carry the whole story.

Create in 03_blueprint/:
- source_map.md: sources/anchors, provenance, selected traditional story or original-fiction label, mechanism mapping, limitations and uncovered concepts.
- teaching_blueprint.md: full learner-facing story, causal storyboard, prediction question/answer, academic payoff and presenter handoff.
- image_prompts.md: one numbered section per NEW insertion with all teaching-story.md fields.
- insertion_plan.json: machine-readable plan defined in teaching-story.md.

Check the complete story equals the actual frame passages in order, not a rich hidden story reduced to slogans for illustration. Validate anchors, contiguous sequences, original order and technically meaningful mappings. Run the plugin's scripts/validate_insertions.py on the plan using the verified Python. Word counts are not proof of pedagogical quality: inspect events and explanations yourself. Do not reject text-heavy slides solely for having text.

Set blueprint_generated true after validation and leave blueprint_approved false.

## Review and revision

Show the full story, mapping, original anchors, insertion count and exact prompts. Distinguish original fiction from traditional material. Ask for changes or permission to generate images and stop here.

For feedback, update affected artifacts together, record it in blueprint_review.md, invalidate downstream approvals as specified in the contract, revalidate and present again. This skill also handles later "revise the prompts" requests.

Only after clear professor approval record wording/timestamp, set blueprint_approved true and hand off to dreaming-course-generate-images with approved plan, prompts and exact story text.
