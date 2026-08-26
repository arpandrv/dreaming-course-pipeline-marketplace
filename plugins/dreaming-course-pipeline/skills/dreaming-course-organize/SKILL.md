---
name: dreaming-course-organize
description: Inventory and classify the protected course-source copy, then automatically hand the project to the processing skill in a fresh agent.
---

# Stage 2 - Organize Source Files

Read `../../references/pipeline-contract.md` completely before acting.

## Preconditions

Require `dependencies_verified: true` and `source_copy_created: true`. Work only from `00_source_original/`; never touch the professor's original dump.

## Organize

1. Inventory every file recursively with relative path, extension, byte size, and detected type where useful. Use Python's built-in `pathlib`, `shutil`, `hashlib`, and `json` modules; these require no package installation.
2. Copy `.ppt`/`.pptx` to `01_organized/pptx/`, `.pdf` to `pdf/`, `.doc`/`.docx` to `docx/`, `.md`/`.markdown` to `markdown/`, and all other types to `others/`.
3. Do not move or delete source-copy files. Preserve names when possible. Resolve collisions with deterministic suffixes and record the mapping.
4. Write an inventory in `01_organized/` with source path, organized path, type, size, status, collision notes, and unreadable or unusual-file warnings.
5. Reconcile totals so every source file has exactly one recorded outcome.
6. Set `files_organized` to true only after successful reconciliation; record the timestamp and inventory path.

## Automatic handoff

After successful organization, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-process`. Include the absolute project root, verified dependency/source/organization flags, verified Python executable, inventory path, counts by type, collisions, unreadable or unusual files, and the requirement to use approved local non-interactive processing without PowerPoint/Presentations connectors or computer use. Do not process files in this agent and do not request a redundant readiness confirmation.
