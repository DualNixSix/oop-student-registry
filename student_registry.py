class Student:
    def __init__(self, name, age = 13, grade = "12th", ids = 1):
        self._ids = ids
        self._name = name
        self._age = age
        self._grade = grade
        
    def __str__(self):
        return f"Student {self._ids}: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"
    
    @property
    def ids (self):
        return self._ids
    
    @property
    def name (self):
        return self._name
    
    @property
    def age (self):
        return self._age
    
    @property
    def grade (self):
        return self._grade
    
    @ids.setter
    def ids (self, newids):
        if type(newids) == int and newids > 0:
            self._ids = newids
        else:
            print("Error: ID must be a number greater than zero.")

    @name.setter
    def name (self, newname):
        if type(newname) == str and newname.isalpha():
            self._name = newname
        else:
            print("Error: Name must be a valid name made up of letters.")

    @age.setter
    def age (self, newage):
        if type(newage) == int and 11 < newage < 18:
            self._age = newage
        else:
            print("Error: Age must be a number greater than zero.")

    @grade.setter
    def grade (self, newgrade):
        valid = ["9th", "10th", "11th", "12th"]  
        if newgrade in valid:
            self._grade = newgrade
        else:
            print("Error: Grade must be between 9th and 12th grade.")
    
    def advance (self, advancedgrade):
        valid = ["9th", "10th", "11th", "12th"]  
        if advancedgrade in valid:
            return f"{self._name} has advanced to {advancedgrade} grade."
        else:
            print("Error: Grade must be between 9th and 12th grade.")

    def study (self, subject):
        if type(subject) == str and subject.isalpha():
            return f"{self._name} is studying {subject}."
        else:
            print("Error: Subject must be a valid subject made up of letters.")
        
student1 = Student("Alice")
print(student1)
print(student1.advance("12th"))
print(student1.study("History"))