#!/usr/bin/env python3
"""Upload index.html to /index.html on zhangyunhai.com FTP root."""
import os, re, socket, sys, time

HOST = os.environ.get("FTP_HOST", "ftp.zhangyunhai.com")
USER = os.environ["FTP_USER"]
PW   = os.environ["FTP_PASS"]
LOCAL = os.path.join(os.path.dirname(__file__), "index.html")
REMOTE = "index.html"

def cmd(s, c, w=0.4):
    s.sendall((c + "\r\n").encode())
    time.sleep(w)
    out = b""
    while True:
        try: chunk = s.recv(4096)
        except socket.timeout: break
        if not chunk: break
        out += chunk
    return out.decode(errors="replace").strip()

s = socket.socket(); s.settimeout(20); s.connect((HOST, 21)); s.recv(4096)
print(cmd(s, f"HOST {HOST}"))
print(cmd(s, f"USER {USER}"))
print(cmd(s, f"PASS {PW}"))
cmd(s, "TYPE I")
print(cmd(s, "PWD"))

s.sendall(b"PASV\r\n"); time.sleep(0.4)
resp = s.recv(4096).decode()
m = re.search(r"(\d+),(\d+),(\d+),(\d+),(\d+),(\d+)", resp)
h1, h2, h3, h4, p1, p2 = map(int, m.groups())
ds = socket.socket(); ds.settimeout(20)
ds.connect((f"{h1}.{h2}.{h3}.{h4}", (p1 << 8) | p2))
s.sendall(f"STOR {REMOTE}\r\n".encode())
time.sleep(0.4)
pre = s.recv(4096).decode().strip()
with open(LOCAL, "rb") as f: ds.sendall(f.read())
ds.shutdown(socket.SHUT_WR); ds.close()
time.sleep(0.5)
try: s.recv(4096)
except: pass
cmd(s, "QUIT"); s.close()
print(f"uploaded {LOCAL} → /{REMOTE}: {pre} ({os.path.getsize(LOCAL):,} bytes)")
