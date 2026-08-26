# yunhai-homepage

Personal landing page at <https://zhangyunhai.com/>. Direct 1-to-1
English translation of `index-cn.html`, keeping the original Chinese
page's structure, layout and CSS intact. No redesign, no build step.

## Local preview

```bash
python3 -m http.server 8080
# open http://localhost:8080/
```

## Deploy (FTP)

```bash
./deploy.sh
# uploads index.html to /index.html on zhangyunhai.com via FTP
```

Credentials come from `~/.hermes/.env` (`FTP_HOST` / `FTP_USER` / `FTP_PASS`).

## Structure

```
yunhai-homepage/
├── index.html      # English version (1:1 translation of index-cn.html)
├── README.md
├── deploy.sh       # FTP deploy helper
├── deploy.py       # FTP socket script (uses 'HOST' command for Microsoft IIS)
└── .gitignore
```
