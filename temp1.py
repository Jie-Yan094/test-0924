students = [
{'id': 1, 'name': 'Alice', 'major': 'Computer Science'},
{'id': 2, 'name': 'Bob', 'major': 'Mathematics'},
{'id': 3, 'name': 'Charlie', 'major': 'Physics'},
]
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Major: {student['major']}")
# This is a sample Python file to demonstrate git commit message editing.

# 寫一個函式，接收一個數字列表，回傳該列表中的最大值。
def find_max(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
# 測試函式
print(find_max([]))  # 輸出應該是 None

# 寫一個程式，從1印到100，但每逢3的倍數印"Fizz"，每逢5的倍數印"Buzz"，每逢3和5的倍數印"FizzBuzz"。
# 其他情況印數字本身。
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
