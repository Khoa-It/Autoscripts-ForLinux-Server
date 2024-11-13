from fn_file import *
import os

content = """
[connection]
id=enp0s3
uuid=3e3cfe61-1159-3c0a-85a0-06fc01e081ac
type=ethernet
autoconnect-priority=-999
interface-name=enp0s3
timestamp=1731507994

[ethernet]

[ipv4]
dns=8.8.8.8;8.8.4.4
method=manual

[ipv6]
addr-gen-mode=eui64
method=auto

[proxy]
"""

file_path = '/etc/NetworkManager/system-connections/enp0s3.nmconnection'
write_content_to_file(file_path,content)
os.system('sudo systemctl restart NetworkManager')
