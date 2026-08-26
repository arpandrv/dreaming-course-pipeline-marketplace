---
name: dreaming-course-blueprint
description: Design the sourced narrative teaching blueprint using processed course materials and the bundled Dharawal story library, run iterative professor review, then hand approved work to image generation.
---

# Stage 4 - Design and Review Blueprint

Read `../../references/pipeline-contract.md` completely before acting.

## Sources

Require `dependencies_verified: true` and `files_processed: true`. Read all relevant material in `02_processed/`, including rendered PowerPoint slides and extracted speaker notes. Also read `../../references/Dharawal_story_transcriptions/README.md` and every story Markdown file in that bundled directory completely. These stories ship with the plugin; do not ask the professor to provide them again.

The bundled stories are required, approved source material for this pipeline and count as source support even when the professor's academic materials do not mention Dharawal culture. Distinguish source statements from interpretation. Identify missing, uncertain, sensitive, or permission-dependent material. Treat the stories as culturally situated sources, not templates to imitate or expand.

## Design

Create a coherent whole-deck teaching arc. Select at least one suitable bundled Dharawal story and meaningfully incorporate it through a clearly attributed story reference, faithful excerpt, or source-grounded narrative sequence. Identify the selected story, why it supports the learning arc, and the exact slides where it is used. The academic topic's lack of an existing Dharawal connection is not grounds for omitting the story library; this pipeline intentionally applies the approved pedagogy across domains.

Use approved Dreaming-inspired pedagogical principles as teaching structure: establish place and relation, present a concrete situation, build observation and tension, invite inference, then reveal the formal academic concept. Preserve the selected story's meaning and cultural context. Do not reduce a story to a generic metaphor, equate cultural beings or events with technical constructs, or invent, merge, continue, imitate, genericise, or reinterpret cultural material. Use only story details supported by the bundled transcription.

If no bundled story can be incorporated without distortion or cultural harm, do not produce a story-free blueprint for approval. Record the specific cultural-review blocker, leave `blueprint_generated` and `blueprint_approved` false, and ask the professor for direction.

Create in `03_blueprint/`:

1. `source_map.md`: course-source inventory, every bundled story considered, selected-story provenance, selection rationale, exact planned use, uncertainties, sensitivities, permissions, and traceability identifiers.
2. `teaching_blueprint.md`: overall learning goals, narrative arc, selected story and its teaching role, transitions, and one numbered entry per proposed slide containing purpose, source linkage, learner question, narrative function, exact or proposed on-slide text, instructor notes, formal concept reveal, visual role, continuity notes, accessibility needs, and cultural-review flag. Every slide using story material must name the story and trace the material to its bundled source.
3. `image_prompts.md`: one numbered 16:9 image specification per proposed slide containing composition, all required on-image text, continuity, exclusions, source constraints, accessibility requirements, and cultural-review flags. A prompt depicting story material may include only people, beings, places, objects, actions, and visual details explicitly supported by the selected transcription.

Do not mark text-heavy slides as rendering risks and do not create fallback layouts merely because an image contains text. Still require exact wording and inspect generated text during the image stage.

Validate completeness, pedagogical sequence, source traceability, story attribution, meaningful use of at least one bundled story, cultural safeguards, and slide-number alignment. Story-free output fails validation. Set `blueprint_generated` to true only after the artifacts pass this check; keep `blueprint_approved` false until review closes.

## Iterative professor review

Lead the review with the selected story or stories, why each was chosen, how its meaning was preserved, and the exact slides where it appears. Then present the proposed slide count, full arc, concept reveals, image approach, uncertainties, and cultural-review flags. Ask whether the professor wants changes or wants to proceed to image generation.

When changes are requested, update the affected blueprint artifacts, preserve traceability, log the request and response in `03_blueprint/blueprint_review.md`, rerun alignment checks, and present the revised result. Continue this back-and-forth in the same agent until the professor is satisfied.

Apply the contract's natural-language review semantics. When the professor clearly authorizes image generation, record their wording and timestamp in `blueprint_review.md` and set `blueprint_approved` to true.

## Approved handoff

After approval, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-generate-images`. Include the absolute project root, approved blueprint paths, slide count, story/source mappings, continuity requirements, exact-text requirements, and remaining non-blocking warnings. Do not generate images in this agent.
