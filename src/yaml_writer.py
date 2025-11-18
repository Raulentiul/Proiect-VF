# src/yaml_writer.py
import yaml
from pathlib import Path

def save_yaml(tools_list, path="output/tools.yml"):
    Path("output").mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump({"tools": tools_list}, f, sort_keys=False, allow_unicode=True)
