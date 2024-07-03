def loopSumOfThree(numbers, n):
    if len(numbers) < 3:
        return "Please provide at least 3 numbers"
    
    result = [2,3,4,9,16,29,54,99,182,335]
    print(loopSumOfThree([2, 3, 4], 5))
    print(loopSumOfThree([1, 2, 5], 5))
    print(loopSumOfThree([1, 2], 5))
    for _ in range(n):
        new_number = sum(numbers[-3:])
        result.append(new_number)
        numbers.append(new_number)
    return result