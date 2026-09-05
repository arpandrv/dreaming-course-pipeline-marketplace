# Dreaming Course Pipeline Contract

## Scope and invariants

This is the local Codex edition of the current insertion-only Dreaming Studio pipeline. No n8n, Supabase, private worker, author account or hardcoded model endpoint is required.

1. Preserve the professor's source folder byte-for-byte. Work on the protected project copy.
2. Read pipeline_state.json before each stage. Record every unsupported/unreadable file. Preserve source wording in extraction; mark OCR uncertainty.
3. Read teaching-story.md for design/revision. Original educational fiction is allowed, and is the default when traditional events do not fit the mechanism. Bundled stories are available references, not a mandatory quota. Label original fiction; do not claim invented dialogue is traditional testimony. Bundling a story does not establish unrestricted rights.
4. Preserve original teaching slides and their relative order. Generate ONLY new narrative insertions. Each sequence is contiguous immediately before its target original slide.
5. Professor review occurs inside blueprint and image generation, not separate confirmation stages. Image generation requires story approval; build requires image approval.
6. Use local Python and powerpoint-rendering.md, respecting execution-permissions.md. Do not install presentation/computer-use plugins as substitutes.
7. Never fabricate successful outputs, approximate source renders or claim agent inspection is professor acceptance.

## Project artifacts

Keep the existing numbered folders:
- 00_source_original/: verified source copy.
- 01_organized/: classified sources and inventory.
- 02_processed/: per-source images, extracted/OCR text, speaker notes, processing_manifest.md.
- 03_blueprint/: source_map.md, teaching_blueprint.md, image_prompts.md, insertion_plan.json, blueprint_review.md.
- 04_images/: slide_NNN.png, new_slide_NNN.png, new1_slide_NNN.png, image_manifest.md, image_review.md.
- 05_output/: final_deck.pptx (or per-source decks), rendered_slides/, qa_report.md, final_manifest.md.
- pipeline_state.json.

Use one flat image-review folder. The manifest selects exactly one current candidate per insertion. Insertion IDs are not original-slide numbers.

## State and invalidation

Keep project_name, operating_system, powerpoint_automation_method, python_executable, dependency_versions and these flags: dependencies_verified, source_copy_created, files_organized, files_processed, blueprint_generated, blueprint_approved, images_generated, images_approved, pptx_built, final_qa_passed. Initialize flags false and set only after verification.

Record original counts per source, insertion count and expected final counts separately. A blueprint revision invalidates its approval and downstream approvals/output status; image revision invalidates image approval and final output status. Keep artifacts recoverable and reuse unchanged approved candidates. An older completed project is not automatically compliant: explain migration and review changed content rather than overwriting it.

## Routing and handoff

0 preflight -> 1 setup-project -> 2 organize -> 3 process -> 4 blueprint + review -> 5 generate-images + review -> 6 build-pptx + QA.

Use existing dreaming-course-* names. Prompt/story revision resumes blueprint; image revision resumes generate-images. No legacy prompts or redundant review skills.

After automatic stages and explicit review approvals, dispatch a fresh subagent through available, permitted delegation, not a new user-owned task. Pass the absolute installed NEXT SKILL.md path and require reading it and its references: a skill name alone does not load instructions. Include project root (source context before setup), Python/render route, verified state, artifacts, insertion/source identities, review decision and warnings. Do not redo completed stages. The coordinator brings child review questions into this conversation and routes the user's reply back; never manufacture approval.

If delegation is unavailable, state the limitation and read/run the next skill locally when permitted. Do not pretend a new agent ran. Review boundaries still apply. Stage 6 ends automatic routing.

## Review semantics

Accept clear natural-language authorization for the current action, not a magic phrase. "Go ahead" at blueprint review authorizes images only. "Make the PPTX" at image review authorizes the current set. Requested changes keep review open; clarify ambiguity. Record actual wording and timestamp.
