# Dreaming Course Pipeline for Codex

The local skill edition of Dreaming Studio: keep the lecture, add complete illustrated teaching stories immediately before the concepts they explain. No web-app account, n8n, Supabase or private API server is required.

## Install from GitHub

```sh
codex plugin marketplace add arpandrv/dreaming-course-pipeline-marketplace --ref main
codex plugin add dreaming-course-pipeline@dreaming-course-pipeline-marketplace
```

For an already installed marketplace:

```sh
codex plugin marketplace upgrade dreaming-course-pipeline-marketplace
codex plugin add dreaming-course-pipeline@dreaming-course-pipeline-marketplace
```

Open a new Codex task after installation/update and provide your source folder:

```text
Use $dreaming-course-preflight with my course folder.
```

## Workflow

0. Preflight: verify Python, install missing packages in a dedicated environment, check local renderer.
1. Setup: protected, hash-verified source copy.
2. Organize: classify sources and record every outcome.
3. Process: slide/page images, selectable text or OCR where needed, verbatim notes and Markdown evidence.
4. Blueprint: full causal story, exact visible passages, technical mapping and insertion anchors. Review/revise here.
5. Images: generate only new story frames. Review and revise selected images here.
6. Build: insert accepted frames into original teaching decks, preserve order and notes, render and verify.

Successful stages use fresh agent handoffs when available. Review stays in the same conversation. Existing skill names remain valid; there are no legacy prompt files or separate confirmation skills.

The story is not a quote-card preface. Characters experience a goal, failed attempt, consequence, discovery and resolution, followed by an explicit academic bridge. The whole story appears in readable captions/dialogue. Original educational fiction is clearly labelled; the unchanged bundled Dharawal stories remain optional attributed references, not a forced quota.

Original PPTX teaching slides are retained, not regenerated as images. Multiple source decks default to separate augmented outputs; PDF pages remain non-editable images. The build reports any feature-fidelity limitations.

## Local requirements

- Codex reasoning, image generation and local command execution. A skill does not grant access to an unavailable image tool or bypass approval controls.
- Windows: installed Microsoft PowerPoint with pywin32 COM.
- macOS: installed Microsoft PowerPoint with osascript/AppleScript and macOS Automation permission.
- Linux: LibreOffice Impress headless export to PDF, then PyMuPDF to images.
- Python packages: requirements.txt, verified/installed by scripts/check_dependencies.py in a dedicated virtual environment, not Codex's managed runtime.

Office automation requests scoped outside-sandbox execution in the user's desktop session. Normal project work remains sandboxed; Linux headless export uses ordinary permitted execution. Missing applications, permissions, packages or unsupported features are reported distinctly.

## Package checks

```sh
python -m unittest discover -s tests
python plugins/dreaming-course-pipeline/scripts/validate_insertions.py /path/to/03_blueprint/insertion_plan.json
```

The first command runs from the repository root. The plan validator checks real source anchors, sequence continuity, identities and complete text fields; professor review still assesses story quality and technical accuracy.
