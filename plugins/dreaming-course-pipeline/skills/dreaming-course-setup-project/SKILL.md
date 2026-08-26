---
name: dreaming-course-setup-project
description: Create and verify the protected working copy for a new Dreaming-inspired course-production project, then automatically hand it to the organization skill in a fresh agent.
---

# Stage 1 - Create Working Copy

Read `../../references/pipeline-contract.md` completely before acting.

## Create and verify

1. Identify the professor's source dump from the user's selection or the single unambiguous candidate in the current workspace. Ask only if multiple plausible folders exist.
2. Create a clearly named project folder outside the source dump and build the standard project structure from the contract.
3. Copy every source file and subdirectory into `00_source_original/`. Preserve filenames, extensions, relative paths, and bytes. Never move, rename, normalize, or edit the source dump.
4. Initialize `pipeline_state.json` from the contract and set `project_name`.
5. Compare source and copy by relative path, file count, byte size, and cryptographic hash. Record discrepancies and copy errors.
6. Set `source_copy_created` to true only when the copy is complete and exact. Record the source path, project path, count, verification result, and timestamp.

## Automatic handoff

After successful verification, follow the contract's agent handoff protocol. Spawn a fresh agent and instruct it to invoke `$dreaming-course-organize`. Include the absolute project root, verified `source_copy_created: true`, source/copy inventory details, and any warnings. Do not organize files in this agent and do not ask the user to start Stage 2 manually.
