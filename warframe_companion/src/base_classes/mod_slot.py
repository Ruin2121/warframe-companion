from warframe_companion.src.base_classes.mod import Mod
from warframe_companion.src.enumerations.polarities import Polarities
from warframe_companion.src.enumerations.mod_slot_types import ModSlotTypes


class ModSlot:
    def __init__(self) -> None:
        self.mod: Mod | None = None
        self.slot_polarity: Polarities | None = None
        self.slot_type: ModSlotTypes = ModSlotTypes.NORMAL
