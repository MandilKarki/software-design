class LightBulb:
    def turn_on(self):
        print("lightbulb turned on")

    def turn_off(self):
        print("lightbulb turned off")


class ElectricPowerSwitch:
    def __init__(self, l: LightBulb):
        self.lightbulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightbulb.turn_off()
            self.on = False
        else:
            self.lightbulb.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()




