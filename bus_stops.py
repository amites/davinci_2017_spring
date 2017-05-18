# https://www.codewars.com/kata/number-of-people-in-the-bus/train/python

def number(bus_stops):
    num_people = 0
    for stop in bus_stops:
        num_people += stop[0] - stop[1]
    return num_people
