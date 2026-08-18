# WAP to find the unique union of two lists

l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]
def find_union(l1, l2):
    return list(set(l1).union(set(l2)))
union_list = find_union(l1, l2)
print(union_list)
