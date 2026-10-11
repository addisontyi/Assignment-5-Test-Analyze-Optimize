# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    # Your code here
    if not numbers:
        return None

    counts = {}

    for num in numbers:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

    most_common = numbers[0]

    for num in counts:
        if counts[num] > counts[most_common]:
            most_common = num

    return most_common

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? A dictionary counts how often each number willappear
- Could it be optimized? This is efficient because each number is processed 
- a constant number of times on average
- Trade-offs: The dictionary uses extra memory, but it makes counting
- a lot faster than having to repeatedly scan the list.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    # Your code here
    result = []
    seen = set()

    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? A set tracks values already found and a list keeps the original order
- Could it be optimized? This is efficient because set membership checks take O(1) time on average
- Trade-offs: It uses extra memory for the set, but avoids searching the result list for duplicates repeatedly.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    # Your code here
    pairs = []
    seen = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n) if no duplicates
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? A set lets us find matching complements without checking all possible pairs
- Could it be optimized? This is already efficient for finding pairs when the input contains no duplicates
- Trade-offs: It uses extra memory for the set, but improves time complexity compared with nested loops.
- Optimization: Using a set to find complements avoids nested loops, which would take O(n^2) time.
- Performance comparison: Using a set-based approach processes the input in O(n) average time,
- instead of comparing every possible pair in O(n^2) time.
- Space comparison: The set uses O(n) extra memory, and a nested-loop approach can use O(1) if output storage is excluded.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # Your code here
    capacity = 2
    items = [None] * capacity
    size = 0

    for i in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print("Resizing from", capacity, "to", new_capacity)

            new_items = [None] * new_capacity

            for j in range(size):
                new_items[j] = items[j]

            items = new_items
            capacity = new_capacity

        items[size] = i
        size += 1


"""
Time and Space Analysis for problem 4:
- When do resizes happen? when size reaches the current capacity
- What is the worst-case for a single append? O(n) when resizing requires copying elements
- What is the amortized time per append overall? O(1)
- Space complexity: O(n)
- Why does doubling reduce the cost overall? It reduces how frequently resizing happens, 
- which keeps total copying work linear
- Trade-offs: Resizing sometimes takes O(n) time and might require extra memory, 
- but doubling keeps the total work across the appends linear.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    # Your code here
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? Each number is only added to a running total once, which avoids repeated calculations
- Could it be optimized? O(n) time is optimal because every input number must be processed
- Trade-offs: The new result list requires extra memory, but stores all the running totals for easy access.
"""


#Problem 1 tests
print("Problem 1:")
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  #3
print(most_frequent([5, 5, 2, 2]))            #5 or 2
print(most_frequent([7]))                     #7
print(most_frequent([]))                      #None

#Problem 2 tests
print("\nProblem 2:")
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  #[4, 5, 6, 7]
print(remove_duplicates([1, 1, 1]))            #[1]
print(remove_duplicates([]))                   #[]
print(remove_duplicates([3, 2, 1]))            #[3, 2, 1]

#Problem 3 tests
print("\nProblem 3:")
print(find_pairs([1, 2, 3, 4], 5))  #[(2, 3), (1, 4)]
print(find_pairs([1, 2, 3], 10))    #[]
print(find_pairs([], 5))             #[]
print(find_pairs([2, 4, 6], 8))     #[(2, 6)]

#Problem 4 tests
print("\nProblem 4:")
add_n_items(6)  #Should print the resized messages
add_n_items(0)  #No resizing
add_n_items(2)  #No resizing
add_n_items(3)  #Only one resize

#Problem 5 tests
print("\nProblem 5:")
print(running_total([1, 2, 3, 4]))  #[1, 3, 6, 10]
print(running_total([5]))            #[5]
print(running_total([]))             #[]
print(running_total([-1, 2, -3]))   #[-1, 1, -2]