"""mtg-mechanics-parser ability parsing module.

Ability class defines ability structures and definitions.
Takes in oracle text and extracts activated, triggered, and static abilities."""


from dataclasses import dataclass
from typing import Optional
from enum import Enum

from mtg_parser.constants.searches import TRIGGER_RE

class AbilityType(Enum):
    ACTIVATED = 'activated'
    TRIGGERED = 'triggered'
    STATIC = 'static'

@dataclass
class Ability:
    type: AbilityType
    raw: str
    effect: str = ''
    
    condition: Optional[str] = None
    cost: Optional[str] = None
    
    
    def normalized_effect(self) -> str:
        return self.effect.lower()
    
    def normalized_condition(self) -> str:
        return (self.condition or '').lower()
    
    def normalized_cost(self) -> str:
        return (self.cost or '').lower()
    

def parse_ability(block: str) -> Ability:
    block = block.strip()

    # Strip ability word prefix (e.g. "Valiant — ", "Landfall — ")
    if ' — ' in block:
        _, block = block.split(' — ', 1)
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
        parts = block.split(',', 1)
        
        trigger = parts[0].strip()
        effect = parts[1].strip() if len(parts) > 1 else ''
        
        return Ability(
            type=AbilityType.TRIGGERED,
            condition=trigger,
            effect=effect,
            raw=block
        )
    
    # Static
    return Ability(
        type=AbilityType.STATIC,
        effect=block,
        raw=block
    )