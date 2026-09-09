def sort_dictionary(d):
    result = {}
    for key in sorted(d):
        result[key] = d[key]

    return result

d = {'banana': 20, 'apple': 10, 'orange': 30, 'grapes': 15}
result = sort_dictionary(d)
print("Sorted Dictionary:", result)
