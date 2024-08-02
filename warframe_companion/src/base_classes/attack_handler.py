from __future__ import annotations
from decimal import Decimal
from warframe_companion.src.base_classes.damage_instance import DamageInstance
from warframe_companion.src.enumerations import (
    NoiseLevels,
    ProjectileTypes,
    TriggerTypes,
    AccuracyDescs,
)


class AttackHandler:
    def __init__(
        self,
        fire_rate: Decimal,
        noise_level: NoiseLevels,
        projectile_type: ProjectileTypes,
        critical_chance: Decimal,
        critical_multiplier: Decimal,
        multishot: Decimal,
        range: Decimal,
        status_chance: Decimal,
        damage: DamageInstance,
        #
        trigger_type: TriggerTypes = TriggerTypes.UNKNOWN,
        minimum_spread: Decimal = Decimal("0.0"),
        maximum_spread: Decimal = Decimal("0.0"),
        ammo_cost: Decimal = Decimal("1.0"),
        punch_through: Decimal = Decimal("0.0"),
        burst_count: int = 0,
        burst_delay: Decimal = Decimal("0.0"),
        AoE_attack: AttackHandler | None = None,
    ) -> None:
        self._trigger_type: TriggerTypes = trigger_type  #
        self._base_minimum_spread: Decimal = minimum_spread  #
        self._base_maximum_spread: Decimal = maximum_spread  #
        self._base_fire_rate: Decimal = fire_rate  #
        self._base_noise_level: NoiseLevels = noise_level  #
        self._projectile_type: ProjectileTypes = projectile_type  #
        self._base_damage: DamageInstance = damage
        self._base_ammo_cost: Decimal = ammo_cost  #
        self._base_critical_chance: Decimal = critical_chance  #
        self._base_critical_multiplier: Decimal = critical_multiplier  #
        self._base_multishot: Decimal = multishot  #
        # This might be moved to base Weapon Class. Not sure if this changes based on firing mode.
        self._base_punch_through: Decimal = punch_through  #
        self._base_range: Decimal = range  #
        self._base_status_chance: Decimal = status_chance  #
        self._burst_count: int = burst_count  #
        self._burst_delay: Decimal = burst_delay  #
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
    def base_minimum_spread(self) -> Decimal:
        """
        Returns the base minimum spread of the weapon.

        Returns:
            float: The base minimum spread of the weapon.
        """
        return self._base_minimum_spread

    @property
    def base_maximum_spread(self) -> Decimal:
        """
        Returns the base maximum spread of the weapon.

        Returns:
            float: The base maximum spread of the weapon.
        """
        return self._base_maximum_spread

    @property
    def base_average_spread(self) -> Decimal:
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
    def base_fire_rate(self) -> Decimal:
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
    def ammo_cost(self) -> Decimal:
        """
        Returns the ammo cost of the weapon.

        Returns:
            float: The ammo cost of the weapon.
        """
        return self._base_ammo_cost

    @property
    def critical_chance(self) -> Decimal:
        """
        Returns the critical chance of the weapon.

        Returns:
            float: The critical chance of the weapon.
        """
        return self._base_critical_chance

    @property
    def critical_multiplier(self) -> Decimal:
        """
        Returns the critical multiplier of the weapon.

        Returns:
            float: The critical multiplier of the weapon.
        """
        return self._base_critical_multiplier

    @property
    def multishot(self) -> Decimal:
        """
        Returns the multishot of the weapon.

        Returns:
            float: The multishot of the weapon.
        """
        return self._base_multishot

    @property
    def punch_through(self) -> Decimal:
        """
        Returns the punch through of the weapon.

        Returns:
            float: The punch through of the weapon.
        """
        return self._base_punch_through

    @property
    def range(self) -> Decimal:
        """
        Returns the range of the weapon.

        Returns:
            float: The range of the weapon.
        """
        return self._base_range

    @property
    def status_chance(self) -> Decimal:
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

    @property
    def base_damage(self) -> DamageInstance:
        """
        Returns the base damage of the weapon.

        Returns:
            DamageInstance: The base damage of the weapon.
        """
        return self._base_damage

    @property
    def burst_count(self) -> int:
        """
        Returns the burst count of the weapon.

        Returns:
            int: The burst count of the weapon.
        """
        return self._burst_count

    @property
    def burst_delay(self) -> Decimal:
        """
        Returns the burst delay of the weapon.

        Returns:
            Decimal: The burst delay of the weapon.
        """
        return self._burst_delay
