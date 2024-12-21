import os

def find_non_utf8_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        f.read()
                except UnicodeDecodeError:
                    print(f"Non-UTF-8 file found: {file_path}")

find_non_utf8_files(".")
