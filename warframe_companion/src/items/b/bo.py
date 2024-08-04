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
    TriggerTypes,
    Updates,
    Weapons,
)


class Bo(Weapon):
    def __init__(self) -> None:
        super().__init__()

        # Item Class
        self._internal_name: Enum = Weapons.BO

        # Weapon Class
        self._mod_type = CompatibilityTags.STAFF
        self._mastery_rank_requirement = MasteryRanks.MR0
        self._max_rank = 30
        self._weapon_slot = CompatibilityTags.MELEE
        self._block_angle = D("60")
        self._combo_duration = D("5.0")
        self._riven_disposition = D("1.35")
        self._follow_through = D("0.5")
        self._sweep_radius = D("0.25")
        self._compatibility_tags = [
            CompatibilityTags.STAVES_STANCE,
        ]
        self._riven_family = Weapons.BO
        self._introduced_update = Updates.VANILLA
        self._sell_price = 5_000
        # TODO: Add Incarnon Form
        self._variants = [self]  # type: ignore

        # Normal Attack
        self._attack_handler = AttackHandler(
            trigger_type=TriggerTypes.NA,
            attack_speed=D("1.00"),
            noise_level=NoiseLevels.SILENT,
            damage=DamageInstance(
                impact_damage=D("126"),
                puncture_damage=D("14"),
            ),
            critical_chance=D("0.125"),
            critical_multiplier=D("2.00"),
            range=D("3.00"),
            status_chance=D("0.20"),
        )
        self._weapon_upgrades_handler.mod_slot_stance.slot_polarity = Polarities.UNAIRU
        self._weapon_upgrades_handler.mod_slot_1.slot_polarity = Polarities.VAZARIN

        self._final_stats = FinalWeaponStatsHandler(self)


if __name__ == "__main__":
    bo = Bo()

    print(bo)
    print(bo.final_stats.quantum)
    print(bo.final_stats.quantized_damage_no_armor)
    print("---------------------------------------------------")
    print(f"Arsenal Total Damage: {bo.final_stats.arsenal_total_damage}")
    print(f"Real Total Damage (no armor): {bo.final_stats.real_total_damage_no_armor}")
    print(f"Real Total Damage (max armor): {bo.final_stats.real_total_damage_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Average Hit: {bo.final_stats.arsenal_average_hit}")
    print(f"Real Average Hit (no armor): {bo.final_stats.real_average_hit_no_armor}")
    print(f"Real Average Hit (max armor): {bo.final_stats.real_average_hit_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Burst DPS: {bo.final_stats.arsenal_burst_dps}")
    print(f"Real Burst DPS (no armor): {bo.final_stats.real_burst_dps_no_armor}")
    print(f"Real Burst DPS (max armor): {bo.final_stats.real_burst_dps_max_armor}")
    print("---------------------------------------------------")
    print(f"Arsenal Sustained DPS: {bo.final_stats.arsenal_sustained_dps}")
    print(f"Real Sustained DPS (no armor): {bo.final_stats.real_sustained_dps_no_armor}")
    print(f"Real Sustained DPS (max armor): {bo.final_stats.real_sustained_dps_max_armor}")
