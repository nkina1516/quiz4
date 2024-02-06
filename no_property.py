class RandomGuess:
    def __init__(self, name, num):
        self._name = name
        self._num = num

    def lets_see(self):
        return self._name, self._num

    def update_guess(self, new_info):
        if not isinstance(new_info, int) or new_info < 5:
            print(f"{self._name}, try again. Your number should be greater than or equal to 5.")
        else:
            self._num = new_info
            print(f"{self._name}, your new number is {self._num}")

def main():
    guesser1 = RandomGuess("Jake", 5)
    print("Current state:", guesser1.lets_see())

    guesser1.update_guess(3)
    guesser1.update_guess(4)  
    print("Updated state:", guesser1.lets_see())

    guesser2 = RandomGuess("Roland", 2)
    print("Current state:", guesser2.lets_see())

if __name__ == "__main__":
    main()

