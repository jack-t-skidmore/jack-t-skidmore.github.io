# Notes for AI agents working on jackskidmore.com

Jack's personal site: a Jekyll site deployed to GitHub Pages by `.github/workflows/`
on every push to `main`. Pushing to `main` publishes, so don't push without Jack's go-ahead.

## How the site is laid out

- **Home (`index.md`)**: a short intro, then a scrolling feed of Jack's ~quarterly
  updates, newest first, with an email signup between each one. The newest 5 are built
  into the page; older ones are fetched as the reader scrolls (`_includes/feed-loader.html`).
  "Featured" is hand-picked: only change it when Jack asks.
- **Writing (`writing.md`)**: Essays and Prayers side by side, then Updates and
  Projects. All lists are generated, so nothing there needs editing by hand.
- **Welcome (`welcome.md`)**: Jack's intro letter for new visitors. Its "latest" link
  points at the newest update in the Home feed automatically.

**Jack's words are his own.** Don't reword, tidy or "improve" anything he has written
(updates, essays, prayers, Welcome, descriptions) unless he asks for that specific
change. Adding links or markup around his words is fine when asked; changing the words
is not. If something reads like a typo, flag it instead of fixing it.
- `/essays/`, `/prayers/`, `/updates/`, `/projects/` are redirects into sections of
  Writing. Keep them working: old emails link to them.
- `preview/` holds unlisted share-by-link drafts (kept out of listings and search).

## Adding content

- **Quarterly update:** copy `updates/_template.md` to `updates/<slug>.md` and set
  `title`, `date` and `description`. It appears on Home and in Writing automatically.
- **Essay or prayer:** a new `.md` in `essays/` or `prayers/` with `layout: page`,
  `title`, `date`, `description`. It shows up in Writing automatically.
- Link-preview images are generated at deploy time by `_og/generate.py` from each
  page's `title` (or `og_title`), so no image needs to be made by hand.

## Things to check when editing updates

Updates are written as emails first, then live on the site. They're shown both on their
own page and stacked together in the Home feed.

- **Section links inside an update** (e.g. the intro's "Read whatever sounds interesting"
  list) should point at that update's own headings, like `[Story time](#story-time)`.
  The id is the heading lowercased, punctuation dropped, spaces to dashes. The Home
  feed prefixes every id and `#` link with the update's slug, so headings that
  repeat across updates ("Story time") don't collide. Don't hand-write prefixed ids,
  and don't link to another update's heading with a bare `#anchor`: use its full URL,
  e.g. `/updates/<slug>/#story-time`.
- After adding or editing an update, open Home and click each section link to confirm it
  lands in the right update. If one doesn't, flag it to Jack.
- Avoid raw HTML `id="..."` attributes in update bodies unless needed. They get
  prefixed too, which is fine, but CSS or scripts targeting them won't match on Home.

## Style

- Controls are square-cornered and flat to match eudo.co / research.eudo.co. Colors
  come from the CSS variables at the top of `assets/css/style.css` (light and dark).
- The header must stay on one row on phones 360px and wider. Re-check that if you add
  a nav item or lengthen a label.
- Header captions ("^ new here?") are set per nav item with `caption:` in `_data/nav.yml`.

## Running it locally

`jekyll serve --livereload` (Ruby 3.3 via Homebrew; Ruby 4.0 can't build one of Jekyll's
native gems). Jekyll doesn't reload `_config.yml`, so restart after changing it.
