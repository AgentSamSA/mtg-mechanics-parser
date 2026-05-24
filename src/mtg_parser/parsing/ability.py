"""mtg-mechanics-parser ability parsing module.

Takes oracle text and extracts activated, triggered, and static abilities."""


import re
from dataclasses import dataclass
from typing import Optional
from enum import Enum

class AbilityType(Enum):
    ACTIVATED = 'activated'
    TRIGGERED = 'triggered'
    STATIC = 'static'
    
TRIGGER_RE = re.compile(r'^(Whenever|When|At)\b', re.IGNORECASE)

@dataclass
class Ability:
    type: AbilityType
    raw: str
    
    condition: Optional[str] = None
    cost: Optional[str] = None
    effect: Optional[str] = None
    

def parse_ability(block: str) -> Ability:
    block = block.strip()
    
    # Activated
    if ':' in block:
        cost, effect = block.split(':', 1)
        return Ability(
            type=AbilityType.ACTIVATED,
            cost=cost.strip(),
            effect=effect.strip(),
            raw=block
        )
    
    # Triggered
    if TRIGGER_RE.match(block):
        if ',' in block:
            trigger, effect = block.split(',', 1)
        else:
            trigger, effect = block, ''
        
        return Ability(
            type=AbilityType.TRIGGERED,
            condition=trigger.strip(),
            effect=effect.strip(),
            raw=block
        )
    
    # Static
    return Ability(
        type=AbilityType.STATIC,
        raw=block
    )