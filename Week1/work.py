import math
import numpy as np

def demo(x):
    '''
    This is a demo function
    Where in you just return square of the number
    args:
        x (int)
    returns:
        x*x (int)
    '''

    
    return x*x

def is_palindrome(string):
    '''
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    '''
    revstr=""
    for i in string:
    revstr=i+string
    if(revstr==string):
    return true

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''

    a=math.sqrt(num)
    return a

def Maximum(arr):
    '''
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''
    list=[]
    list.extend(arr)
    max1=list.max()
    list.remove()
    max2=list.max()
    
    
    return max1,max2

def even_sort(arr):
    '''
    This function sorts the array giving higher preference to even numbers
    args:
        arr (list)
    returns:
        sort_arr (list)
    ex:
        arr = [15, 2, 6, 88, 7]
        ## then
        sort_arr = [2, 6, 88 ,7 ,15]
        ## This is any even number is smaller than any odd number
    '''

    evenlist=[]
    oddlist=[]
    for i in arr:
        if(i%2==0):
            evenlist.append(i)
        else:
                oddlist.append(i)
     evenlist.sort()
    oddlist.sort()
    sort_arr=[]
    sort_arr.extend(evenlist)
    sort_arr.extend(oddlist)
                
    return sort_arr


def eqn_solver(A, B, C):
    '''
    This function solves a two variable system
    i.e.,
        A = [ 1, 2 ]
        B = [ 3, 4 ]
        C = [ 5, 6 ]
        then it means
        1x + 3y = 5
        2x + 4y = 6
        Hence you are required to find x, y for such a linear system
    args:
        A, B, C (list, list, list) representing coefficients in the equation
    returns:
        x, y (float, float)
    '''

    
    return None
