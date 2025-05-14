from SignalEmitter import SignalEmitter

class ConsoleEmitter(SignalEmitter):
    def emitDot(self):
        print("Beep (dot)")

    def emitDash(self):
        print("Beeeeep (dash)")