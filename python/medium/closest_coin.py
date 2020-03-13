# Write an AI for 2d map game. You have a grid, my position is X. There are coins strewn about in the space.
# Given the location of all coins find the closets coin. You can move up, down, right and left only (not diagonally).

# -----------------------------
# | . | X | . | . | . | . | . |
# -----------------------------
# | . | . | . | o | . | . | . |
# -----------------------------
# | o | . | . | . | . | o | . |
# -----------------------------
# | . | . | . | . | . | . | . |
# -----------------------------
# | . | . | . | o | . | . | . |
# -----------------------------

# distance((2, 1) => (1, 3)) = 3 (1 left + 2 down)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def closest_coin(your_position: Point, coin_positions: [Point]):
    shortest_path = -1
    result = None
    for coin_position in coin_positions:
        x_distance = abs(your_position.x - coin_position.x)
        y_distance = abs(your_position.y - coin_position.y)
        total_distance = x_distance + y_distance

        if shortest_path == -1 or total_distance < shortest_path:
            shortest_path = total_distance
            result = coin_position

    return result.x, result.y or -1


if __name__ == '__main__':
    your_position = Point(1, 0)
    coin_positions = [
        Point(3, 1),
        Point(0, 2),
    ]
    print(closest_coin(your_position=your_position, coin_positions=coin_positions))
