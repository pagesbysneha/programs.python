#WAP To find the intersection of 2 list
l1 = [10, 20, 30, 40, 50]
l2 = [30, 40, 50, 60, 70]

def find_intersection(l1, l2):
    return list(set(l1).intersection(set(l2)))

common_elements = find_intersection(l1, l2)
print(common_elements)
