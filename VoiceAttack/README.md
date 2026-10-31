# WoW: Forever rogue with VoiceAttack

A 20-command starting setup using SpecialEffect's mouse-and-voice approach. Keep the gaming mouse for movement and aiming; use voice for ability slots and menus. The short rogue names are suggestions and can be changed to whatever the player finds comfortable.

**Status:** files generated and structurally checked on macOS. Import into VoiceAttack 2.2, recognition, and gameplay have not been tested on a Windows PC. The files are ready for that test; they are not a claim of verified Forever compatibility.

## Files

- `WoW-Forever-Rogue.vap`: expanded XML VoiceAttack profile with 20 command entries and 36 spoken alternatives.
- `rogue-commands.csv`: editable phrase/key/spell list, also a manual setup fallback.
- `Rogue-Quick-Reference.html`: open in a browser to view or print the command sheet.
- `WINDOWS-CHECK.md`: record the first Windows test here.

No GAVPI installation is required. This is an independent adaptation of the control approach, not a SpecialEffect release or endorsement. It does not include their executable or packaged game settings.

## Set it up together

1. Install the current **stable VoiceAttack 2.2** from [voiceattack.com](https://voiceattack.com/). Start with the trial. Select the headset microphone and an installed English speech engine. Confirm the level meter moves. If no usable engine is available, follow VoiceAttack's [speech-engine guidance](https://voiceattack.com/alternate.aspx). Version 2.2 also offers [Vosk engines](https://voiceattack.com/vosk), currently labeled beta for English. Keep one speech-control app active while testing.
2. Turn **listening off** while configuring. In the trial, edit its existing profile and choose **Import Commands**, then select `WoW-Forever-Rogue.vap`. First select only `map`, `jump`, and `target`. Make room by removing unused demonstration commands; do not delete personal commands you want to retain. The trial retains only 20 command entries, so bring in the remaining 17 only after the first three work. Semicolon-separated phrases are alternative names for the same command, not extra actions. In a registered copy, **Import Profile** can load the whole file directly.
3. Choose the actual running game window/process as VoiceAttack's input target using its target selector / profile **Send commands to this target** option. Do not choose Battle.net or a browser page with WoW in its title. Imported commands use the active window until you configure this; target selection does not by itself guarantee commands are ignored outside the game and may focus the game. Pause listening before switching apps. Do not leave the test profile listening unattended.
4. In WoW, explicitly set Tab to next enemy, Space to jump, B to backpack, M to world map, C to character, P to spellbook, and L to quest log. Confirm Escape closes panels. These are proposed bindings; verify them in Forever's UI.
5. Enable an additional **non-paging action bar**, then bind its 12 buttons to `1 2 3 4 5 6 7 8 9 0 - =`. On clients that label it **Bottom Left Action Bar**, use that bar's individual button bindings. Place the spells in the order below, as each becomes available. Do not bind the voice keys only to the primary bar: entering stealth can replace its buttons. Remove conflicting old bindings through the game's UI and check that the additional bar stays unchanged in both states.
6. Turn listening on, focus the game somewhere quiet, and test “map”, “jump”, and “target”. Then import/test the other commands. If import fails, the CSV provides the exact manual fallback: create a command, enter the phrases separated by semicolons, add **Key Press**, choose the listed key, and press/release it for **0.10 seconds**. No loops or extra actions are needed.

The `.vap` uses the established expanded XML layout (`ExportVAVersion` 1.10.0) for import into current VoiceAttack; it was generated here, not exported by a running Windows copy. The CSV fallback is included in case the importer requires adjustment.

## Rogue slots

| Button / key | Main phrase | Spell to place on the additional bar |
| --- | --- | --- |
| 1 | sinister strike / strike | Sinister Strike |
| 2 | eviscerate / finish | Eviscerate |
| 3 | slice and dice / slice | Slice and Dice |
| 4 | stealth | Stealth |
| 5 | kick | Kick |
| 6 | gouge | Gouge |
| 7 | sprint | Sprint |
| 8 | evasion | Evasion |
| 9 | vanish | Vanish |
| 10 / 0 | sap | Sap |
| 11 / minus | ambush | Ambush |
| 12 / equals | backstab | Backstab |

Numbered alternatives preserve SpecialEffect's vocabulary: one through nine, zero, ten (minus), and eleven (equals). **“ten” does not press zero.** The quick-reference sheet shows every alias.

Leave slots for unlearned spells empty and add them later. An unavailable spell, insufficient energy/combo points, cooldown, wrong position, or unmet stealth requirement is an in-game condition; voice input does not bypass it. This is a general rogue leveling vocabulary, not a talent build or combat rotation. If a later build uses a different primary attack, update the slot and spoken names together.

Mirror Sinister Strike and Kick on comfortable mouse buttons if possible. Try Evasion or Vanish on another reachable button. Voice response must be measured before depending on it for urgent actions; the 0.10-second key duration is only the key hold time, not total speech latency.

## Conversation and movement

Use VoiceAttack's listening button, or configure its listening hotkey on an unused gaming-mouse button. Pause it before voice chat or typing in game chat. The word “escape” closes a panel; it does not mute recognition or stop movement. This starter sends no movement holds: use the mouse for movement, steering, and clicks. If the player wants voice movement later, configure and test that separately with a reliable stop action.

Each recognized phrase sends one key stroke. It never chooses abilities, reads game state, repeats a rotation, or presses several combat abilities from one utterance.

## If something does not work

- **No recognized command:** check the selected microphone/engine, listen toggle, and log. Try a shorter alias or the numbered alternative.
- **Recognized but no in-game action:** confirm the target and actual game binding; try Standard versus DirectX input mode. Test a longer key duration, such as 0.15 seconds. If the game runs elevated, VoiceAttack may need matching privileges; do not make elevation your first troubleshooting step.
- **Wrong spell after stealth:** rebind to the additional non-paging bar and check both stealth states.
- **Unexpected ability while talking:** pause listening; replace the short alias with a distinctive phrase or use a mouse listening toggle.

Complete [the Windows acceptance check](WINDOWS-CHECK.md) before treating the setup as working.

## Sources and what changed

- [SpecialEffect's WoW guide and gameplay demonstration](https://gameaccess.info/how-to-play-world-of-warcraft-with-voice-controls-draft/): original numbered slots, Tab targeting, mouse/voice use, and menu phrases. The original ZIP's `GAVPI/Profiles/WoW.XML` was downloaded and inspected on October 30, 2026.
- The adaptation preserves its number/key mappings and the eight menu/target/jump commands above. It adds rogue spell names and aliases, replaces the original short key holds with 0.10-second presses, and leaves the mouse responsible for movement. It does not copy their old `WTF` settings or require replacing account files.
- [VoiceAttack manual](https://www.voiceattack.com/VoiceAttackHelpV2.pdf): importing commands versus profiles, phrase alternatives, trial limit, and input targeting. [Official troubleshooting](https://voiceattack.com/howto.aspx): key duration and input modes.
- [Blizzard's Forever rogue deep dive](https://news.blizzard.com/en-us/article/24310968/world-of-warcraft-forever-class-deep-dives-rogue-and-warlock): rogue context. Final spell availability and bindings must be checked in the installed client.
- [Public XML format research](https://github.com/corinthian/voiceattack-vap-builder): field layout cross-check only; its code is not bundled or executed by this setup.

To regenerate after editing the CSV, run `python3 tools/build_rogue_voiceattack.py` from the repository root. Run `python3 tools/verify_rogue_voiceattack.py` afterward. These offline checks cannot establish Windows import or gameplay compatibility.
