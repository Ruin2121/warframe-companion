from __future__ import annotations
from typing import TYPE_CHECKING
from decimal import Decimal as D

from warframe_companion.src.base_classes.damage_instance import DamageInstance
from warframe_companion.src.enumerations.trigger_types import TriggerTypes

if TYPE_CHECKING:
    from warframe_companion.src.base_classes.weapon import Weapon


###
# TODO: Quantized stats assume base damage currently, this should be fixed when mod support is added.
###
class FinalWeaponStatsHandler:
    def __init__(self, weapon: Weapon) -> None:
        self._weapon = weapon
        self.attack_handler = self._weapon.attack_handler
        self.base_damage = self.attack_handler.base_damage
        self.quantum = D(self.base_damage.total_damage / 16)

    @property
    def final_critical_chance(self) -> D:
        # TODO: Fix when mod support is added
        return self.attack_handler.critical_chance

    @property
    def final_critical_multiplier(self) -> D:
        # TODO: Fix when mod support is added
        return self.attack_handler.critical_multiplier

    @property
    def final_fire_rate(self) -> D:
        # TODO: Fix when mod support is added
        return self.attack_handler.base_fire_rate

    @property
    def final_multishot(self) -> D:
        # TODO: Fix when mod support is added
        return self.attack_handler.multishot

    @property
    def effective_fire_rate(self) -> D:
        # We are assuming that Auto-Spool weapons are fully spooled
        if self.attack_handler.trigger_type in (
            TriggerTypes.AUTO,
            TriggerTypes.AUTO_SPOOL,
            TriggerTypes.SEMI,
        ):
            return self.final_fire_rate

        elif self.attack_handler.trigger_type == TriggerTypes.BURST:
            burst_count = self.attack_handler.burst_count
            burst_delay = self.attack_handler.burst_delay
            fire_rate = self.final_fire_rate

            return burst_count / ((1 / fire_rate) + ((burst_count - 1) * burst_delay))

        else:
            return D("0")

    @property
    def final_magazine_size(self) -> int:
        # TODO: Fix when mod support is added
        return self._weapon.base_magazine_size

    @property
    def num_shots_per_mag(self) -> D:
        return self.final_magazine_size / self.attack_handler.ammo_cost

    @property
    def final_reload_time(self) -> D:
        # TODO: Fix when mod support is added
        return self._weapon.reload_time

    @property
    def proportion_time_spent_shooting_vs_reloading(self) -> D:
        # TODO: Check if this is correct
        return self.num_shots_per_mag / (
            D(self.effective_fire_rate) * D(self.final_reload_time) + self.num_shots_per_mag
        )

    @property
    def quantized_impact(self) -> D:
        return self.quantum * (self.base_damage.damage_impact / self.quantum).to_integral_exact()

    @property
    def quantized_puncture(self) -> D:
        return self.quantum * (self.base_damage.damage_puncture / self.quantum).to_integral_exact()

    @property
    def quantized_slash(self) -> D:
        return self.quantum * (self.base_damage.damage_slash / self.quantum).to_integral_exact()

    @property
    def quantized_cold(self) -> D:
        return self.quantum * (self.base_damage.damage_cold / self.quantum).to_integral_exact()

    @property
    def quantized_electricity(self) -> D:
        return (
            self.quantum * (self.base_damage.damage_electricity / self.quantum).to_integral_exact()
        )

    @property
    def quantized_heat(self) -> D:
        return self.quantum * (self.base_damage.damage_heat / self.quantum).to_integral_exact()

    @property
    def quantized_toxin(self) -> D:
        return self.quantum * (self.base_damage.damage_toxin / self.quantum).to_integral_exact()

    @property
    def quantized_blast(self) -> D:
        return self.quantum * (self.base_damage.damage_blast / self.quantum).to_integral_exact()

    @property
    def quantized_corrosive(self) -> D:
        return self.quantum * (self.base_damage.damage_corrosive / self.quantum).to_integral_exact()

    @property
    def quantized_gas(self) -> D:
        return self.quantum * (self.base_damage.damage_gas / self.quantum).to_integral_exact()

    @property
    def quantized_magnetic(self) -> D:
        return self.quantum * (self.base_damage.damage_magnetic / self.quantum).to_integral_exact()

    @property
    def quantized_radiation(self) -> D:
        return self.quantum * (self.base_damage.damage_radiation / self.quantum).to_integral_exact()

    @property
    def quantized_viral(self) -> D:
        return self.quantum * (self.base_damage.damage_viral / self.quantum).to_integral_exact()

    @property
    def quantized_tau(self) -> D:
        return self.quantum * (self.base_damage.damage_tau / self.quantum).to_integral_exact()

    @property
    def quantized_void(self) -> D:
        return self.quantum * (self.base_damage.damage_void / self.quantum).to_integral_exact()

    @property
    def quantized_true(self) -> D:
        return self.quantum * (self.base_damage.damage_true / self.quantum).to_integral_exact()

    @property
    def quantized_damage_no_armor(self) -> DamageInstance:
        return DamageInstance(
            self.quantized_impact,
            self.quantized_puncture,
            self.quantized_slash,
            self.quantized_cold,
            self.quantized_electricity,
            self.quantized_heat,
            self.quantized_toxin,
            self.quantized_blast,
            self.quantized_corrosive,
            self.quantized_gas,
            self.quantized_magnetic,
            self.quantized_radiation,
            self.quantized_viral,
            self.quantized_tau,
            self.quantized_void,
            self.quantized_true,
        )

    @property
    def quantized_damage_max_armor(
        self,
    ) -> DamageInstance:  # sourcery skip: low-code-quality
        # It might be nice to refactor this later.

        q_imp = self.quantized_impact * D("0.10")
        q_pun = self.quantized_puncture * D("0.10")
        q_sla = self.quantized_slash * D("0.10")
        q_col = self.quantized_cold * D("0.10")
        q_ele = self.quantized_electricity * D("0.10")
        q_hea = self.quantized_heat * D("0.10")
        q_tox = self.quantized_toxin * D("0.10")
        q_bla = self.quantized_blast * D("0.10")
        q_cor = self.quantized_corrosive * D("0.10")
        q_gas = self.quantized_gas * D("0.10")
        q_mag = self.quantized_magnetic * D("0.10")
        q_rad = self.quantized_radiation * D("0.10")
        q_vir = self.quantized_viral * D("0.10")
        q_tau = self.quantized_tau * D("0.10")
        q_voi = self.quantized_void * D("0.10")
        q_tru = self.quantized_true * D("0.10")

        if q_imp == 0:
            nq_imp = D("0")
        elif q_imp > D("1"):
            nq_imp = q_imp
        else:
            nq_imp = D("1")

        if q_pun == 0:
            nq_pun = D("0")
        elif q_pun > D("1"):
            nq_pun = q_pun
        else:
            nq_pun = D("1")

        if q_sla == 0:
            nq_sla = D("0")
        elif q_sla > D("1"):
            nq_sla = q_sla
        else:
            nq_sla = D("1")

        if q_col == 0:
            nq_col = D("0")
        elif q_col > D("1"):
            nq_col = q_col
        else:
            nq_col = D("1")

        if q_ele == 0:
            nq_ele = D("0")
        elif q_ele > D("1"):
            nq_ele = q_ele
        else:
            nq_ele = D("1")

        if q_hea == 0:
            nq_hea = D("0")
        elif q_hea > D("1"):
            nq_hea = q_hea
        else:
            nq_hea = D("1")

        if q_tox == 0:
            nq_tox = D("0")
        elif q_tox > D("1"):
            nq_tox = q_tox
        else:
            nq_tox = D("1")

        if q_bla == 0:
            nq_bla = D("0")
        elif q_bla > D("1"):
            nq_bla = q_bla
        else:
            nq_bla = D("1")

        if q_cor == 0:
            nq_cor = D("0")
        elif q_cor > D("1"):
            nq_cor = q_cor
        else:
            nq_cor = D("1")

        if q_gas == 0:
            nq_gas = D("0")
        elif q_gas > D("1"):
            nq_gas = q_gas
        else:
            nq_gas = D("1")

        if q_mag == 0:
            nq_mag = D("0")
        elif q_mag > D("1"):
            nq_mag = q_mag
        else:
            nq_mag = D("1")

        if q_rad == 0:
            nq_rad = D("0")
        elif q_rad > D("1"):
            nq_rad = q_rad
        else:
            nq_rad = D("1")

        if q_vir == 0:
            nq_vir = D("0")
        elif q_vir > D("1"):
            nq_vir = q_vir
        else:
            nq_vir = D("1")

        if q_tau == 0:
            nq_tau = D("0")
        elif q_tau > D("1"):
            nq_tau = q_tau
        else:
            nq_tau = D("1")

        if q_voi == 0:
            nq_voi = D("0")
        elif q_voi > D("1"):
            nq_voi = q_voi
        else:
            nq_voi = D("1")

        if q_tru == 0:
            nq_tru = D("0")
        elif q_tru > D("1"):
            nq_tru = q_tru
        else:
            nq_tru = D("1")

        return DamageInstance(
            nq_imp,
            nq_pun,
            nq_sla,
            nq_col,
            nq_ele,
            nq_hea,
            nq_tox,
            nq_bla,
            nq_cor,
            nq_gas,
            nq_mag,
            nq_rad,
            nq_vir,
            nq_tau,
            nq_voi,
            nq_tru,
        )

    @property
    def arsenal_average_hit(self) -> D:
        return (
            self.arsenal_total_damage
            * (1 + (self.final_critical_chance * (self.final_critical_multiplier - 1)))
        ).quantize(D("1.00"))

    @property
    def real_average_hit_no_armor(self) -> D:
        return (
            self.real_total_damage_no_armor
            * (1 + (self.final_critical_chance * (self.final_critical_multiplier - 1)))
        ).quantize(D("1.00"))

    @property
    def real_average_hit_max_armor(self) -> D:
        return (
            self.real_total_damage_max_armor
            * (1 + (self.final_critical_chance * (self.final_critical_multiplier - 1)))
        ).quantize(D("1.00"))

    @property
    def arsenal_total_damage(self) -> D:
        return (self.base_damage.total_damage * self.final_multishot).to_integral_exact()

    @property
    def real_total_damage_no_armor(self) -> D:
        return (self.quantized_damage_no_armor.total_damage * self.final_multishot).quantize(
            D("1.00")
        )

    @property
    def real_total_damage_max_armor(self) -> D:
        return (self.quantized_damage_max_armor.total_damage * self.final_multishot).quantize(
            D("1.00")
        )

    @property
    def arsenal_burst_dps(self) -> D:
        return (self.arsenal_average_hit * self.effective_fire_rate).quantize(D("1.00"))

    @property
    def real_burst_dps_no_armor(self) -> D:
        return (self.real_average_hit_no_armor * self.effective_fire_rate).quantize(D("1.00"))

    @property
    def real_burst_dps_max_armor(self) -> D:
        return (self.real_average_hit_max_armor * self.effective_fire_rate).quantize(D("1.00"))

    @property
    def arsenal_sustained_dps(self) -> D:
        return (self.arsenal_burst_dps * self.proportion_time_spent_shooting_vs_reloading).quantize(
            D("1.00")
        )

    @property
    def real_sustained_dps_no_armor(self) -> D:
        return (
            self.real_burst_dps_no_armor * self.proportion_time_spent_shooting_vs_reloading
        ).quantize(D("1.00"))

    @property
    def real_sustained_dps_max_armor(self) -> D:
        return (
            self.real_burst_dps_max_armor * self.proportion_time_spent_shooting_vs_reloading
        ).quantize(D("1.00"))
