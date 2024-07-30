import os
import json


def verify_inventory_data() -> None:
    """
    Verifies that the inventory data is valid.
    """

    # Check if player_data directory exists, if not create it
    player_data_dir = "player_data"
    if not os.path.exists(player_data_dir):
        os.makedirs(player_data_dir)

    # Check if inventory.json file exists in player_data directory
    inventory_file = os.path.join(player_data_dir, "inventory.json")
    if not os.path.isfile(inventory_file):
        # If not, create it
        with open(inventory_file, "w") as f:
            json.dump({}, f)
