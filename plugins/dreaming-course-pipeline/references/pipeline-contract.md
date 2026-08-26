# Dreaming Course Pipeline Contract

## Governing rules

1. Never modify the professor's original dump folder.
2. Work only from the copied project folder created by Stage 1.
3. Before each project stage, inspect `pipeline_state.json`, verify `dependencies_verified: true`, and verify the required prior-stage flags.
4. Never silently skip unreadable or unsupported files. Record every file, failure, warning, and uncertainty in the relevant manifest.
5. During ingestion, do not summarize, paraphrase, correct, interpret, or modernize source text.
6. Treat Dreaming and other cultural material as culturally situated source material, not generic creative raw material. The bundled Dharawal transcriptions are approved, attributed source material for this pipeline and count as source support. Their inclusion authorizes faithful quotation, reference, and pedagogical use as written; it does not authorize inventing, merging, continuing, imitating, genericising, or reinterpreting stories or cultural details.
7. Every blueprint must select and meaningfully incorporate at least one suitable bundled Dharawal story. A course topic that does not itself mention Dharawal material is not a reason to omit the library. If no story can be used without distortion or cultural harm, stop in the blueprint stage, record the specific blocker, and request human direction. Never approve or hand off a story-free blueprint.
8. Stage 0 must verify a real Python 3 interpreter, the complete package set, and the platform renderer before Stage 1 begins. Windows uses local `pywin32` COM automation of installed Microsoft PowerPoint. macOS uses Python `subprocess` with built-in `/usr/bin/osascript` and AppleScript to automate installed Microsoft PowerPoint after macOS Automation permission is granted. Neither route may be replaced by a Codex PowerPoint/Presentations connector, computer use, GUI clicking, `System Events`, keystrokes, browser automation, Aspose, LibreOffice, or a cloud document service. Unsupported platforms or missing/denied renderers are genuine blockers.
9. Human review occurs inside the blueprint stage before image generation and inside the image stage before PowerPoint creation.
10. Maintain a traceable audit trail in project artifacts and `pipeline_state.json`.
11. Stop only at a required human-review loop, a genuine blocker, or the completed final stage. Successful non-review stages automatically hand off to a fresh agent.

## Standard project structure

```text
project_root/
  00_source_original/
  01_organized/
    pptx/
    pdf/
    docx/
    markdown/
    others/
  02_processed/
    pptx/
    pdf/
    docx/
    markdown/
    others/
    processing_manifest.md
  03_blueprint/
    source_map.md
    teaching_blueprint.md
    image_prompts.md
    blueprint_review.md
  04_images/
    slide_001.png
    new_slide_001.png
    new1_slide_001.png
    image_manifest.md
    image_review.md
  05_output/
    final_deck.pptx
    rendered_slides/
    qa_report.md
    final_manifest.md
  pipeline_state.json
```

`04_images/` is one flat review folder. Do not create `generated`, `approved`, or `superseded` image subfolders.

## State file

Initialize `pipeline_state.json` with these keys. A stage updates only its own flags and audit metadata.

```json
{
  "project_name": "",
  "dependencies_verified": false,
  "operating_system": "",
  "powerpoint_automation_method": "",
  "python_executable": "",
  "dependency_versions": {},
  "source_copy_created": false,
  "files_organized": false,
  "files_processed": false,
  "blueprint_generated": false,
  "blueprint_approved": false,
  "images_generated": false,
  "images_approved": false,
  "pptx_built": false,
  "final_qa_passed": false
}
```

## Project discovery

Operate on the project selected by the user or the single unambiguous project under the current working directory. If multiple plausible projects or state files exist, ask the user to select one. Never guess across projects.

## Agent handoff protocol

At every successful non-terminal transition, spawn a fresh agent using the available agent-delegation capability. Do not merely recommend the next command and do not run the next stage in the same agent.

Stage 0 is the sole handoff exception to the project-root field because the project does not exist yet. Its handoff must provide the absolute professor-source path or selected working context, the intended project-parent context if known, and the verified pipeline Python path. Stage 1 creates the project root; all later handoffs must provide it.

Give the new agent a handoff containing:

- the absolute project-root path;
- the completed stage and verified state flags;
- the verified Python executable and dependency-preflight status;
- the exact next skill to invoke;
- the artifacts it must read;
- unresolved warnings, uncertainties, and cultural-review flags;
- an instruction not to redo completed stages.

Use this handoff shape:

```text
Continue the Dreaming Course Pipeline in a fresh agent.
Project root: <absolute path>
Completed stage: <stage and skill>
Verified state: <relevant flags>
Artifacts: <paths>
Warnings/flags: <items or none>
Invoke and follow: $<next-skill>
Read that skill and the shared pipeline contract completely. Do not redo completed stages.
```

Confirm that the new agent was dispatched. If delegation is unavailable or fails, report the blocker and exact next skill; never claim the handoff succeeded.

## Human-review semantics

Do not require a magic approval phrase. Accept natural-language permission when the current context makes the user's intent to proceed clear and no requested changes remain. Infer narrowly: enthusiasm, impatience, slang, or minor typos can still be approval when the action is unambiguous, but an ambiguous response requires one concise clarification.

Record the user's wording and timestamp in the relevant review file. A request for changes keeps the review loop open. Examples such as “go ahead and make the PowerPoint,” “just do the thing,” or “I'm alright; I'll fix it myself” can close image review when they clearly mean no more agent revisions are requested and the current images should be used.
