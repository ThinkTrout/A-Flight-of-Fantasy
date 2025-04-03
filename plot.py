from colors import *

chapters = {
    1: {
        "text": f'Welcome to {PURPLE}A Flight of Fantasy{DEFAULT}, a text-based RPG game created by {LIGHT_GREEN}ThinkTrout{DEFAULT}. Click on the arrow and press [ENTER] to continue.',
        "type": "continue",
    },

    2: {
        "text": f'You are {BLUE}Florian{DEFAULT}, a traveling merchant with a portable shop on his back.',
        "type": "continue",
    },

    3: {
        "text": f"Throughout the game, you will be in control of Florian's actions, choosing meaningful {YELLOW}dialogue{DEFAULT} options, balancing and managing {LIGHT_GREEN}resources{DEFAULT}, and even making the most basic {RED}survival{DEFAULT} decisions.",
        "type": "continue",
    },

    4: {
        "text": f'Are you ready to begin your {PURPLE}Flight of Fantasy?{DEFAULT}',
        "type": "choice",
        "options": [
            "[Y] - Yes",
            "[N] - No"
        ],
        "inputs": {
            "y": 4.1,  
            "n": 4.2   
        }
    },

    4.1: {
        "text": f"{ITALIC}You begin your adventure.{DEFAULT}",
        "type": "continue"
    },

    4.2: {
        "text": f"{ITALIC}*Some mysterious higher being changes your mind and you begin the adventure anyways.*{DEFAULT}",
        "type": "continue",
    },

    5: {
        "type": "continue",
        "text": f"{ITALIC}You awake on the outskirts of a village.{DEFAULT}"
    }
}
