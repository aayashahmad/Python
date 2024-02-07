# pos = -1

# def search(list, n):
#     global pos  # Define 'pos' as a global variable within the function
#     i = 0
#     while i < len(list):
#         if list[i] == n:
#             pos = i
#             return True
#         i += 1  # Increment 'i' within the loop
#     return False  # Move this outside of the loop

# # Test the function
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Renamed 'list' to 'lst' to avoid conflict with built-in function
# num = 9
# if search(lst, num):
#     print("Element found at position:", pos + 1)
# else:
#     print("Element is not present in the list")

l=list()
n=int(input("Enter elements"))
print("enter",n,"values")
for i in range(n):
    l.append(int(input()))
s=int(input("Enter element to be searched"))
for i in range(len(l)):
    if l[i]==s:
        print(s,"is found at position", i+1 )
        break
    else:
        print(s,"is not fount in list")
