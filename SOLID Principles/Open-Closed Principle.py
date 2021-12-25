'''
O => Open-Closed Principle
"Software entities ... should be open for extension, but closed for modification."
A class/function should be open for extension, and closed for modification.
'''

class Storage():
     def authenticate(self,client):
          if client=='aws':
               pass
          elif client=='azure':
               pass
          return client
     def upload(self,filename):
          if client=='aws':
               pass
          elif client=='azure':
               pass

'''
The functions authenticate, upload does not conform to the open-closed principle because it cannot be closed against new kinds of storage.
If we add a new storage, gcp, We have to modify the authenticate, upload functions.
You see, for every new storage, a new logic is added to the authenticate, upload functions. 
This is quite a simple example. When your application grows and becomes complex, 
you will see that the if statement would be repeated over and over again 
in the authenticate, upload functions each time a new storage is added, all over the application.
'''
class Storage():
     def authenticate(self,client):
          if client=='aws':
               pass
          elif client=='azure':
               pass
          elif client=='gcp':
               pass
          return client
     def upload(self,filename):
          if client=='aws':
               pass
          elif client=='azure':
               pass
          elif client=='gcp':
               pass

'''
How do we make it conform to OCP?
'''
from abc import ABC, abstractmethod
class Auth(ABC):
     @abstractmethod
     def authenticate(self):
          pass
class Uploader(ABC):
     @abstractmethod
     def upload_file(self):
          pass

class Aws(Auth, Uploader):
     def authenticate(self):
          pass
     def upload_file(self):
          pass

class Azure(Auth, Uploader):
     def authenticate(self):
          pass
     def upload_file(self):
          pass

class GCP(Auth, Uploader):
     def authenticate(self):
          pass
     def upload_file(self):
          pass


'''
Every storage adds its own implementation. 
Now, if we add a new storage, we doesn't change the methods need to change. 
All we need to do is add the new storage class.
Now conforms to the OCP principle.
'''
