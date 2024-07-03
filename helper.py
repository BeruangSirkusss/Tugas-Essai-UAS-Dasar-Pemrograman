def loopSumOfThree(numbers, n):
    if len(numbers) < 3:
        return "Please provide at least 3 numbers"
    
    result = []
    for _ in range(n):
        new_number = sum(numbers[-3:])
        result.append(new_number)
        numbers.append(new_number)
    return result