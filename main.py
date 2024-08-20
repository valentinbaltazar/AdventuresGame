from websockets_api_example import run_application
import uuid

workflows = {'animated':'./workflows/test_workflow.json'}


def play_game():
    story = StoryProgress()
    hero_player = Hero(hair='(long dark blue hair)', body='', face='', weapon='longsword', armor='gold armor')
    pipeline = LoadPipeline('./workflows') # Load the pipeline for animated images

    print(5*'=' + "Adventure v0.0.1" + 5*'=')
    print("Welcome to the adventure game. In this adventure you will set the scene and make a hero!")

    # Testing workflow with user inputs and class
    user_prompt = input("What setting is you hero found? (ex: in the arid desert): ")

    # Modify hero based on user input
    hero_player.hair = input("Describe your heros hair: (ex: long dark blue hair): ")
    hero_player.weapon = input("Describe your heros weapon: (ex: longsword): ")
    hero_player.armor = input("Describe your heros armor: (ex: gold armor): ")

    hero_desc = hero_player.hero_prompt()
    file_path = pipeline.simple_match('animated')

    # Prompt will merge user input and Hero object details
    prompt = "{user_prompt} landscape, {hero_desc}".format(user_prompt=user_prompt, hero_desc=hero_desc)
    print(prompt)
    run_application(file_path, prompt)

class StoryProgress:
    """Tracks the story and player progress
    TODO: Make or load a story"""
    
    def __init__(self, story_progress='', step='Start'):
        self.story_progress = story_progress
        self.step = step # start or end of story

    def progress_story(self, text):
        self.story_progress += '\n' + text # add the next step in the story, and save as progress
        return self.story_progress




class LoadPipeline:
    """Loads a pipeline matching a criteria
    TODO: Make this dynamic, chooses workflow on the fly"""
    def __init__(self, directory):
        self.current_worflow = None
        self.current_directory = directory

    def simple_match(self, key):
        """Match and return a workflow based on key input"""
        return workflows[key]

class Hero:
    """Main hero class, story protagonist (player)"""
    def __init__(self, hair='', body='', face='', weapon='', armor=''):
        self.hair = hair
        self.body = body
        self.face = face
        self.weapon = weapon
        self.armor = armor

    def hero_prompt(self):
        """Combines user details, to make hero prompt
        TODO: output only the requested description, person, gear, tools etc"""
        description = "A male hero with {hair}, {body}, {face}, {weapon}, {armor}".format(hair=self.hair,
                                                                      body=self.body,
                                                                      face=self.face,
                                                                      weapon=self.weapon,
                                                                      armor=self.armor)
        return description



if __name__ == '__main__':
    play_game()