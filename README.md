# yunhai-homepage

Personal landing page at <https://zhangyunhai.com/>. Apple HIG-styled,
lightweight single-file HTML, no build step.

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

## Design notes

- Apple HIG: system font, optical sizes, 96px side margins, spring easing
- Light by default, dark mode via `prefers-color-scheme`
- Reduced-motion fallback
- No external font/CSS dependencies (system fonts only)
- No JavaScript

## Structure

```
yunhai-homepage/
├── index.html      # the whole page
├── README.md
├── deploy.sh       # FTP deploy helper
└── .gitignore
```
