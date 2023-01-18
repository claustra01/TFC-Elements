import json
import os

# read json
def read_json (file_path) -> dict:
    f = open(file_path, "r")
    dict = json.load(f)
    f.close
    return dict


# write json
def write_json(dict, file_path):
    f = open(file_path, "w")
    json.dump(dict, f, indent=2, ensure_ascii=False)
    f.close()
    
    
# create directory
def create_dir(dir_path):
    os.makedirs(dir_path, exist_ok=True)


# create nested dict
def create_nested_dict(list, val, dict, n=0):
    if n < len(list) - 1:
        dict[list[n]] = {}
        create_nested_dict(list, val, dict[list[n]], n + 1)
    else:
        dict[list[n]] = val
  
      
# create simple state
def create_simple_state(dir_path, file_path, model_path):
    dict = {}
    create_dir(dir_path)
    create_nested_dict(["variants", "", "model"], model_path, dict)
    write_json(dict, file_path)
    
# create custom block model
def create_custom_block_model(dir_path, file_path, dict):
    create_dir(dir_path)
    write_json(dict, file_path)
    
    
# create simple blockitem model
def create_simple_blockitem(dir_path, file_path, parent_path):
    dict = {}
    dict["parent"] = parent_path
    create_dir(dir_path)
    write_json(dict, file_path)


# create simple item model

