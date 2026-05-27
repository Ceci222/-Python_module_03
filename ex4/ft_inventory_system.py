import sys


def arg_parser(args: list[str]) -> dict[str, int]:
    parsed_data: dict[str, int] = {}
    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, quantity_str = parts
        try:
            quantity = int(quantity_str)  #if it's not "3" like "a" = error
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        if name in parsed_data:
            print(f"Redundant item '{name}' - discarding")
            continue
        parsed_data[name] = quantity  # I add quantity only once it's been checked
    return parsed_data
