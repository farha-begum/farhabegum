def printthearray(arr,n):
    for i in range(n):
        print(arr[i],end="")
print()
def generateallbinarystrings(n,arr,i):
    if i==n:
        printthearray(arr,n)
        return
    arr[i]=0
    generateallbinarystrings(n,arr,i+1)
    arr[i]=1
    generateallbinarystrings(n,arr,i+1)
if __name__=="__main__":
    n=2
    arr=[None]*n
    generateallbinarystrings(n,arr,0)
