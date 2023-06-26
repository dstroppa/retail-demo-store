#!/usr/local/bin/python3

import yaml

# Parse yaml file
def parse_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)
    
# for each item in the yaml file, print out the name and the value
def print_yaml(file_path):
    data = parse_yaml(file_path)
    for item in data:
        print(item["name"])

if __name__ == "__main__":
    print_yaml("./data/categories.yaml")

  