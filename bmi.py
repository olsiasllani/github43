from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age, weight, height):
     self.name = name
     self.age = age
     self._weight = weight
     self._height = height

     @property
     def weight(self):
         return self._weight

     @weight.setter
     def weight(self, value):
         if value < 0:
             raise ValueError("Weight cannot be negative")
         self._weight = value

         @property
         def height(self):
             return  self._height

         @height.setter
         def height(self, value) :
             if value < 0 :
                 raise ValueError("Height cannot be negative")
             self._height = value
             
             @abstractmethod
             def calculate_bmi(self):
                 
                 pass
             
             @abstractmethod
