'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # U:
        # We recieve an array of numbers, and a separate number (k).
        # Moving from left to right across the array:
            # We look at the first k numbers (i.e. If k equals 3 then we compare the first 3 numbers. If k is 5 then we compare the first 5 numbers).
            # Then we compare at the next k-number of numbers starting with arr[1]
            # Then we compare at the next k-number of numbers starting with arr[2]
            # Then we compare at the next k-number of numbers starting with arr[3], etc etc. until the k-th number reaches the end of the array (arr[len(arr)-1]).
            # The function needs to return an array of numbers consisting of the largest number of each comparison.
        # The length of the new array outputed will be the length of the original array minus the length of k minus 1: 
            # len(output) = len(arr) - (k-1)
    # P:
        # Create an empty array to hold the max values of each window.
        # Create variables that will represent the starting and ending indexes of each window.
            # First index will be zero to begin at the start of the array.
            # Second index will just equal the input value "k". It will just be k and not k - 1 because we will be using nums[first_index : second_index] and this syntax does not return the actual value of the second_index.
        # Create a while loop so that as long as the last window index minus 1 is less than the length of the array:
            # Create a variable for the current window which will include the numbers in the range from the first window index up to the last window index.
            # Sort this array of the current window.
            # Append the last value of the current window to the window maxes array.
            # Incriment the first and last window indexes by +1
        # Return the window maxes array.
        
        window_maxes = []
        first_window_index = 0
        last_window_index = k 
        while (last_window_index - 1) < len(nums):
            current_window = nums[first_window_index : last_window_index]
            print(f'Current Window Before Sort: {current_window}')
            current_window.sort()
            print(f'Current Window After Sort: {current_window}')
            window_maxes.append(current_window[-1])
            print(f'Window Maxes: {window_maxes}')
            first_window_index += 1
            last_window_index += 1

        return window_maxes

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
