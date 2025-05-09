def has_duplicates(lst):
    seen=set()
    for item in lst:
        if item in seen:
            return True
        else:
            return False
print(has_duplicates([5,6,7,8,9]))
print(has_duplicates([1,2,3,4,2]))
print(has_duplicates([]))
print(has_duplicates([5]))
