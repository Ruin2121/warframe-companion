from enum import Enum


class TriggerTypes(Enum):
    AUTO = "Auto"
    SEMI = "Semi"
    BURST = "Burst"
    AUTO_BURST = "Auto-Burst"
    SIM_BURST = "Simultaneous Burst"
    MAG_BURST = "Mag Burst"
    DUPLEX = "Duplex"
    ACTIVE = "Active"
    HELD = "Held"

    CHARGE = "Charge"
    CHARGE_FULL_INDEF = "Charge | Full Quickshot | Indefinite Hold"
    CHARGE_HALF_INDEF = "Charge | Half Quickshot | Indefinite Hold"
    CHARGE_NO_INDEF = "Charge | No Quickshot | Indefinite Hold"
    CHARGE_FULL_INSTANT = "Charge | Full Quickshot | Instant Auto-Release"
    CHARGE_HALF_INSTANT = "Charge | Half Quickshot | Instant Auto-Release"
    CHARGE_NO_INSTANT = "Charge | No Quickshot | Instant Auto-Release"
    CHARGE_NO_INSTANT_AUTO = (
        "Charge | No Quickshot | Instant Auto-Release and Auto Trigger"
    )
    CHARGE_AUTO_INSTANT = "Charge | Autocharge | Instant Auto-Release"
    CHARGE_AUTO_INDEF = "Charge | Autocharge | Indefinite Hold"
    CHARGE_AUTOQS_INSTANT = "Charge | Autocharged Quickshot | Instant Auto-Release"
    CHARGE_FULL_DELAYED = "Charge | Full Quickshot | Delayed Auto-Release"
    CHARGE_NO_DELAYED = "Charge | No Quickshot | Delayed Auto-Release"

    UNKNOWN = "Unknown"
