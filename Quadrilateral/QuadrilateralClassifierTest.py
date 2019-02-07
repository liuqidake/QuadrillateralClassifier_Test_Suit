#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
import pandas as pd
import time


# In[10]:


def test_quadrilateral_classifiers():
    """
    
    Test QuadrilateralClassifier with more than 1000 test cases. Print OK if 
    no bugs were detected in the classifier, or ERROR if more than zero bugs were detected
    """
    compile_file()
    test_normal_cases()
    test_error_cases()
    print("OK")


# In[11]:


def compile_file():
    os.system('clang++ -c QuadrilateralClassifier.cpp')
    os.system('clang++ -c main.cpp')
    os.system('clang++ -o fuzz main.o QuadrilateralClassifier.o')


# In[12]:


def test_normal_cases():
    """
    
    Test input files which is suppose to yeild sqaure, rectangle, rhmbus, parallelogram
    trapezoid and kite from classifier
    """
    shape_name = ["square","rectangle","rhombus","parallelogram","trapezoid","kite"]
    for shape in shape_name:
        test_shape(shape)
    


# In[13]:


def test_shape(shape):
    direc = os.fsencode("input/"+shape)
    for file in os.listdir(direc):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            os.system("./fuzz input/"+shape+"/"+filename)
            output_shape = pd.read_csv("output.txt", header = None)[0][0]
            if output_shape != shape:
                print("Error")
        else:
            continue


# In[14]:


def test_error_cases():
    """
    
    Test four types of error
    """
    error_name = ["error_one","error_two","error_three","error_four"]
    i = 1
    while i <= 4:
        test_error(i, error_name[i-1])
        i+=1


# In[15]:


def test_error(i, folder):
    direc = os.fsencode("input/"+folder)
    for file in os.listdir(direc):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            os.system("./fuzz input/"+folder+"/"+filename)
            output_shape = pd.read_csv("output.txt", header = None)[0][0]
            if output_shape != ("error "+str(i)):
                print("Error")
        else:
            continue


# In[16]:


test_quadrilateral_classifiers()

