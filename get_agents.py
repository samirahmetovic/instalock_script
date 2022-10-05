import os

def get_agent_list():
    current_path = os.getcwd() + "\\\\assets"
    agent_list = os.listdir(current_path)

    agent_list = list(map(lambda name: name[:-4], agent_list))
    return agent_list