"""簡單計算工具（測試 Claude Code GitHub Action 用，故意留有 bug）"""


def add(a, b):
    """回傳兩數相加"""
    return a + b


def average(numbers):
    """回傳數字清單的平均值；空 list 回傳 0"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(average([1, 2, 3]))
