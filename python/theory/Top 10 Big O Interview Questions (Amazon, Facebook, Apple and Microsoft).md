Product and Sum

def foo(array):
    sum = 0 #---------------------------------------------------------0(1)
    product = 1  #----------------------------------------------------0(1)
    for i in array: #-------------------------------------------------0(n)
        sum += i  #---------------------------------------------------0(1)
    
    for i in array:  #------------------------------------------------0(n)
        product *= i  #-----------------------------------------------0(1)
    print("Sum = "+str(sum)+", Product = "+str(product)) #------------0(1)
Time Complexity: O(n)
Space complexity: O(1)


Print Pairs

def printPairs(array):
    for i in array:  #---------------------------------------------0(n^2)
        for j in array:  #-----------------------------------------0(n)
            print(str(i)+","+str(j))  #----------------------------0(1)
Time Complexity: O(n^2)




Print Unordered Pairs

def printUnorderedPairs(array):
    for i in range(0,len(array):  #------------------------------0(n^2)
        for j in range(i+1,len(array):  #------------------------0(n)
            print(array[i] + "," + array[j])  #------------------0(1)
Two approaches to calculate Time Complexity:

1. Counting Iterations:

1st -----> n-1

2nd ----> n-2

        .

        .

        n

(n-1)+(n-2) +(n-3)+....+2+1 = 1+2+.....(n-3)+(n-2)+(n-1) = n(n-1)/2 = n^2 - n/2 = n^2

2. Average Work

Outer Loop -------> N times

Inner Loop?

1st -----> 10

2nd ----> 9

        .                   5 ----->10/2

        .                   n ----->n/2

        1

n*n/2 = n^2/2 = n^2

Time Complexity: O(n^2)




Print Unordered Pairs 2 Arrays

def printUnorderedPairs(arrayA, arrayB):
    for i in range(0,len(arrayA):  #------------------------------0(n)
        for j in range(len(arrayB):  #----------------------------0(m)
            if arrayA[i] < arrayB[j]: #---------------------------0(1)
                print(array[i] + "," + array[j])  #---------------0(1)
Time Complexity: O(n*m)



Print Unordered Pairs 2 Arrays 100000 Units

def printUnorderedPairs(arrayA, arrayB):
    for i in range(0,len(arrayA):  #-------------------------------0(n)
        for j in range(len(arrayB):  #-----------------------------0(m)
            for k in range(0,1000000): #---------------------------0(1) #constant time operation
                print(array[i] + "," + array[j])  #----------------0(1)
Time Complexity: O(n*m)



Reverse

def revers(array):
    for i in range(0, int(len(array)/2)):  #--------------------------0(n/2)
        other = len(array)-i-1  #-------------------------------------0(1)
        temp = array[i]  #--------------------------------------------0(1)
        array[i] = array[other]  #------------------------------------0(1)
        array[other] = temp  #----------------------------------------0(1)
    print(array)  #---------------------------------------------------0(1)
Time Complexity: O(n)



Which of the following are equivalent to O(n)? Why?

1. O(N +P), where P < N/2

- O(N) - drop non-dominant term

2. O(2N)

- O(N) - drop constant

3. O(N + logN)

- O(N) - drop non-dominant term

4. O(N + NlogN)

- O(NlogN) - drop non-dominant term

5. O(N + M)

- O(N + M) - we cannot drop M since there is no established relation between N and M (Eg: M could be larger or not)
