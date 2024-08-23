"""Progress through the story given user inputs"""

from stories.DnD.the_wealthy_merhcant import narration
import random

class Encounter:
    """Encounter class with title, purpose, narration, and choices"""
    def __init__(self, encounter):
        # self.encounter = encounter
        self.title = encounter['title']
        self.purpose = encounter['purpose']
        self.narration = encounter['narration']
        self.choices = encounter['choices']

        # Keep track of choice outcomes
        self.enc_state = ['?']*len(self.choices)
        self.opt_state = None
    
    def play_encounter(self):
        """Moves down the encounter tree"""
        print(self.title)
        print(self.narration)

        if isinstance(self.choices[0], dict):
            for idx, choice in enumerate(self.choices):
                print("{number}: {select} - {tag}".format(number=idx, select=choice['path'], tag=self.enc_state[idx]))

            user_idx = input("Select from above: ")
            user_enc_idx = int(user_idx)

            print("You have chosen path: {path}".format(path=self.choices[user_enc_idx]['path']))

            solution = self.random_outcome(self.choices[user_enc_idx]['options'])
        else:
            # print("{number}: {select} - {tag}".format(number=idx, select=choice, tag=self.enc_state[idx]))
            solution = self.random_outcome(self.choices)

        return solution
           
    
    def random_outcome(self, enum):
      
        self.opt_state = ['?']*len(enum)

        while "?" in self.opt_state:
            for idx, opt in enumerate(enum):
                print("{number}: {select} - {tag}".format(number=idx, select=opt, tag=self.opt_state[idx]))
            
            user_idx = input("Select from above: ")
            user_enc_idx = int(user_idx)

            luck = random.randint(0,20)
            if luck > 5:
                print("Success!!")
                self.opt_state[user_enc_idx] = "Pass"
                return enum[user_enc_idx]
            else:
                print("Attempt Failed...")
                self.opt_state[user_enc_idx] = "Failed"

        return "You have been killed!"




class Story:
    """Returns the Narration object, and related information"""
    def __init__(self, narration_module):
        self.narration_module = narration_module
        self.corpus = self.narration_module.story_narration
        self.end = False
        self.progress = ["New"]*len(self.corpus['encounters'])

        # Load as many Encounter class as there are possible encounters
        self.encounters = [Encounter(enc) for enc in self.corpus['encounters']]

    def get_encounters(self):
        print("Choose Next Encounter: ")
        for idx, enc in enumerate(self.encounters):
            print("{number}: {select} - {tag}".format(number=idx, select=enc.title, tag=self.progress[idx]))

        user_idx = input("Selection from above: ")
        user_enc_idx = int(user_idx)

        self.progress[user_enc_idx] = "Continue"

        outcome = self.encounters[user_enc_idx].play_encounter()

        print(outcome)
    
        
    def _print_options(list):
        """Prints options from a list"""
        for idx, choice in enumerate(list):
            if isinstance(choice, dict):
                print("{number}: {select}".format(number=idx, select=choice['path']))
            else:
                print("{number}: {select}".format(number=idx, select=choice))


    def get_headers(self):
        """Story main sections"""

        headers = list(self.corpus.keys())

        print(headers)
        # print(sub_headers)

    def get_section(self, key):
        return self.corpus[key]

    def get_structure(self):
        self._traverse_tree(self.corpus)

    def _traverse_tree(self, tree, parent_key=''):
        """Go down dictionary tree and get all keys"""
        if isinstance(tree, str):
            # Dont continue, ends at string node
            print("End of node.")
        elif isinstance(tree, dict):
            for key, value in tree.items():
                full_key = f"{parent_key}.{key}" if parent_key else key
                print(full_key)
                self._traverse_tree(value, parent_key=full_key)
        elif isinstance(tree, list):
            for idx, item in enumerate(tree):
                full_key = f"{parent_key}[{idx}]"
                try:
                    print(full_key)
                    print(item.keys()) # Assumes list has dict items
                    self._traverse_tree(item, parent_key=full_key)
                except:
                    # Some list end with string nodes
                    self._traverse_tree(item, parent_key=full_key)




if __name__ == '__main__':
    story = Story(narration) # Start a new story
    intro = story.get_section('introduction')
    print(intro)
    print("Let the adventure begin...")

    keep_playing = 'y'
    while keep_playing == 'y':
        story.get_encounters()
        # print("Play another encounter? (y/n): ")
        user_res = input("Play another encounter? (y/n): ")
        keep_playing = user_res

    outro = story.get_section('epilogue')
    print(outro)
    


