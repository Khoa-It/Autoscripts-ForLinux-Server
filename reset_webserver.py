import os

def stop_service():
    os.system('sudo systemctl stop httpd')
    print("Web server stopped successfully.")

def delete_directory(domain_name):
    directory = f'/var/www/html/{domain_name}'
    if os.path.exists(directory):
        os.system(f'rm -rf {directory}')
        print(f"Deleted directory: {directory}")
    else:
        print(f"Directory {directory} does not exist.")

def delete_configuration_file(domain_name):
    config_path = f'/etc/httpd/conf.d/{domain_name}.conf'
    if os.path.exists(config_path):
        os.system(f'rm -f {config_path}')
        print(f"Deleted configuration file: {config_path}")
    else:
        print(f"Configuration file {config_path} does not exist.")

def delete_logs(domain_name):
    error_log = f'/var/log/httpd/{domain_name}_error.log'
    access_log = f'/var/log/httpd/{domain_name}_access.log'
    for log_file in [error_log, access_log]:
        if os.path.exists(log_file):
            os.system(f'rm -f {log_file}')
            print(f"Deleted log file: {log_file}")
        else:
            print(f"Log file {log_file} does not exist.")

def restart_service():
    os.system('sudo systemctl start httpd')
    print("Web server restarted successfully.")

def reset_webserver(domain_name):
    stop_service()  # Tắt dịch vụ Apache trước khi thực hiện reset
    delete_directory(domain_name)
    delete_configuration_file(domain_name)
    delete_logs(domain_name)
    restart_service()

# Thực thi script reset web server
domain_name = input("Enter the domain name to reset (delete domain and web file): ")
reset_webserver(domain_name)
