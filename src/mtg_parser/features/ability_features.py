"""mtg-mechanics-parser ability feature definition.

Defines our ability features based on our scoring criteria.
Contains accumulator function to sum our point totals for scoring."""


from dataclasses import dataclass
from typing import List, Dict, Callable, Optional

from mtg_parser.constants.features import FEATURES

@dataclass
class AbilityFeatures:
    baseline_score: int = 0
    
    # Special features
    has_search: int = 0
    plus1_counter: int = 0
    
    # Triggered abilities
    enters_trigger: int = 0
    dies_trigger: int = 0
    repeatable_trigger: int = 0
    
    # Token features
    token_pt_total: int = 0
    
    # Activated abilities
    activated_limiter: int = 0
    activated_no_limiter: int = 0
    
    # Global effects
    has_global: int = 0
    
    # Card advantage
    card_advantage: int = 0
    
    # Recursion
    has_recursion_battlefield: int = 0
    
    # Impulse draw
    has_exile_access: int = 0
    
    # Removal
    has_destroy: int = 0
    has_mass_destroy: int = 0
    has_bounce: int = 0
    has_deck_stack: int = 0
    has_minus_X: int = 0
    
    # Mana production
    mana_produced: int = 0
    mana_reduction: int = 0
    
    # Damage
    has_direct_damage: int = 0
    
    def add(self, updates: dict):
        for k, v in updates.items():
            setattr(self, k, getattr(self, k) + v)
    
    def to_vector(self) -> List[int]:
        return [
            self.baseline_score,
            self.has_search,
            self.plus1_counter,
            self.enters_trigger,
            self.dies_trigger,
            self.repeatable_trigger,
            self.token_pt_total,
            self.activated_limiter,
            self.activated_no_limiter,
            self.has_global,
            self.card_advantage,
            self.has_recursion_battlefield,
            self.has_exile_access,
            self.has_destroy,
            self.has_mass_destroy,
            self.has_bounce,
            self.has_deck_stack,
            self.has_minus_X,
            self.mana_produced,
            self.mana_reduction,
            self.has_direct_damage,
        ]