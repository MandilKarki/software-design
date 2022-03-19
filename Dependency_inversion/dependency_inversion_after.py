from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("Lightbulb: turned on....")

    def turn_off(self):
        print("Lightbulb: turned of....")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on....")

    def turn_off(self):
        print("Fan: turned of....")


class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()