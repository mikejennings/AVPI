# WoW: Forever voice starter for Windows

A first-session profile for playing with a mouse and voice. This is a configuration for the existing GAVPI application, not a new executable. It has not yet been tested in the Windows app or the WoW: Forever client.

## Get started together

1. Download and extract the upstream GAVPI release linked in the repository README. Keep all files from its ZIP together. Download `Profiles/WoW-Forever-Starter.xml` from this branch too.
2. Open GAVPI, select **File > Open Profile**, and load that XML.
3. Before listening, select **Profile > Modify**, then **Associate With... > Browse...** and choose the actual WoW: Forever game executable on this PC, not the Battle.net launcher. Save the profile locally. The executable path is machine-specific, so it is intentionally absent from the shared XML. Without this association, commands can send keys to whichever application is focused.
4. In WoW's key bindings, explicitly set or confirm the bindings below. They are proposed bindings, not verified Forever defaults. Put suitable abilities in the six matching action bar slots. Put a mount in another slot and bind that slot to F8 when a mount is available.
5. In GAVPI Settings select the installed English speech recognizer and voice. Start with push-to-talk **Off** so no keyboard key needs to be held. Use the **Listen** and **Stop** buttons with the mouse. If ordinary conversation triggers commands, try **Toggle** mode with an unused key mapped to a spare gaming-mouse button using the mouse software; verify that mapping works before relying on it.
6. Test somewhere quiet and out of combat. Begin with “map”, “bags”, and “jump”, then add targeting and abilities. Check the Recognized column when a phrase misses. Stop listening before typing into chat: executable association does not distinguish game chat from gameplay.

## Suggested bindings

| Say | Key sent | Bind this in WoW |
| --- | --- | --- |
| ability one … ability six | 1 … 6 | Corresponding six action bar slots |
| target | Tab | Target next enemy |
| jump | Space | Jump |
| bags | B | Toggle bags |
| map | M | Toggle world map |
| character | C | Toggle character panel |
| cancel | Escape | Escape / close current panel |
| mount | F8 | Action bar slot containing the chosen mount |

The mouse remains available for movement and camera control using the player's preferred in-game bindings. Keep the most time-sensitive abilities on comfortable mouse buttons where possible; measure voice response in practice before relying on it for interrupts or emergencies.

## Personalize after the first session

Change phrase triggers in **Profile > Modify** to words the player finds comfortable. For example, rename a numbered ability to its spell name after picking a class. Keep phrases distinct and start with a small vocabulary. Stop listening while editing, then save and restart listening to reload the vocabulary.

Each phrase produces one brief key stroke (key down, 60 ms wait, key up). There are no repeated casts, held movement keys, or automatic combat rotations. “cancel” sends Escape; it does not stop the microphone or reliably stop character movement. Use GAVPI's Stop button to stop listening. Do not remove the release action when changing a sequence.

## Windows acceptance check

- Profile opens without errors; all 13 phrases appear.
- “map”, “bags”, and “jump” perform the intended single action with the game focused.
- Each numbered command activates only its assigned slot.
- After associating the executable, speaking a command with another application focused sends no input there.
- Stop disables recognition; restarting Listen restores it.
- Test a normal voice-chat conversation and adjust phrases or toggle mode if needed.

These checks still need to be performed on the player's Windows PC. This profile does not establish approval under the game's input policies.
