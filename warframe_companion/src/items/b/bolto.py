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


class Bolto(Weapon):
    def __init__(self) -> None:
        super().__init__()

        # Item Class
        self._internal_name: Enum = Weapons.BOLTO

        # Weapon Class
        self._mod_type = CompatibilityTags.PISTOL
        self._mastery_rank_requirement = MasteryRanks.MR7
        self._max_rank = 30
        self._weapon_slot = CompatibilityTags.SECONDARY
        self._base_max_ammo_count: int = 210
        self._base_ammo_pickup_amount: int = 40
        self._ammo_type = CompatibilityTags.SECONDARY
        self._riven_disposition = D("1.51")
        self._base_magazine_size: int = 15
        self._reload_time: D = D("1.30")
        self._compatibility_tags = [
            CompatibilityTags.PROJECTILE,
        ]
        self._riven_family = Weapons.BOLTO
        self._introduced_update = Updates.VANILLA
        self._sell_price = 5_000
        self._variants = [self]  # type: ignore

        # Normal Attack
        self._attack_handler = AttackHandler(
            trigger_type=TriggerTypes.SEMI,
            minimum_spread=D("0.50"),
            maximum_spread=D("7.00"),
            fire_rate=D("3.33"),
            noise_level=NoiseLevels.ALARMING,
            projectile_type=ProjectileTypes.PROJECTILE,
            damage=DamageInstance(
                impact_damage=D("6.4"),
                puncture_damage=D("57.6"),
            ),
            ammo_cost=D("1.0"),
            critical_chance=D("0.16"),
            critical_multiplier=D("2.40"),
            multishot=D("1.0"),
            punch_through=D("0.0"),
            status_chance=D("0.022"),
            projectile_speed=D("75.0"),
        )
        self._weapon_upgrades_handler.mod_slot_exilus.slot_polarity = Polarities.NARAMON
        self._weapon_upgrades_handler.mod_slot_1.slot_polarity = Polarities.VAZARIN

        self._final_stats = FinalWeaponStatsHandler(self)


if __name__ == "__main__":
    bolto = Bolto()

    print(bolto)
    print(bolto.final_stats.quantum)
    print(bolto.final_stats.quantized_damage_no_armor)
    print("---------------------------------------------------")
    print(f"Arsenal Total Damage: {bolto.final_stats.arsenal_total_damage}")
    print(f"Real Total Damage (no armor): {bolto.final_stats.real_total_damage_no_armor}")
    print(f"Real Total Damage (max armor): {bolto.final_stats.real_total_damage_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Average Hit: {bolto.final_stats.arsenal_average_hit}")
    print(f"Real Average Hit (no armor): {bolto.final_stats.real_average_hit_no_armor}")
    print(f"Real Average Hit (max armor): {bolto.final_stats.real_average_hit_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Burst DPS: {bolto.final_stats.arsenal_burst_dps}")
    print(f"Real Burst DPS (no armor): {bolto.final_stats.real_burst_dps_no_armor}")
    print(f"Real Burst DPS (max armor): {bolto.final_stats.real_burst_dps_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Sustained DPS: {bolto.final_stats.arsenal_sustained_dps}")
    print(f"Real Sustained DPS (no armor): {bolto.final_stats.real_sustained_dps_no_armor}")
    print(f"Real Sustained DPS (max armor): {bolto.final_stats.real_sustained_dps_max_armor}")
