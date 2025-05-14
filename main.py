from MorseConstants import MORSE
from PyLedEmitter import PyLedEmitter

import sys


input = sys.argv[1]
emitter = PyLedEmitter(1)

for char in input:
    for signal in MORSE[char.capitalize()]:
        match signal:
            case ".":
                emitter.emitDot()
            case "-":
                emitter.emitDash()
            case _:
                emitter.pauseBetweenWord()

        emitter.pauseBetweenLetterPart()

    emitter.pauseBetweenLetter()