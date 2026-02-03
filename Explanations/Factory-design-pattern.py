from abc import ABC, abstractmethod
#ABC = Abstract Base Class
#Python does not have an interface keyword like Java, so we use ABC and @abstractmethod to play that role.

#step 1 : Define the product interface
class Coffee(ABC): # Coffee is an interface (conceptually) Why? We CANNOT create Coffee() , It contains no logic ,It enforces a rule ,any Coffee class MUST have prepare()
    @abstractmethod
    def prepare(self): # An abstract method Just a signature, Forces child classes to implement it ,❌ If a class inherits from Coffee without prepare() → ERROR
        pass
   
   
   
#step 2 : Create concrete product classes
class Espresso (Coffee): #They implement the Coffee interface.
    def prepare(self):
        return "preparing Espresso with love."
    
class Cappuccino (Coffee): #They implement the Coffee interface.
    def prepare(self):
        return "preparing a Cappuccino with passion."
    
    
class Latte (Coffee): #They implement the Coffee interface.
    def prepare(self):
        return "preparing a Latte ."

#step 3 : Create the factory class
class CoffeeMachine:
    def make_coffee(self,coffee_type):
              if coffee_type=="Espresso":
                  return Espresso().prepare()
              elif coffee_type == "Latte":
                 return Latte().prepare()
              elif coffee_type == "Cappuccino":
                  return Cappuccino().prepare()
              else:
                  return "Unknown coffee type!" 
# Role of the Factory
# - Centralize object creation
# - Hide the creation logic
# - Return a consistent product   


       
#step 4: Use the Factory to create Products
if __name__ == "__main__":
    machine = CoffeeMachine()
    coffee  = machine.make_coffee('Espresso')
    print(coffee)  # Output: preparing Espresso with love.
    
    coffee  = machine.make_coffee('Latte')
    print(coffee)  # Output: preparing a Latte .

    coffee  = machine.make_coffee('Cappuccino')
    print(coffee)  # Output: preparing a Cappuccino with passion.