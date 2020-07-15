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
    # E:
    i = 0
    j = 0
    current_index = arr[i]
    while i <= len(arr):
        for j in arr:
            if current_index == j:
                i += 1
                single_number(arr)
            else:
                return j


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")