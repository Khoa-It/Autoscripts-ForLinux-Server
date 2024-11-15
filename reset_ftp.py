import os

def stop_service():
    os.system('sudo systemctl stop vsftpd')
    print('Service vsftpd stopped successfully!')

def delete_user(username):
    # Xóa người dùng nếu tồn tại
    if os.system(f'id -u {username} > /dev/null 2>&1') == 0:
        os.system(f'sudo userdel -r {username}')
        print(f'User {username} and their home directory deleted successfully!')
    else:
        print(f"User '{username}' does not exist.")

def reset_ftp():
    stop_service()
    ftp_user = input("Enter ftp user that you want delete: ")
    if not ftp_user:
        print('Skipping user delete')
        exit()
    delete_user(ftp_user)
    print('delete ftp user successfull !')

# Thực thi reset FTP
reset_ftp()
print('reset ftp successfull')
