from enum import Enum


class CompatibilityTags(Enum):
    """
    Enumeration of combatibility tags in the game.

    This includes item slots, mod types, etc.
    """

    # Related to Primary Slot Weapons
    PRIMARY = "Primary"
    RIFLE = "Rifle"
    SHOTGUN = "Shotgun"
    ASSAULT_RIFLE = "Assault Rifle"
    BOW = "Bow"
    SNIPER = "Sniper"
    LAUNCHER = "Launcher"
    CROSSBOW = "Crossbow"
    LONGBOW = "Longbow"
    SPEARGUN = "Speargun"

    # Related to Secondary Slot Weapons
    SECONDARY = "Secondary"
    PISTOL = "Pistol"
    DUAL_PISTOLS = "Dual Pistols"
    THROWN = "Thrown"
    TOME = "Tome"
    SHOTGUN_SIDEARM = "Shotgun Sidearm"

    # Related to Melee Slot Weapons
    MELEE = "Melee"
    ASSAULT_SAW = "Assault Saw"
    BLADE_AND_WHIP = "Blade and Whip"
    CLAWS = "Claws"
    DAGGER = "Dagger"
    DUAL_DAGGERS = "Dual Daggers"
    DUAL_NIKANAS = "Dual Nikanas"
    DUAL_SWORDS = "Dual Swords"
    FIST = "Fist"
    GLAIVE = "Glaive"
    GUNBLADE = "Gunblade"
    HAMMER = "Hammer"
    HEAVY_BLADE = "Heavy Blade"
    HEAVY_SCYTHE = "Heavy Scythe"
    MACHETE = "Machete"
    NIKANA = "Nikana"
    NUNCHAKU = "Nunchaku"
    POLEARM = "Polearm"
    RAPIER = "Rapier"
    SCYTHE = "Scythe"
    SPARRING = "Sparring"
    STAFF = "Staff"
    SWORD = "Sword"
    SWORD_AND_SHIELD = "Sword and Shield"
    TWOHANDED_NIKANA = "Two-Handed Nikana"
    TONFA = "Tonfa"
    WARFANS = "Warfans"
    WHIP = "Whip"

    # Related to Arch-weapons
    ARCHGUN = "Archgun"
    ARCHMELEE = "Archmelee"

    # Related to Warframes
    PARAZON = "Parazon"
    EXALTED_WEAPON = "Exalted Weapon"

    # Related to Companions
    COMPANION = "Companion"
    BEAST = "Beast"
    KUBROW = "Kubrow"
    KAVAT = "Kavat"
    ROBOTIC_COMPANION = "Robotic Companion"
    ROBOTIC_WEAPON = "Robotic Weapon"
    HOUND = "Hound"
    MOA = "Moa"
    SENTINEL = "Sentinel"

    # Secondary Compatibility Tags
    ASSAULT_AMMO = "Assault Ammo"
    SNIPER_AMMO = "Sniper Ammo"
    PROJECTILE = "Projectile"
    SINGLESHOT = "Single Shot"
    SECONDARYSHOTGUN = "Secondary Shotgun"
    DUAL_SWORDS_STANCE = "Dual Swords Stance"
    FIST_STANCE = "Fist Stance"
    SWORDS_STANCE = "Swords Stance"
    STAVES_STANCE = "Staves Stance"
