from decimal import Decimal as D
from enum import Enum

from warframe_companion.src.base_classes.attack_handler import AttackHandler
from warframe_companion.src.base_classes.damage_instance import DamageInstance
from warframe_companion.src.base_classes.final_weapon_stats_handler import (
    FinalWeaponStatsHandler,
)
from warframe_companion.src.base_classes.weapon import Weapon
from warframe_companion.src.enumerations import (
    CompatibilityTags,
    MasteryRanks,
    NoiseLevels,
    Polarities,
    ProjectileTypes,
    TriggerTypes,
    Updates,
    Weapons,
)


class MK1Braton(Weapon):
    def __init__(self) -> None:
        super().__init__()

        # Item Class
        self._internal_name: Enum = Weapons.MK1BRATON

        # Weapon Class
        self._mod_type = CompatibilityTags.RIFLE
        self._mastery_rank_requirement = MasteryRanks.MR0
        self._max_rank = 30
        self._weapon_slot = CompatibilityTags.PRIMARY
        self._base_max_ammo_count: int = 540
        self._base_ammo_pickup_amount: int = 80
        self._ammo_type = CompatibilityTags.PRIMARY
        self._riven_disposition = D("1.35")
        self._base_magazine_size: int = 60
        self._reload_time: D = D("2.0")
        self._compatibility_tags = [
            CompatibilityTags.ASSAULT_AMMO,
        ]
        self._riven_family = Weapons.BRATON
        self._introduced_update = Updates.VANILLA
        self._sell_price = 2_500
        # TODO: Add Incarnon form
        self._variants = [self]  # type: ignore

        # Normal Attack
        self._attack_handler = AttackHandler(
            trigger_type=TriggerTypes.AUTO,
            minimum_spread=D("1.0"),
            maximum_spread=D("4.0"),
            fire_rate=D("7.50"),
            noise_level=NoiseLevels.ALARMING,
            projectile_type=ProjectileTypes.HITSCAN,
            damage=DamageInstance(
                impact_damage=D("4.5"),
                puncture_damage=D("4.5"),
                slash_damage=D("9"),
            ),
            ammo_cost=D("1.0"),
            critical_chance=D("0.08"),
            critical_multiplier=D("1.50"),
            multishot=D("1.0"),
            punch_through=D("0.0"),
            range=D("300.0"),
            status_chance=D("0.05"),
        )
        self._weapon_upgrades_handler.mod_slot_exilus.slot_polarity = Polarities.NARAMON

        self._final_stats = FinalWeaponStatsHandler(self)


if __name__ == "__main__":
    mk1_braton = MK1Braton()

    print(mk1_braton)
    print(mk1_braton.final_stats.quantum)
    print(mk1_braton.final_stats.quantized_damage_no_armor)
    print("---------------------------------------------------")
    print(f"Arsenal Total Damage: {mk1_braton.final_stats.arsenal_total_damage}")
    print(f"Real Total Damage (no armor): {mk1_braton.final_stats.real_total_damage_no_armor}")
    print(f"Real Total Damage (max armor): {mk1_braton.final_stats.real_total_damage_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Average Hit: {mk1_braton.final_stats.arsenal_average_hit}")
    print(f"Real Average Hit (no armor): {mk1_braton.final_stats.real_average_hit_no_armor}")
    print(f"Real Average Hit (max armor): {mk1_braton.final_stats.real_average_hit_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Burst DPS: {mk1_braton.final_stats.arsenal_burst_dps}")
    print(f"Real Burst DPS (no armor): {mk1_braton.final_stats.real_burst_dps_no_armor}")
    print(f"Real Burst DPS (max armor): {mk1_braton.final_stats.real_burst_dps_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Sustained DPS: {mk1_braton.final_stats.arsenal_sustained_dps}")
    print(f"Real Sustained DPS (no armor): {mk1_braton.final_stats.real_sustained_dps_no_armor}")
    print(f"Real Sustained DPS (max armor): {mk1_braton.final_stats.real_sustained_dps_max_armor}")
