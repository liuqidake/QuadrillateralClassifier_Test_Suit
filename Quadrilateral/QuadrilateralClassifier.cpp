//
//  QuadrilateralClassifier.cpp
//  assignment4
//
//  Created by Qi Liu on 1/31/19.
//  Copyright © 2019 Qi Liu. All rights reserved.
//


#include "QuadrilateralClassifier.hpp"
#include <cmath>
#include <fstream>
#include <sstream>
#include <set>

struct Point{
    double x;
    double y;
};

struct PointComparator{
    bool operator()(const Point& lhs, const Point& rhs){
        return lhs.x != rhs.x || lhs.y != rhs.y;
    }
};

double ComputeSlope(const Point& pa, const Point& pb){
    //Get the slope rate by computing the value of the x values difference divided by y vlaues diofference of two points
    if(pa.x-pb.x == 0) return 1;
    return (pa.y-pb.y) /  (pa.x-pb.x);
}

double ComputeLength(const Point& pa,  const Point& pb){
    //return the sqaure of two points' distance
    return std::pow(pa.x-pb.x,2) + std::pow(pa.y-pb.y,2);
}

bool IsParallel(const Point firstA, const Point& firstB, const Point& secondA, const Point& secondB){
    //If the two line has the same slope rate, return true
    return ComputeSlope(firstA, firstB) == ComputeSlope(secondA, secondB);
}

bool EqualNeigborLateral(const Point& leftPoint, const Point& midPoint, const Point& rightPoint){
    return ComputeLength(leftPoint, midPoint) == ComputeLength(midPoint, rightPoint);
}

bool PerpendicularNeighborLateral(const Point& leftPoint, const Point& midPoint, const Point& rightPoint){
    //If two lines are perpendicular, then the dot product of two vector is zero
    
    //the vector of the first line
    double vector1X = leftPoint.x - midPoint.x;
    double vector1Y = leftPoint.y - midPoint.y;
    
    //the vector of the second line
    double vector2X = midPoint.x - rightPoint.x;
    double vector2Y = midPoint.y - rightPoint.y;
    
    return vector1X*vector2X + vector1Y*vector2Y == 0;
}


bool IsParallelogram(const std::vector<Point>& points){
    //If two pairs pf laterl are both parallal to each other, then it is a parllelogram
    return IsParallel(points[0], points[1], points[2], points[3]) && IsParallel(points[0], points[3], points[2], points[1]);
}

bool TwoPairsOfAdjacentCongruentSides(const std::vector<Point>& points){
    return (EqualNeigborLateral(points[0], points[1], points[2]) && EqualNeigborLateral(points[2], points[3], points[0])) || (EqualNeigborLateral(points[1], points[2], points[3]) && EqualNeigborLateral(points[3], points[0], points[1]));
}

bool OnlyOnePairParallel(const std::vector<Point>& points){
    return IsParallel(points[0], points[1], points[2], points[3]) || IsParallel(points[1], points[2], points[3], points[4]);
}

void CheckShape(const std::vector<Point>& points, std::ofstream &out){
    //Case 1: parallelogram
    if(IsParallelogram(points)){
        bool neighborLateralPerpendicular = PerpendicularNeighborLateral(points[0], points[1], points[2]);
        bool neighborLateralEqual = EqualNeigborLateral(points[0], points[1], points[2]);
        //If the neighbor laterals have equal length and they are penpendicular to each other, then
        // it is a sqaure
        if(neighborLateralPerpendicular && neighborLateralEqual){
            out<<"square"<<std::endl;
        }
        //If the neighbor laterlas are only perpendicular to each other, then it is a rectangle
        else if (neighborLateralPerpendicular){
            out<<"rectangle"<<std::endl;
        }
        //If the neighbor laterlas only has the same length, then it is a rhombus
        else if ( neighborLateralEqual){
            out<<"rhombus"<<std::endl;
        }
        //Otherwise it is just an parallelogram
        else {
            out<<"parallelogram"<<std::endl;
        }
    }
    //Case 2: kite
    //If it is not a parallelogram but has two pairs of laterals with same length but not for all four, the it is a kite
    else if (TwoPairsOfAdjacentCongruentSides(points)){
        out<<"Kite"<<std::endl;
    }
    //Case 3: trapezoid
    //If it is not a parallelogram but there is only one pair of laterls are parallal to each other, then it is a trpezoid.
    else if (OnlyOnePairParallel(points)){
        out<<"trapezoid"<<std::endl;
    } else {
        out<<"Unable to catagorized"<<std::endl;
    }
}

std::vector<Point> splitStr(std::string& data){
    std::istringstream iss(data);
    std::vector<std::string> results((std::istream_iterator<std::string>(iss)),
                                     std::istream_iterator<std::string>());
    std::vector<Point> points;
    points.push_back({0,0});
    
    points.push_back({std::stod(results[0]), std::stod(results[1])});
    points.push_back({std::stod(results[2]), std::stod(results[3])});
    points.push_back({std::stod(results[4]), std::stod(results[5])});
    
    return points;
    
}

void readInput(std::string fileName){
    std::ifstream input(fileName);
    std::string coordinate;
    std::ofstream out;
    out.open("Output.txt");
    while(std::getline(input, coordinate)){
        std::vector<Point>  points = splitStr(coordinate);
        std::set<Point,PointComparator> set;
        for(int i = 0; i< points.size(); i++){
            set.insert(points[i]);
        }
        if(set.size()< 4){
            out<<"Invalid input"<<std::endl;
            continue;
        }
        CheckShape(points, out);
    }
    
}
