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
        

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
