#!/usr/bin/env bash
# Upload index.html to zhangyunhai.com root via FTP.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"

source ~/.hermes/.env
: "${FTP_HOST:=ftp.zhangyunhai.com}"
: "${FTP_USER:=administrator}"
: "${FTP_PASS:?FTP_PASS must be set in ~/.hermes/.env}"

python3 "$HERE/deploy.py"
