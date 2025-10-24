class Inverter:
    """A simple CMOS inverter model."""

    def __init__(self, name="inv"):
        self.name = name
        self.input = None
        self.output = None

    def connect(self, input_net):
        """Connect the inverter's input to a net."""
        self.input = input_net

    def logic(self):
        """Perform the logic operation of the inverter."""
        if self.input is None:
            raise ValueError("Input not connected")
        self.output = not self.input

    def __str__(self):
        return f"{self.name}: input={self.input}, output={self.output}"

if __name__ == '__main__':
    # Example usage
    inverter = Inverter()
    inverter.connect(True)
    inverter.logic()
    print(inverter)

    inverter.connect(False)
    inverter.logic()
    print(inverter)
