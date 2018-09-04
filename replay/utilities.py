from enum import IntEnum


class Character(IntEnum):
    INVALID = -1
    ERROR_1 = 0
    ERROR_2 = 1
    ZETTERBURN = 2
    ORCANE = 3
    WRASTOR = 4
    KRAGG = 5
    FORSBURN = 6
    MAYPUL = 7
    ABSA = 8
    ETALUS = 9
    ORI = 10
    RANNO = 11
    CLAIREN = 12


class Action(IntEnum):
    INVALID = -1
    JUMP_PRESS = 0
    JUMP_RELEASE = 1
    ATTACK_PRESS = 2
    ATTACK_RELEASE = 3
    SPECIAL_PRESS = 4
    SPECIAL_RELEASE = 5
    STRONG_PRESS = 6
    STRONG_RELEASE = 7
    STRONG_LEFT_PRESS = 8
    STRONG_LEFT_RELEASE = 9
    STRONG_RIGHT_PRESS = 10
    STRONG_RIGHT_RELEASE = 11
    STRONG_UP_PRESS = 12
    STRONG_UP_RELEASE = 13
    STRONG_DOWN_PRESS = 14
    STRONG_DOWN_RELEASE = 15
    DODGE_PRESS = 16
    DODGE_RELEASE = 17
    UP_PRESS = 18
    UP_RELEASE = 19
    UP_TAP = 20
    DOWN_PRESS = 21
    DOWN_RELEASE = 22
    DOWN_TAP = 23
    LEFT_PRESS = 24
    LEFT_RELEASE = 25
    LEFT_TAP = 26
    RIGHT_PRESS = 27
    RIGHT_RELEASE = 28
    RIGHT_TAP = 29
    ANGLES_ENABLED = 30
    ANGLES_DISABLED = 31


class Stage(IntEnum):
    INVALID = -1
    MENU = 0
    TREETOP_LODGE = 1
    FIRE_CAPITOL = 2
    AIR_ARMADA = 3
    ROCK_WALL = 4
    MERCHANT_PORT = 5
    CRASH_GAME = 6
    BLAZING_HIDEOUT = 7
    TOWER_HEAVEN = 8
    TEMPEST_PEAK = 9
    FROZEN_FORTRESS = 10
    AETHERIAL_GATES = 11
    ENDLESS_ABYSS = 12
    UNAVAILABLE = 13
    CEO_RING = 14
    SPIRIT_TREE = 15
    STAGE_NAME = 16
    NEO_FIRE_CAPITAL = 17
    SWAMPY_ESTUARY = 18


class StageType(IntEnum):
    INVALID = -1
    BASIC = 0
    AETHER = 1
