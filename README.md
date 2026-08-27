# Benjamin Lai Portfolio

Personal portfolio site for Benjamin Lai (ByBenJim), video producer and social media strategist based in Singapore.

Static site, no build step required. The work grid is rendered directly in `index.html` (not built by JavaScript) so search engines and social-share scrapers can read it without executing JS. Each project is one `.work-card` block plus a matching entry in the `VideoObject` JSON-LD near the top of `index.html`; add or remove projects by editing both together.

## SEO

- `robots.txt` and `sitemap.xml` point at `https://benjamin-lai-portfolio.vercel.app/`. **If you deploy to a different Vercel URL or a custom domain, update that URL in five places:** `index.html` (canonical, og:url, og:image, twitter:image), `robots.txt`, and `sitemap.xml`.
- `og-image.png` (1200x630) is the link-preview image for social shares; regenerate it with `python3 generate_og_image.py` if you change the headline copy.
- Structured data: a `Person` schema and a `VideoObject` list (one per project) are embedded as JSON-LD in `index.html`'s `<head>`.

## Local preview

```
npx serve .
```

## Deploy

Deployed on Vercel from this GitHub repo. Any push to `main` redeploys automatically.
