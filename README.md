# Great Escape Games: website redesign concept

A working concept build. Eight static pages, fully navigable on desktop and
mobile.

**Start at `proposal.html`** for the pitch, or `index.html` for the site itself.

## Viewing it

Double-click `index.html`. It runs straight off the filesystem, no server
needed. To serve it locally instead:

```bash
python -m http.server 8000
```

Fonts (Cinzel, Barlow Condensed, Spectral) load from Google Fonts, so type
falls back to system serifs if you open it offline. Everything else is local.

## Pages

| File | Covers |
| --- | --- |
| `index.html` | Home: hero, both halls with live open/closed, categories, new stock, events, rooms |
| `products.html` | Shop: 17 items, filterable by range, card-finder handoff |
| `events.html` | Calendar filterable by hall and system, weekly schedules, house rules |
| `rooms.html` | Three private rooms, rate card, booking form with live total |
| `about.html` | The 1996 story, what the shop is for |
| `visit.html` | Addresses, hours, maps handoff, contact form, account sign-in |
| `legal.html` | Terms, privacy, in-store house rules |
| `proposal.html` | The pitch: what's wrong with the current site and what changed |

## Structure

```
assets/css/geg.css   one stylesheet, design tokens at the top
assets/js/geg.js     one script, no dependencies
assets/img/          generated backdrops, plates, grain, emblem
assets/img/cut/      product shots with the white studio background keyed out
assets/img/products/ the original product JPEGs, kept as source
build.py             emits the eight HTML files
```

The header, footer, nav drawer and icon sprite are defined once in `build.py`
so the pages can't drift apart. Edit there, then:

```bash
python build.py
```

If you'd rather hand the HTML to someone else and drop the generator, that's
fine too. The output is plain static HTML with no build step required to
deploy.

## What's real and what isn't

- **Real**: both addresses, phone numbers and all trading hours; the 1996
  founding and Gary Lane; private room rates and booking blocks; social links;
  the TCGplayer card finder link. All taken from the current site.
- **Placeholder**: the event calendar, product prices and stock counts. Made
  up but plausible, so the design could be judged with realistic content in it.
  Replace before this goes near customers.
- **Not wired up**: forms confirm on screen but don't send. Accounts,
  payments and live inventory need a back end.

## Artwork

Product photography is official supplier imagery (Games Workshop, Pokémon),
cut off its white studio background so it sits on the dark plates. Clear
licensing with the publishers before launch.

The atmospheric backdrops, heraldic category plates, grain overlay and room
images are all generated for this build, so nothing there needs licensing. The generator lives in the scratchpad; regenerate or restyle
by adjusting the tint and glyph tables in it.

The emblem is the store's own logo, taken from the current site.
