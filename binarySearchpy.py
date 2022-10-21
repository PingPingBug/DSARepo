import random

def binary_search(list1, low, high, n):   
  
   # Check base case for the recursive function  
   if low <= high:  
  
      mid = (low + high) // 2  
  
      # If element is available at the middle itself then return the its index  
      if list1[mid] == n:   
         return mid   
  
      # If the element is smaller than mid value, then search moves  
      # left sublist1  
      elif list1[mid] > n:   
         return binary_search(list1, low, mid - 1, n)   
  
      # Else the search moves to the right sublist1  
      else:   
         return binary_search(list1, mid + 1, high, n)   
  
   else:   
      return -1


# Ask input


# num = int(input("Enter the lenght of the array"))

# arr = [None]*num
 
# i = 0

# while i<num:

#     inp = input("Enter the num: ")

#     try:
#         arr[i]= (int(inp))
#         i += 1

#     except:
#         print("Please Enter a valid input")


arr = random.

print(arr)

sortedArr = arr.sort()


print(binary_search(sortedArr, 0, len(sortedArr)-1, num))

