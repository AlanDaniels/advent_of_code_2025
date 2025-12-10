#!/usr/bin/env python3


def main(turns: list[int]) -> int:
    dial = 50
    zeroes = 0
    for turn in turns:
        (direction, count) = (turn[0], int(turn[1:]))
        match direction:
            case 'L':
                dial -= count
            case 'R':
                dial += count
            case _:
                raise ValueError("Invalid direction: {}".format(direction))
        dial %= 100
        if dial == 0:
            zeroes += 1
        print("{0} {1:2d} {2:2d}{3}".format(direction, count, dial, " ZERO" if dial == 0 else ""))
    return zeroes


def read_input(filename: str) -> list[int]:
    result = []
    with open(filename) as fp:
        for line in fp:
            result.append(line.strip())
    return result


if __name__ == "__main__":
    # Correct answer = 3
    trial_turns = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    result = main(trial_turns)
    print("RESULT =", result)
    assert result == 3
    # Correct answer = 1152. Got it correct!
    real_deal = read_input("problem_01_input.txt")
    result = main(real_deal)
    print("RESULT =", result)
    assert result == 1152
    print("All done!")