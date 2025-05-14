from MorseConstants import MORSE
from PyLedEmitter import PyLedEmitter

import sys

input = sys.argv[1]
emitter = PyLedEmitter(0.3)

for char in input:
    print(char)

    for signal in MORSE[char.capitalize()]:
        print(signal)

        match signal:
            case ".":
                emitter.emitDot()
            case "-":
                emitter.emitDash()
            case _:
                emitter.pauseBetweenWord()

        emitter.pauseBetweenLetterPart()

    emitter.pauseBetweenLetter()








