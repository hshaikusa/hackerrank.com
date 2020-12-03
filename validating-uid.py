# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys

CHECK_RE1 = re.compile('[^a-zA-Z0-9]')
def check_re1(mystring):
   return not CHECK_RE1.search(mystring)

def unique(list1):
    # intilize a null list 
    unique_list = [] 
    
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x)
    return unique_list

if __name__ == '__main__':
    try:
        n = int(input().strip())
        if (n <1) or (n>100):
            #print(f"n = {n}")
            raise IOError
    except IOError:
        print("Error inputing the number...please enter the number between 1 and 100")
        raise
    
    for i in range(n):
        try:
            str=input().__str__()
            # instantiate the parser and fed it some HTML
            if (check_re1(str)):
                            upper = 0 # check for minimum of 2 upper case letters
                            num = 0 # check for minimum of 3 numbers
                            for ch in str:
                                #print(ch)
                                if ch.isalpha():
                                    if ch.isupper():
                                        upper +=1
                                elif ch.isnumeric() :
                                    num +=1
            if (num >=3) and (upper >=2) and (len(list(str)) - len(unique(list(str))) == 0):
                print("Valid")
            else:
                print("Invalid")
            
        except EOFError:
            break
