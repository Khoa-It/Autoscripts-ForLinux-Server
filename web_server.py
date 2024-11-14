import os
from fn_file import *

def install_package():
    opinion = input("Would you like to install httpd for web (y/n): ")
    if opinion == 'y':
        os.system('sudo yum install httpd -y')
    else:
        print('Dont need httpd !')

def is_domain(domain_name='google.com'):
    if not domain_name:
        return False
    extension = ['vn', 'com']
    arr = domain_name.split('.')
    if len(arr) == 1:
        return False
    if arr[-1] not in extension:
        return False
    return True
    
    
def create_directory(domain_name):
    os.system('chmod -R 777 /var/www/html')
    web_content = f'<p>Xin chào đây là trang web : {domain_name} </p>'
    directory = f'/var/www/html/{domain_name}'
    os.makedirs(directory, exist_ok=True)
    write_content_to_file(f'{directory}/index.html', web_content)
    command = [
        f'chmod -R 777 {directory}',
        f'chmod -R 777 {directory}/index.html',
    ]
    for cmd in command:
        os.system(cmd)
    
    
def create_configuration_file(domain_name):
    handle_path = f'/etc/httpd/conf.d/{domain_name}.conf'
    file_content = f"""
    <VirtualHost *:80>
        ServerAdmin admin@{domain_name}
        DocumentRoot /var/www/html/{domain_name}
        ServerName {domain_name}
        ServerAlias www.{domain_name}

        ErrorLog /var/log/httpd/{domain_name}_error.log
        CustomLog /var/log/httpd/{domain_name}_access.log combined
    </VirtualHost>
    """
    write_content_to_file(handle_path,file_content)
    os.system(f'chmod -R 777 {handle_path}')
    
        
    
def restart_service():
    command = [
        f'sudo systemctl enable httpd',
        f'sudo systemctl restart httpd',
    ]
    for cmd in command:
        os.system(cmd)

install_package()
domain_name  = input("Enter domain name for website (domain name must have dns config in your laptop): ")
if not is_domain(domain_name):
    print('domain is unvalid !')
    exit()
create_directory(domain_name)
create_configuration_file(domain_name)
restart_service()


