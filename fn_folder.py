import os

def create_folder(my_path):
    if os.path.exists(my_path):
        print('Folder is already existed !')
    else:
        os.mkdir(my_path)
        print('Create folder successfull !')

def set_folder_owner(username, folder_path):
    if not os.path.exists(folder_path):
        print('Folder not exists.')
        return
    os.system(f'sudo chown -R {username}:{username} {folder_path}')
    
def set_permission_folder( folder_path, permission):
    if not os.path.exists(folder_path):
        print('Folder not exists.')
        return
    os.system(f'sudo chmod -R {permission} {folder_path}')

        
