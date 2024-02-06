from dataclasses import dataclass

@dataclass
class Student:
    Number: str

def main():
    students = [
        ("12", "14", "1", "12345"),
        ("Harley Waffleman", "2007", "Criminal Justice", "MeCant University")
    ]

count = Student.count(0)
print("length of first position:",count)

if __name__ == "__main__":
    main()
