from websockets_api_example import run_application
import uuid

def run_user_prompt(file_path):
    # Testing workflow with user inputs
    user_prompt = input("Input a promt to generate a picture:")

    run_application(file_path, user_prompt)


if __name__ == '__main__':
    file_path = './workflows/test_workflow.json'

    run_user_prompt(file_path)