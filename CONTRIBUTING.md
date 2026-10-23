# Contributing

This is an experimental fan translation. Use issues for reports and pull requests for focused changes.

## Report a problem

Include the patch version, emulator and version, selected character, stage, and steps that trigger the problem. Add a screenshot showing the complete dialogue box. Say whether the problem is mistranslation, clipped text, a wrong portrait, or a progression failure.

Do not upload ROMs, emulator binaries, or save states to issues or pull requests. Describe the location instead. Untranslated Japanese text is expected at this stage.

## Translation changes

- Preserve the Japanese meaning and the speaker's tone. Do not summarize dialogue to fit a page.
- Use first names consistently for characters: Takao, Kai, Rei, Max, Daichi, Kyouju, and others. Use “White Tiger Clan” for 白虎族.
- Keep speaker IDs and scene order unchanged.
- The builder wraps English at 24 characters per line. Extra pages are allowed. A single newline forces a line break; a blank line forces a page break. Preserve {N1} on its own line when it appears.
- UI fields have smaller fixed capacities. Standard abbreviations such as `Lv.`, `Pow`, and `Sync` are acceptable in labels.
- Do not replace scenes containing unknown commands. Document and test those commands first.

## Validate changes

Run `python tools/build.py --rom "/path/to/original.gba"` without Python's `-O` option. Assertions are used for build checks. Test changed scenes in an emulator and record exactly what was exercised. A byte-matching IPS check confirms patch construction, not gameplay correctness.

Keep a clear distinction between natural progression tests and isolated scene-substitution tests. Neither implies the full game has been tested.
