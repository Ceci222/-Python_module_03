import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        values = coords.split(",")  # split returns a list

        if len(values) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(values[0])
        except ValueError as e:
            print(f"Error on parameter '{values[0]}': {e}")
            continue

        try:
            y = float(values[1])
        except ValueError as e:
            print(f"Error on parameter '{values[1]}': {e}")
            continue

        try:
            z = float(values[2])
        except ValueError as e:
            print(f"Error on parameter '{values[2]}': {e}")
            continue

        return (x, y, z)  # returns a tuple
#  The infinite loop keeps running till sth fails.
#  If it does it starts again, else keeps going till the return and then stops


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")

    x, y, z = first_pos  # unpacking tuple into a simple variable.
    print(f"It includes: X={x}, Y={y}, Z={z}")

    distance_center = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance to center: {round(distance_center, 4)}")
    # rounds to 4 decimals
    print()

    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    x1, y1, z1 = first_pos
    x2, y2, z2 = second_pos
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")
    print()


if __name__ == "__main__":
    main()
