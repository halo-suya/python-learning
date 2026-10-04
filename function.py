def say_hello(name):
    print("Hello", name)


names = ["Tom", "Jack", "Alice"]

for name in names:
    say_hello(name)


def double(number):
    return number * 2

result = double(5)
print(result)

def double(number):
    return number * 2

numbers = [1, 2, 3, 4, 5]

results = []

for number in numbers:
    result = double(number)
    results.append(result)

print(results)

student = {
    "name": "Tom",
    "age": 18
}

student["age"] = 19

print(student)

students = [
    {"name": "Tom", "age": 18},
    {"name": "Jack", "age": 20},
    {"name": "Alice", "age": 19}
]

for student in students:
    print(student["name"], student["age"])

def introduce(student):
    print("My name is", student["name"])
    print("I am", student["age"], "years old")


for student in students:
    introduce(student)

for student in students:
    if student["age"] >= 19:
        print(student["name"], "is an adult")