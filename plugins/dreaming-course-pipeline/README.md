# Dreaming Course Pipeline for Codex

This plugin packages a seven-stage course-production workflow beginning with dependency preflight. The user starts Stage 0 once; successful stages automatically hand the project to fresh agents until a human review is required.

## Install

Add the folder containing `.agents/plugins/marketplace.json` as a local marketplace:

```powershell
codex plugin marketplace add "C:\path\to\dreaming-course-pipeline-marketplace"
```

Restart Codex, open the Plugins directory, and install **Dreaming Course Pipeline**. To share it, send the entire `dreaming-course-pipeline-marketplace` folder or publish it in a Git repository.

## Start the pipeline

Select the plugin and provide the source folder, or invoke the entry skill directly:

```text
$dreaming-course-preflight
```

The automatic chain is:

0. `$dreaming-course-preflight` — verifies Python, installs missing Python packages, and rechecks them
1. `$dreaming-course-setup-project`
2. `$dreaming-course-organize`
3. `$dreaming-course-process`
4. `$dreaming-course-blueprint` — pauses for iterative professor review
5. `$dreaming-course-generate-images` — pauses for iterative image review
6. `$dreaming-course-build-pptx`

Each completed non-review stage spawns a fresh agent with a structured handoff and invokes the next skill. The professor does not need to start each stage manually. If a handoff fails because agent delegation is unavailable, the current agent reports the blocker and the exact next skill instead of pretending the stage continued.

Stage 0 uses `requirements.txt` and the bundled dependency-check script to create or reuse a dedicated pipeline virtual environment, install only missing packages, run `pip check`, and verify the complete set. It does not modify Codex's bundled Python. Stage 3 uses `python-pptx` for speaker notes, installed Microsoft PowerPoint for PPTX-to-PDF export, and `PyMuPDF` for PDF-to-image rendering. Windows controls PowerPoint with `pywin32` COM. macOS controls PowerPoint from Python through built-in `osascript` and AppleScript after the user grants macOS Automation permission. Neither route uses a Codex PowerPoint/Presentations connector, computer use, GUI clicking, browser automation, Aspose, or a cloud document service.

## Platform requirements

- **Windows:** locally installed Microsoft PowerPoint and the Stage 0-installed `pywin32` package.
- **macOS:** locally installed Microsoft PowerPoint for Mac, built-in `/usr/bin/osascript` and `/usr/bin/sdef`, and one-time macOS Automation permission for the calling Codex/Python host. PowerPoint may launch or appear briefly, but the pipeline does not click or type in it.
- **Linux and other platforms:** no approved renderer; preflight stops before creating a project.

## Bundled story library

The plugin includes the curated Dharawal story transcriptions in `references/Dharawal_story_transcriptions/`. The blueprint stage reads the complete library, selects at least one suitable story, and incorporates it with attribution and source traceability. A blueprint containing no bundled story material fails validation. Professors do not have to provide the stories for each project.

## Cultural and editorial safeguards

The shared contract in `references/pipeline-contract.md` applies to every stage. It preserves originals, requires faithful ingestion, prevents invented or genericised cultural content, records failures, and places human review inside the blueprint and image-generation stages.
