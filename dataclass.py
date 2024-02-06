from dataclasses import dataclass

@dataclass
class Student:
    Name: str
    Year: str
    Major: str
    School: str

def main():
    students=[
        Student("Brad Jones", "2004", "Theatre Studies", "Kent University"),
        Student("Harley Waffleman", "2007", "Criminal Justice", "MeCant University")
    ]
    
    print(students[0])
    print(students[1])

if __name__ == "__main__":
    main()

