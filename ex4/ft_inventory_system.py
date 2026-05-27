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
            quantity = int(quantity_str)  # if it's not "3" like "a" = error
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        if name in parsed_data:
            print(f"Redundant item '{name}' - discarding")
            continue
        parsed_data[name] = quantity
        # I add quantity only once it's been checked
    return parsed_data


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = arg_parser(sys.argv[1:])  # sys.argv[1:] here not in function
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_items = len(inventory)
    total_quantity = 0

    for item in inventory.values():
        total_quantity = total_quantity + item

    print(f"Total quantity of the {total_items} items: {total_quantity}")

    for key in inventory.keys():
        value = inventory[key]
        percentage = round((value * 100) / total_quantity, 1)
        print(f"Item {key} represents {percentage}%")

    most_abundant_item = ""
    quantity = 0

    for key in inventory.keys():
        value = inventory[key]
        if quantity == 0 and value > 0:
            quantity = value
            most_abundant_item = key
        elif value > quantity:
            quantity = value
            most_abundant_item = key

    print(f"Item most abundant: {most_abundant_item} with quantity {quantity}")

    least_abundant_item = ""
    least_quantity = quantity

    for key in inventory.keys():
        value = inventory[key]
        if least_quantity > value:
            least_quantity = value
            least_abundant_item = key

    print(f"Item least abundant: {least_abundant_item} "
          f"with quantity {least_quantity}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
"""

python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value

"""