'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n < 0:
        return 0
    
    if n == 0:
        return 1

    number_of_ways = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    return number_of_ways
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
