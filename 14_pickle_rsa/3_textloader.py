import os
import string


class TextLoader:
    def __init__(self, path):
        if os.path.isdir(path):
            self.path = path
            self.file_paths = []

            for f in os.listdir(self.path):
                file_path = os.path.join(self.path, f)
                if os.path.isfile(file_path):
                    self.file_paths.append(file_path)
        else:
            raise ValueError(path + " is not a directory")

    def __len__(self):
        return len(self.file_paths)

    def __get_text(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().lower().translate(str.maketrans('', '', string.punctuation))
    
    def __getitem__(self, idx):
        return self.__get_text(self.file_paths[idx])

    def __iter__(self):
        for file_path in self.file_paths:
            yield self.__get_text(file_path)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["file_paths"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        
        self.file_paths = []
        for f in os.listdir(self.path):
            file_path = os.path.join(self.path, f)
            if os.path.isfile(file_path):
                self.file_paths.append(file_path)
