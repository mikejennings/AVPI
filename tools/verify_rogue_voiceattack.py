#!/usr/bin/env python3
"""Offline consistency checks only. Does not run VoiceAttack or inject input."""
import csv
import json
from pathlib import Path
import uuid
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'VoiceAttack'
# Independent expected VK assignments: digits 0-9, OEM minus/plus, navigation.
EXPECTED = {'sinister strike': 49, 'eviscerate': 50, 'slice and dice': 51,
            'stealth': 52, 'kick': 53, 'gouge': 54, 'sprint': 55,
            'evasion': 56, 'vanish': 57, 'sap': 48, 'ambush': 189,
            'backstab': 187, 'target': 9, 'jump': 32, 'bags': 66,
            'map': 77, 'character': 67, 'spellbook': 80, 'quest log': 76,
            'escape': 27}


def verify():
    root = ET.parse(OUT / 'WoW-Forever-Rogue.vap').getroot()
    assert root.tag == 'Profile'
    cmds = root.findall('Commands/Command')
    assert len(cmds) == 20
    with (OUT / 'rogue-commands.csv').open(newline='', encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == len(cmds)
    assert root.findtext('UseProcessOverride') == 'false'  # Target setup documented, not preconfigured.
    seen = set()
    for cmd, row in zip(cmds, rows):
        name = cmd.findtext('CommandString')
        assert name == row['phrases']
        primary = name.split(';')[0]
        assert primary in EXPECTED
        for phrase in name.split(';'):
            assert phrase == phrase.strip() and phrase not in seen
            seen.add(phrase)
        assert cmd.findtext('Enabled') == 'true'
        assert cmd.findtext('UseSpokenPhrase') == 'true'
        assert cmd.findtext('UseShortcut') == cmd.findtext('UseMouse') == 'false'
        assert cmd.findtext('KeepRepeating') == 'false'
        assert cmd.findtext('RepeatType') == '0'
        assert all(cmd.findtext(tag) == 'false' for tag in
                   ('RepeatIfKeysDown', 'RepeatIfMouseDown', 'RepeatIfJoystickDown'))
        actions = cmd.findall('ActionSequence/CommandAction')
        assert len(actions) == 1, f'{primary}: unexpected extra action'
        action = actions[0]
        assert action.findtext('ActionType') == 'PressKey'
        assert action.findtext('Disabled') == 'false'
        assert action.findtext('Duration') == '0.1'
        assert action.findtext('InputMode') == '0'
        keys = action.findall('KeyCodes/unsignedShort')
        assert len(keys) == 1 and int(keys[0].text) == EXPECTED[primary] == int(row['key_code'])
        assert int(keys[0].text) not in (65, 68, 83, 87), 'No held/movement keys in starter'
        assert cmd.findtext('Description') == row['bind_to']
    ids = [node.text for node in root.iter('Id')]
    assert len(ids) == len(set(ids))
    for value in ids:
        uuid.UUID(value)
    # Preserve original SpecialEffect's unusual final two spoken-number mappings.
    aliases = {phrase: int(cmd.findtext('ActionSequence/CommandAction/KeyCodes/unsignedShort'))
               for cmd in cmds for phrase in cmd.findtext('CommandString').split(';')}
    assert [aliases[x] for x in ('one', 'zero', 'ten', 'eleven')] == [49, 48, 189, 187]
    assert len(seen) == 36
    report = {'offline_checks': 'passed', 'command_entries': len(cmds),
              'spoken_alternatives': len(seen), 'key_hold_seconds': 0.1,
              'windows_import': 'NOT TESTED', 'speech_recognition': 'NOT TESTED',
              'wow_forever_gameplay': 'NOT TESTED'}
    print(json.dumps(report, indent=2))
    return report


if __name__ == '__main__':
    verify()
