class BanditScout:
    def __init__(self):
        self.name = "Bandit Scout"
        self.size = "Medium"
        self.type = "Human"
        self.alignment = "Lawful Evil"
        self.armor_class = 12  # Leather Armor
        self.hit_points = 6  # (1d10 + 1)
        self.speed = 30  # in feet
        self.stats = {
            "STR": 8,   # Strength
            "DEX": 8,   # Dexterity
            "CON": 12,  # Constitution
            "INT": 8,   # Intelligence
            "WIS": 4,   # Wisdom
            "CHA": 8    # Charisma
        }
        self.condition_immunities = ["sobriety"]  # Immune to the condition of being sober
        self.senses = {
            "sight": 60,  # Darkvision range in feet
            "passive_perception": 7
        }
        self.languages = ["Common", "Thieves Cant"]
        self.challenge_rating = 0  # 0 XP

    def scout_ability(self):
        """Special ability: Scout"""
        return "If woken and attacked, the scout will call for reinforcements while running away."

    def drunken_dash(self):
        """Action: Drunken Dash"""
        return "Movement: When taking the dash action, succeed on a DC15 dexterity saving throw or fall prone."

    def __str__(self):
        return (f"{self.name} (Size: {self.size}, Type: {self.type}, Alignment: {self.alignment})\n"
                f"AC: {self.armor_class}, HP: {self.hit_points}, Speed: {self.speed}ft\n"
                f"Stats: {self.stats}\n"
                f"Condition Immunities: {self.condition_immunities}\n"
                f"Senses: {self.senses}\n"
                f"Languages: {', '.join(self.languages)}\n"
                f"Challenge Rating: {self.challenge_rating}\n"
                f"Special Ability: {self.scout_ability()}\n"
                f"Action: {self.drunken_dash()}")

# Example of creating a Bandit Scout object
# bandit_scout = BanditScout()

# To print the bandit scout details:
# print(bandit_scout)
