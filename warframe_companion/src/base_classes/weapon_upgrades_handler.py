from warframe_companion.src.base_classes.mod_slot import ModSlot
from warframe_companion.src.base_classes.arcane_slot import ArcaneSlot
from warframe_companion.src.enumerations.mod_slot_types import ModSlotTypes


class WeaponUpgradesHandler:
    def __init__(self) -> None:
        self._mod_slot_1: ModSlot = ModSlot()
        self._mod_slot_2: ModSlot = ModSlot()
        self._mod_slot_3: ModSlot = ModSlot()
        self._mod_slot_4: ModSlot = ModSlot()
        self._mod_slot_5: ModSlot = ModSlot()
        self._mod_slot_6: ModSlot = ModSlot()
        self._mod_slot_7: ModSlot = ModSlot()
        self._mod_slot_8: ModSlot = ModSlot()
        self._mod_slot_stance: ModSlot = ModSlot()
        self._mod_slot_exilus: ModSlot = ModSlot()
        self._arcane_slot: ArcaneSlot = ArcaneSlot()

        self._mod_slot_exilus.slot_type = ModSlotTypes.EXILUS
        self._mod_slot_stance.slot_type = ModSlotTypes.STANCE

    @property
    def mod_slot_1(self) -> ModSlot:
        return self._mod_slot_1

    @property
    def mod_slot_2(self) -> ModSlot:
        return self._mod_slot_2

    @property
    def mod_slot_3(self) -> ModSlot:
        return self._mod_slot_3

    @property
    def mod_slot_4(self) -> ModSlot:
        return self._mod_slot_4

    @property
    def mod_slot_5(self) -> ModSlot:
        return self._mod_slot_5

    @property
    def mod_slot_6(self) -> ModSlot:
        return self._mod_slot_6

    @property
    def mod_slot_7(self) -> ModSlot:
        return self._mod_slot_7

    @property
    def mod_slot_8(self) -> ModSlot:
        return self._mod_slot_8

    @property
    def mod_slot_stance(self) -> ModSlot:
        return self._mod_slot_stance

    @property
    def mod_slot_exilus(self) -> ModSlot:
        return self._mod_slot_exilus

    @property
    def arcane_slot(self) -> ArcaneSlot:
        return self._arcane_slot
