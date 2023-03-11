import yaml


def get_yaml(yaml_file_name):
    try:
        with open(yaml_file_name, "r") as f:
            data = yaml.safe_load(f)
            return data
    except Exception as e:
        print(e)
