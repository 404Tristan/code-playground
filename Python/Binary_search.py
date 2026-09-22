def binary_search(numbers_list,target):
    middle = (len(numbers_list)-1)//2                                       # to know the middle which is 5 that has a value of 6
    full_lenght = len(numbers_list)-1                                       # 11-1 = 10, useful to access list indeces
    state = True                                                            # Useful when the target is in left by setting it in False

    if target in numbers_list:                                              # If conditional. Return not in list if False
        while True:                                                         # Always true
            if numbers_list[middle] == target:
                return middle                                               # return the current index of the target
            elif numbers_list[middle] < target:
                if state == True:                                           # For right target
                    current = middle + 1
                    middle = ((full_lenght-current)//2) + current
                else:                                                       # For left target
                    current = middle + 1
                    middle = ((current-full_lenght)//2) + current

            elif numbers_list[middle] > target:
                full_lenght = 0
                current = middle - 1
                middle = (current//2)
                state = False

    else:
        return "Search not found"


numbers_list = [1,2,3,4,5,6,7,8,9,10,11]
target = int(input("Search a number in a list: "))
print(f"Its in index: {binary_search(numbers_list,target)}")

