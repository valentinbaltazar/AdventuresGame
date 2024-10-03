story_narration = {
    "introduction": """
    You are amateur adventurers that have all been hired by a town merchant, Hudson McBay. 
    He is transporting a sack of 20 valuable stones from his town of Firebug to Fort Muck, 
    a local trading post. The trail between the two passes through a valley in the wilderness, 
    and he is afraid of being robbed by bandits. In exchange for protecting him, 
    he has offered you each 10% of his profits from selling the stones.
    """,
    
    "encounters": [
        {
            "title": "The Fork in the Road",
            "purpose": "To introduce the players to choices & consequences, skill checks, and non-combat ways of dealing with situations.",
            "narration": """
            While traveling along to Fort Muck, you reach a fork in the road. 
            You have the options of taking the high road to the left, 
            which is guarded by bandits, or taking the low road to the right, 
            which may be flooded because of recent heavy rains.
            """,
            "choices": [
                {
                    "path": "High Road",
                    "options": [
                        "Sneak past the bandit sentry (Stealth skill check)",
                        "Escape into the bushes (Nature skill check)",
                        "Find another way to deal with the situation"
                    ]
                },
                {
                    "path": "Low Road",
                    "options": [
                        "Ford the creek (Athletics skill check)",
                        "Skip across stones in the creek (Acrobatics skill check)",
                        "Look for an easier crossing (Survival skill check)",
                        "Invent some other way to cross"
                    ]
                }
            ]
        },
        {
            "title": "The Negotiation",
            "purpose": "To introduce the players to role-playing and social interaction.",
            "narration": """
            Upon reaching Fort Muck, Hudson McBay takes the players to a seedy bar 
            where the trade is supposed to take place. The players have a chance 
            to look around and inspect the other patrons for signs of danger. 
            After a bit, Hudson McBay calls the players over – he is having trouble 
            negotiating with the buyer, a strangely dressed man nicknamed Pat Stonepaw. 
            Hudson wants a better price than 10 gold per stone and would like their help. 
            A better price means more pay for the players.
            """,
            "choices": [
                "Insight checks to learn what Pat wants (respect)",
                "History/Religion to learn about his culture from his robes",
                "Persuasion to kindly ask for a better price",
                "Intimidation to force one (backfires on low roll)"
            ]
        },
        {
            "title": "Bar-Room Brawl",
            "purpose": "To introduce the players to combat.",
            "narration": """
            After the negotiation is complete and money is exchanged, 
            a group of four drunk bar patrons stand up and approach. 
            They saw the money and try to threaten everyone into handing it over, 
            and will initiate combat using bar stools as clubs.
            """,
            "choices": [
                "Getting lowered to 0HP will knock the players out.",
                "Wayward fireballs will cause minor fires in the bar.",
                "Murdering them will anger the town guards."
            ]
        }
    ],
    
    "epilogue": """
    Hudson McBay pays the players their wages. Each player gets 10%, 
    (which is the same as the negotiated value of two stones). 
    He thanks them for their services and then goes on his way with other business in the town.
    """
}
