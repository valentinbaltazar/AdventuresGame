class Adventure:
    def __init__(self, title, intro, encounters, epilogue):
        self.title = title
        self.intro = intro
        self.encounters = encounters  # List of Encounter objects
        self.epilogue = epilogue

class Encounter:
    def __init__(self, name, purpose, description, choices):
        self.name = name
        self.purpose = purpose
        self.description = description
        self.choices = choices  # List of Choice objects

class Choice:
    def __init__(self, description, skill_check, outcome):
        self.description = description
        self.skill_check = skill_check  # Skill and type of check required
        self.outcome = outcome  # Possible outcomes

class Character:
    def __init__(self, name, stats, abilities):
        self.name = name
        self.stats = stats  # Dictionary of character stats
        self.abilities = abilities  # List of abilities

class Merchant:
    def __init__(self, name, cargo, payment_offer):
        self.name = name
        self.cargo = cargo  # What the merchant is transporting
        self.payment_offer = payment_offer  # Payment details for players

# Sample Data Structure
merchant = Merchant(
    name="Hudson McBay",
    cargo="20 valuable stones",
    payment_offer="10% of profits from selling the stones"
)

encounters = [
    Encounter(
        name="The Fork in the Road",
        purpose="Introduce choices & consequences, skill checks, and non-combat scenarios",
        description="A fork in the road leading to either a bandit-guarded high road or a possibly flooded low road.",
        choices=[
            Choice(description="Take the high road", skill_check="Stealth or Nature", outcome="Avoid or confront bandits"),
            Choice(description="Take the low road", skill_check="Athletics, Acrobatics, or Survival", outcome="Cross the flooded area")
        ]
    ),
    Encounter(
        name="The Negotiation",
        purpose="Introduce role-playing and social interaction",
        description="Assist Hudson McBay in negotiating a better price for the stones.",
        choices=[
            Choice(description="Use Insight", skill_check="Insight", outcome="Understand Pat's motivations"),
            Choice(description="Use Persuasion", skill_check="Persuasion", outcome="Negotiate better price"),
            Choice(description="Use Intimidation", skill_check="Intimidation", outcome="Risk backfiring")
        ]
    ),
    Encounter(
        name="Bar-Room Brawl",
        purpose="Introduce combat",
        description="Fight off drunk patrons attempting to rob the group after negotiation.",
        choices=[
            Choice(description="Fight", skill_check="Combat", outcome="Defeat the patrons"),
            Choice(description="Non-lethal action", skill_check="Roleplay", outcome="Avoid angering town guards")
        ]
    )
]

epilogue = "Hudson McBay pays the players 10% of the profits, thanks them, and leaves to continue his business."

adventure = Adventure(
    title="The Wealthy Merchant",
    intro="A half-hour adventure for 0th level characters inspired by /u/pliantreality of Reddit.",
    encounters=encounters,
    epilogue=epilogue
)
