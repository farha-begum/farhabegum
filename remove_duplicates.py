def remove_duplicates(lst):
    seen=set()
    unique_list=[]
    for item in lst:
        if item not in seen:
           unique_list.append(item)
           seen.add(item)
    return unique_list
print(remove_duplicates([1,2,3,4,3,2,1]))
print(remove_duplicates([1,2,3,2]))
print(remove_duplicates([]))
