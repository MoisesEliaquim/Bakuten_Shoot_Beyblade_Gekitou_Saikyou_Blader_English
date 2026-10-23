# Validation policy

Starting with version 0.14, batches of short dialogue using an established format receive automatic validation and sampled visual review. An uninspected resource is not considered emulator-tested simply because its format matches a tested one.

Every batch must validate the original ROM identity, speaker sequence, supported commands, runtime-name command counts, text encoding, line widths, and scene endings. Independently applying the IPS must reproduce the generated ROM. These checks are inexpensive and remain mandatory.

Visual review prioritizes long text, pagination, dynamic names, new commands, and any font or engine changes. Short text using unchanged formats can be sampled. Release metadata records exactly which resources were inspected and any deferred checks.

Portable reconstruction may be deferred to milestone releases. Version 0.14 still includes this check because the existing release workflow runs it in a few seconds.

The final review must cover the campaign, alternate routes, natural post-battle triggers, saving and loading, and remaining visual coverage. Isolated resource substitution validates display and termination, not the natural gameplay trigger or a complete battle.
