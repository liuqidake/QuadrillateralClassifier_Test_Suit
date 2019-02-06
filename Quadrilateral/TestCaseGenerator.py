#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import os
import random



def test_case_generator():
    """
    
    Generate test cases for all types of shape and errors
    """
    square_generator()
    rectangle_generator()
    rhombus_generator()
    parallelogram_generator()
    trapezoid_generator()
    kite_generator()
    error_one()
    error_two()
    error_three()
    error_four()



def square_generator():
    """
    
    Generating 99 test cases for testing square shape
    """
    os.makedirs("input/square")
    i = 1;
    while i <= 100:
        data = []
        data.append([i,0,i,i,0,1])
        df = pd.DataFrame(data)
        file_name = "input/square"+"/"+"square"+str(i)+".txt";
        df.to_csv(file_name, sep=" ", index = False, header= False)
        i += 1




def rectangle_generator():
    """
    Generating 200 test cases for testing rectangle shape
    """
    os.makedirs("input/rectangle")
    i = 2;
    j = 1;
    while i <= 99:
        x = i
        y1 = random.randint(1,x-1)
        y2 = random.randint(x+1, 100)
        data1 = []
        data1.append([x,0,x,y1,0,y1]);
        file_name1 = "input/rectangle/"+"rectangle"+str(j)+".txt";
        df1 = pd.DataFrame(data1)
        df1.to_csv(file_name1, sep=" ", index = False, header= False)
        j += 1
        data2 = []
        data2.append([x,0,x,y2,0,y2]);
        file_name2 = "input/rectangle/"+"rectangle"+str(j)+".txt";
        df2 = pd.DataFrame(data2)
        df2.to_csv(file_name2, sep=" ", index = False, header= False)
        j += 1
        i += 1
        



def parallelogram_generator():
    """
    Generating 49 test cases for testing parallelogram shape
    """
    os.makedirs("input/parallelogram")
    i = 2
    while i <= 50:
        x1 = i
        x2 = random.randint(1,100-x1)
        y = random.randint(1,100)
        file_name = "input/parallelogram/"+"parallelogram"+str(i-1)+".txt"
        data = []
        data.append([x1,0,x1+x2, y, x2, y])
        df = pd.DataFrame(data)
        df.to_csv(file_name, sep=" ", header=None, index = False)
        i+=1
        




def rhombus_generator():
    """
    Generating 100 test cases for testing rhombus shape
    """
    os.makedirs("input/rhombus")
    i = 1
    j = 2
    while i <= 49 and j <=50:
        data = []
        data.append([j, i, i+j, i+j, i, j])
        df = pd.DataFrame(data)
        file_name = "input/rhombus/"+"rhombus"+str(i)+".txt"
        df.to_csv(file_name, sep=" ", header=None, index= False)
        i+=1
        j+=1




def trapezoid_generator():
    """
    Generating 98 test cases for testing trapezoid shape
    """
    os.makedirs("input/trapezoid")
    i = 3
    while i<=100:
        x1 = i
        x2 = random.randint(2, x1-1)
        x3 = random.randint(0,x2-1)
        y = random.randint(1,100)
        data = []
        data.append([x1,0,x2,y,x3,y])
        df = pd.DataFrame(data)
        file_name = "input/trapezoid/"+"trapezoid"+str(i-2)+".txt"
        df.to_csv(file_name, sep=" ", header=None, index=False)
        i+=1




def kite_generator():
    """
    Generating 99 test cases for testing trapezoid shape
    """
    os.makedirs("input/kite")
    i = 1
    while i <= 99:
        x = i
        y = random.randint(x+1,100)
        data = []
        data.append([x,0,y,y,0,x])
        df = pd.DataFrame(data)
        file_name="input/kite/kite"+str(i)+".txt"
        df.to_csv(file_name, sep=" ", header=None, index=False)
        i+=1




def error_one():
    """
    Generating 300 test cases for testing error one
    """
    os.makedirs("input/error_one")
    i = 1
    #contains negative number
    while i <= 100:
        pos = random.randint(0,5)
        num = random.randint(-100,-1)
        j = 0
        line = []
        while j <6:
            if j== pos:
                line.append(num)
            line.append(random.randint(0,100))
            j += 1
        data = []
        data.append(line)
        df = pd.DataFrame(data)
        file_name = "input/error_one/error_one"+str(i)+".txt"
        df.to_csv(file_name, sep=" ", header= None, index=False)
        i+=1
    #contain invalid characters
    while i < 200:
        line = [];
        j = 0
        while j <6:
            character = (chr(97+random.randint(0,25)))
            line.append(character)
            j+=1
        data = []
        data.append(line)
        df = pd.DataFrame(data)
        file_name = "input/error_one/error_one"+str(i)+".txt"
        df.to_csv(file_name, sep=" ", header=None, index= False)
        i += 1
    #out of range
    while i<300:
        line=[]
        j = 0
        while j < 3:
            line.append(random.randint(-100,-1))
            line.append(random.randint(101, 400))
            j+=1
        data = []
        data.append(line)
        df = pd.DataFrame(data)
        file_name = "input/error_one/error_one"+str(i)+".txt"
        df.to_csv(file_name, sep=" ", header= None, index=False)
        i+=1
    



def error_two():
    """
    Generating 100 test cases for testing error two
    """
    os.makedirs("input/error_two")
    i = 0
    while i <=100:
        cointcidence_num1 = random.randint(1,100)
        cointcidence_num2 = random.randint(1,100)
        data=[]
        line = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100),
               cointcidence_num1, cointcidence_num2,cointcidence_num1,cointcidence_num2]
        data.append(line)
        df = pd.DataFrame(data)
        file_name = "input/error_two/error_two"+str(i+1)+".txt"
        df.to_csv(file_name, sep=" ", header=None, index=False)
        i+=1



def error_three():
    """
    Generating 100 test cases for testing error three
    """
    os.makedirs("input/error_three")
    i = 0
    while i <100:
        x1 = random.randint(2,100)
        x2 = random.randint(0,x1-1)
        y1 = random.randint(2,100)
        y2 = random.randint(0, y1-1)
        y3 = random.randint(y1,100)
        line = [x1, y1, x2, y3, x1, y2]
        data = []
        data.append(line)
        df = pd.DataFrame(data)
        file_name = "input/error_three/error_three"+str(i)+".txt"
        df.to_csv(file_name, sep=" ", header=None, index=False)
        i+=1




def error_four():
    """
    Generating 100 test cases for testing error four
    """
    os.makedirs("input/error_four")
    i = 0
    while i< 100:
        slope = random.randint(-5,5)
        constant = 0
        smallest = 0
        if slope <0:
            constant = random.randint(20,100)
        else:
            constant = random.randint(0,20)
        line = []
        while smallest <3:
            line.append(smallest)
            line.append(smallest*slope+constant)
            smallest+=1
        data = []
        data.append(line)
        df = pd.DataFrame(data)
        file_name = "input/error_four/error_four"+str(i)+".txt"
        df.to_csv(file_name, sep=" ", header=None, index=False)
        i+=1    



test_case_generator()

