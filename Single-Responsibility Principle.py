'''
SOLID design principles
It is a mnemonic acronym for five design principles intended to make software designs more understandable, flexible, and maintainable.
'''
'''
S => Single-responsibility principle
"There should never be more than one reason for a class to change".
In other words, every class should have only one responsibility.
'''

class Books():
     def __init__(self):
          self.books={}
          self.number=0
     def add_book(self, book):
          self.number+=1
          self.books[self.number]=book
     def store_books(self,filename):
          with open(filename, "w") as f:
               f.write(str(self.books))

'''
The Books class violates the SRP.
How does it violate SRP?
SRP states that classes should have one responsibility, here, we can draw out two responsibilities: books database management and books properties management. 
The constructor and add_book manage the Books properties while the save manages the Books storage on a database.
How will this design cause issues in the future?
If the application changes in a way that it affects database management functions. The classes that make use of Books properties will have to be touched and recompiled to compensate for the new changes.
You see this system smells of rigidity, it’s like a domino effect, touch one card it affects all other cards in line.
To make this conform to SRP, we create another class that will handle the sole responsibility of storing Books to a database:
'''
class Books():
     def __init__(self):
          self.books={}
          self.number=0
     def add_book(self, book):
          self.number+=1
          self.books[self.number]=book
class Storebooks():
     @staticmethod
     def store_books(filename,books):
          with open(filename, "w") as f:
               f.write(str(books))
'''
When designing our classes, we should aim to put related features together, 
so whenever they tend to change they change for the same reason. 
And we should try to separate features if they will change for different reasons. - Steve Fenton
'''


