from abc import ABC, abstractmethod

class phoneType(ABC):

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def tell(self):
        pass

    @abstractmethod
    def screenSize(self):
        pass

class Apple(phoneType):
    def __init__(self, size):
        self.size = size
    
    def show(self):
        print("You have an iPhone")

    def tell(self):
        print("You have an iPhone 15")
    
    def screenSize(self):
        print(f"The size of your screen is: {self.size} inches")

class Android(phoneType):
    def __init__(self, size):
        self.size = size
    
    def show(self):
        print("You have an Android")

    def tell(self):
        print("You have a Samsung Galaxy S24")
    
    def screenSize(self):
        print(f"The size of your screen is: {self.size} inches")

def main():
    Person1 = Android(size=6.2)
    Person1.show()
    Person1.tell()
    Person1.screenSize()

    Person2 = Apple(size=6.12)
    Person2.show()
    Person2.tell()
    Person2.screenSize()

if __name__ == "__main__":
    main()

