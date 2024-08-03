from __future__ import annotations
from decimal import Decimal
from warframe_companion.src.base_classes.attack_handler import AttackHandler
from warframe_companion.src.base_classes.final_weapon_stats_handler import (
    FinalWeaponStatsHandler,
)
from warframe_companion.src.base_classes.item import Item
from warframe_companion.src.base_classes.weapon_upgrades_handler import (
    WeaponUpgradesHandler,
)
from warframe_companion.src.enumerations import CompatibilityTags, MasteryRanks, Weapons


class Weapon(Item):
    def __init__(self) -> None:
        super().__init__()
        self._mod_type: CompatibilityTags
        self._mastery_rank_requirement: MasteryRanks
        self._max_rank: int
        self._weapon_slot: CompatibilityTags
        self._base_max_ammo_count: int
        self._base_ammo_pickup_amount: int
        self._ammo_type: CompatibilityTags
        self._block_angle: Decimal = Decimal("0.0")
        self._riven_disposition: Decimal
        self._base_magazine_size: int = 0
        self._reload_time: Decimal = Decimal("0.0")
        self._combo_decay: Decimal = Decimal("0.0")
        self._min_combo: int = 0
        self._combo_duration: Decimal = Decimal("0.0")
        self._follow_through: Decimal = Decimal("0.0")
        self._sweep_radius: Decimal = Decimal("0.0")
        self._compatibility_tags: list[CompatibilityTags] = []
        self._riven_family: Weapons
        self._variants: list[Weapon] = []
        self._attack_handler: AttackHandler
        self._weapon_upgrades_handler: WeaponUpgradesHandler = WeaponUpgradesHandler()

        self._final_stats: FinalWeaponStatsHandler

    @property
    def mod_type(self) -> CompatibilityTags:
        return self._mod_type

    @property
    def block_angle(self) -> Decimal:
        return self._block_angle

    @property
    def combo_duration(self) -> Decimal:
        return self._combo_duration

    @property
    def follow_through(self) -> Decimal:
        return self._follow_through

    @property
    def sweep_radius(self) -> Decimal:
        return self._sweep_radius

    @property
    def mastery_rank_requirement(self) -> MasteryRanks:
        return self._mastery_rank_requirement

    @property
    def max_rank(self) -> int:
        return self._max_rank

    @property
    def weapon_slot(self) -> CompatibilityTags:
        return self._weapon_slot

    @property
    def base_max_ammo_count(self) -> int:
        return self._base_max_ammo_count

    @property
    def base_ammo_pickup_amount(self) -> int:
        return self._base_ammo_pickup_amount

    @property
    def ammo_type(self) -> CompatibilityTags:
        return self._ammo_type

    @property
    def riven_disposition(self) -> Decimal:
        return self._riven_disposition

    @property
    def base_magazine_size(self) -> int:
        return self._base_magazine_size

    @property
    def reload_time(self) -> Decimal:
        return self._reload_time

    @property
    def compatibility_tags(self) -> list[CompatibilityTags]:
        return self._compatibility_tags

    @property
    def riven_family(self) -> Weapons:
        return self._riven_family

    @property
    def variants(self) -> list[Weapon]:
        return self._variants

    @property
    def attack_handler(self) -> AttackHandler:
        return self._attack_handler

    @property
    def weapon_upgrades_handler(self) -> WeaponUpgradesHandler:
        return self._weapon_upgrades_handler

    @property
    def final_stats(self) -> FinalWeaponStatsHandler:
        return self._final_stats

    @property
    def combo_decay(self) -> Decimal:
        return self._combo_decay

    @property
    def min_combo(self) -> int:
        return self._min_combo
