#Remove duplicates from a list
#Use a set (since sets don’t allow duplicates)


def remove_duplicates(lst):
    return list(set(lst))


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
