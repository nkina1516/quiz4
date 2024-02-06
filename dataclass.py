from dataclasses import dataclass

@dataclass
class Student:
    Name: str
    Year: str
    Major: str
    School: str

def main():
    Student1 = Student(Name="Brad Jones", Year="2004", Major="Theatre Studies", 
School="Kent University")
    Student2 = Student(Name="Harley Waffleman", Year="2007", Major="Criminal Justice", 
School="MeCant University")

    print("Student 1:", Student1.Name, "\n" "Year graduated:", Student1.Year, "\n" 
"Major:", Student1.Major, "\n" "Graduate From:", Student1.School, "\n")
    print("Student 2:", Student2.Name, "\n" "Year graduated:", Student2.Year, "\n" 
"Major:", Student2.Major, "\n" "Graduate From:", Student2.School, "\n")

if __name__ == "__main__":
    main()

