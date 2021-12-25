'''
I => Interface-Segregation Principle
Make fine grained interfaces that are client specific.
Clients should not be forced to depend upon interfaces that they do not use.
This principle deals with the disadvantages of implementing big interfaces.

Interfaces should be granularly split and be as small as possible
'''
class Mobile():
     def voice(self):
          raise NotImplementationError
     def text(self):
          raise NotImplementationError
     def camera(self):
          raise NotImplementationError

class BestMobile():
     def voice(self):
          raise NotImplementationError
     def text(self):
          raise NotImplementationError
     def camera(self):
          raise NotImplementationError

class OldMobile():
     def voice(self):
          raise NotImplementationError
     def text(self):
          raise NotImplementationError
    def camera(self):
          raise NotImplementationError


'''
In old mobiles we don't find any camera, it will not implement this.
'''



from abc import ABC,abstractmethod

class Phone(ABC):
     @abstractmethod
     def voice(self):
          pass
     
class Text(ABC):
     @abstractmethod
     def text_message(self):
          pass

class Camera(ABC):
     @abstractmethod
     def photo(self):
          pass

class BestPhone(Phone,Text,Camera):
     def voice(self):
          #implementation
     def text_message(self):
          #implementation
     def photo(self):
          #implementation

class OldPhone(Phone,Text):
     def voice(self):
          #implementation
     def text_message(self):
          #implementation
     
class Pager(Text):
     def text_message(self):
          #implementation


'''
We can use the interfaces to get different properties to mobiles.
'''




     
          
