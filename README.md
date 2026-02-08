📘 Array Problems – Brute Force, Better & Optimal Approaches

This repository contains solutions to commonly asked array problems, solved using Brute Force, Better, and Optimal approaches.
The goal is to understand time & space trade-offs and build strong DSA fundamentals for interviews.

📌 Problems Covered

Largest Element in an Array

Second Largest Element

Second Smallest Element

Check if Array is Sorted

Remove Duplicates and Count Unique Elements

1️⃣ Largest Element in an Array
🧠 Problem

Find the largest element in a given array.

🔹 Brute Force Approach

Sort the array

Return the last element

Time Complexity: O(n log n)
Space Complexity: O(1)

🔹 Optimal Approach

Traverse the array once

Keep track of the maximum

Time Complexity: O(n)
Space Complexity: O(1)

2️⃣ Second Largest Element in an Array
🧠 Problem

Find the second largest distinct element.

🔹 Brute Force Approach

Sort the array

Traverse from the end to find the first element smaller than max

Time Complexity: O(n log n)
Space Complexity: O(1)

🔹 Better Approach

Find largest element

Traverse again to find the largest element smaller than max

Time Complexity: O(n)
Space Complexity: O(1)

🔹 Optimal Approach

Track largest and second_largest in one traversal

Time Complexity: O(n)
Space Complexity: O(1)

3️⃣ Second Smallest Element in an Array
🧠 Problem

Find the second smallest distinct element.

🔹 Brute Force Approach

Sort the array

Traverse from the start to find first element greater than minimum

Time Complexity: O(n log n)
Space Complexity: O(1)

🔹 Optimal Approach

Track smallest and second_smallest in one traversal

Time Complexity: O(n)
Space Complexity: O(1)

4️⃣ Check if Array is Sorted
🧠 Problem

Check whether the array is sorted in ascending order.

🔹 Brute Force Approach

Sort a copy of the array

Compare with original array

Time Complexity: O(n log n)
Space Complexity: O(n)

🔹 Optimal Approach

Compare every adjacent pair

Time Complexity: O(n)
Space Complexity: O(1)

5️⃣ Remove Duplicates and Count Unique Elements
🧠 Problem

Remove duplicates from an array and return the count of unique elements.

🔹 Brute Force Approach (Unsorted Array)

Use a set

Time Complexity: O(n)
Space Complexity: O(n)

🔹 Optimal Approach (Sorted Array – Two Pointer)

⚠️ Array must be sorted

Use two pointers

Overwrite duplicates in-place

Time Complexity: O(n)
Space Complexity: O(1)
