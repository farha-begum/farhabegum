def is_sorted(list):
    return all(list[i]<=list[i+1]for i in range(len(list)-1))
print(is_sorted([2,4,6,8,10]))
print(is_sorted([10,8,6,4,2]))
print(is_sorted([6,8,4,10,2]))
print(is_sorted([5,3,1]))
           
