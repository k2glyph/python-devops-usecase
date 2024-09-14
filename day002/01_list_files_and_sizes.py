import os

def list_files_and_sizes(directory, output_file='file_sizes.txt'):
    try:
        with open(output_file, 'w') as f:
            for root, dirs, files in os.walk(directory):
                # print(f'{root}, {dirs}, {files}')
                for file in files:
                    filepath=os.path.join(root, file)
                    size=os.path.getsize(filepath)
                    f.write(f'file: {filepath} and size: {size} bytes\n')
    except FileNotFoundError:
        print(f'The directory {directory} doesnot exists.')
    except Exception as e:
        print(f'An error occured: {e}')


list_files_and_sizes("nepal/")