Big O 
- the language and metric we use to describe the efficiency of algorithms.
- shows how the runtime of the function increases as the size of the input increases.
- we are measuring the number of operations and space complexity.

Space Complexity: 
- the amount of the memory that some code used.

Big O Notations
- Best Case: Omega
- Average Case: Big Theta
- Worst Case: Big O

Runtime Complexity
Linear Time Complexity
- time complexity will grow in direct proportion to the size of input data.

Drop Constants
- it is very possible that O(n) code is faster than O(1) code for specific input, 
but big O just describes the rate of increase.
- different computers with different architectures have different constant factors.
However, we are just interested in the algorithm, not the hardware when doing the 
asymptotic analysis, so we ignore such constant factors.

O(n^2) - nested loops:
2 loops --> n*n=n^2
3 loops --> n*n*n=n^3
In terms of Big O it doesn't matter if it is ^3, ^4, or ^10 we are still going to write it as O(n^2).
This is very inefficient code because as the number of elements increase the number of operations increase in quadratic manner.


Non Dominant Terms
Two loops:
one loop is O(n^2) - completes 100 operations
the following one is O(n) - completes 10 operation
Total time complexity is O(n^2 + n) ---> In terms of Big O we can simplify this by removing non-dominant terms (O(n^2)- dominant term, 
term with higher power, O(n) - non-dominant term, term with lower power) ---> O(n^2)


O(log n)
Divide and Conquer - searching for a number in a sorted array.
For axample and array of 8 sorted elements, we divide it 3 time until we find the required number. ---> 2^3=8 (Since we are dividing 
by 2 we are using base two notation 2^3)
2^3=8 ---> log2_8 = 3
This complexity is crucial when we work with really big numbers ---> log2_1,048,576=20
It is very efficient compared to O(n) or O(n^2) - if we increase the number of elements, the number of operations increases slightly.

Space Complexity 
- is a measure of amount of the working storage that an algorithm needs.
How much memory in the worst case is needed at any point in the algorithm.
Eg: a function summing up number from input until zero calling itself recursively.
Recursive methods like this count in the space stack. So every time each call adds a level to the stack and this takes up actual memory. 
This function takes O(n) space complexity.

Different Terms for Input - Add vs Multiply
Eg: two loops in a sequence passing n, each loop is O(n) time complexity. ---> O(n) + O(n) = O(2n) we can drop constant ---> O(n) 
If we change parameters and have one loop passing a and another one passing b instead of n ---> O(a) + O(b) = O(a+b) we cannot simplify 
it anymore. - If your algorithm is in the form "do this, then when you are all done , do that" ---> add runtimes
If we now have nested loops. Loop b inside loop a --> O(a*b) - If your algorithmm is in the form "do this for each time you do that" --->
---> multiply runtimes

How to measure the codes using Big O?
Rule 1 Any assignments statements and if statements that are executed once regardless of the size of the problem O(1)
Rule 2 A simple "for" loop from 0 to n (with no internal loops) O(n)
Rule 3 A nested loop of the same type takes quadratic time complexity O(n^2)
Rule 4 A loop, in which the controlling parameter is divided by two at each step O(log n)
Rule 5 When dealing with multiple statements, just add them up

-------------------------------------------------------------------------------------------------
