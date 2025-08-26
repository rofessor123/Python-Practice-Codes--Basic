#Sort list of tuples by second element

def sort_by_second(tuples):
    return sorted(tuples, key=lambda x: x[1])


print(sort_by_second([(1, 3), (2, 2), (3, 1)]))
