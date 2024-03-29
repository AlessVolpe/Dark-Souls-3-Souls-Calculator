"""
A little script to calculate the souls needed to reach a certain level in Dark Souls 3
"""
from math import floor


def levels_2_12(level):
    times = level - 2
    return floor(673 * ((1 + 2.5 / 100) ** times))


def levels_13_onwards(level):
    return floor(0.02 * pow(level, 3) + 3.06 * pow(level, 2) + 105.6 * level + 895)


def min_souls_needed(level):
    souls_2_12 = sum(levels_2_12(lvl) for lvl in range(2, min(level + 1, 13)))
    souls_13_onwards = sum(levels_13_onwards(lvl) for lvl in range(13, level + 1))
    return souls_2_12 + souls_13_onwards


def souls_needed(current, desired):
    if desired == current or desired < 2:
        return 0

    min_current = min_souls_needed(current)
    min_desired = min_souls_needed(desired)
    return min_desired - min_current


if __name__ == '__main__':
    current_level = int(input("Input current level: "))
    desired_level = int(input("Input desired level: "))

    if desired_level < current_level:
        quit("Desired level can't be less than current level")

    print("The souls needed to reach level %d from level %d is %d" % (current_level,
                                                                      desired_level,
                                                                      souls_needed(current_level, desired_level)))
    quit(0)
