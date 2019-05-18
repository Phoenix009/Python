class LogicGate:
    def __init__(self, name):
        self.label = name
        self.output = None

    def getlabel(self):
        return self.label

    def getoutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def getpinA(self):
        if self.pinA is None:
            return int(input("Enter the pin value A for gate " + str(self.getlabel()) + " : "))
        else:
            return self.pinA.getFrom().getoutput()

    def getpinB(self):
        if self.pinB is None:
            return int(input("Enter the pin value b for gate " + str(self.getlabel()) + " : "))
        else:
            return self.pinB.getFrom().getoutput()


    def setNextPin(self, source):
        """source should be a Connector object"""
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("!!NO EMPTY PINS!!")


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("!!NO EMPTY PINS!!")

    def getPin(self):
        if self.pin is None :
            return int(input("Enter the pin value for gate " + str(self.getlabel()) + " : "))
        else:
            return self.pin.getFrom().getoutput()


class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        self.pinA = self.getpinA()
        self.pinB = self.getpinB()
        return self.pinA and self.pinB


class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        self.pinA = self.getpinA()
        self.pinB = self.getpinB()
        return self.pinA or self.pinB


class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)
        self.pin = None

    def performGateLogic(self):
        self.pin = self.getPin()
        return int(not self.pin)


class Connector:
    def __init__(self, fromgate, togate):
        self.fgate = fromgate
        self.tgate = togate

        self.tgate.setNextPin(self)

    def getFrom(self):
        return self.fgate

class NandGate(AndGate):
    def __init__(self, n):
        AndGate.__init__(self, n)

    def performGateLogic(self):
        return int(not AndGate.performGateLogic(self))

class NorGate(OrGate):
    def __init__(self, n):
        OrGate.__init__(self, n)

    def performGateLogic(self):
        return int(not OrGate.performGateLogic(self))


g1 = NorGate("G1")
g2 = NotGate("G2")
c1 = Connector(g1, g2)
print(g2.getoutput())


