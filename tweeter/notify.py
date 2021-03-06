
try:
    import rtmidi
except ImportError:
    import rtmidi_python as rtmidi

import time
import threading
import Queue
from . import midiutil

notes = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 0,
    'n': 1,
    'o': 2,
    'p': 3,
    'q': 4,
    'r': 5,
    's': 6,
    't': 7,
    'u': 8,
    'v': 9,
    'w': 10,
    'x': 11,
    'y': 0,
    'z': 1,
}

def note_to_midi(n):
    return notes.get(n.lower(), ord(n) % 12)

class NotifierThread(threading.Thread):
    def __init__(self, channel, queue):
        self.queue = queue
        self.midiout = rtmidi.MidiOut()
        self.midiout.open_port(0)
        self.midiout.send_message(midiutil.all_notes_off(channel))
        self.channel = channel
        threading.Thread.__init__(self)

    def run(self):
        while True:
            word = self.queue.get(True)
            self.play_word(word)

    def play_word(self,word):
        while word:
            notes = []
            octave = 3
            prev = -1
            for l in word[:10]:
                n = note_to_midi(l)
                if n <= prev:
                    octave += 1
                notes.append((l, 12 * octave + n))
                prev = n

            for (letter, note) in notes:

                if letter.isupper():
                    velocity = 120
                else:
                    velocity = 100

                self.midiout.send_message(midiutil.note_on(self.channel, note,
                                                           velocity))
                time.sleep(0.05)

            time.sleep(0.1)
            for (letter, note) in notes:
                self.midiout.send_message(midiutil.note_off(self.channel,
                                                            note))
                time.sleep(0.05)

            word = word[10:]

def spawn_notifier(channel = 10):
    queue = Queue.Queue()
    thread = NotifierThread(channel, queue)
    thread.daemon = True
    thread.start()
    return queue

