l = []
n = int(input("Enter number of elements: "))
print("Enter", n, "elements:")
for i in range(n):
    l.append(int(input()))
l.sort()  # Sort the list after all elements have been added
print("After sorting:")
print(l)

s = int(input("Enter the element to search: "))
low = 0
high = len(l) - 1
while low <= high:
    mid = (low + high) // 2
    if l[mid] == s:
        print(s, "is found at position", mid + 1)
        break
    elif l[mid] < s:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element is not present")
