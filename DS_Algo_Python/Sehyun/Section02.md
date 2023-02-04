# 1. Recursion

## What is Recursion?
- Recursion = a way of solving a problem by having a function calling itself
- Performing the same operation multiple times with different inputs
- In every step we try smaller inputs to make the problem smaller
- Base condition is needed to stop the recursion, otherwise infinite loop will occur.

## Why Recursion?
1. Recursive thinking is really important in programming and it helps you break down big problems into smaller ones and easier to use
  - when to choose recursion?
2. The prominent usage of recursion in data structures like trees and graphs.
3. Interviews
4. It is used in many algorithms (divide and conquer, greedy and dynamic programming)

## How Recursion works?
1. A method calls it self
2. Exit from infinite loop

## Recursive vs Iterative Solutions
|Points|Recursion|Iteration|
|-|-|-|
|Space efficient?|No|Yes|
|Time efficient?|No|Yes|
|Easy to code?|Yes|No|

## When to use/avoid Recursion?
- When to use it?
  - When we can easily breakdown a problem into similar subproblem
  - When we are fine with extra overhead (both time and space) that comes with it
  - When we need a quick working solution instead of efficient one
  - When traverse a tree
  - When we use memoization in recursion
- When avoid it?
  - If time and space complexity matters for us.
  - Recursion uses more memory. If we use embedded memory. For example an application that takes more memory in the phone is not efficient
  - Recursion can be slow

## How to write Recursion in 3 steps?
1. Recursive case - the flow
2. Base case - the stopping criterion
3. Unintentional case - the constraint

## How to find Fibonacci numbers using Recursion?
1. Recursive case - the flow
  ```
  f(n) = f(n-1) + f(n-2)
  ```
2. Base case - the stopping criterion
  
3. Unintentional case - the constraint