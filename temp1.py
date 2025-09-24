# 寫一個函式，接收一個數字列表，回傳該列表中的最大值。
def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)
# 測試函式
print(find_max([]))  # 輸出應該是 None
print(find_max([3, 1, 4, 1, 5, 9]))  # 輸出應該是 9
