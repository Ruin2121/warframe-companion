from cleo.commands.command import Command
from warframe_companion.src.utilities.verify_inventory_data import verify_inventory_data
from warframe_companion.src.utilities.read_inventory_into_dict import read_inventory_into_dict
from warframe_companion.src.inventory import INVENTORY


class MainCommand(Command):
    """
    Main Command
    """

    name = "main"
    description = "Main Command"

    arguments = []

    def handle(self) -> None:
        verify_inventory_data()
        read_inventory_into_dict()

        print("Hello World!")
        print(INVENTORY)
