from pygcode.dialects.utils import WordType
from .linuxcnc import CLEAN_FLOAT, REGEX_FLOAT, WORD_MAP

WORD_MAP = WORD_MAP.copy()

WORD_MAP["E"] = WordType(
    cls=float,
    value_regex=REGEX_FLOAT,
    description="The amount to extrude between the starting point and ending point",
    clean_value=CLEAN_FLOAT,
)
