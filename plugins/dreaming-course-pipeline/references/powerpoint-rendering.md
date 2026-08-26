# Local PowerPoint Rendering

Use this reference in Stage 0, Stage 3, and Stage 6 whenever PowerPoint must be probed or a PPTX must be rendered. Read `execution-permissions.md` first. Select exactly one route from the operating system recorded in `pipeline_state.json`. Never substitute a Codex PowerPoint/Presentations connector, computer use, GUI clicking, browser automation, or a cloud converter.

## Shared invariants

- Work only on the pipeline's copied input or generated output, never the professor's original dump.
- Request outside-sandbox execution before every PowerPoint probe or export. Do not perform a sacrificial sandboxed attempt first.
- Windows exports slides directly to PNG through PowerPoint COM. macOS exports to temporary PDF through AppleScript and uses `PyMuPDF` to render each page to a high-resolution PNG.
- Open source decks read-only where the platform API supports it.
- Suppress macro execution where the platform API supports it. If PowerPoint shows a security, repair, compatibility, password, or trust prompt, stop and record the blocker; do not click through it.
- Always close the opened presentation and terminate only the PowerPoint process created by the pipeline. Use cleanup code even after export failure.
- Verify that the rendered-image count exactly matches the PPTX slide count. On macOS, also verify that the PDF exists, is non-empty, and has the same page count before accepting rendered images.
- Record the operating system, PowerPoint version, automation method, outside-sandbox execution status, command/script path, intermediate PDF path when applicable, slide/page count, image dimensions, warnings, and errors in the relevant manifest.

## Windows route

Use the Stage 0-verified `pywin32` package and the exact pipeline Python. Run every COM command through Codex's outside-sandbox/elevated execution path in the user's normal desktop session. This is required even if a sandboxed probe appears worth trying; a sandbox may lack the interactive logon context that Office COM requires.

The helper must call `pythoncom.CoInitialize()`, create an isolated `PowerPoint.Application` with `win32com.client.DispatchEx`, disable macros where supported, keep the application non-visible, and open the copied PPTX read-only and without a presentation window. Export directly with `presentation.Export(output_folder, "PNG", width, height)`. Use `1600 x 900` for a 16:9 deck; for a different source aspect ratio, derive the height from `presentation.PageSetup.SlideWidth` and `SlideHeight` instead of stretching the slide. Normalize PowerPoint's generated filenames into the pipeline's `slide_NNN.png` convention only after confirming a complete export.

Close the presentation, quit the created PowerPoint application in `finally`, release COM references, and call `pythoncom.CoUninitialize()` in final cleanup. Do not terminate other PowerPoint instances. Treat `0x80070520` or another logon-session error from a sandboxed process as evidence that outside-sandbox execution is required, not as evidence of a missing application.

Do not use this route outside Windows. `pywin32` and PowerPoint COM are not available on macOS.

## macOS route

Use the built-in `/usr/bin/osascript` command from Python's `subprocess` module to send AppleScript commands to the locally installed **Microsoft PowerPoint** application. Run the invoking Python/`osascript` command through Codex's outside-sandbox execution path so it shares the user's desktop session and can request macOS Automation permission. This does not require a Python package such as `pywin32` or `aspose-slides`.

### Preflight requirements

Require all of the following before export:

1. `sys.platform == "darwin"`.
2. `/usr/bin/osascript` exists and is executable.
3. `/usr/bin/sdef` exists so the installed PowerPoint scripting dictionary can be inspected when terminology differs by version.
4. Microsoft PowerPoint for Mac is installed and `osascript -e 'id of application "Microsoft PowerPoint"'` resolves it.
5. macOS permits the calling host to automate Microsoft PowerPoint. A first automation attempt may display an operating-system permission prompt. Ask the user to grant that macOS Automation permission and retry once. If permission is denied or still unavailable, stop with the exact error; do not use computer use to bypass it.

The permission is an operating-system authorization, not permission to control PowerPoint through GUI clicking. Do not use `System Events`, keystrokes, menu selection, mouse actions, `activate`, or computer use.

### Invocation pattern

Call `osascript` from Python with the input and output paths as separate arguments. Do not interpolate or shell-escape user paths into AppleScript source.

The AppleScript should implement an `on run argv` handler that:

1. reads the PPTX path from `item 1 of argv` and the PDF path from `item 2 of argv`;
2. tells `Microsoft PowerPoint` to open the POSIX input file;
3. saves the active presentation to the POSIX output path using PowerPoint's `save as PDF` format;
4. closes that presentation without changing the PPTX; and
5. quits the PowerPoint instance after cleanup.

Use `/usr/bin/sdef <resolved-PowerPoint-app-path>` to confirm the installed version's `save`, `close`, and PDF-format terminology before executing the export. The commonly exposed PDF enumeration is `save as PDF`, but the installed scripting dictionary is authoritative. Build the subprocess as an argument array such as `[/usr/bin/osascript, <script-file>, <absolute-pptx>, <absolute-pdf>]` with `shell=False`, capture stdout/stderr, require a zero exit status, and use a bounded timeout.

PowerPoint may launch or appear briefly during AppleScript automation. Do not describe this route as headless. It is local programmatic application automation that requires no GUI interaction after macOS Automation permission is granted.

## Unsupported platforms

This plugin has no approved PowerPoint renderer for Linux or other operating systems. Stop during Stage 0 with an explicit unsupported-platform blocker rather than installing Aspose, LibreOffice, or another unapproved renderer.
