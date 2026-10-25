def binary_search(numbers, target):
    middle = len(numbers) // 2
    right = len(numbers) # For Middle can access last element
    left = 0

    while left < right:
        if numbers[middle] == target:
            return middle # return index of target

        # Right:
        elif numbers[middle] < target:
            left = middle + 1
            middle = (right - middle) // 2 + middle

        # Left
        elif numbers[middle] > target:
            right = middle
            middle = middle//2

               #  0   1   2   3   4   5   6   7   8   9
list_of_number = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]

target = int(input("Check index: "))
print(f"The index is: {binary_search(list_of_number,target)}")