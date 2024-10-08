#This is an example that uses the websockets api to know when a prompt execution is done
#Once the prompt execution is done it downloads the images using the /history endpoint

import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import json
import urllib.request
import urllib.parse

import random

from PIL import Image
import io
import os

# Set server address (local host) and client id
server_address = "127.0.0.1:8188"
client_id = str(uuid.uuid4())

def queue_prompt(prompt):
    p = {"prompt": prompt, "client_id": client_id}
    data = json.dumps(p).encode('utf-8')
    req =  urllib.request.Request("http://{}/prompt".format(server_address), data=data)
    return json.loads(urllib.request.urlopen(req).read())

def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
        return response.read()

def get_history(prompt_id):
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        return json.loads(response.read())

def get_images(ws, prompt):
    prompt_id = queue_prompt(prompt)['prompt_id']
    output_images = {}
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                data = message['data']
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    break #Execution is done
        else:
            continue #previews are binary data

    history = get_history(prompt_id)[prompt_id]
    for o in history['outputs']:
        for node_id in history['outputs']:
            node_output = history['outputs'][node_id]
            if 'images' in node_output:
                images_output = []
                for image in node_output['images']:
                    image_data = get_image(image['filename'], image['subfolder'], image['type'])
                    images_output.append(image_data)
            output_images[node_id] = images_output

    return output_images

def load_workflow(file_path):
    """Load workflow from JSON and return as prompt input"""

    with open(file_path, 'r') as file:
        json_string = file.read()

    return json_string

def run_workflow(prompt_text, user_prompt):
    """Run workflow and return images object"""

    prompt = json.loads(prompt_text)

    # Changes the Seed of the KSampler node to avoid stalling
    prompt["3"]["inputs"]["seed"] = random.randint(1,999)
    
    # Change prompt to that of the user
    prompt["6"]["inputs"]["text"] = user_prompt

    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_images(ws, prompt)

    return images

def save_output(images):
    """Saves output image in specefied directory"""
    
    save_directory = './images/'  # Change this to your desired directory

    # Ensure the directory exists
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for node_id in images:
        for idx, image_data in enumerate(images[node_id]):
            # Create a file path for each image
            file_path = os.path.join(save_directory, f'image_{node_id}_{idx}.png')  # You can change the file extension if needed
            
            # Open the image from byte data
            image = Image.open(io.BytesIO(image_data))
            image.show()
            
            # Save the image to the specified file path
            image.save(file_path)
            print(f'Saved image {file_path}')


def run_text_to_image(file_path, user_prompt):
    """Run worflow, and save output image to file path"""
    prompt_text = load_workflow(file_path)
    images = run_workflow(prompt_text, user_prompt)
    save_output(images)


if __name__ == '__main__':
    file_path = './workflows/test_workflow.json'

    user_prompt = "beautiful scenery nature glass bottle landscape, purple galaxy bottle"
    run_text_to_image(file_path, user_prompt)