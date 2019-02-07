clang++ -c main.cpp QuadrilateralClassifier.cpp
clang++ -o fuzz main.o QuadrilateralClassifier.o

clang++ -fprofile-instr-generate -fcoverage-mapping main.cpp QuadrilateralClassifier.cpp -o main
LLVM_PROFILE_FILE="main.profraw" ./fuzz input/square/square1.txt 
xcrun llvm-profdata merge -sparse main.profraw -o main.profdata
xcrun llvm-cov show ./main -instr-profile=main.profdata
