from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from warframe_companion.src.base_classes.weapon import Weapon


class FinalWeaponStatsHandler:
    def __init__(self, weapon: Weapon) -> None:
        self._weapon = weapon

    @property
    def quantum(self) -> float:
        return self._weapon.attack_handler.total_damage / 16
