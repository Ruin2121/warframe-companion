from enum import Enum

from warframe_companion.src.inventory import INVENTORY
from warframe_companion.src.base_classes.singleton_base import SingletonBase
from warframe_companion.src.enumerations.updates import Updates


class Item(SingletonBase):
    def __init__(self) -> None:
        super().__init__()
        self._internal_name: Enum
        self._introduced_update: Updates
        self._sell_price: int

    @property
    def internal_name(self) -> Enum:
        """
        Returns the internal name of the item.

        Returns:
            Enum: The internal name as an Enumeration.
        """
        return self._internal_name

    @property
    def external_name(self) -> str:
        """
        Returns the external name of the item.

        Returns:
            str: The external name of the item.
        """
        return self.internal_name.value

    @property
    def introduced_update(self) -> Updates:
        """
        Returns the update the item was introduced in.

        Returns:
            Updates: The update the item was introduced in.
        """
        return self._introduced_update

    @property
    def sell_price(self) -> int:
        """
        Returns the sell price of the item.

        Returns:
            int: The sell price of the item.
        """
        return self._sell_price

    @property
    def quantity_owned(self) -> int:
        """
        Returns the quantity of the item owned.

        Returns:
            int: The quantity of the item owned.
        """

        return INVENTORY[self.internal_name]
