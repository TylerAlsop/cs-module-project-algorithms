'''
Input: a List of integers
Returns: a List of integers
'''
import numpy

def product_of_all_other_numbers(arr):
    # Your code here
    # U:
        # Recieves a list of numbers.
        # Function needs to return an array where each number has been replaced by the product of all the other numbers in the array excluding the number itself.
    # P:
        # We are going to multipy all of the numbers in the list and then divide by the current number.
        # Need to loop through the list
        # For each number we will have a variable called result.
        # Result will equal itself multiplied by the number and then divided by the number.
    for i in arr:
        result = numpy.prod(arr) / i
        print(arr)
        return result

    print(arr)



    


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

##########################################################################################
# The above plan failed. New Plan: