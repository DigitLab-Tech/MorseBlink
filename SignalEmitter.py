from abc import ABC, abstractmethod
from MorseConstants import MORSE_BETWEEN_LETTER_PART_LENGHT, MORSE_BETWEEN_LETTER_LENGHT, MORSE_BETWEEN_WORD_LENGHT
import time

class SignalEmitter(ABC):
      def __init__(self, unitDuration: float):
            self.unitDuration = unitDuration

      @abstractmethod
      def emitDot(self):
        pass

      @abstractmethod
      def emitDash(self):
        pass
    
      def pauseBetweenLetterPart(self):
        time.sleep(self.unitDuration * MORSE_BETWEEN_LETTER_PART_LENGHT)

      def pauseBetweenLetter(self):
        time.sleep(self.unitDuration * MORSE_BETWEEN_LETTER_LENGHT)

      def pauseBetweenWord(self):
        time.sleep(self.unitDuration * MORSE_BETWEEN_WORD_LENGHT)