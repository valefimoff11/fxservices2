from enum import Enum
from dataclasses import dataclass

class Codes(Enum):
    ALERT = 1
    GO = 2

code = Codes.GO

print(Codes.GO == code)

@dataclass
class DC:
    attr1: str
    attr2: int

d = DC("sss", 1)
print(d.attr1)
