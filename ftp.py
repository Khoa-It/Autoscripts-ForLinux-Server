import os
from fn_file import *
from fn_folder import *
from fn_user import *
from config_file_ftp import *

def install_pakage():
    opinion = input("Would you like to install vsftpd for ftp server (y/n): ")
    if opinion == 'y':
        os.system('sudo yum install -y vsftpd')
        print('install successfull !')
    else:
        print('you dont need install !')

def stop_service():
    os.system('sudo systemctl stop vsftpd')
    print('stop service successfull !')

def handle_user():
    username = input("Enter the username: ")
    create_user(username)
    user_dir = f'/home/{username}/ftp'
    create_folder(user_dir)
    set_folder_owner(username, user_dir)
    set_permission_folder(user_dir, 755)
    set_permission_folder(f'/home/{username}', 755)
    set_permission_folder('/home', 755)
    print(f'Directory {user_dir} created and permissions set!')
    write_content_to_file('/etc/vsftpd/vsftpd.conf', vsftpd_configuration_ver2(user_dir))
    
os.system('clear')
print('stop firewall .......')
os.system('sudo systemctl stop firewalld')
print('stop firewall successfull')
os.system('sudo setenforce 0')
install_pakage()
stop_service()
my_path = '/var/ftp/pub'
if not os.path.exists(my_path):
    os.system('sudo mkdir -p /var/ftp/pub')
set_permission_folder('/var/ftp', 755)
set_permission_folder('/var/ftp/pub', 755)
handle_user()
os.system('sudo systemctl enable vsftpd')
os.system('sudo systemctl restart vsftpd')
print('ftp configuration successfull !')
