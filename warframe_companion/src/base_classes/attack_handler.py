from __future__ import annotations
from warframe_companion.src.enumerations import (
    NoiseLevels,
    ProjectileTypes,
    TriggerTypes,
    AccuracyDescs,
)


class AttackHandler:
    def __init__(
        self,
        fire_rate: float,
        noise_level: NoiseLevels,
        projectile_type: ProjectileTypes,
        critical_chance: float,
        critical_multiplier: float,
        multishot: float,
        range: float,
        status_chance: float,
        #
        trigger_type: TriggerTypes = TriggerTypes.UNKNOWN,
        minimum_spread: float = 0.0,
        maximum_spread: float = 0.0,
        ammo_cost: float = 1,
        punch_through: float = 0.0,
        impact_damage: float = 0.0,
        puncture_damage: float = 0.0,
        slash_damage: float = 0.0,
        cold_damage: float = 0.0,
        electricity_damage: float = 0.0,
        heat_damage: float = 0.0,
        toxin_damage: float = 0.0,
        blast_damage: float = 0.0,
        corrosive_damage: float = 0.0,
        gas_damage: float = 0.0,
        magnetic_damage: float = 0.0,
        radiation_damage: float = 0.0,
        viral_damage: float = 0.0,
        void_damage: float = 0.0,
        true_damage: float = 0.0,
        AoE_attack: AttackHandler | None = None,
    ) -> None:
        self._trigger_type: TriggerTypes = trigger_type  #
        self._base_minimum_spread: float = minimum_spread  #
        self._base_maximum_spread: float = maximum_spread  #
        self._base_fire_rate: float = fire_rate  #
        self._base_noise_level: NoiseLevels = noise_level  #
        self._projectile_type: ProjectileTypes = projectile_type  #
        self._base_damage_impact: float = impact_damage  #
        self._base_damage_puncture: float = puncture_damage  #
        self._base_damage_slash: float = slash_damage  #
        self._base_damage_cold: float = cold_damage  #
        self._base_damage_electricity: float = electricity_damage  #
        self._base_damage_heat: float = heat_damage  #
        self._base_damage_toxin: float = toxin_damage  #
        self._base_damage_blast: float = blast_damage  #
        self._base_damage_corrosive: float = corrosive_damage  #
        self._base_damage_gas: float = gas_damage  #
        self._base_damage_magnetic: float = magnetic_damage  #
        self._base_damage_radiation: float = radiation_damage  #
        self._base_damage_viral: float = viral_damage  #
        self._base_damage_void: float = void_damage  #
        self._base_damage_true: float = true_damage  #
        self._base_ammo_cost: float = ammo_cost  #
        self._base_critical_chance: float = critical_chance  #
        self._base_critical_multiplier: float = critical_multiplier  #
        self._base_multishot: float = multishot  #
        # This might be moved to base Weapon Class. Not sure if this changes based on firing mode.
        self._base_punch_through: float = punch_through  #
        self._base_range: float = range  #
        self._base_status_chance: float = status_chance  #
        self._AoE_attack: AttackHandler | None = AoE_attack  #

    @property
    def trigger_type(self) -> TriggerTypes:
        """
        Returns the trigger type of the weapon.

        Returns:
            TriggerTypes: The trigger type of the weapon.
        """
        return self._trigger_type

    @property
    def base_minimum_spread(self) -> float:
        """
        Returns the base minimum spread of the weapon.

        Returns:
            float: The base minimum spread of the weapon.
        """
        return self._base_minimum_spread

    @property
    def base_maximum_spread(self) -> float:
        """
        Returns the base maximum spread of the weapon.

        Returns:
            float: The base maximum spread of the weapon.
        """
        return self._base_maximum_spread

    @property
    def base_average_spread(self) -> float:
        """
        Returns the base average spread of the weapon.

        Returns:
            float: The base average spread of the weapon.
        """
        return (self._base_minimum_spread + self._base_maximum_spread) / 2

    @property
    def base_accuracy(self) -> AccuracyDescs:
        """
        Returns the base accuracy of the weapon.

        Returns:
            AccuracyDescs: The base accuracy of the weapon.
        """
        average_spread = self.base_average_spread

        match average_spread:
            case average_spread if average_spread > 12:
                return AccuracyDescs.VERY_LOW
            case average_spread if 6 < average_spread < 10:
                return AccuracyDescs.LOW
            case average_spread if 4 < average_spread < 6:
                return AccuracyDescs.MEDIUM
            case average_spread if 1 < average_spread < 3:
                return AccuracyDescs.HIGH
            case average_spread if 0 < average_spread < 1:
                return AccuracyDescs.VERY_HIGH
            case _:
                return AccuracyDescs.INVALID

    @property
    def base_fire_rate(self) -> float:
        """
        Returns the base fire rate of the weapon.

        Returns:
            float: The base fire rate of the weapon.
        """
        return self._base_fire_rate

    @property
    def base_noise_level(self) -> NoiseLevels:
        """
        Returns the base noise level of the weapon.

        Returns:
            NoiseLevels: The base noise level of the weapon.
        """
        return self._base_noise_level

    @property
    def projectile_type(self) -> ProjectileTypes:
        """
        Returns the projectile type of the weapon.

        Returns:
            ProjectileTypes: The projectile type of the weapon.
        """
        return self._projectile_type

    @property
    def base_damage_impact(self) -> float:
        """
        Returns the base impact damage of the weapon.

        Returns:
            float: The base impact damage of the weapon.
        """
        return self._base_damage_impact

    @property
    def base_damage_puncture(self) -> float:
        """
        Returns the base puncture damage of the weapon.

        Returns:
            float: The base puncture damage of the weapon.
        """
        return self._base_damage_puncture

    @property
    def base_damage_slash(self) -> float:
        """
        Returns the base slash damage of the weapon.

        Returns:
            float: The base slash damage of the weapon.
        """
        return self._base_damage_slash

    @property
    def base_damage_cold(self) -> float:
        """
        Returns the base cold damage of the weapon.

        Returns:
            float: The base cold damage of the weapon.
        """
        return self._base_damage_cold

    @property
    def base_damage_electricity(self) -> float:
        """
        Returns the base electricity damage of the weapon.

        Returns:
            float: The base electricity damage of the weapon.
        """
        return self._base_damage_electricity

    @property
    def base_damage_heat(self) -> float:
        """
        Returns the base heat damage of the weapon.

        Returns:
            float: The base heat damage of the weapon.
        """
        return self._base_damage_heat

    @property
    def base_damage_toxin(self) -> float:
        """
        Returns the base toxin damage of the weapon.

        Returns:
            float: The base toxin damage of the weapon.
        """
        return self._base_damage_toxin

    @property
    def base_damage_blast(self) -> float:
        """
        Returns the base blast damage of the weapon.

        Returns:
            float: The base blast damage of the weapon.
        """
        return self._base_damage_blast

    @property
    def base_damage_corrosive(self) -> float:
        """
        Returns the base corrosive damage of the weapon.

        Returns:
            float: The base corrosive damage of the weapon.
        """
        return self._base_damage_corrosive

    @property
    def base_damage_gas(self) -> float:
        """
        Returns the base gas damage of the weapon.

        Returns:
            float: The base gas damage of the weapon.
        """
        return self._base_damage_gas

    @property
    def base_damage_magnetic(self) -> float:
        """
        Returns the base magnetic damage of the weapon.

        Returns:
            float: The base magnetic damage of the weapon.
        """
        return self._base_damage_magnetic

    @property
    def base_damage_radiation(self) -> float:
        """
        Returns the base radiation damage of the weapon.

        Returns:
            float: The base radiation damage of the weapon.
        """
        return self._base_damage_radiation

    @property
    def base_damage_viral(self) -> float:
        """
        Returns the base viral damage of the weapon.

        Returns:
            float: The base viral damage of the weapon.
        """
        return self._base_damage_viral

    @property
    def base_damage_void(self) -> float:
        """
        Returns the base void damage of the weapon.

        Returns:
            float: The base void damage of the weapon.
        """
        return self._base_damage_void

    @property
    def base_damage_true(self) -> float:
        """
        Returns the base true damage of the weapon.

        Returns:
            float: The base true damage of the weapon.
        """
        return self._base_damage_true

    @property
    def total_physical_damage(self) -> float:
        """
        Returns the total physical damage of the weapon.

        Returns:
            float: The total physical damage of the weapon.
        """
        return self.base_damage_impact + self.base_damage_puncture + self.base_damage_slash

    @property
    def total_elemental_damage(self) -> float:
        """
        Returns the total elemental damage of the weapon.

        Returns:
            float: The total elemental damage of the weapon.
        """
        return (
            self.base_damage_cold
            + self.base_damage_electricity
            + self.base_damage_heat
            + self.base_damage_toxin
        )

    @property
    def total_compound_damage(self) -> float:
        """
        Returns the total compound damage of the weapon.

        Returns:
            float: The total compound damage of the weapon.
        """
        return (
            self.base_damage_blast
            + self.base_damage_corrosive
            + self.base_damage_gas
            + self.base_damage_magnetic
            + self.base_damage_radiation
            + self.base_damage_viral
        )

    @property
    def total_special_damage(self) -> float:
        """
        Returns the total special damage of the weapon.

        Returns:
            float: The total special damage of the weapon.
        """
        return self.base_damage_void + self.base_damage_true

    @property
    def total_damage(self) -> float:
        """
        Returns the total damage of the weapon.

        Returns:
            float: The total damage of the weapon.
        """
        return (
            self.total_physical_damage
            + self.total_elemental_damage
            + self.total_compound_damage
            + self.total_special_damage
        )

    @property
    def ammo_cost(self) -> float:
        """
        Returns the ammo cost of the weapon.

        Returns:
            float: The ammo cost of the weapon.
        """
        return self._base_ammo_cost

    @property
    def critical_chance(self) -> float:
        """
        Returns the critical chance of the weapon.

        Returns:
            float: The critical chance of the weapon.
        """
        return self._base_critical_chance

    @property
    def critical_multiplier(self) -> float:
        """
        Returns the critical multiplier of the weapon.

        Returns:
            float: The critical multiplier of the weapon.
        """
        return self._base_critical_multiplier

    @property
    def multishot(self) -> float:
        """
        Returns the multishot of the weapon.

        Returns:
            float: The multishot of the weapon.
        """
        return self._base_multishot

    @property
    def punch_through(self) -> float:
        """
        Returns the punch through of the weapon.

        Returns:
            float: The punch through of the weapon.
        """
        return self._base_punch_through

    @property
    def range(self) -> float:
        """
        Returns the range of the weapon.

        Returns:
            float: The range of the weapon.
        """
        return self._base_range

    @property
    def status_chance(self) -> float:
        """
        Returns the status chance of the weapon.

        Returns:
            float: The status chance of the weapon.
        """
        return self._base_status_chance

    @property
    def AoE_attack(self) -> AttackHandler | None:
        """
        Returns the AoE attack of the weapon.

        Returns:
            AttackHandler: The AoE attack of the weapon.
        """
        return self._AoE_attack
