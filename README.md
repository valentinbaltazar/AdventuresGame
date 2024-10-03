# DnD Adventure Game

This project is a learning experience  to showcase OOP in python, along with the use of machine learning models to generate both text and artwork in a first person adventure game.

The input is a simple PDF of an adventure from a DnD playthrough. The PDF is parsed by ChatGPT into subsections and then that is used as input to the game.

The game uses the parsed data as input to create the characters, gameplay, options and artwork. The artwork uses custom workflows to call a StableDiffusion type model to generate fun and interesting artwork both based on the users input and choices in the game and the information from the adventure. These models are all **text to image** based, but I am also working on implementing a text to speech to narrate the game as well.

TO DO:
- Frontend interface


