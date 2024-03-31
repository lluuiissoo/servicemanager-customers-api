import os
import json
from app.version.git_client import GitClient
from app.version.git_data_model import GitData

def read_json_file(file_path):
    """
    Read JSON file if it exists.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    dict: The parsed JSON data if the file exists, otherwise returns None.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError as e:
                msg = f"Error decoding JSON: {e}"
                print(msg) #TODO: Switch to logging
                raise Exception(msg)
    else:
        msg = f"File '{file_path}' does not exist."
        print(msg) #TODO: Switch to logging
        return None


git_data_file_path = './git_data.json' #TODO: Send to config file

def get_git_data() -> GitData:

    json_file_data = read_json_file(git_data_file_path)
    if json_file_data:
        print("JSON data successfully loaded from file:")
        print(json_file_data)
        git_data: GitData = GitData(**json_file_data)
        return git_data
    else:
        print("Failed to load JSON data from file. Attempting to load from local env.")
        git_client = GitClient()
        git_data: GitData = git_client.get_git_info()
        print (git_data)
        return git_data
