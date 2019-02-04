//
//  QuadrilateralClassifier.hpp
//  assignment4
//
//  Created by Qi Liu on 1/31/19.
//  Copyright © 2019 Qi Liu. All rights reserved.
//

#ifndef QuadrilateralClassifier_hpp
#define QuadrilateralClassifier_hpp

#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>


struct Point;
struct PointComparator;

/**
 Compute the slope rate between two points
 */
double ComputeSlope(const Point& pa, const Point& pb);


/**
 Compute the distance between two points
 */
double ComputeLength(const Point& pa,  const Point& pb);


/**
 check if two lines are parallal
 
 @param firstA first end point of the first line
 @param firstB second end point of the first line
 @param secondA first end point of the second line
 @param secondB second end point of the second line
 */
bool IsParallel(const Point firstA, const Point& firstB, const Point& secondA, const Point& secondB);


/**
 Check if the neighbor laterals has the same length
 */
bool EqualNeigborLateral(const Point& leftPoint, const Point& midPoint, const Point& rightPoint);


/**
 Check if the neighbor laterals are perpendicular to each other
 */
bool PerpendicularNeighborLateral(const Point& leftPoint, const Point& midPoint, const Point& rightPoint);

/**
 Check if the quadrilaterla is a parallelogram
 */
bool IsParallelogram(const std::vector<Point>& points);

/**
 Check if the there are two pairs of laterals having the same length but not same for all four
 */
bool TwoPairsOfAdjacentCongruentSides(const std::vector<Point>& points);

/**
 Only one pair of laterals are parallal to each other
 */
bool OnlyOnePairParallel(const std::vector<Point>& points);

/**
 Check if the quarilaterla is a trapezoid
 */
bool IsTrapezoid(const std::vector<Point>& points);


/**
 Categorize the shape based on four points
 */
void CheckShape(const std::vector<Point>& shape, std::ofstream &out);

void readInput(std::string fileName);

void parseLine(std::string& data, std::vector<Point>& points, std::ofstream& out);

bool hasCoincide(std::set<Point,PointComparator>& set, const std::vector<Point> points);

bool hasColinear(const std::vector<Point> points);

bool hasIntersection(const std::vector<Point> points);

bool isIntersected(const Point& lineAPointA, const Point& lineAPointB, const Point& lineBPointA, const Point& lineBPointB);

Point getIntersectionPoint(const Point& lineAPointA, const Point& lineAPointB, const Point& lineBPointA, const Point& lineBPointB);


#endif /* QuadrilateralClassifier_hpp */
