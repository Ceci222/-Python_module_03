import sys


def arg_parser(args: list[str]) -> dict[str,int]:
    parsed_data = dict[str,int] = {}
    for arg in args[1:]:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter {arg}")
            continue
    return parsed_data