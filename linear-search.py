"""
This program uses the basic linear search equation
"""

#Defining the linear search function
def search_result(arr, y, n):
    for x in range(0, n): #creating a loop from 0 to n
        #If arrays index eqauls to the item we want to find, return the index.
        if arr[x] == n: 
            return x
    return False

#Making array
array = [1, 2, 3, 4, 155, 998, 66, 56, 798, 23, 34 , 56, 3764, 1000]
#Value we want to get the index of, If the the value is not in the array the code returns "Number not found".
find = 3764
length_arr = len(array)

#Invoking the function to a variable.
answer = search_result(array, length_arr, find)

if answer == False:
    print("Number not found")
else:
    print(f"Number found at index of {answer}")
    

    
