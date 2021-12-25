'''
L => Liskov-Substitution Principle
"Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."
A derived class can assume the place of its super class, and everything should work.
'''
class Kitchenappliance:
     def on():
          pass
     def off():
          pass
     def setTemp():
          pass

class Toaster(kitchenappliance):
     def on():
          pass
     def off():
          pass
     def setTemp():
          pass

class Juicer(kitchenappliance):
     def on():
          pass
     def off():
          pass

'''
Above our principle not following because here Juicer doesn't have property temperature.
'''

class Kitchenappliance:
     def on():
          pass
     def off():
          pass

class KitchenApplianceWithApp(Kitchenappliance):
     def set_temp():
          pass

class Toaster(KitchenApplianceWithApp):
     def on():
          pass
     def off():
          pass
     def set_temp():
          pass

class Juicer(Kitchenappliance):
     def on():
          pass
     def off():
          pass

'''
Here it follows the LSP without missing it properties in super class
'''
