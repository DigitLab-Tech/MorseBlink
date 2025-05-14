
import time
import gpiod

from gpiod.line import Direction, Value
from SignalEmitter import SignalEmitter
from MorseConstants import MORSE_DOT_LENGHT, MORSE_DASH_LENGHT

class PyLedEmitter(SignalEmitter):
    def __init__(self, unitDuration: float):
        self.line = 17
        self.unitDuration = unitDuration
        self.chip = "/dev/gpiochip0"
        self.consumer = "PyLedEmitter"
        self.config = {
            self.line: gpiod.LineSettings(
                direction=Direction.OUTPUT, output_value=Value.ACTIVE
            )
        }

    def emitDot(self):
        with gpiod.request_lines(
            self.chip,
            consumer = self.consumer,
            config = self.config
        ) as request:
             request.set_value(self.line, Value.ACTIVE)
             time.sleep(self.unitDuration * MORSE_DOT_LENGHT)
             request.set_value(self.line, Value.INACTIVE)

    def emitDash(self):
        with gpiod.request_lines(
            self.chip,
            consumer = self.consumer,
            config = self.config
        ) as request:
             request.set_value(self.line, Value.ACTIVE)
             time.sleep(self.unitDuration * MORSE_DASH_LENGHT)
             request.set_value(self.line, Value.INACTIVE)
