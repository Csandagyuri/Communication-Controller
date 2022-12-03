
from dataclasses import dataclass


@dataclass
class Connection:
    type: str
    address: str
    target_id: str
