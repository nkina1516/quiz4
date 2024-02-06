from dataclasses import dataclass

@dataclass
class Student:
    Name: str
    Year: str
    Major: str
    School: str
    
    def display_info(self):
        return f"Name: {self.Name}\nYear: {self.Year}\nMajor: {self.Major}\nSchool: {self.School}"

def find_earliest_graduate(students):
    earliest_student = min(students, key=lambda student: int(student.Year))
    return earliest_student

def main():
    students = [
        Student("Brad Jones", "2004", "Theatre Studies", "Kent University"),
        Student("Harley Waffleman", "2007", "Criminal Justice", "MeCant University")
    ]

    print(students[0])
    print(students[1])
    
    print("Student who graduated earlier:")
    earliest_graduate = find_earliest_graduate(students)
    print(earliest_graduate.display_info())

if __name__ == "__main__":
    main()

