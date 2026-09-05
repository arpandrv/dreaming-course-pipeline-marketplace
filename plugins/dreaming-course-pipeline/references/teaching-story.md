# Teaching story and insertion plan

## Story first, not decoration

Start with the exact concept and observable operation in the source course. Choose an analogy by mechanism, not shared words. Explain story entity/action -> academic entity/operation and where that correspondence stops. "Cooperation" alone does not teach MVC.

Default to an original educational story in a vivid connected Darwin landscape, with two or three distinct animal characters, waterways and fictional dialogue, unless the professor requests another setting. Build a goal, obstacle, failed attempt, concrete consequence, discovery and resolution. Each event causes the next. Do not merely show a successful request travelling through departments, or label unrelated animals Model/View/Controller.

For MVC demonstrate state/rules, presentation of state and input handling, tracing an interaction according to the course's MVC variant. For other concepts demonstrate their actual operations (e.g. recursion needs smaller subproblems, a base case and return/unwinding). Check the original source rather than inventing technical correspondences.

Write the full learner-facing story before splitting it into frames. Aim for one excellent contiguous sequence at the main objective, usually 4–7 frames; add frames when necessary. Each frame normally has 35–85 words of actual narration/dialogue, not a slogan. The concatenated frame text IS the full story; a richer blueprint hidden behind short captions is not acceptable. Presenter notes supplement, not replace, learner-visible storytelling.

Ask a concrete prediction question, then resolve it with the academic mechanism. Keep academic names out of setup frames; the final bridge may explicitly name and map the concept before the untouched teaching slide. Include the precise presenter handoff.

## Provenance and visual direction

The bundled Dharawal transcriptions are optional reference material, not a quota. Read the index and selected text fully. Use traditional material only when actual events fit without distortion; attribute it and record source-use limitations. Do not claim packaging grants unrestricted rights.

Otherwise label the first frame and source map "Original educational story", with no claim of authentic Dreaming, inherited teaching or real elders' speech. Fictional dialogue, thought bubbles and expressive scenes are allowed. Do not invent ceremonies, sacred meanings or imitate named Indigenous artists. Use specific landscape, composition, texture and colour directions rather than treating all Aboriginal art as one generic style.

Repeat a full Character bible for each frame: names, species, stable appearance, accessories and colours. Keep it identical across a sequence unless a story event explicitly changes an attribute. Visual direction describes actions, positions, panel layout, atmosphere and caption/bubble placement. It must not repeat story text or add unapproved labels. Prioritize understandable actions and legible text over scenery.

Only the On-slide story text is printed, verbatim exactly once. All planning metadata and presenter narration remain outside the image prompt's printable text. Use 16:9 images with 5% safe margins unless source dimensions call for a matched aspect ratio.

## Artifacts

Write source_map.md, teaching_blueprint.md and image_prompts.md directly as Markdown, not a JSON envelope required by the hosted API.

Each image section is headed "## 1. Title", numbered consecutively. Include these exact single-line fields with backtick-wrapped values:
- Placement: Between original slides X and Y in source; sequence N, frame M of K (say before slide 1 for an opening insertion).
- Insert before source: exact organized source identifier, including relative path where filenames collide.
- Insert before slide: original 1-based target number.
- Narration: full presenter script (at least 35 words).
- On-slide story text: complete learner-visible passage (normally 35–85 words).
- Concept connection: specific operation represented and its role in the mapping.
- Character bible: complete stable designs, repeated per frame.
- Visual direction: scene/layout only, not extra caption text.

Format field lines as "- **Field name:**" followed by the backtick-wrapped value. Synchronize these fields with insertion_plan.json; any requested wording change updates both.

insertion_plan.json has:
- sources: array of {source, slide_count}, derived from processing, not guessed.
- insertions: array in final narrative order, each {id, source, insert_before_slide, sequence, frame, frame_count, story_text, narration, concept_connection, character_bible, visual_direction}.
- id is consecutive from 1; slide numbers are original source numbers.
- One sequence uses one source/anchor and frames 1..frame_count in order. Do not scatter setup/payoff around unrelated lecture slides.
- Distinct complete sequences may target later concepts.
- All text fields contain approved full text, not file pointers.

Run scripts/validate_insertions.py PLAN before review and build. It checks structure and anchors; separately inspect narrative causality, technical accuracy, provenance and equality with Markdown. Do not treat word minimums as proof of quality.

Revisions preserve unaffected text and anchors. Image-only edits preserve story text/narration unless explicitly changed by the professor; never collapse the story into slogans.
