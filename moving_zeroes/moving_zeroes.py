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
            # Create a variable for the current index.
            # Create a variable for the array length which will be used for the last index in the array.
            # Create a while loop for as long as the array index is less than the array length
                # If the current index is zero
                    # We need to remove the zero and append it to the end of the array. Will use .pop() and .append()
                    # Then decrease the array length because we no longer want to access the zero appended to the end.
                # If the current index is a non-zero number (else statement):
                    # We need to increase the current index for the while loop.
                # Return the adjusted array.

    # E:
    current_index = 0
    arr_len = len(arr)
    print(arr)

    while current_index < arr_len:
        if arr[current_index] == 0:
            remove_num = arr.pop(current_index)
            arr.append(remove_num)
            arr_len -= 1
            print(arr)
        else:
            current_index += 1
    print(arr)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")