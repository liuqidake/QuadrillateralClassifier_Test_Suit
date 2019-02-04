#!/bin/bash
clang++ -c main.cpp
clang++ -o main main.o

./main input.txt

cmp --silent output.txt test.txt && echo '###Passed###' || echo '###Failed###'
