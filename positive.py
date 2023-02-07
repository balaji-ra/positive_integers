def positive_numbers(lst):
    positive_lst = []
    for num in lst:
        if num > 0:
            positive_lst.append(num)
    return positive_lst

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("Positive numbers in list1:", positive_numbers(list1))
print("Positive numbers in list2:", positive_numbers(list2))
