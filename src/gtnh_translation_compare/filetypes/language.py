from enum import Enum


class Language(Enum):
    en_US = "en_US"
    zh_CN = "zh_CN"
    ja_JP = "ja_JP"

    @classmethod
    def from_str(cls, s: str) -> "Language":
        return cls(s)
