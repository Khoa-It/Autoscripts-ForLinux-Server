import configparser
import subprocess

def get_current_gateway():
    # Chạy lệnh `ip route` và lấy kết quả
    result = subprocess.run("ip route | grep default", shell=True, capture_output=True, text=True)
    # Phân tích chuỗi để lấy Gateway
    if result.returncode == 0:
        gateway = result.stdout.split()[2]  # Địa chỉ Gateway nằm ở vị trí thứ 3 trong kết quả
        return gateway
    else:
        print("Không thể lấy địa chỉ Gateway")
        return None

# Cấu hình thông tin mạng
interface_name = "enp0s3"
ip_address = "192.168.1.10/24"
gateway = "192.168.1.1"
dns_servers = "8.8.8.8;8.8.4.4"

# Đường dẫn file cấu hình
config_file_path = f"/etc/NetworkManager/system-connections/{interface_name}.nmconnection"

# Đọc nội dung file cấu hình gốc
with open(config_file_path, "r") as file:
    original_content = file.readlines()
    
# Chỉnh sửa nội dung file
new_content = []
in_ipv4_section = False
for line in original_content:
    # Kiểm tra khi vào phần [ipv4]
    if line == "[ipv4]\n":
        in_ipv4_section = True
    elif line.startswith("[") and in_ipv4_section:
        # Nếu gặp một phần khác ([ipv6], [proxy], v.v.), kết thúc phần [ipv4]
        in_ipv4_section = False

    # Chỉ chỉnh sửa khi đang ở trong phần [ipv4]
    if in_ipv4_section:
        if line.startswith("method="):
            new_content.append("method=manual\n")
        elif line.startswith("addresses1="):
            new_content.append(f"addresses1={ip_address},{gateway}\n")
        elif line.startswith("dns="):
            new_content.append(f"dns={dns_servers}\n")
        else:
            new_content.append(line)
    else:
        new_content.append(line)


# Ghi lại nội dung mới vào file cấu hình
with open(config_file_path, "w") as file:
    file.writelines(new_content)
print("Static IP configuration written to file.")

# Khởi động lại NetworkManager để áp dụng cấu hình mới
subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
print("NetworkManager restarted.")