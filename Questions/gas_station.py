"""
Solves the valid gas station problem
"""


def valid_station(gas, cost):
    remaining = 0
    i = 0
    start = 0
    while i < len(cost):
        remaining += gas[i]
        remaining -= cost[i]
        i += 1
        if remaining < 0:
            remaining = 0
            start = i
    if start == 0:
        return start
    else:
        if sum(gas[:start]) - sum(cost[:start]) + remaining >= 0:
            return start
        else:
            return -1


def main():
    gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
    cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
    print(valid_station(gas=gas, cost=cost))


if __name__ == "__main__":
    main()
