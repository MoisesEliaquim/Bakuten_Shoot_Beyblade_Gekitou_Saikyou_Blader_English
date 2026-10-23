# Headerless dialogue continuations

Resources 605, 606, 609, and 610 begin directly with CP932 text. They contain no leading `FF` speaker command and terminate with `WWEE`, like the supported dialogue resources.

Their translation entries use `"speaker": null`. The builder validates that the original contains no speaker commands and emits the translated text without introducing an `FF` command. Headered resources continue to require an exact match with the original speaker sequence. Mixed resources that begin without a header but later change speakers remain unsupported.

For the version 0.17 isolated display checks, a fixture emits resource 604 with its terminal `WWEE` replaced by `PP`, then executes the translated continuation bytes unchanged. This establishes Kyouju's portrait and verifies that the continuation preserves it. The fixture modification is not present in the released patch.

The natural reward caller, including any contextual text or state it supplies, still needs gameplay verification. A successful continuation fixture is not evidence that the reward event has been reached naturally.
