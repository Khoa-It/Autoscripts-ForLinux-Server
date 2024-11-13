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

def write_array_to_file(filepath, content_array):
    try:
        with open(filepath, "w") as file:
            file.writelines(content_array)
        print(f"Successfully wrote to {filepath}.")
    except PermissionError:
        print(f"Error: Permission denied to write to the file {filepath}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")