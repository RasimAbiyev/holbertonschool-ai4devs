# Bug Descriptions

## Bug 1 – bug1.py

Intended Behavior:
Calculate and return the arithmetic average of a list of numbers. If the list is empty, return 0.

Issue Type:
Syntax Error.

Notes:
The if statement is missing a colon after the condition. Python cannot parse the code until this syntax error is corrected.

## Bug 2 – bug2.js

Intended Behavior:
Calculate and return the sum of all prices in an array.

Issue Type:
Logical Error.

Notes:
The function uses the multiplication assignment operator (*=) instead of the addition assignment operator (+=). Since total starts at 0, the result is always 0.

## Bug 3 – bug3.py

Intended Behavior:
Retrieve and display a student's name using the provided list index.

Issue Type:
Runtime Exception.

Notes:
The function accesses index 5 in a list containing only four elements. This causes an IndexError because the requested index is outside the valid range.

## Bug 4 – bug4.c

Intended Behavior:
Calculate and display the sum of all elements in an integer array.

Issue Type:
Off-by-One Error.

Notes:
The for loop uses i <= size instead of i < size. This causes an out-of-bounds array access and undefined behavior.

## Bug 5 – bug5.js

Intended Behavior:
Sort an array of numeric scores in ascending numerical order.

Issue Type:
Misuse of Library Method.

Notes:
The sort() method is called without a numeric comparison function. JavaScript therefore sorts the numbers lexicographically rather than numerically. The method also modifies the original array.
