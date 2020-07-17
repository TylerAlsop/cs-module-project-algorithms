'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # U:
        # Recieves a list of numbers.
        # Function needs to move all non-zero numbers to the right of the array.
    # P:
        # For each of the non-zero numbers they need to be moved to the right of the array.
        ##########################################################################################
        # The above plan failed. New Plan:
            # Create a filter
    # E:
    temp_arr_1 = []
    count = 0
    for i in arr:
        if arr[i] != 0:
            arr[count + 1] = arr[i]
    while count < arr_length:
        arr[count + 1] = 0
    print(arr)


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")