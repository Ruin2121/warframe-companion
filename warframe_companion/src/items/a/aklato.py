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


class Aklato(Weapon):
    def __init__(self) -> None:
        super().__init__()

        # Item Class
        self._internal_name: Enum = Weapons.AKLATO

        # Weapon Class
        self._mod_type = CompatibilityTags.DUAL_PISTOLS
        self._mastery_rank_requirement = MasteryRanks.MR3
        self._max_rank = 30
        self._weapon_slot = CompatibilityTags.SECONDARY
        self._base_max_ammo_count: int = 210
        self._base_ammo_pickup_amount: int = 40
        self._ammo_type = CompatibilityTags.SECONDARY
        self._riven_disposition = D("1.52")
        self._base_magazine_size: int = 30
        self._reload_time: D = D("2.40")
        self._compatibility_tags = []
        self._riven_family = Weapons.AKLATO
        self._introduced_update = Updates.VANILLA
        self._sell_price = 5_000
        self._variants = [self]  # type: ignore

        # Normal Attack
        self._attack_handler = AttackHandler(
            trigger_type=TriggerTypes.SEMI,
            minimum_spread=D("4.0"),
            maximum_spread=D("14.0"),
            fire_rate=D("5.00"),
            noise_level=NoiseLevels.ALARMING,
            projectile_type=ProjectileTypes.HITSCAN,
            damage=DamageInstance(
                impact_damage=D("6"),
                puncture_damage=D("10"),
                slash_damage=D("24"),
            ),
            ammo_cost=D("1.0"),
            critical_chance=D("0.10"),
            critical_multiplier=D("1.80"),
            multishot=D("1.0"),
            punch_through=D("0.0"),
            range=D("300.0"),
            status_chance=D("0.06"),
        )
        self._weapon_upgrades_handler.mod_slot_exilus.slot_polarity = Polarities.MADURAI

        self._final_stats = FinalWeaponStatsHandler(self)


if __name__ == "__main__":
    aklato = Aklato()

    print(aklato)
    print(aklato.final_stats.quantum)
    print(aklato.final_stats.quantized_damage_no_armor)
    print("---------------------------------------------------")
    print(f"Arsenal Total Damage: {aklato.final_stats.arsenal_total_damage}")
    print(f"Real Total Damage (no armor): {aklato.final_stats.real_total_damage_no_armor}")
    print(f"Real Total Damage (max armor): {aklato.final_stats.real_total_damage_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Average Hit: {aklato.final_stats.arsenal_average_hit}")
    print(f"Real Average Hit (no armor): {aklato.final_stats.real_average_hit_no_armor}")
    print(f"Real Average Hit (max armor): {aklato.final_stats.real_average_hit_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Burst DPS: {aklato.final_stats.arsenal_burst_dps}")
    print(f"Real Burst DPS (no armor): {aklato.final_stats.real_burst_dps_no_armor}")
    print(f"Real Burst DPS (max armor): {aklato.final_stats.real_burst_dps_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Sustained DPS: {aklato.final_stats.arsenal_sustained_dps}")
    print(f"Real Sustained DPS (no armor): {aklato.final_stats.real_sustained_dps_no_armor}")
    print(f"Real Sustained DPS (max armor): {aklato.final_stats.real_sustained_dps_max_armor}")
