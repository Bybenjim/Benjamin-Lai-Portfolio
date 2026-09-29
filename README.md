# Video Production Singapore | Bybenjim (Benjamin Lai)

One-page video production portfolio for Benjamin Lai (Bybenjim), targeting search traffic for "Video Production Singapore" and related terms. Corporate, product, social and event video production, plus editing and post-production.

Static site, no build step required. The work grid, services, and FAQ are all rendered directly in `index.html` (not built by JavaScript) so search engines and social-share scrapers can read everything without executing JS. Each project is one `.work-card` block plus a matching entry in the `VideoObject` JSON-LD near the top of `index.html`; add or remove projects by editing both together.

## SEO

- Primary keyword: Video Production Singapore. Secondary: Video Editor Singapore, Corporate/Social Media/Product Video Production Singapore, Event Videography Singapore, Video Editing Services Singapore.
- `robots.txt` and `sitemap.xml` point at `https://benjamin-lai-portfolio.vercel.app/`. **If you deploy to a different Vercel URL or a custom domain, update that URL in five places:** `index.html` (canonical, og:url, og:image, twitter:image), `robots.txt`, and `sitemap.xml`.
- `og-image.png` (1200x630) is the link-preview image for social shares; regenerate it with `python3 generate_og_image.py` if you change the headline copy.
- Structured data in `index.html`'s `<head>`: `Person` (Benjamin Lai), a `Service` list (the five offerings), `FAQPage` (matches the visible FAQ text exactly, required for FAQ rich results), and a `VideoObject` list for the portfolio.
- The FAQ section uses native `<details>/<summary>`, no JS needed, keyboard-accessible by default.
- Video players are click-to-load: only a thumbnail `<img>` loads on page load, the YouTube iframe loads on interaction. Keeps initial page weight low regardless of portfolio size.

## Local preview

```
npx serve .
```

## Deploy

Deployed on Vercel from this GitHub repo. Any push to `main` redeploys automatically.
