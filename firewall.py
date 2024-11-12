import subprocess

def show_menu():
    print("Firewall Management")
    print("1. Turn on firewall")
    print("2. Turn off firewall")
    print("3. Check firewall status")
    print("0. exit")
    print("---------------------")


def firewall_status():
    sub_command = ["sudo", "systemctl", "is-active", "firewalld"]
    status = subprocess.run(sub_command, capture_output=True, text=True).stdout.strip()
    return status

def stop_firewall():
    print("==================")
    print("turnning off firewall ...")
    stop_command = ["sudo", "systemctl", "stop", "firewalld"]
    result = subprocess.run(stop_command, capture_output=True, text=True)
    
    # Kiểm tra nếu có lỗi trong quá trình tắt tường lửa
    if result.returncode == 0:
        print("Turnoff successfull.")
    else:
        print("Cannot turnoff firewall. Error:", result.stderr)
    print("===============")

def start_firewall():
    print("Starting the firewall...")
    start_command = ["sudo", "systemctl", "start", "firewalld"]
    result = subprocess.run(start_command, capture_output=True, text=True)
    
    # Check if there was an error while starting the firewall
    if result.returncode == 0:
        print("Firewall started successfully.")
    else:
        print("Failed to start the firewall. Error:", result.stderr)    

def main():
    show_menu()
    while True:
        print("===============")
        choice = int(input("Enter your choice: "))
        print("===============")
        
        if choice == 3:
            status = firewall_status()
            print(f"Your firewall: {status}")
        elif choice == 0:
            break
        elif choice == 2:
            stop_firewall()
        elif choice == 1:
            start_firewall()
        else:
            print("Your choice is invalid")


if __name__ == "__main__":
    main()