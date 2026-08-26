# Execution Permissions

Use ordinary sandboxed execution for normal project discovery, hashing, copying, parsing, image processing, manifest writing, and other work inside approved workspace paths.

Use Codex's **outside-sandbox/elevated command execution mode** for the two boundary operations below. Here, "elevated" means execution outside the Codex filesystem/process sandbox in the user's normal desktop session. It does **not** mean an Administrator shell and does not authorize unrelated system changes.

## Operations that require outside-sandbox execution

1. Creating or updating the dedicated pipeline virtual environment when its path is outside the current writable workspace, and downloading or installing its packages when network/package-install access is required.
2. Launching or automating locally installed Microsoft PowerPoint:
   - Windows: every `pywin32` COM probe, version query, source-deck export, and final-deck QA export.
   - macOS: every `/usr/bin/osascript` command that resolves, launches, queries, or automates Microsoft PowerPoint.

Do not run a known Office-automation command inside the sandbox first merely to demonstrate that it fails. Before executing it, use the command tool's approval mechanism and request outside-sandbox execution—for example, `sandbox_permissions: "require_escalated"` when that field is available—with a concise explanation of the exact Office or dependency operation. Do not request a blanket reusable approval for arbitrary Python execution.

If the active permission profile disables or rejects outside-sandbox execution, stop at that boundary and report it as an **execution-permission blocker**. Include the attempted operation and the required execution mode. Do not misdiagnose the result as missing PowerPoint, broken COM registration, or a corrupt deck; do not repeatedly retry in the sandbox; and do not fall back to a Codex Presentations connector, computer use, GUI clicking, or an unapproved renderer.

After permission is granted, retry the operation once through the outside-sandbox path. A direct command for the user to run manually may be offered only as a diagnostic fallback when Codex cannot request the needed mode; it is not the normal pipeline route.

## Windows COM requirements

Run the PowerPoint helper with the exact pipeline virtual-environment Python. The helper must:

1. call `pythoncom.CoInitialize()` before creating any COM object;
2. create an isolated instance with `win32com.client.DispatchEx("PowerPoint.Application")`;
3. suppress macros where supported and avoid opening a presentation window;
4. work only on the pipeline copy or generated final deck;
5. close the presentation and call `PowerPoint.Application.Quit()` in `finally`; and
6. call `pythoncom.CoUninitialize()` in final cleanup.

A Windows error such as `0x80070520` ("A specified logon session does not exist") from a sandboxed process is evidence of the wrong execution context. Request outside-sandbox execution instead of asking the user to reinstall or restart PowerPoint.

## macOS automation requirements

Run the Python process that invokes `/usr/bin/osascript` through the outside-sandbox path so it shares the user's desktop session and can request macOS Automation permission. The user may still need to approve the operating system's one-time permission for the calling host to control Microsoft PowerPoint. Do not use Administrator privileges, `System Events`, keystrokes, menu selection, mouse actions, or computer use.
