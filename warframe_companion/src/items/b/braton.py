from enum import Enum

from warframe_companion.src.base_classes.weapon import Weapon
from warframe_companion.src.base_classes.attack_handler import AttackHandler
from warframe_companion.src.enumerations import (
    Weapons,
    CompatibilityTags,
    MasteryRanks,
    Updates,
    TriggerTypes,
    NoiseLevels,
    ProjectileTypes,
    Polarities,
)


class Braton(Weapon):
    def __init__(self) -> None:
        super().__init__()

        # Item Class
        self._internal_name: Enum = Weapons.BRATON

        # Weapon Class
        self._mod_type = CompatibilityTags.RIFLE
        self._mastery_rank_requirement = MasteryRanks.MR0
        self._max_rank = 30
        self._weapon_slot = CompatibilityTags.PRIMARY
        self._base_max_ammo_count: int = 540
        self._base_ammo_pickup_amount: int = 80
        self._ammo_type = CompatibilityTags.PRIMARY
        self._riven_disposition = 1.35
        self._base_magazine_size: int = 45
        self._reload_time: float = 2.0
        self._compatibility_tags = [
            CompatibilityTags.ASSAULT_AMMO,
        ]
        self._riven_family = Weapons.BRATON
        self._introduced_update = Updates.VANILLA
        self._sell_price = 7_500
        self._variants = [self]

        # Normal Attack
        self._attack_handler = AttackHandler(
            trigger_type=TriggerTypes.AUTO,
            minimum_spread=2.0,
            maximum_spread=5.0,
            fire_rate=8.75,
            noise_level=NoiseLevels.ALARMING,
            projectile_type=ProjectileTypes.HITSCAN,
            impact_damage=7.92,
            puncture_damage=7.92,
            slash_damage=8.16,
            ammo_cost=1,
            critical_chance=0.12,
            critical_multiplier=1.60,
            multishot=1,
            punch_through=0.0,
            range=300.0,
            status_chance=0.06,
        )
        self._weapon_upgrades_handler.mod_slot_exilus.slot_polarity = Polarities.NARAMON

        # TODO: Add Incarnon Form
        # self._incarnon_form =


if __name__ == "__main__":
    braton = Braton()

    print(braton)
    print(braton.final_stats.quantum)
