# Local PowerPoint Rendering

Use this reference in Stage 3 and Stage 6 whenever a PPTX must be rendered. Select exactly one route from the operating system recorded in `pipeline_state.json`. Never substitute a Codex PowerPoint/Presentations connector, computer use, GUI clicking, browser automation, or a cloud converter.

## Shared invariants

- Work only on the pipeline's copied input or generated output, never the professor's original dump.
- Export the presentation to a temporary PDF, then use `PyMuPDF` to render each PDF page to a high-resolution PNG.
- Open source decks read-only where the platform API supports it.
- Suppress macro execution where the platform API supports it. If PowerPoint shows a security, repair, compatibility, password, or trust prompt, stop and record the blocker; do not click through it.
- Always close the opened presentation and terminate only the PowerPoint process created by the pipeline. Use cleanup code even after export failure.
- Verify that the PDF exists, is non-empty, and has exactly the same number of pages as the PPTX has slides before accepting rendered images.
- Record the operating system, PowerPoint version, automation method, command/script path, PDF path, page count, image dimensions, warnings, and errors in the relevant manifest.

## Windows route

Use the Stage 0-verified `pywin32` package to create an isolated `PowerPoint.Application` COM process. Disable macros, keep the application non-visible, open the copied PPTX read-only and without a presentation window, export it to PDF, close it, and quit the created COM process in `finally` cleanup.

Do not use this route outside Windows. `pywin32` and PowerPoint COM are not available on macOS.

## macOS route

Use the built-in `/usr/bin/osascript` command from Python's `subprocess` module to send AppleScript commands to the locally installed **Microsoft PowerPoint** application. This does not require a Python package such as `pywin32` or `aspose-slides`.

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
