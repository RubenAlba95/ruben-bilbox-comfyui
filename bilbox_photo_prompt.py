import json
import os

EMPTY_TEXT = ""
def read_json_file(file_path):
    try:
        # Open file, load JSON content into python dictionary, and return it.
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def get_list(data, name, tag="name", can_be_null=True):
    ret = [EMPTY_TEXT] if can_be_null else []
    if(isinstance(data, dict) and name in data):
        ret.extend([d[tag] for d in data[name] if tag in d])
    return ret

class RubenBilboXPhotoPrompt:

    def __init__(self):
        pass


    @classmethod
    def INPUT_TYPES(self):
        # Get current file's directory
        p = os.path.dirname(os.path.realpath(__file__))

        try:
            file_path = os.path.join(p, './web/PromptGeek/photo_data.json')
            with open(file_path) as f:
                self.json_data = json.load(f)
        except Exception as e:
            print(f"An error occurred during BilboX's PromptGeek Photo Prompt initialization: {str(e)}")

        # "[STYLE OF PHOTO] photo of a [SUBJECT], [IMPORTANT FEATURE], [MORE DETAILS], [POSE OR ACTION],[FRAMING],
        #  [SETTING/BACKGROUND], [LIGHTING],[CAMERA ANGLE], [CAMERA PROPERTIES],in style of [PHOTOGRAPHER]"
        return {
            "required": {
                "style": ((get_list(self.json_data,"style")), ),
                "subject": ("STRING", {"default": "", "multiline": True,"placeholder": "[SUBJECT], [IMPORTANT FEATURE], [MORE DETAILS], [POSE OR ACTION]"}),
                "framing": ((get_list(self.json_data,"framing")), ),
                "setting_background": ("STRING", {"default": "", "multiline": True}),
                "lighting": ((get_list(self.json_data,"lighting")), ),
                "camera_angle": ((get_list(self.json_data,"camera angle")), ),
                "camera_properties": ((get_list(self.json_data,"camera properties")), ),
                "film_types": ((get_list(self.json_data,"film types")), ),
                "lenses": ((get_list(self.json_data,"lenses")), ),
                "filters_effects": ((get_list(self.json_data,"filters effects")), ),
                "photographers": ((get_list(self.json_data,"photographers")), ),
                
                "preview": ("STRING", {"default": "", "multiline": True, "placeholder":"Preview"}),
                "log_prompt": (["No", "Yes"], {"default":"No"}),
            },
        }

    RETURN_TYPES = ('STRING', 'STRING')
    RETURN_NAMES = ('full_composed_prompt', 'subject_only')
    FUNCTION = 'prompt_styler'
    CATEGORY = 'BilboX'

    def prompt_styler(self, style, subject, framing,
                      setting_background, lighting, camera_angle,
                      camera_properties, film_types, lenses,
                      filters_effects, photographers,
                      preview, log_prompt):
        # # Process and combine prompts in templates
        # # The function replaces the positive prompt placeholder in the template,
        # # and combines the negative prompt with the template's negative prompt, if they exist.
        # positive_prompt = replace_and_combine(self.json_data,
        #     style, subject, framing, setting_background, lighting,
        #     camera_angle, camera_properties, film_types, lenses,
        #     filters_effects, photographers)
        # If logging is enabled (log_prompt is set to "Yes"), 
        # print the style, positive and negative text, and positive and negative prompts to the console
        if log_prompt == "Yes":
            print(f"full_composed_prompt: {preview}")
            print(f"subject_only: {subject}")

        return preview, subject
