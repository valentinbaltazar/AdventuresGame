"""Loads the narration from file"""

from stories.DnD.the_wealthy_merhcant import narration

class GetNarrationInfo:
    """Returns the Narration object, and related information"""
    def __init__(self, narration_module):
        self.narration_module = narration_module
        self.corpus = self.narration_module.story_narration

    def get_headers(self):
        """Story main sections"""

        headers = list(self.corpus.keys())

        print(headers)
        # print(sub_headers)

    def get_structure(self):
        self._traverse_tree(self.corpus)

    def _traverse_tree(self, tree, parent_key=''):
        """Go down dictionary tree and get all keys"""
        if isinstance(tree, str):
            # Dont continue, ends at string node
            print("End of node.")
        elif isinstance(tree, dict):
            for key, value in tree.items():
                full_key = f"{parent_key}.{key}" if parent_key else key
                print(full_key)
                self._traverse_tree(value, parent_key=full_key)
        elif isinstance(tree, list):
            for idx, item in enumerate(tree):
                full_key = f"{parent_key}[{idx}]"
                try:
                    print(full_key)
                    print(item.keys()) # Assumes list has dict items
                    self._traverse_tree(item, parent_key=full_key)
                except:
                    # Some list end with string nodes
                    self._traverse_tree(item, parent_key=full_key)




if __name__ == '__main__':
    story = GetNarrationInfo(narration)
    story.get_headers()
    story.get_structure()