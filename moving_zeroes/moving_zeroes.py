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
        # For each of the non-zero numbers they need to be moved to the 
    # E:
    temp_index = 0
    for i in arr:
        print(arr)
        if arr[i] != 0:
            arr[temp_index] = arr[i]
            temp_index += 1
            print(arr)

    while temp_index < len(arr):
        arr[temp_index] = 0
        temp_index += 1
            
    print(arr)



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")