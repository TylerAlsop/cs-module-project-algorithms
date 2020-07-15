'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # U:
        # Recieves a list of numbers where each number except for one is in the list twice.
        # Function needs to return the integer that appears in the list only once.
    # P:
        # Need to loop through the list
        # For each number we need to find out of that same number exists anywhere else in the list.
            # If the number does not exist anywhere else in the list then we return that number.
        ##########################################################################################
        # The above plan failed. New Plan:
            # Remove all the duplicates from the array and set that to a new array variable
            # Sum up the numbers in that array
            # Multiply that sum by 2
            # Subtract the sum of the numbers in the original array.
            # Return the difference.
    # E:
    arr_without_duplicates = set(arr)
    return 2 * sum(arr_without_duplicates) - sum(arr)




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")