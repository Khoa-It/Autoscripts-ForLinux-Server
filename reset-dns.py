from fn_file import *
import os
import glob


def reset_named_conf_content(ip):
    return f"""
//
// named.conf
//
// Provided by Red Hat bind package to configure the ISC BIND named(8) DNS
// server as a caching only nameserver (as a localhost DNS resolver only).
//
// See /usr/share/doc/bind*/sample/ for example named configuration files.
//
options {{
        listen-on port 53 {{ 127.0.0.1; {ip}; }};
        listen-on-v6 port 53 {{ ::1; }};
        directory       "/var/named";
        forwarders {{8.8.8.8;8.8.4.4; }};
        dump-file       "/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";
        secroots-file   "/var/named/data/named.secroots";
        recursing-file  "/var/named/data/named.recursing";
        allow-query     {{ localhost; }};

        recursion yes;

        dnssec-validation yes;

        managed-keys-directory "/var/named/dynamic";
        geoip-directory "/usr/share/GeoIP";

        pid-file "/run/named/named.pid";
        session-keyfile "/run/named/session.key";

        include "/etc/crypto-policies/back-ends/bind.config";
}};

logging {{
        channel default_debug {{
                file "data/named.run";
                severity dynamic;
        }};
}};

zone "." IN {{
        type hint;
        file "named.ca";
}};

include "/etc/named.rfc1912.zones";
include "/etc/named.root.key";
"""

def reset_resolv_file_content(ip):
    return f"""
# Generated by NetworkManager
nameserver {ip}
nameserver 8.8.8.8
nameserver 8.8.4.4
"""

def delete_domain_files(directory, extensions):
    for ext in extensions:
        # Tìm tất cả các file có đuôi mở rộng được chỉ định
        files = glob.glob(os.path.join(directory, f"*.{ext}"))
        for file_path in files:
            try:
                os.remove(file_path)
                print(f"Deleted {file_path}")
            except PermissionError:
                print(f"Error: Permission denied to delete {file_path}.")
            except Exception as e:
                print(f"An error occurred while deleting {file_path}: {e}")

name_conf_file = '/etc/named.conf'
domain_path = '/var/named'
resolv_file = '/etc/resolv.conf'
ip_address = input('Enter your ip:')
if not ip_address:
    print('Null value ip_address')
    exit()
# Tắt dịch vụ DNS
os.system("systemctl stop named")
print("DNS service stopped.")

write_content_to_file(resolv_file, reset_resolv_file_content(ip_address))
write_content_to_file(name_conf_file, reset_named_conf_content(ip_address))
delete_domain_files(domain_path, ["vn", "com"])

