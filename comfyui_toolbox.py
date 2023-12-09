import json
import folder_paths
import os
from pathlib import Path
import random

JSON_OUT_PATH = os.path.join(folder_paths.output_directory, "json")
Path(JSON_OUT_PATH).mkdir(parents=True, exist_ok=True)

class TestJsonPreview:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("JSON",)
    FUNCTION = "json_test"
    CATEGORY = "test"

    def json_test(self, text):
        return (text, )

class SaveJson:
    def __init__(self):
        self.output_dir = JSON_OUT_PATH
        self.prefix_append = ""
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "filename": ("STRING", {"default": "ComfyUI_Json"}),
                "json": ("JSON",),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "save_json"
    OUTPUT_NODE = True
    CATEGORY = "toolbox"

    def save_json(self, filename="ComfyUI_Json", json_content={}):
        pretty_json = json.dumps(json_content, indent=4)
        with open(Path(self.output_dir) / f"{filename}{self.prefix_append}.json", "w") as outfile:
            outfile.write(pretty_json)
        return { "ui": { "json_file": f"{filename}{self.prefix_append}.json" }}

class PreviewJson(SaveJson):
    def __init__(self):
        self.output_dir = folder_paths.get_temp_directory()
        self.prefix_append = "_temp_" + ''.join(random.choice("abcdefghijklmnopqrstupvxyz") for x in range(5))
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "json_content": ("JSON",),
            },
        }

# class PreviewVideo:
#     ...

NODE_CLASS_MAPPINGS = {
    "TestJsonPreview": TestJsonPreview,
    "PreviewJson": PreviewJson,
    "SaveJson": SaveJson,
    #"PreviewVideo": PreviewVideo
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "PreviewJson": "Preview Json",
    "SaveJson": "Save Json",
    "TestJsonPreview": "Test Json Preview",
    #"PreviewVideo": "Preview Video"
}

WEB_DIRECTORY = "web"