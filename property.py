from collections.abc import Iterable
class Boxer:
    def __init__(self, name, stance):
        self._name = name
        self._stance = stance
    
    @property
    def details(self):
        return self._name, self._stance

    @details.setter
    def details(self, new_details):
        if not isinstance(new_details, str):
            inp1 , inp2 = new_details
        else: 
            inp1=new_details
            inp2="No answer"
        self._name = inp1
        self._stance = inp2


def main():
    boxer = Boxer("Gervonta Davis", "Southpaw")

    print("Boxer details (using properties):", boxer.details)

    boxer.details = "Jaron Ennis"
    print("Boxer details after change (using properties):", boxer.details)

    boxer.details = ["Jaron Boots Ennis" , "Orthodox"]
    print("Boxer details after change:", boxer.details)

if __name__ == "__main__":
    main()
