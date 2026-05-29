"""mtg-mechanics-parser mechanics and type definitions.

Contains various game mechanic and typing definitions."""


from mtg_parser.utils.normalizer import normalize_keyword

RAW_ABILITY_WORDS = {
    'Adamant',
    'Addendum',
    'Alliance',
    'Battalion',
    'Bloodrush',
    'Celebration',
    'Channel',
    'Chroma',
    'Cohort',
    'Constellation',
    'Converge',
    'Corrupted',
    "Council's dilemma",
    'Coven',
    'Delirium',
    'Descend 4',
    'Descend 8',
    'Domain',
    'Eerie',
    'Eminence',
    'Enrage',
    'Fateful hour',
    'Fathomless Descent',
    'Ferocious',
    'Formidable',
    'Grandeur',
    'Hellbent',
    'Heroic',
    'Imprint',
    'Inspired',
    'Join forces',
    'Kinship',
    'Landfall',
    'Lieutenant',
    'Magecraft',
    'Metalcraft',
    'Morbid',
    'Pack tactics',
    'Parade!',
    'Paradox',
    'Parley',
    'Radiance',
    'Raid',
    'Rally',
    'Revolt',
    'Spell mastery',
    'Strive',
    'Sweep',
    'Tempting offer',
    'Threshold',
    'Underdog',
    'Undergrowth',
    'Valiant',
    'Will of the council',
    'Will of the Planeswalkers',
}

ABILITY_WORDS = {normalize_keyword(word) for word in RAW_ABILITY_WORDS}

RAW_CREATURE_TYPES = "Advisor, Aetherborn, Alien, Ally, Angel, Antelope, Ape, Archer, Archon, Armadillo, Army, Artificer, Assassin, Assembly-Worker, Astartes, Atog, Aurochs, Avatar, Azra, Badger, Balloon, Barbarian, Bard, Basilisk, Bat, Bear, Beast, Beaver, Beeble, Beholder, Berserker, Bird, Bison, Blinkmoth, Boar, Bringer, Brushwagg, Camarid, Camel, Capybara, Caribou, Carrier, Cat, Centaur, Child, Chimera, Citizen, Cleric, Clown, Cockatrice, Construct, Coward, Coyote, Crab, Crocodile, C'tan, Custodes, Cyberman, Cyclops, Dalek, Dauthi, Demigod, Demon, Deserter, Detective, Devil, Dinosaur, Djinn, Doctor, Dog, Dragon, Drake, Dreadnought, Drix, Drone, Druid, Dryad, Dwarf, Echidna, Efreet, Egg, Elder, Eldrazi, Elemental, Elephant, Elf, Elk, Employee, Eye, Faerie, Ferret, Fish, Flagbearer, Fox, Fractal, Frog, Fungus, Gamer, Gargoyle, Germ, Giant, Gith, Glimmer, Gnoll, Gnome, Goat, Goblin, God, Golem, Gorgon, Graveborn, Gremlin, Griffin, Guest, Hag, Halfling, Hamster, Harpy, Hedgehog, Hellion, Hero, Hippo, Hippogriff, Homarid, Homunculus, Horror, Horse, Human, Hydra, Hyena, Illusion, Imp, Incarnation, Inkling, Inquisitor, Insect, Jackal, Jellyfish, Juggernaut, Kangaroo, Kavu, Kirin, Kithkin, Knight, Kobold, Kor, Kraken, Llama, Lamia, Lammasu, Leech, Lemur, Leviathan, Lhurgoyf, Licid, Lizard, Lobster, Manticore, Masticore, Mercenary, Merfolk, Metathran, Minion, Minotaur, Mite, Mole, Monger, Mongoose, Monk, Monkey, Moogle, Moonfolk, Mount, Mouse, Mutant, Myr, Mystic, Nautilus, Necron, Nephilim, Nightmare, Nightstalker, Ninja, Noble, Noggle, Nomad, Nymph, Octopus, Ogre, Ooze, Orb, Orc, Orgg, Otter, Ouphe, Ox, Oyster, Pangolin, Peasant, Pegasus, Pentavite, Performer, Pest, Phelddagrif, Phoenix, Phyrexian, Pilot, Pincher, Pirate, Plant, Platypus, Porcupine, Possum, Praetor, Primarch, Prism, Processor, Qu, Rabbit, Raccoon, Ranger, Rat, Rebel, Reflection, Rhino, Rigger, Robot, Rogue, Sable, Salamander, Samurai, Sand, Saproling, Satyr, Scarecrow, Scientist, Scion, Scorpion, Scout, Sculpture, Seal, Serf, Serpent, Servo, Shade, Shaman, Shapeshifter, Shark, Sheep, Siren, Skeleton, Skunk, Slith, Sliver, Sloth, Slug, Snail, Snake, Soldier, Soltari, Spawn, Specter, Spellshaper, Sphinx, Spider, Spike, Spirit, Splinter, Sponge, Squid, Squirrel, Starfish, Surrakar, Survivor, Symbiote, Synth, Tentacle, Tetravite, Thalakos, Thopter, Thrull, Tiefling, Time Lord, Toy, Treefolk, Trilobite, Triskelavite, Troll, Turtle, Tyranid, Unicorn, Vampire, Varmint, Vedalken, Villain, Volver, Wall, Walrus, Warlock, Warrior, Weasel, Weird, Werewolf, Whale, Wizard, Wolf, Wolverine, Wombat, Worm, Wraith, Wurm, Yeti, Zombie, Zubera"

CREATURE_TYPES = set(x.strip().lower() for x in RAW_CREATURE_TYPES.split(','))

EVENT_VALUE = {
    'draw': 1,
    'put_into_hand': 1,
    'return_to_hand': 1,
    'discard': -1
}