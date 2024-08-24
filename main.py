from websockets_api_example import run_text_to_image
from stories.DnD.the_wealthy_merhcant import character1
from check_character import GetCharInfo

from story import Story
from stories.DnD.the_wealthy_merhcant import narration

import random
import uuid

workflows = {'animated':'./workflows/test_workflow.json'}


def play_game():
    print(5*'=' + "Adventure v0.0.1" + 5*'=')
    print("Welcome to the DnD Adventrues Game.")
    playing = input("Whould you like to play? (y/n): ")

    while playing == 'y':
        char_info = GetCharInfo(character1)
        char_name, char_class = char_info.get_class_info()

        char_name_list = [char_name, 'LoserNPC']
        char_class_list = [char_class, 'LoserNPC']

        # Load the main character chosen by user
        main_char = None
        for idx in range(len(char_name_list)):
            select_char = input("Would you like to play as: {char_name}? (y/n)".format(char_name=char_name))
            if select_char == 'y':
                main_char = char_class_list[idx]
                break
        
        print("Great, you have chosen the mighty {name}!!".format(name=main_char.name))

        line_break(10) # prints line break

        print("Here is how your chracter looks:")

        # For now we load prompt with full str and see what happens
        prompt = main_char.__str__()

        # print(prompt)
        run_text_to_image(workflows['animated'], prompt)

        # Start story and progress it
        story = Story(narration) # Start a new story
        intro = story.get_section('introduction')
        print(intro)
        print("Let the adventure begin...")

        # Set the scene for the intro
        intro_prompt = "Paint this as a scene: {scene}".format(scene=intro)
        run_text_to_image(workflows['animated'], intro_prompt)


        keep_playing = 'y'
        while keep_playing == 'y':
            story.get_encounters()
            # print("Play another encounter? (y/n): ")
            user_res = input("Play another encounter? (y/n): ")
            keep_playing = user_res

        outro = story.get_section('epilogue')
        print(outro)

        break

def line_break(n):
    print(n*'+~~===~~+')

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