from typing import Type

import data
import math

# Write your functions for each part in the space below.


# Part 1

def first_element(list2:list[list[int]]) -> list[int]:
    list1 = []
    finalList = []
    for x in range(len(list2)):
        if len(list2[x]) > 0:
            list1.append(list2[x])

    for x in range(len(list1)):
            finalList.append(list1[x][0])
    return finalList

# Part 2
def x_coordinate(list1:list[data.Point]) -> list[float]:
    list2 = []
    for x in range(len(list1)):
            list2.append(list1[x].x)
    return list2
# Part 3
def are_in_positive_quadrant(list1:list[data.Point]) -> list[data.Point]:
    list2 = []
    for x in range(len(list1)):
        if list1[x].x >= 0 and list1[x].y >= 0:
            list2.append(list1[x])

    return list2
# Part 4
def distance(points1:data.Point, points2:data.Point) -> float:
    return math.sqrt((points1.x - points2.x)**2 + (points1.y - points2.y)**2)


# Part 5

def manhattan_distance(points1:data.Point, points2:data.Point) -> float:
    return abs(points1.x - points2.x) + abs(points1.y - points2.y)




# Part 6

def distance_all(list1:list[data.Point]) -> list[float]:
    list2 = []
    for x in range(len(list1)):
        list2.append(math.sqrt(list1[x].x ** 2 + list1[x].y ** 2))
    return list2