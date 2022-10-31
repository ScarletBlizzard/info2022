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
        

if __name__ == "__main__":
    txt_loader = TextLoader("sample")
    print(txt_loader.file_paths)
    print(len(txt_loader))
    print(txt_loader[0])
    for i, txt in enumerate(txt_loader):
        print(f"{i}:", txt.split("\n")[0])
