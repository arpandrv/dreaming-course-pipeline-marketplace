# Dreaming Course Pipeline for Codex

This plugin packages a six-stage course-production workflow. The user starts Stage 1 once; successful stages automatically hand the project to fresh agents until a human review is required.

## Install

Add the folder containing `.agents/plugins/marketplace.json` as a local marketplace:

```powershell
codex plugin marketplace add "C:\path\to\dreaming-course-pipeline-marketplace"
```

Restart Codex, open the Plugins directory, and install **Dreaming Course Pipeline**. To share it, send the entire `dreaming-course-pipeline-marketplace` folder or publish it in a Git repository.

## Start the pipeline

Select the plugin and provide the source folder, or invoke the first skill directly:

```text
$dreaming-course-setup-project
```

The automatic chain is:

1. `$dreaming-course-setup-project`
2. `$dreaming-course-organize`
3. `$dreaming-course-process`
4. `$dreaming-course-blueprint` — pauses for iterative professor review
5. `$dreaming-course-generate-images` — pauses for iterative image review
6. `$dreaming-course-build-pptx`

Each completed non-review stage spawns a fresh agent with a structured handoff and invokes the next skill. The professor does not need to start each stage manually. If a handoff fails because agent delegation is unavailable, the current agent reports the blocker and the exact next skill instead of pretending the stage continued.

## Bundled story library

The plugin includes the curated Dharawal story transcriptions in `references/Dharawal_story_transcriptions/`. The blueprint stage reads the complete library, selects at least one suitable story, and incorporates it with attribution and source traceability. A blueprint containing no bundled story material fails validation. Professors do not have to provide the stories for each project.

## Cultural and editorial safeguards

The shared contract in `references/pipeline-contract.md` applies to every stage. It preserves originals, requires faithful ingestion, prevents invented or genericised cultural content, records failures, and places human review inside the blueprint and image-generation stages.
