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