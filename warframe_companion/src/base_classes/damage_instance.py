from decimal import Decimal


class DamageInstance:
    def __init__(
        self,
        impact_damage: Decimal = Decimal(0.0),
        puncture_damage: Decimal = Decimal(0.0),
        slash_damage: Decimal = Decimal(0.0),
        cold_damage: Decimal = Decimal(0.0),
        electricity_damage: Decimal = Decimal(0.0),
        heat_damage: Decimal = Decimal(0.0),
        toxin_damage: Decimal = Decimal(0.0),
        blast_damage: Decimal = Decimal(0.0),
        corrosive_damage: Decimal = Decimal(0.0),
        gas_damage: Decimal = Decimal(0.0),
        magnetic_damage: Decimal = Decimal(0.0),
        radiation_damage: Decimal = Decimal(0.0),
        viral_damage: Decimal = Decimal(0.0),
        tau_damage: Decimal = Decimal(0.0),
        void_damage: Decimal = Decimal(0.0),
        true_damage: Decimal = Decimal(0.0),
    ) -> None:
        self.damage_impact: Decimal = impact_damage
        self.damage_puncture: Decimal = puncture_damage
        self.damage_slash: Decimal = slash_damage
        self.damage_cold: Decimal = cold_damage
        self.damage_electricity: Decimal = electricity_damage
        self.damage_heat: Decimal = heat_damage
        self.damage_toxin: Decimal = toxin_damage
        self.damage_blast: Decimal = blast_damage
        self.damage_corrosive: Decimal = corrosive_damage
        self.damage_gas: Decimal = gas_damage
        self.damage_magnetic: Decimal = magnetic_damage
        self.damage_radiation: Decimal = radiation_damage
        self.damage_viral: Decimal = viral_damage
        self.damage_tau: Decimal = tau_damage
        self.damage_void: Decimal = void_damage
        self.damage_true: Decimal = true_damage

    @property
    def total_physical_damage(self) -> Decimal:
        """
        Returns the total physical damage of the weapon.

        Returns:
            float: The total physical damage of the weapon.
        """
        return self.damage_impact + self.damage_puncture + self.damage_slash

    @property
    def total_elemental_damage(self) -> Decimal:
        """
        Returns the total elemental damage of the weapon.

        Returns:
            float: The total elemental damage of the weapon.
        """
        return (
            self.damage_cold
            + self.damage_electricity
            + self.damage_heat
            + self.damage_toxin
        )

    @property
    def total_compound_damage(self) -> Decimal:
        """
        Returns the total compound damage of the weapon.

        Returns:
            float: The total compound damage of the weapon.
        """
        return (
            self.damage_blast
            + self.damage_corrosive
            + self.damage_gas
            + self.damage_magnetic
            + self.damage_radiation
            + self.damage_viral
        )

    @property
    def total_special_damage(self) -> Decimal:
        """
        Returns the total special damage of the weapon.

        Returns:
            float: The total special damage of the weapon.
        """
        return self.damage_tau + self.damage_void + self.damage_true

    @property
    def total_damage(self) -> Decimal:
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

    def __str__(self) -> str:
        return f"I: {self.damage_impact.quantize(Decimal('1.00'))}, P: {self.damage_puncture.quantize(Decimal('1.00'))}, S: {self.damage_slash.quantize(Decimal('1.00'))}, Col: {self.damage_cold.quantize(Decimal('1.00'))}, E: {self.damage_electricity.quantize(Decimal('1.00'))}, H: {self.damage_heat.quantize(Decimal('1.00'))}, To: {self.damage_toxin.quantize(Decimal('1.00'))}, B: {self.damage_blast.quantize(Decimal('1.00'))}, Cor: {self.damage_corrosive.quantize(Decimal('1.00'))}, G: {self.damage_gas.quantize(Decimal('1.00'))}, M: {self.damage_magnetic.quantize(Decimal('1.00'))}, R: {self.damage_radiation.quantize(Decimal('1.00'))}, Vi: {self.damage_viral.quantize(Decimal('1.00'))}, Ta: {self.damage_tau.quantize(Decimal('1.00'))}, Vo: {self.damage_void.quantize(Decimal('1.00'))}, Tr: {self.damage_true.quantize(Decimal('1.00'))}"
