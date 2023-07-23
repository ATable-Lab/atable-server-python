import yaml
import re

def get_yaml(yaml_file_name):
    try:
        with open(yaml_file_name, "r") as f:
            data = yaml.safe_load(f)
            return data
    except Exception as e:
        print(e)


def get_collection_name_from_class_name(class_name):
    if class_name.endswith("Controller"):
        # Get the substring without the word "Controller"
        name_without_controller = class_name[:-10]
        # Convert to snake_case
        snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name_without_controller).lower()
    else:
        raise Exception("Invalid Controller class name")
    return snake_case_name
