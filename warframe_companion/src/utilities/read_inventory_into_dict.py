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
    for key in expected_inventory:
        for item_enum in item_enums:
            try:
                enum_entry = item_enum(key)  # type: ignore
                INVENTORY[enum_entry] = expected_inventory[key]
            except ValueError:
                continue
