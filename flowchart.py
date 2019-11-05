numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
print(*numbers)


def sort(numbers):
    j = 0
    n = (len(numbers))
    iterations = 1
    while iterations < n:
        j = 0
        while j <= n-2:
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                temp2 = numbers[j]
                numbers[j+1] = temp2
                numbers[j] = temp
                j = j + 1
            else:
                j += 1
        iterations += 1


sort(numbers)
print(*numbers)
