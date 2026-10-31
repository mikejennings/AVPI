#!/usr/bin/env python3
"""Build a dependency-free expanded XML .vap and a printable cheat sheet.

The serialized field names are VoiceAttack's XML interchange format. No original
SpecialEffect software or third-party generator code is included. Import and
speech/input behavior require acceptance testing in VoiceAttack on Windows.
"""
import csv
from html import escape
from pathlib import Path
import uuid
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'VoiceAttack'
NAMESPACE = uuid.UUID('2ba19dcb-8a12-4d09-83f9-2b5f72617720')
XSI = 'http://www.w3.org/2001/XMLSchema-instance'
ET.register_namespace('xsi', XSI)


def add(parent, tag, value):
    node = ET.SubElement(parent, tag)
    node.text = str(value).lower() if isinstance(value, bool) else str(value)
    return node


def fields(parent, values):
    for tag, value in values.items():
        add(parent, tag, value)


def ident(label):
    return str(uuid.uuid5(NAMESPACE, label))


def build():
    with (OUT / 'rogue-commands.csv').open(newline='', encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream))
    phrases = set()
    assert len(rows) == 20, 'Keep the starter within the trial command limit'
    for row in rows:
        row['phrases'] = row['phrases'].strip()
        for phrase in row['phrases'].split(';'):
            assert phrase and phrase == phrase.strip() and phrase not in phrases
            phrases.add(phrase)
        assert 1 <= int(row['key_code']) <= 254
    profile = ET.Element('Profile', {'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema'})
    fields(profile, {'Id': ident('profile'), 'Name': 'WoW Forever - Rogue - SpecialEffect approach'})
    commands = ET.SubElement(profile, 'Commands')
    for row in rows:
        name = row['phrases']
        cmd = ET.SubElement(commands, 'Command')
        ET.SubElement(cmd, 'Referrer', {f'{{{XSI}}}nil': 'true'})
        fields(cmd, {'ExecType': 3, 'Confidence': 0, 'PrefixActionCount': 0,
                     'IsDynamicallyCreated': False, 'TargetProcessSet': False,
                     'TargetProcessType': 0, 'TargetProcessLevel': 0, 'CompareType': 0,
                     'ExecFromWildcard': False, 'IsSubCommand': False, 'IsOverride': False,
                     'BaseId': ident(name + '-base'), 'OriginId': str(uuid.UUID(int=0)),
                     'SessionEnabled': True, 'Id': ident(name), 'CommandString': name})
        sequence = ET.SubElement(cmd, 'ActionSequence')
        action = ET.SubElement(sequence, 'CommandAction')
        fields(action, {'PairingSet': False, 'PairingSetElse': False, 'Ordinal': 0})
        ET.SubElement(action, 'ConditionMet', {f'{{{XSI}}}nil': 'true'})
        fields(action, {'IndentLevel': 0, 'ConditionSkip': False, 'IsSuffixAction': False,
                        'DecimalTransient1': 0, 'Id': ident(name + '-press'),
                        'ActionType': 'PressKey', 'Duration': '0.1', 'Delay': 0})
        add(ET.SubElement(action, 'KeyCodes'), 'unsignedShort', row['key_code'])
        fields(action, {'Context': '', 'X': 0, 'Y': 0, 'Z': 0, 'InputMode': 0,
                        'ConditionPairing': 0, 'ConditionGroup': 0, 'ConditionStartOperator': 0,
                        'ConditionStartValue': 0, 'ConditionStartValueType': 0,
                        'ConditionStartType': 0, 'DecimalContext1': 0, 'DecimalContext2': 0,
                        'DateContext1': '0001-01-01T00:00:00', 'DateContext2': '0001-01-01T00:00:00',
                        'Disabled': False})
        ET.SubElement(action, 'RandomSounds')
        ET.SubElement(action, 'ConditionExpressions')
        fields(cmd, {'Async': True, 'Enabled': True, 'Category': row['category'],
                     'Description': row['bind_to'], 'UseShortcut': False,
                     'keyValue': 0, 'keyShift': 0, 'keyAlt': 0, 'keyCtrl': 0, 'keyWin': 0,
                     'keyPassthru': True, 'UseSpokenPhrase': True, 'onlyKeyUp': False,
                     'RepeatNumber': 2, 'RepeatType': 0, 'CommandType': 0,
                     'SourceProfile': str(uuid.UUID(int=0)), 'UseConfidence': False,
                     'minimumConfidenceLevel': 0, 'UseJoystick': False, 'joystickNumber': 0,
                     'joystickButton': 0, 'joystickNumber2': 0, 'joystickButton2': 0,
                     'joystickUp': False, 'KeepRepeating': False, 'UseProcessOverride': False,
                     'ProcessOverrideActiveWindow': True, 'LostFocusStop': True,
                     'PauseLostFocus': False, 'LostFocusBackCompat': True, 'UseMouse': False,
                     **{f'Mouse{i}': False for i in range(1, 10)}, 'MouseUpOnly': False,
                     'MousePassThru': True, 'joystickExclusive': False,
                     'UseProfileProcessOverride': False, 'ProfileProcessOverrideActiveWindow': False,
                     'RepeatIfKeysDown': False, 'RepeatIfMouseDown': False,
                     'RepeatIfJoystickDown': False, 'AH': 0, 'CL': 0, 'HasMB': False,
                     'UseVariableHotkey': False, 'CLE': 0, 'EX1': False, 'EX2': False})
        ET.SubElement(cmd, 'InternalId', {f'{{{XSI}}}nil': 'true'})
        add(cmd, 'HasInput', True)
    fields(profile, {'OverrideGlobal': False, 'GlobalHotkeyIndex': 0,
                     'GlobalHotkeyEnabled': False, 'OverrideMouse': False, 'MouseIndex': 0,
                     'OverrideStop': False, 'StopCommandHotkeyEnabled': False,
                     'DisableShortcuts': False, 'UseOverrideListening': False,
                     'OverrideJoystickGlobal': False, 'GlobalJoystickIndex': 0})
    ET.SubElement(profile, 'ReferencedProfile', {f'{{{XSI}}}nil': 'true'})
    fields(profile, {'ExportVAVersion': '1.10.0', 'ExportOSVersionMajor': 10,
                     'ExportOSVersionMinor': 0, 'OverrideConfidence': False, 'Confidence': 0,
                     'CatchAllEnabled': False, 'InitializeCommandEnabled': False,
                     'UseProcessOverride': False, 'HasMB': False})
    ET.indent(profile, space='  ')
    ET.ElementTree(profile).write(OUT / 'WoW-Forever-Rogue.vap', encoding='utf-8', xml_declaration=True)
    body = '\n'.join('<tr><td>' + '</td><td>'.join(escape(x) for x in
                    (r['phrases'].replace(';', ' / '), r['key'], r['bind_to'])) + '</td></tr>' for r in rows)
    (OUT / 'Rogue-Quick-Reference.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8">
<title>WoW Forever Rogue — Voice commands</title>
<style>body{font:18px system-ui;max-width:1000px;margin:30px auto;padding:0 18px}table{border-collapse:collapse;width:100%}th,td{padding:8px;text-align:left;border-bottom:1px solid #bbb}h1{font-size:28px}@media print{body{font-size:12px;margin:0}th,td{padding:5px}}</style>
<h1>WoW Forever Rogue — Voice commands</h1>
<p>Mouse for movement. Say one command per action. Spells work only when learned and usable.</p>
<p>Bind abilities on an additional bar that stays the same in stealth. Test both states.</p>
<table><thead><tr><th>Say any of these</th><th>Key</th><th>Bind / place here</th></tr></thead><tbody>''' + body + '''</tbody></table>
<p>Pause VoiceAttack listening before chatting, typing or changing apps. Escape closes a panel; it does not stop movement or mute voice control.</p>
<p>Adapted from SpecialEffect’s numbered-slot and mouse/voice approach. This is an independent profile; Windows import and gameplay testing are pending.</p></html>''', encoding='utf-8')
    print(f'Built {len(rows)} commands with {len(phrases)} spoken alternatives; Windows import not tested.')


if __name__ == '__main__':
    build()
