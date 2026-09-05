---
name: dreaming-course-setup-project
description: After dependency preflight passes, create and verify the protected working copy for a new Dreaming-inspired course-production project, then automatically hand it to organization.
---

# Stage 1 - Create Working Copy

Read `../../references/pipeline-contract.md` completely before acting.

## Precondition

Require a Stage 0 handoff containing `dependency_preflight_passed: true`, operating system, verified PowerPoint automation method, Python executable, version, and successful package results. If this skill is invoked directly without that evidence, do not create a project. Spawn a fresh agent to invoke `$dreaming-course-preflight`, pass it the selected source path or current working context, and wait for its verified result. If delegation is unavailable, read/run preflight locally under the shared contract before setup.

## Create and verify

1. Identify the professor's source dump from the user's selection or the single unambiguous candidate in the current workspace. Ask only if multiple plausible folders exist.
2. Create a clearly named project folder outside the source dump and build the standard project structure from the contract. Use Python's `pathlib`, `shutil`, and `json` modules for deterministic local filesystem work.
3. Copy every source file and subdirectory into `00_source_original/`. Preserve filenames, extensions, relative paths, and bytes. Never move, rename, normalize, or edit the source dump.
4. Initialize `pipeline_state.json` from the contract. Set `project_name`, `dependencies_verified: true`, `operating_system`, `powerpoint_automation_method`, `python_executable`, and `dependency_versions` from the verified Stage 0 handoff.
5. Compare source and copy by relative path, file count, byte size, and SHA-256 using Python's `hashlib`. Record discrepancies and copy errors.
6. Set `source_copy_created` to true only when the copy is complete and exact. Record the source path, project path, count, verification result, and timestamp.

## Automatic handoff

After successful verification, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-organize`. Include the absolute project root, verified `source_copy_created: true`, source/copy inventory details, and any warnings. Use the shared contract's local-continuation fallback only if delegation is unavailable; do not ask the user to start Stage 2 manually.
