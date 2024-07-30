import json
from warframe_companion.src.inventory import INVENTORY


def read_inventory_into_dict() -> None:
    with open("player_data/inventory.json", "r") as f:
        inventory: dict = json.load(f)

    # TODO : This isn't going to work long term
    # TODO : Iterate through the inventory and build a new dictionary by match-case on the internal name and its string value
    # TODO : Then update INVENTORY with the new dictionary
    INVENTORY.update(inventory)
