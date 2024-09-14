import os

def list_files_and_sizes(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath=os.path.join(root,file)
            size=os.path.getsize(filepath)
            print(f'{file}: {size} bytes')

list_files_and_sizes("../../")