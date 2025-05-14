from MorseConstants import MORSE
from ConsoleEmitter import ConsoleEmitter

import sys


input = sys.argv[1]
emitter = ConsoleEmitter(1)

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