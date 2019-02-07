#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os


# In[12]:


def line_coverage():
    os.system("clang++ -std=c++11 -fprofile-instr-generate -fcoverage-mapping main.cpp QuadrilateralClassifier.cpp -o main")
    os.system("rm -f *.profdata")
    os.system("mkdir profile")
    os.system("touch ./profile/main.profdata")
    os.system("touch ./default.profraw")
    os.system("rm ./profile/.DS_Store.profraw")
    os.system("rm ./profile/.DS_Store.profdata")
    prev = "main"
    
    for (root,dirs,files) in os.walk("input", topdown=True):
        for name in files:
            filename = root+"/"+name
            os.system("LLVM_PROFILE_FILE=\"./profile/"+prev+".profraw\" ./main "+filename)
            print("LLVM_PROFILE_FILE=\"./profile/"+prev+".profraw\" ./main "+filename)
            os.system("LLVM_PROFILE_FILE=\"./profile/"+name[0:-4]+".profraw\" ./main "+filename+"> output.txt")
            os.system("xcrun llvm-profdata merge -sparse ./profile/"+prev+".profdata ./profile/"+name[0:-4]+".profraw -o ./profile/"
                      +name+".profdata")
    os.system("xcrun llvm-cov show ./main -instr-profile=./profile/"+prev+".profdata > coverage.txt")


# In[13]:


line_coverage()


# In[ ]:




