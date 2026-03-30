# Function to find the maximum sum of a subarray
def max_subarray_sum(numbers):
    max_sum = numbers[0]     
    current_sum = numbers[0]

    for num in numbers[1:]:   # loop through remaining elements
        current_sum = max(num, current_sum + num)  # extend or restart
        max_sum = max(max_sum, current_sum)        # track the best

    return max_sum

print(max_subarray_sum([1, 2, 3, 4])) 


# Function to find the maximum sum of a subarray
def max_subarray_sum(numbers):
    max_sum = numbers[0]      # start with first element
    current_sum = numbers[0]

    for num in numbers[1:]:   # loop through remaining elements
        current_sum = max(num, current_sum + num)  # extend or restart
        max_sum = max(max_sum, current_sum)        # track the best

    return max_sum

print(max_subarray_sum([1, 2, 3, 4])) 


# Function to return a list of words sorted by length
def sort_by_length(words):
    return sorted(words, key=len)  # use len as the sorting key

print(sort_by_length(["banana", "hi", "apple", "go"]))


# Function to find all prime numbers within a given range
def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):   # loop through range
        if num < 2:                      # primes start at 2
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # check divisors
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(find_primes(1, 20))


# Function to find the most frequent character in a string
def most_frequent_char(text):
    frequency = {}                  # empty dictionary to count chars
    for char in text:
        if char == " ":             # skip spaces
            continue
        if char in frequency:
            frequency[char] += 1    # increment if already seen
        else:
            frequency[char] = 1     # add new character

    most_frequent = max(frequency, key=frequency.get)  # get highest count
    return most_frequent

print(most_frequent_char("hello world"))
