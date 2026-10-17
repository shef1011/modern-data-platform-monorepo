# 1. Python Challenge: The "Heavy Hitter" (Log Analysis)

## Real-World Context
You are working at a Berlin mobility startup. The DevOps team noticed a spike in API traffic and suspects a bot attack. They give you a massive stream of IP addresses. You need to quickly find the k most frequent IP addresses so the security team can block them.

## LeetCode Equivalent
347. Top K Frequent Elements

## Problem Statement
Given a list of numbers (or IP addresses), return the k most frequent elements.

## Example
Input:
- nums = [1, 1, 1, 2, 2, 3]
- k = 2

Output:
- [1, 2]

## Constraints
Your algorithm's time complexity must be better than O(N log N), where N is the number of elements.

Hint: Think about heaps or bucket sort.

## Why This Matters
In real-world systems like API gateways, log processors, and traffic monitoring tools, you often need to identify the most frequent sources of activity. This helps detect:
- bot traffic
- abusive requests
- hot data keys
- unusual spikes in system activity

## Key Idea
Use a frequency map to count occurrences, then select the top k items efficiently.

## Efficient Approaches
- Heap-based solution
- Bucket-sort / frequency bucket approach
- Counter + sorting by frequency

## Expected Complexity
- Counting frequencies: O(N)
- Selecting top k: O(N log k) with a heap
- Overall: O(N log k), which is efficient and better than O(N log N) in many practical cases

## Challenge Objective
Implement a Python solution that:
- handles large input efficiently
- returns the most frequent elements
- respects the problem constraints

## Bonus Thinking
How would this change if the input were a live stream rather than a fixed list? What would be the trade-offs between memory usage and speed?
