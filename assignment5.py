
# Part 1: Defining a Class and __init__
class Student:
    def __init__(self, name, grade_level, score):
        self.name = name
        self.grade_level = grade_level
        self.score = score

    # Part 3: Adding and Calling Methods
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am in the {self.grade_level} grade.")

    # Part 4: Updating Values through Methods
    def improve_score(self, extra_points):
        self.score += extra_points
        print(f"{self.name}'s score has improved to {self.score}!")


# Part 2: Creating Objects and Accessing Attributes
student1 = Student("Alice", "10th", 85)
student2 = Student("Bob", "12th", 92)

# Print attributes directly
print(f"{student1.name} has a score of {student1.score}.")
print(f"{student2.name} has a score of {student2.score}.")

# Call introduce() method
student1.introduce()
student2.introduce()

# Call improve_score() method
student1.improve_score(5)

# Final check
print(f"Final check - {student1.name}'s score is: {student1.score}")