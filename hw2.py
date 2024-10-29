from data import *

# Write your functions for each part in the space below.

# Part 1
# This functions takes two parameters of type Point and will return an output of type Rectangle.
#This function must also assign each Point to its fitting corner value.
def create_rectangle(point1: Point, point2: Point) -> Rectangle:
    if point1.x < point2.x:
        tl_x = point1.x
        br_x = point2.x
    else:
        br_x = point1.x
        tl_x = point2.x
    if point1.y < point2.y:
        tl_y = point2.y
        br_y = point1.y
    else:
        br_y = point2.y
        tl_y = point1.y
    return Rectangle(Point(tl_x, tl_y), Point(br_x, br_y))

# Part 2
#This function takes two parameters of input type Duration and returns an output of type bool.
#This function will return True if the first Duration is shorter than the second and False if not.
def shorter_duration_than(d1: Duration, d2: Duration) -> bool:
    if d1.minutes < d2.minutes:
        return True
    elif d1.minutes == d2.minutes and d1.seconds < d2.seconds:
        return True
    else:
        return False
# Part 3
#This function takes one parameter of input type list[Song] and one of input type Duration.
#It returns an output of type list[Song] of all songs in the input list with a Duration less than
#the input Duration parameter.
def songs_shorter_than(list: list[Song], time: Duration) -> list[Song]:
    newList = []
    for s in list:
        if shorter_duration_than(s.duration, time):
            newList.append(s)
    return newList

# Part 4
#This function takes one parameter of type list[Song] and another of type list[int] and returns an
#output of type Duration. This duration will be the total run time of the given songs.
def running_time(songs: list[Song], nums: list[int]) -> Duration:
    sum_minutes = 0
    sum_seconds = 0
    for s in nums:
        if s >= 0 and s < len(nums):
            sum_minutes += songs[s].duration.minutes
            sum_seconds += songs[s].duration.seconds
    if sum_seconds > 59:
        min = sum_seconds // 59
        sum_seconds -= (59 * min)
        sum_minutes += min
    return Duration(sum_minutes, sum_seconds)

# Part 5
#This function takes one parameter of type list[list[str]] and another of type list[str] and returns an
#output of type bool.  This function must return True if the route is valid, and False otherwise.
# A route is valid when there is a link (as dictated by the first argument to the function)
# between consecutive cities in the list.
def validate_route(routes: list[list[str]], input: list[str]):
    count = 0
    for i in range(len(input) - 1):
        city1 = input[i]
        city2 = input[i + 1]
        if [city1, city2] in routes or [city2, city1] in routes:
            count += 1
    if count == len(input) - 1:
        return True
    else:
        return False
# Part 6
#This function takes one parameter of type list[int] returns an output of type Optional[int].
# This function must return the index at which the longest contiguous repetition begins, or None
# if there is no such repetition
def longest_repetition(list: list[int]) -> int or None:
    count = 0
    longest_rep = 0
    idx = 0
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            count += 1
            if count > longest_rep:
                idx = (i + 1) - count
                longest_rep = count
        else:
            count = 0
    if longest_rep == 0:
        return None
    else:
        return idx
    

