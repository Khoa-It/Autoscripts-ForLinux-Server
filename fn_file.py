import os
def read_file_to_array(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file {filepath}.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return []  # Trả về mảng rỗng nếu có lỗi

def write_content_to_file(filepath, content):
    try:
        with open(filepath, "w") as file:
            if isinstance(content, list):
                file.writelines(content)
            else:
                file.write(content)
        print(f"Successfully wrote to {filepath}.")
    except PermissionError:
        print(f"Error: Permission denied to write to the file {filepath}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        
def create_file(path):
    with open(path, 'w') as file:
        pass

def set_file_owner(username, file_path):
    if not os.path.exists(file_path):
        print('File not exists.')
        return
    os.system(f'sudo chown -R {username}:{username} {file_path}')
    
def set_permission_file(file_path, permission):
    if not os.path.exists(file_path):
        print('file not exists.')
        return
    os.system(f'sudo chmod {permission} {file_path}')