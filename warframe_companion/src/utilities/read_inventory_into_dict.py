from enum import Enum
import json

# from warframe_companion.src.enumerations.warframes import Warframes
from warframe_companion.src.enumerations.weapons import Weapons
from warframe_companion.src.inventory import INVENTORY


def read_inventory_into_dict() -> None:
    item_enums: list[Enum] = [Weapons]  # type: ignore

    with open("player_data/inventory.json", "r") as f:
        inventory: dict = json.load(f)

    # Construct Expected Dictionary
    expected_inventory: dict[str, int] = {}

    for item_enum in item_enums:
        for item in item_enum:  # type: ignore
            item: Enum
            expected_inventory[item.value] = 0

    # Update Expected Dictionary
    expected_inventory |= inventory

    with open("player_data/inventory.json", "w") as f:
        json.dump(expected_inventory, f, indent=4)

    # Update INVENTORY
    # Create a lookup dictionary for item enums
    item_enum_lookup = {}
    for item_enum in item_enums:
        for item in item_enum:  # type: ignore
            item_enum_lookup[item.value] = item

    for key in expected_inventory:
        if key in item_enum_lookup:
            INVENTORY[item_enum_lookup[key]] = expected_inventory[key]
        else:
            raise ValueError(f"unrecognized key: {key}")
