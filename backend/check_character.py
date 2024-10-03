"""Need to standardize character so they can be displayed to user"""
import importlib
import inspect


from stories.DnD.the_wealthy_merhcant import character1

class GetCharInfo:
    """Returns class and name for a character module"""
    def __init__(self, mod_name=None):
        self.mod_name = mod_name # module with a chracters class
    

    def get_class_info(self):
        # Retrieve all classes from the module
        classes = inspect.getmembers(self.mod_name, inspect.isclass)

        # Assuming there's only one class in the module
        class_name, class_type = classes[0]

        # Instantiate the class
        instance = class_type()

        # Check the instance
        print(f"Created an instance of {class_name}: {instance}")

        return class_name, instance


if __name__ == '__main__':

    # The name of the file without the `.py` extension
    # module_name = "./stories/DnD/the_wealthy_merhcant/character1.py"

    # Import the module
    # module = importlib.import_module(character1)
    
    char_info = GetCharInfo(character1)
    char1_name, char_class = char_info.get_class_info()
    print(char1_name)
