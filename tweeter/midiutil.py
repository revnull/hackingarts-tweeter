'''
Utility functions for composing MIDI messages, etc.

Reference: http://www.midi.org/techspecs/midimessages.php
'''

## MIDI Message constants
#
# Channel voice messages.  The second nibble gets set with the channel.
NOTE_OFF       = 0b10000000
NOTE_ON        = 0b10010000
POLY_KEY_PRES  = 0b10100000  # Polyphonic key pressure (Aftertouch)
C_CHANGE       = 0b10110000  # Controller change
PROG_CHANGE    = 0b11000000
CHAN_PRESS     = 0b11010000  # Channel pressure (Aftertouch)
PITCH_WHEEL    = 0b11100000  # Pitch wheel change

__all__ = [
           'all_notes_off', 'reset_all_controllers', 'note_on', 'note_off',
           'poly_key_press', 'controller_change', 'program_change',
           'channel_press', 'pitch_wheel'
           ]

def all_notes_off(channel):
    return [C_CHANGE | (_ch(channel) - 1), 123, 0]

def reset_all_controllers(channel):
    return [C_CHANGE | (channel - 1), 121, 0]

def note_on(channel, note, velocity):
    return [NOTE_ON | (_ch(channel) - 1), _7bit(note), _7bit(velocity)]

def note_off(channel, note):
    return [NOTE_OFF | (_ch(channel) - 1), _7bit(note), 0]

def poly_key_press(channel, note, val):
    return [POLY_KEY_PRES | (_ch(channel) - 1), _7bit(note), _7bit(val)]

def controller_change(channel, cont_num, val):
    if not 0 <= cont_num <= 119:
        raise Exception("Invalid controller number %s" % cont_num)
    return [C_CHANGE | (_ch(channel) - 1), cont_num, _7bit(val)]

def program_change(channel, program):
    return [PROG_CHANGE | (_ch(channel) - 1), _7bit(program)]

def channel_press(channel, val):
    return [CHAN_PRESS | (_ch(channel) - 1), _7bit(val)]

def pitch_wheel(channel, lsb, msb):
    return [PITCH_WHEEL | (_ch(channel) - 1), _7bit(lsb), _7bit(msb)]

def _ch(channel):
    if not 1 <= channel <= 16:
        raise Exception("Channel %s is out of range" % channel)
    return channel

def _7bit(n):
    if not 0 <= n <= 127:
        raise Exception("Value %s is not 7-bit" % n)
    return n
