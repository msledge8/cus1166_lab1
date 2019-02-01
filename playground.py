print("Practice Basic Program:\nHello World")
name = input("What is your name? ")
print("Hello %s" % name)
print("Practice basic program finished.")

first = 1688
second = 1.6888888
third = True
fourth = None
print(f"\n\nPractice Variables:\nVariable 1: {first}.\nVariable 2: {second}. Its type is {type(second)}")
print(f"Variable 3: {third}")
print(f"Variable 4: {fourth}\nPractice variables finished.")

tuple1 = (10,20,10)
print(f"\n\nPractice tuple: \ntuple1[0] has the value {tuple1[0]} and is of type: {type(tuple1)}\nPractice tuple finished.")

list1 = ["Harry", "Ron", "Hermione"]
list1 = [1,2,3]
print(f"\n\nPractice List: \nl[0] has the value {list1[0]} and is of type: {type(list1)}\nPractice list finished.")

set1 = set()
set1.add(1)
set1.add(4)
set1.add(6)
print("\n\nPractice set:")
print(set1)
print("Practice set finished.")

print("\n\nPractice dictionary:")
grade = dict()
grade["Hermione"] = "A+"
grade["Harry"] = "B+"
grade["Ron"] = "B-"
print(grade)
print("Practice dictionary finished.")

print("\nPractice Conditionals:")
num1 = int(input("Enter a number: "))
if num1 > 0:
    print("The number is positive.")
elif num1 < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
print("Practice conditionals finished.\n\nPractice loops:")

for x in range(9):
    print(x)
for i, j in enumerate(range(3, 10)):
    print(f"{i} - {j}")
print("Practice loops finished.\n\nPractice functions:")


def is_odd(num2):
    if (num2 % 2) == 0:
        return False
    else:
        return True


practice = int(input("Enter odd number: "))

print(is_odd(practice))
print("Practice functions finished.")


class Cube:
    def __init__(self, x):
        self.x = x

    def print_cube(self):
        print(f"{self.x} cubed is {self.x * self.x * self.x}.")


cubed = Cube(2)

print("\nPractice class:")
cubed.print_cube()
print("Practice class finished.")
