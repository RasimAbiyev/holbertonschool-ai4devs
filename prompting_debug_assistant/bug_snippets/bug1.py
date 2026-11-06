def calculate_average(numbers):
    if not numbers
        return 0

    total = 0
    for number in numbers:
        total += number

    average = total / len(numbers)
    return average


scores = [80, 90, 75, 85]
result = calculate_average(scores)
print("Average:", result)
