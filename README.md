# Walibee – Premium Passport Covers

This is a small static website for the Walibee passport covers demo. It uses Tailwind CSS (via CDN) and minimal vanilla JavaScript for interactions (dark mode toggle, image upload, live preview).

## Structure

- `index.html` — main page
- `Css/style.css` — additional styles
- `js/script.js` — page scripts
- `Readme/README.md` — older README (committed earlier)

## Run locally

Recommended: use the VS Code Live Server extension for a quick local preview.

1. Install the Live Server extension in VS Code (Ritwick Dey).
2. Open the folder `walibee-website` in VS Code.
3. Right-click `index.html` and choose *Open with Live Server* (or click the Go Live button).

Or use a simple Python server from the project root:

```powershell
cd "c:\Users\mirza.baig_dmclinica\Desktop\walibee-website"
python -m http.server 5500

# Then open http://localhost:5500 in your browser
```

## Deploy (GitHub Pages)

This repository is named as a user site: `Wall-EBaig.github.io`.
If you want the site live at `https://wall-ebaig.github.io/`, ensure the repository is public and GitHub Pages is set to deploy from branch `main` (it should publish automatically for a repo named `USERNAME.github.io`).

## Notes

- If you want me to add a license, CI, or a custom domain, tell me and I can add it.
