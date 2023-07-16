class Student:
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
    def __repr__(self):
        return f"Student: ({self.first_name}, {self.last_name}, {self.grade})"
    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and self.grade == other.grade
    def __hash__(self) -> int:
        return hash((self.first_name, self.last_name, self.grade ))

if __name__ == "__main__":
    student1 = Student("John", "Brown", "3")
    student2 = Student("John", "Brown", "3")
    print(student1)
    print(student1 == student2)

# or you can use dataclass instead of these rpr eq hash etc here see it!!

from dataclasses import dataclass
from dataclasses import field
from typing import List

def my_factory():
    return [1, 2, 3]

@dataclass(init=True, repr= True, eq=True, order=True, unsafe_hash=False, frozen=False)
class Student:
    first_name: str = field(default ="Default Value and str to show what we expect as input")
    last_name: str = field(default ="Default")
    grades: List[int] = field(default_factory = my_factory, init=True, repr=True, compare=True, hash=True, metadata={'unit' : "grades from first unit"})

if __name__ == "__main__":
    student1 = Student("John", "Brown", "3")
    student2 = Student("John", "Brown", "3")
    print(student1)
    print(student1 == student2)

def sorting(li):
    sorted_li = []
    for item in li:
        if

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)

