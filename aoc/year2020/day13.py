#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/13
"""


from data.utils import get_input


def part1(text):
    time, notes = text.splitlines()

    earliest = int(time)
    buses = (int(bus) for bus in notes.split(",") if bus != "x")
    minimum = min(buses, key=lambda bus: (bus - earliest) % bus)

    return (minimum - earliest) % minimum * minimum


def part2(text):
    _, notes = text.splitlines()

    time, lcm = 0, 1
    for i, bus in enumerate(notes.split(",")):
        if bus == "x":
            continue

        bus = int(bus)
        k = -(time + i) * pow(lcm, -1, bus) % bus
        time += k * lcm
        lcm *= bus

    return time


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 13)

    print(part1(text))
    print(part2(text))
