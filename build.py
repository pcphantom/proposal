#!/usr/bin/env python3
"""Builds the Great Escape Games concept site.

Plain static HTML comes out the other side, with no server and no framework. The
header, footer, drawer and icon sprite live here once so eight pages can't
drift apart. Edit here, run `python build.py`, commit the HTML.
"""
from pathlib import Path

ROOT = Path(__file__).parent

NAV = [
    ("home", "index.html", "Home"),
    ("products", "products.html", "Shop"),
    ("events", "events.html", "Events"),
    ("rooms", "rooms.html", "Private Rooms"),
    ("about", "about.html", "About"),
    ("visit", "visit.html", "Visit"),
]

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="i-search" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.7" d="M11 4a7 7 0 1 1 0 14 7 7 0 0 1 0-14zm5 12 4.5 4.5"/></symbol>
  <symbol id="i-user" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.7" d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm-8 8c0-3.3 3.6-5.5 8-5.5s8 2.2 8 5.5"/></symbol>
  <symbol id="i-menu" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.7" d="M3 6h18M3 12h18M3 18h18"/></symbol>
  <symbol id="i-close" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.7" d="m5 5 14 14M19 5 5 19"/></symbol>
  <symbol id="i-ig" viewBox="0 0 24 24"><path fill="currentColor" d="M7.8 2h8.4C19.4 2 22 4.6 22 7.8v8.4a5.8 5.8 0 0 1-5.8 5.8H7.8C4.6 22 2 19.4 2 16.2V7.8A5.8 5.8 0 0 1 7.8 2m-.2 2A3.6 3.6 0 0 0 4 7.6v8.8C4 18.39 5.61 20 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6C20 5.61 18.39 4 16.4 4H7.6m9.65 1.5a1.25 1.25 0 1 1 0 2.5 1.25 1.25 0 0 1 0-2.5M12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10m0 2a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"/></symbol>
  <symbol id="i-fb" viewBox="0 0 24 24"><path fill="currentColor" d="M5 3h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2m13 2h-2.5A3.5 3.5 0 0 0 12 8.5V11h-2v3h2v7h3v-7h3v-3h-3V9a1 1 0 0 1 1-1h2V5z"/></symbol>
  <symbol id="i-yt" viewBox="0 0 24 24"><path fill="currentColor" d="M10 15l5.19-3L10 9v6m11.56-7.83c.13.47.22 1.1.28 1.9.07.8.1 1.49.1 2.09L22 12c0 2.19-.16 3.8-.44 4.83-.25.9-.83 1.48-1.73 1.73-.47.13-1.33.22-2.65.28-1.3.07-2.49.1-3.59.1L12 19c-4.19 0-6.8-.16-7.83-.44-.9-.25-1.48-.83-1.73-1.73-.13-.47-.22-1.1-.28-1.9-.07-.8-.1-1.49-.1-2.09L2 12c0-2.19.16-3.8.44-4.83.25-.9.83-1.48 1.73-1.73.47-.13 1.33-.22 2.65-.28 1.3-.07 2.49-.1 3.59-.1L12 5c4.19 0 6.8.16 7.83.44.9.25 1.48.83 1.73 1.73z"/></symbol>
  <symbol id="i-dc" viewBox="0 0 24 24"><path fill="currentColor" d="M19.54 5.34A16.4 16.4 0 0 0 15.5 4.1a.06.06 0 0 0-.07.03c-.17.31-.37.71-.5 1.03a15.2 15.2 0 0 0-4.55 0c-.14-.33-.34-.72-.52-1.03a.06.06 0 0 0-.06-.03 16.4 16.4 0 0 0-4.05 1.24.06.06 0 0 0-.02.02C2.9 9.2 2.2 12.95 2.55 16.65a.07.07 0 0 0 .02.05 16.5 16.5 0 0 0 4.97 2.5.06.06 0 0 0 .07-.02c.38-.52.72-1.07 1.02-1.65a.06.06 0 0 0-.04-.09c-.53-.2-1.05-.45-1.55-.74a.06.06 0 0 1 0-.1l.3-.24a.06.06 0 0 1 .07 0 11.8 11.8 0 0 0 10 0 .06.06 0 0 1 .07 0l.3.24a.06.06 0 0 1 0 .1c-.5.3-1.01.54-1.55.74a.06.06 0 0 0-.03.09c.3.58.64 1.13 1.01 1.65a.06.06 0 0 0 .07.02 16.4 16.4 0 0 0 4.98-2.5.06.06 0 0 0 .02-.05c.42-4.29-.69-8.01-2.94-11.3a.05.05 0 0 0-.03-.02M8.68 14.44c-.98 0-1.79-.9-1.79-2s.79-2.01 1.79-2.01c1 0 1.8.91 1.79 2 0 1.11-.79 2.01-1.79 2.01m6.61 0c-.98 0-1.79-.9-1.79-2s.79-2.01 1.79-2.01c1 0 1.8.91 1.79 2 0 1.11-.78 2.01-1.79 2.01"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.7" d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z"/><circle cx="12" cy="10" r="2.6" fill="none" stroke="currentColor" stroke-width="1.7"/></symbol>
</svg>"""

RIBBON = """<div class="ribbon">
  <div class="wrap">
    <span>Concept redesign &middot; <b>sample events, stock &amp; pricing</b></span>
    <div class="ribbon-phones">
      <a href="tel:19169270810">Sacramento: 916 927 0810</a>
      <a href="tel:19162591797">Rocklin: 916 259 1797</a>
    </div>
  </div>
</div>"""


def header():
    links = []
    for key, href, label in NAV:
        if key == "events":
            links.append("""      <div class="nav-drop">
        <button type="button" aria-haspopup="true">Events
          <svg width="9" height="9" viewBox="0 0 10 10" aria-hidden="true"><path d="M1 3l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>
        </button>
        <div class="nav-drop-menu">
          <a href="events.html">All Events<small>Both halls, one calendar</small></a>
          <a href="events.html#sacramento">Sacramento<small>Howe Ave</small></a>
          <a href="events.html#rocklin">Rocklin<small>Rocklin Rd</small></a>
        </div>
      </div>""")
        else:
            links.append(f'      <a data-nav="{key}" href="{href}">{label}</a>')
    return """<header class="site-head">
  <div class="wrap nav">
    <a class="brand" href="index.html">
      <img src="assets/img/emblem.png" alt="Great Escape Games">
      <span class="brand-txt"><b>Great Escape</b><span>Games &middot; Est. 1996</span></span>
    </a>

    <nav class="nav-links" aria-label="Main">
%s
    </nav>

    <div class="nav-tools">
      <button class="icon-btn" data-search-open aria-expanded="false" aria-label="Search the shop">
        <svg><use href="#i-search"/></svg>
      </button>
      <a class="icon-btn" href="visit.html#account" aria-label="Your account">
        <svg><use href="#i-user"/></svg>
      </a>
      <a class="btn btn--sm nav-cta" href="rooms.html#book">Book a table</a>
      <button class="icon-btn burger" data-drawer-open aria-expanded="false" aria-label="Open menu">
        <svg><use href="#i-menu"/></svg>
      </button>
    </div>
  </div>
</header>

<div class="searchbar" data-search>
  <div class="wrap">
    <form onsubmit="return false">
      <input type="search" placeholder="Search singles, kits, paints, sleeves&hellip;" aria-label="Search">
      <button class="icon-btn" type="button" data-search-close aria-label="Close search"><svg><use href="#i-close"/></svg></button>
    </form>
    <p class="hint">Try &ldquo;Space Wolves&rdquo;, &ldquo;Commander deck&rdquo;, &ldquo;Contrast paint&rdquo;. Or browse the <a href="products.html">full shop</a></p>
  </div>
</div>

<div class="drawer" data-drawer>
  <div class="drawer-top">
    <span class="brand">
      <img src="assets/img/emblem.png" alt="" width="34">
      <span class="brand-txt"><b>Great Escape</b><span>Games</span></span>
    </span>
    <button class="icon-btn" data-drawer-close aria-label="Close menu"><svg><use href="#i-close"/></svg></button>
  </div>
  <div class="drawer-body">
    <a class="dlink" href="index.html"><em>01</em> Home</a>
    <a class="dlink" href="products.html"><em>02</em> Shop</a>
    <a class="dlink" href="events.html"><em>03</em> Events</a>
    <a class="dlink" href="rooms.html"><em>04</em> Private Rooms</a>
    <a class="dlink" href="about.html"><em>05</em> About</a>
    <a class="dlink" href="visit.html"><em>06</em> Visit &amp; Contact</a>
    <a class="btn btn--block mt-l" href="rooms.html#book">Book a table</a>
  </div>
  <div class="drawer-foot">
    <h4>Call the shop</h4>
    <p class="muted small">Sacramento: <a href="tel:19169270810">916 927 0810</a><br>
       Rocklin: <a href="tel:19162591797">916 259 1797</a></p>
  </div>
</div>""" % "\n".join(links)


FOOTER = """<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-col">
        <div class="foot-brand">
          <img src="assets/img/emblem.png" alt="">
          <span class="brand-txt"><b>Great Escape</b><span>Games &middot; Est. 1996</span></span>
        </div>
        <p class="muted small">Two halls in the Sacramento valley, open seven days, run by people who still play. Come in, sit down, roll something.</p>
        <div class="socials">
          <a href="https://www.instagram.com/explore/locations/252481501/great-escape-games-and-comics/?hl=en" target="_blank" rel="noopener" aria-label="Instagram"><svg><use href="#i-ig"/></svg></a>
          <a href="https://www.facebook.com/GEGsacramento" target="_blank" rel="noopener" aria-label="Facebook"><svg><use href="#i-fb"/></svg></a>
          <a href="https://discord.com/invite/QqpvvqK" target="_blank" rel="noopener" aria-label="Discord"><svg><use href="#i-dc"/></svg></a>
          <a href="https://www.youtube.com/channel/UCLXZYz1W28wHGWhjYSmiPtQ/videos" target="_blank" rel="noopener" aria-label="YouTube"><svg><use href="#i-yt"/></svg></a>
        </div>
      </div>

      <div class="foot-col">
        <h4>The Shop</h4>
        <ul>
          <li><a href="products.html">All products</a></li>
          <li><a href="https://greatescapegamesllc.tcgplayerpro.com/" target="_blank" rel="noopener">Card finder</a></li>
          <li><a href="events.html">Events calendar</a></li>
          <li><a href="rooms.html">Private rooms</a></li>
          <li><a href="about.html">Our story</a></li>
          <li><a href="visit.html">Contact us</a></li>
        </ul>
      </div>

      <div class="foot-col">
        <h4>Sacramento</h4>
        <p class="small"><a href="tel:19169270810">916 927 0810</a><br>1250 Howe Ave #3a<br>Sacramento, CA 95825</p>
        <div class="foot-hours"><span>Mon&ndash;Thu</span><b>12pm&ndash;10pm</b></div>
        <div class="foot-hours"><span>Fri</span><b>12pm&ndash;12am</b></div>
        <div class="foot-hours"><span>Sat</span><b>12pm&ndash;10pm</b></div>
        <div class="foot-hours"><span>Sun</span><b>12pm&ndash;6pm</b></div>
      </div>

      <div class="foot-col">
        <h4>Rocklin</h4>
        <p class="small"><a href="tel:19162591797">916 259 1797</a><br>5050 Rocklin Road, Suite A22<br>Rocklin, CA 95677</p>
        <div class="foot-hours"><span>Mon&ndash;Tue</span><b>12pm&ndash;7pm</b></div>
        <div class="foot-hours"><span>Wed</span><b>12pm&ndash;9pm</b></div>
        <div class="foot-hours"><span>Thu</span><b>12pm&ndash;10pm</b></div>
        <div class="foot-hours"><span>Fri</span><b>12pm&ndash;11pm</b></div>
        <div class="foot-hours"><span>Sat</span><b>12pm&ndash;10pm</b></div>
        <div class="foot-hours"><span>Sun</span><b>12pm&ndash;6pm</b></div>
      </div>
    </div>

    <div class="foot-bar">
      <span>&copy; <span data-year></span> Great Escape Games Inc. Concept redesign.</span>
      <nav>
        <a href="visit.html#contact">Feedback</a>
        <a href="legal.html#terms">Terms &amp; Conditions</a>
        <a href="legal.html#privacy">Privacy Policy</a>
        <a href="proposal.html">About this proposal</a>
      </nav>
    </div>
  </div>
</footer>"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700'
         '&family=Barlow+Condensed:wght@400;500;600'
         '&family=Spectral:ital,wght@0,300;0,400;0,500;1,400&display=swap" rel="stylesheet">')


def page(slug, title, desc, body):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/img/favicon.png">
{FONTS}
<link rel="stylesheet" href="assets/css/geg.css">
</head>
<body data-page="{slug}">

{SPRITE}

{RIBBON}

{header()}

<main>
{body}
</main>

{FOOTER}

<script src="assets/js/geg.js"></script>
</body>
</html>
"""
    name = "index.html" if slug == "home" else f"{slug}.html"
    (ROOT / name).write_text(html, encoding="utf-8")
    return name


def phead(crumb, eyebrow, h1, lede, plate):
    return f"""  <section class="phead" style="background-image:url('assets/img/{plate}.jpg')">
    <div class="wrap">
      <p class="crumbs"><a href="index.html">Home</a> &rsaquo; <span>{crumb}</span></p>
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
    </div>
  </section>"""


# ============================================================== home page ===

HOME = """  <section class="hero" data-hero>
    <div class="wrap">
      <div class="hero-grid">
        <div>
          <p class="eyebrow">Sacramento &amp; Rocklin &middot; Since 1996</p>
          <h1>Pull up a chair,<em>the table&rsquo;s set.</em></h1>
          <p class="lede">Two halls, seven nights a week. Warhammer, Magic, Pok&eacute;mon, D&amp;D and a shelf of board games deep enough to lose an evening in. Come to win the tournament or come to learn which end of the dice goes up. Both get a seat.</p>
          <div class="btn-row">
            <a class="btn" href="events.html">See this week&rsquo;s events</a>
            <a class="btn btn--ghost" href="rooms.html#book">Book a private room</a>
          </div>
          <div class="hero-stats">
            <div><b>1996</b><span>Doors open since</span></div>
            <div><b>Two</b><span>Halls to play in</span></div>
            <div><b>7 nights</b><span>Every single week</span></div>
          </div>
        </div>

        <div class="hero-show">
          <div class="hero-slides">
            <div class="hero-slide" data-title="Spearhead: Fangs of the Blood God" data-sub="Blades of Khorne &middot; Age of Sigmar &middot; In stock, both halls">
              <img src="assets/img/cut/spearhead-khorne.png" alt="Spearhead: Blades of Khorne, Fangs of the Blood God boxed set">
            </div>
            <div class="hero-slide" data-title="Wolf Guard Terminators" data-sub="Space Wolves &middot; Warhammer 40,000 &middot; New release">
              <img src="assets/img/cut/wolf-guard-terminators.png" alt="Space Wolves Wolf Guard Terminators miniatures">
            </div>
            <div class="hero-slide" data-title="Kamandora&rsquo;s Blades" data-sub="Warhammer Underworlds &middot; Warband &amp; cards">
              <img src="assets/img/cut/kamandoras-blades.png" alt="Kamandora's Blades Warhammer Underworlds warband">
            </div>
            <div class="hero-slide" data-title="Paldea Adventure Chest" data-sub="Pok&eacute;mon TCG &middot; Great for a first collection">
              <img src="assets/img/cut/paldea-chest.png" alt="Pok&eacute;mon Paldea Adventure Chest">
            </div>
          </div>
          <div class="hero-cap">
            <h3 data-cap-title></h3>
            <p data-cap-text></p>
          </div>
          <div class="dots" role="group" aria-label="Featured releases"></div>
        </div>
      </div>
    </div>
  </section>

  <section class="halls" aria-label="Our locations">
    <div class="hall" data-hall-status="sacramento">
      <p class="eyebrow">Hall the First</p>
      <h3><span class="open-dot" aria-hidden="true"></span> Sacramento</h3>
      <p class="hall-hours" data-status-text></p>
      <address>1250 Howe Ave #3a, Sacramento, CA 95825</address>
      <p class="hall-hours">Mon&ndash;Thu <b>12&ndash;10</b> &middot; Fri <b>12&ndash;12</b> &middot; Sat <b>12&ndash;10</b> &middot; Sun <b>12&ndash;6</b></p>
      <div class="hall-links">
        <a class="tlink" href="events.html#sacramento">What&rsquo;s on <span>&rarr;</span></a>
        <a class="tlink" href="visit.html#sacramento">Directions <span>&rarr;</span></a>
        <a class="tlink" href="tel:19169270810">916 927 0810 <span>&rarr;</span></a>
      </div>
    </div>
    <div class="hall" data-hall-status="rocklin">
      <p class="eyebrow">Hall the Second</p>
      <h3><span class="open-dot" aria-hidden="true"></span> Rocklin</h3>
      <p class="hall-hours" data-status-text></p>
      <address>5050 Rocklin Road, Suite A22, Rocklin, CA 95677</address>
      <p class="hall-hours">Mon&ndash;Tue <b>12&ndash;7</b> &middot; Wed <b>12&ndash;9</b> &middot; Thu <b>12&ndash;10</b> &middot; Fri <b>12&ndash;11</b> &middot; Sat <b>12&ndash;10</b> &middot; Sun <b>12&ndash;6</b></p>
      <div class="hall-links">
        <a class="tlink" href="events.html#rocklin">What&rsquo;s on <span>&rarr;</span></a>
        <a class="tlink" href="visit.html#rocklin">Directions <span>&rarr;</span></a>
        <a class="tlink" href="tel:19162591797">916 259 1797 <span>&rarr;</span></a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">The Armoury</p>
        <h2>What gets played here</h2>
        <p>Six shelves, a wall of singles, and whatever you brought in a bag. If it needs dice, cards or a tape measure, odds are somebody&rsquo;s already running it.</p>
      </div>
      <div class="grid grid--3">
        CATEGORY_TILES
      </div>
    </div>
  </section>

  <section class="section section--plate">
    <div class="wrap">
      <div class="sec-head" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;max-width:none;flex-wrap:wrap">
        <div style="max-width:620px">
          <p class="eyebrow">Just through the door</p>
          <h2>New on the shelves</h2>
          <p>Fresh stock, no pre-order limbo. If it&rsquo;s listed here it&rsquo;s on a shelf in one of the two halls right now.</p>
        </div>
        <a class="tlink" href="products.html">Browse the whole shop <span>&rarr;</span></a>
      </div>
      <div class="grid grid--4">
        HOME_PRODUCTS
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head sec-head--center">
        <p class="eyebrow eyebrow--center">The Muster</p>
        <h2>What&rsquo;s on this week</h2>
        <p>Weekly locals, monthly majors, and the odd all-nighter. Newcomers are welcome at every one of them. Say so at the counter and we&rsquo;ll pair you with someone patient.</p>
      </div>
      <div class="grid grid--2">
        HOME_EVENTS
      </div>
      <div class="btn-row mt-l" style="justify-content:center">
        <a class="btn btn--ghost" href="events.html#sacramento">All Sacramento events</a>
        <a class="btn btn--ghost" href="events.html#rocklin">All Rocklin events</a>
      </div>
    </div>
  </section>

  <section class="section section--plate">
    <div class="wrap">
      <div class="grid grid--2" style="align-items:center;gap:clamp(28px,5vw,64px)">
        <div>
          <p class="eyebrow">The War Room</p>
          <h2>A room of your own</h2>
          <p class="lede">Three private rooms at Sacramento for the campaign that needs a door on it. Book by the hour or take a half-day. Table, chairs, and nobody drifting past to watch you roll a one.</p>
          <ul style="list-style:none;padding:0;margin:0 0 28px;display:flex;flex-direction:column;gap:12px">
            <li><b style="color:var(--bone)">Dragon &amp; Wolf Rooms</b><span class="muted">: $15/hour, seats six comfortably</span></li>
            <li><b style="color:var(--bone)">Party Room</b><span class="muted">: $25/hour, birthdays and big groups</span></li>
            <li><b style="color:var(--bone)">Half &amp; full days</b><span class="muted">: for the campaigns that run long</span></li>
          </ul>
          <div class="btn-row">
            <a class="btn" href="rooms.html#book">Check availability</a>
            <a class="btn btn--ghost" href="rooms.html">Room details</a>
          </div>
        </div>
        <div class="grid" style="gap:14px">
          <div class="room rev" style="background-image:url('assets/img/room-dragon.jpg');min-height:170px">
            <h3 style="margin:0">The Dragon Room</h3>
            <p class="muted small" style="margin:0">Six seats &middot; whiteboard wall &middot; a door that shuts</p>
            <p class="rate" style="font-size:1.5rem">$15 <span>/ hour</span></p>
          </div>
          <div class="room rev" style="background-image:url('assets/img/room-party.jpg');min-height:170px">
            <h3 style="margin:0">The Party Room</h3>
            <p class="muted small" style="margin:0">Twelve seats &middot; bring your own cake</p>
            <p class="rate" style="font-size:1.5rem">$25 <span>/ hour</span></p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap wrap--narrow center">
      <p class="eyebrow eyebrow--center">The Fellowship</p>
      <h2>Nobody games alone in here</h2>
      <p class="lede">Most of the people at these tables walked in the first time not knowing a soul. Ask at the counter who&rsquo;s looking for a fourth. Somebody always is.</p>
      <div class="ornament" aria-hidden="true"><i></i></div>
      <div class="grid grid--3" style="text-align:left">
        <div class="panel rev">
          <h3>New to the hobby?</h3>
          <p class="muted small">Learn-to-play runs every Sunday at both halls. Nothing to buy, nothing to bring. There are loaner armies and starter decks behind the counter.</p>
        </div>
        <div class="panel rev">
          <h3>Looking for a group?</h3>
          <p class="muted small">The Discord has a channel for every system we run, plus a looking-for-players board that actually gets used.</p>
          <p><a class="tlink" href="https://discord.com/invite/QqpvvqK" target="_blank" rel="noopener">Join the Discord <span>&rarr;</span></a></p>
        </div>
        <div class="panel rev">
          <h3>Hunting a single?</h3>
          <p class="muted small">Our card inventory is searchable and priced live. If it&rsquo;s in the case, it&rsquo;s in there.</p>
          <p><a class="tlink" href="https://greatescapegamesllc.tcgplayerpro.com/" target="_blank" rel="noopener">Open the card finder <span>&rarr;</span></a></p>
        </div>
      </div>
    </div>
  </section>

  CRIER
"""

CRIER = """<section class="section section--tight crier">
    <div class="wrap crier-in">
      <div>
        <p class="eyebrow">Word from the Crier</p>
        <h2 style="margin-bottom:10px">Know before the rest</h2>
        <p class="muted">Release dates, tournament sign-ups, and the occasional heads-up when something rare lands in the case. One email a week at most. We&rsquo;ve got games to run.</p>
      </div>
      <div>
        <form data-mock>
          <label class="is-hidden" for="crier-email">Email address</label>
          <input id="crier-email" type="email" required placeholder="you@example.com">
          <button class="btn" type="submit">Sign up</button>
        </form>
        <p class="form-said">Signed up. Watch for the confirmation in your inbox.</p>
        <p class="form-note" style="margin-top:12px">No spam, no resale. Unsubscribe any time.</p>
      </div>
    </div>
  </section>"""

CATEGORIES = [
    ("01", "Warhammer 40,000", "Open play Tuesdays and Saturdays, monthly RTTs, eight terrain tables at Rocklin.", "plate-40k", "sys-40k"),
    ("02", "Age of Sigmar", "Saturday open play and Spearhead clashes, with a crowd that will happily teach you.", "plate-aos", "sys-aos"),
    ("03", "Magic: The Gathering", "Commander twice a week, Friday Night Magic at both halls, a draft every set.", "plate-mtg", "sys-mtg"),
    ("04", "Pok&eacute;mon TCG", "League nights at both halls, Cups through the season, Juniors always welcome.", "plate-pokemon", "sys-pokemon"),
    ("05", "Dungeons &amp; Dragons", "Adventurers League every Friday, and a learn-to-play table on Sundays.", "plate-dnd", "sys-dnd"),
    ("06", "Board Games", "Game nights Monday and Saturday, plus a library you can pull anything from.", "plate-board", "sys-board"),
]


def category_tiles():
    """Tiles answer 'what gets played here', so they land on the calendar with
    that system already filtered. Every one of the six has events."""
    out = []
    for n, name, blurb, plate, anchor in CATEGORIES:
        out.append(f"""<a class="cat rev" href="events.html#{anchor}" style="background-image:url('assets/img/{plate}.jpg')">
          <span class="cat-n">{n}</span>
          <h3>{name}</h3>
          <p>{blurb}</p>
        </a>""")
    return "\n        ".join(out)


# ================================================================ products ===
# image, system label, filter tags, plate, price html, stock html, flag html
PRODUCTS = [
    ("spearhead-khorne", "Spearhead: Fangs of the Blood God", "Age of Sigmar", "cat-aos", "plate-aos", "$75.00", ("", "In stock"), "New"),
    ("wolf-guard-terminators", "Space Wolves: Wolf Guard Terminators", "Warhammer 40,000", "cat-40k", "plate-40k", "$65.00", ("is-low", "2 left at Rocklin"), "New"),
    ("kamandoras-blades", "Kamandora&rsquo;s Blades", "Warhammer Underworlds", "cat-uw", "plate-underworlds", "$45.00", ("", "In stock"), "New"),
    ("paldea-chest", "Paldea Adventure Chest", "Pok&eacute;mon TCG", "cat-pkmn", "plate-pokemon", "$49.99", ("", "In stock"), ""),
    ("biosanctic-broodsurge", "Biosanctic Broodsurge Battleforce", "Warhammer 40,000 &middot; Battleforce", "cat-40k", "plate-40k", "<s>$230.00</s>$199.00", ("is-low", "1 left"), "Deal"),
    ("battletome-khorne", "Chaos Battletome: Blades of Khorne", "Age of Sigmar &middot; Book", "cat-aos cat-book", "plate-aos", "$58.00", ("", "In stock"), ""),
    ("kharadron-dice", "Kharadron Overlords Dice", "Age of Sigmar &middot; Dice", "cat-aos", "plate-aos", "$30.00", ("", "In stock"), ""),
    ("arjac-rockfist", "Arjac Rockfist", "Warhammer 40,000 &middot; Character", "cat-40k", "plate-40k", "$40.00", ("", "In stock"), ""),
    ("red-revelation", "Regiment of Renown: The Red Revelation", "Age of Sigmar", "cat-aos", "plate-aos", "$110.00", ("", "In stock"), "New"),
    ("drop-pods", "Space Marines: Drop Pods", "Warhammer 40,000", "cat-40k", "plate-40k", "$65.00", ("", "In stock"), ""),
    ("solar-aux", "Solar Auxilia Launch Box", "The Horus Heresy", "cat-hh", "plate-neutral", "$175.00", ("is-out", "Order in, 5 days"), ""),
    ("drekkis-privateers", "Drekki&rsquo;s Privateers", "Age of Sigmar", "cat-aos", "plate-aos", "$60.00", ("", "In stock"), ""),
    ("endrin-dock", "Zontari Endrin Dock", "Age of Sigmar &middot; Terrain", "cat-aos", "plate-aos", "$50.00", ("", "In stock"), ""),
    ("datacards-space-wolves", "Datasheet Cards: Space Wolves", "Warhammer 40,000 &middot; Cards", "cat-40k cat-book", "plate-40k", "$30.00", ("", "In stock"), ""),
    ("warscrolls-kharadron", "Warscroll Cards: Kharadron Overlords", "Age of Sigmar &middot; Cards", "cat-aos cat-book", "plate-aos", "$27.50", ("", "In stock"), ""),
    ("wolf-guard-headtakers", "Wolf Guard Headtakers", "Warhammer 40,000", "cat-40k", "plate-40k", "$50.00", ("is-low", "3 left"), "New"),
    ("wolf-guard-battle-leader", "Wolf Guard Battle Leader", "Warhammer 40,000 &middot; Character", "cat-40k", "plate-40k", "$30.00", ("", "In stock"), ""),
]


def product_card(p, tagged=False):
    img, name, system, tags, plate, price, stock, flag = p
    flag_html = f'\n            <span class="pcard-flag tag tag--brass">{flag}</span>' if flag else ""
    data = f' data-tags="{tags}"' if tagged else ""
    alt = name.replace("&rsquo;", "'").replace("&middot;", "-").replace("&eacute;", "e")
    return f"""<a class="pcard rev ticked"{data} href="products.html">
          <div class="pcard-media" style="background-image:url('assets/img/{plate}.jpg')">{flag_html}
            <img src="assets/img/cut/{img}.png" alt="{alt}">
          </div>
          <div class="pcard-body">
            <p class="pcard-meta">{system}</p>
            <h3>{name}</h3>
            <div class="pcard-foot"><span class="price">{price}</span><span class="stock {stock[0]}">{stock[1]}</span></div>
          </div>
        </a>"""


# ================================================================== events ===
# date(dow, num, mon), title, hall, time, cost, extra, blurb, tags, chips
MAJORS = [
    (("Sat", "08", "Aug"), "Grand Muster: 40k RTT", "Rocklin", "10:00am", "$30 entry", "32 seats",
     "Three rounds, 2000 points, Pariah Nexus missions. Prize support out of the case, and the top table gets an audience whether it wants one or not.",
     "loc-rocklin sys-40k", [("tag--brass", "Tournament"), ("", "Warhammer 40,000")]),
    (("Sun", "09", "Aug"), "Learn to Play: D&amp;D 5e", "Sacramento", "1:00pm", "Free", "Ages 12+",
     "Two hours, pre-made characters, dice provided. You will fight one goblin and probably lose to a door.",
     "loc-sacramento sys-dnd", [("tag--free", "Free"), ("", "Dungeons &amp; Dragons")]),
    (("Sat", "15", "Aug"), "Spearhead Clash", "Rocklin", "11:00am", "$25 entry", "16 seats",
     "Small boxes, short games, four rounds finished before dinner. The right first tournament if you&rsquo;ve never sat down at one.",
     "loc-rocklin sys-aos", [("tag--brass", "Tournament"), ("", "Age of Sigmar")]),
    (("Fri", "21", "Aug"), "Midnight Commander", "Sacramento", "8:00pm", "$10 entry", "Runs till close",
     "Four hours of pods, snacks on the house, and one rule: no tutors before midnight. We don&rsquo;t enforce it, but we do judge.",
     "loc-sacramento sys-mtg", [("tag--brass", "Late night"), ("", "Magic: The Gathering")]),
    (("Sat", "22", "Aug"), "Prerelease Weekend", "Both halls", "12:00pm", "$35 entry", "Seats both days",
     "Six packs, build a forty-card deck, four rounds of Swiss. Every seat takes home the promo whether you win a single game or not.",
     "loc-sacramento loc-rocklin sys-mtg", [("tag--brass", "Prerelease"), ("", "Magic: The Gathering")]),
    (("Sun", "23", "Aug"), "Brush &amp; Basecoat: Contrast Clinic", "Sacramento", "1:00pm", "Free", "Paints provided",
     "Two hours on getting a squad table-ready without losing your weekend to it. Bring a model or borrow one of ours.",
     "loc-sacramento sys-painting", [("tag--free", "Free"), ("", "Painting")]),
    (("Sat", "29", "Aug"), "Pok&eacute;mon League Cup", "Rocklin", "11:00am", "$20 entry", "Juniors &amp; Masters",
     "Sanctioned, championship points on the line, and a Junior bracket that runs alongside so nobody sits out.",
     "loc-rocklin sys-pokemon", [("tag--brass", "Sanctioned"), ("", "Pok&eacute;mon TCG")]),
    (("Sat", "29", "Aug"), "Underworlds Grand Clash", "Sacramento", "12:00pm", "$20 entry", "24 seats",
     "Five rounds, rivals decks legal, one long afternoon of very small warbands doing very violent things.",
     "loc-sacramento sys-underworlds", [("tag--brass", "Tournament"), ("", "Warhammer Underworlds")]),
    (("Sun", "30", "Aug"), "Board Game Bring &amp; Buy", "Rocklin", "12:00pm", "Free", "Tables from 11:30",
     "Clear the shelf, fill the shelf. Bring what you&rsquo;ve stopped playing, leave with something you haven&rsquo;t.",
     "loc-rocklin sys-board", [("tag--free", "Free"), ("", "Board Games")]),
]

FRIDAY_FNM = (("Fri", "07", "Aug"), "Friday Night Magic: Modern", "Sacramento", "6:00pm", "$15 entry", "",
              "Four rounds of Swiss, packs down the standings. The kitchen-table decks turn up too, so don&rsquo;t talk yourself out of it.",
              "loc-sacramento sys-mtg", [("tag--brass", "Weekly"), ("", "Magic: The Gathering")])


def event_card(e, tagged=False):
    (dow, num, mon), title, hall, time, cost, extra, blurb, tags, chips = e
    data = f' data-tags="{tags}"' if tagged else ""
    bits = f"<b>{hall}</b> <span>{time}</span> <span>{cost}</span>"
    if extra:
        bits += f" <span>{extra}</span>"
    chip_html = "".join(f'<span class="tag {c}">{t}</span>' for c, t in chips)
    href = "events.html#" + ("sacramento" if "loc-sacramento" in tags else "rocklin")
    return f"""<a class="ecard rev"{data} href="{href}">
          <div class="ecard-date"><span class="dow">{dow}</span><span class="dnum">{num}</span><span class="mon">{mon}</span></div>
          <div class="ecard-body">
            <h3>{title}</h3>
            <p class="ecard-line">{bits}</p>
            <p>{blurb}</p>
            <div class="tag-row">{chip_html}</div>
          </div>
        </a>"""


WEEKLY_SAC = [
    ("Mon", "6:00pm", "Commander Night", "Magic: The Gathering", "Free", "Casual pods, rule zero at the table, decks to borrow."),
    ("Tue", "5:30pm", "40k Open Play", "Warhammer 40,000", "Free", "Tables and terrain held until nine. Bring any points level."),
    ("Wed", "6:00pm", "Pok&eacute;mon League", "Pok&eacute;mon TCG", "$5", "Promos while they last. Juniors very welcome."),
    ("Thu", "6:30pm", "Draft Night", "Magic: The Gathering", "$25", "Latest set, eight seats minimum, packs down the standings."),
    ("Fri", "6:00pm", "Friday Night Magic", "Magic: The Gathering", "$15", "Modern one week, Pioneer the next. Ask which."),
    ("Fri", "6:00pm", "Adventurers League", "Dungeons &amp; Dragons", "Free", "Drop-in table, characters kept behind the counter."),
    ("Sat", "11:00am", "Age of Sigmar Open Play", "Age of Sigmar", "Free", "Bring a list, find a game. Somebody will teach you."),
    ("Sat", "4:00pm", "Board Game Social", "Board Games", "Free", "Library&rsquo;s open. Ask for a recommendation."),
    ("Sun", "12:00pm", "Learn to Play", "Rotating system", "Free", "Different game every week. Nothing to bring."),
    ("Sun", "1:00pm", "Painting Table", "Hobby", "Free", "Paints and a wet palette out. Advice if you want it."),
]

WEEKLY_ROC = [
    ("Mon", "5:00pm", "Board Game Night", "Board Games", "Free", "Quiet start to the week. Long games encouraged."),
    ("Tue", "6:00pm", "Yu-Gi-Oh! Locals", "Yu-Gi-Oh!", "$10", "Advanced format, four rounds, prize packs."),
    ("Wed", "6:00pm", "Underworlds Night", "Warhammer Underworlds", "$5", "Three rounds, decks checked at the door."),
    ("Thu", "6:00pm", "Commander Night", "Magic: The Gathering", "Free", "Pods of four, precons perfectly welcome."),
    ("Fri", "6:00pm", "FNM Draft", "Magic: The Gathering", "$18", "Latest set. Sign-up sheet goes up at five."),
    ("Sat", "10:00am", "40k Open Play", "Warhammer 40,000", "Free", "Eight tables, full terrain, all day."),
    ("Sat", "2:00pm", "Lorcana Locals", "Disney Lorcana", "$10", "Four rounds, casual pace, promos on the table."),
    ("Sun", "1:00pm", "Pok&eacute;mon League", "Pok&eacute;mon TCG", "$5", "League play and trading. Bring your binder."),
]


def weekly_table(rows):
    body = "\n".join(
        f"""            <tr>
              <td class="t-day">{d}</td>
              <td class="t-time">{t}</td>
              <td><b style="color:var(--bone)">{title}</b><br><span class="muted small">{blurb}</span></td>
              <td>{system}</td>
              <td class="t-time">{cost}</td>
            </tr>""" for d, t, title, system, cost, blurb in rows)
    return f"""<div class="tbl-scroll">
        <table class="tbl">
          <thead><tr><th>Day</th><th>Time</th><th>Event</th><th>System</th><th>Entry</th></tr></thead>
          <tbody>
{body}
          </tbody>
        </table>
      </div>"""


# =================================================================== build ===

def build_home():
    body = (HOME
            .replace("CATEGORY_TILES", category_tiles())
            .replace("HOME_PRODUCTS", "\n        ".join(product_card(p) for p in PRODUCTS[:8]))
            .replace("HOME_EVENTS", "\n        ".join(event_card(e) for e in [MAJORS[0], FRIDAY_FNM, MAJORS[1], MAJORS[2]]))
            .replace("CRIER", CRIER))
    return page("home", "Great Escape Games | Tabletop, TCG &amp; Miniatures in Sacramento &amp; Rocklin",
                "Sacramento and Rocklin's tabletop hall since 1996. Warhammer, Magic: The Gathering, Pokemon, D&amp;D and board games, seven nights a week across two locations.",
                body)


def build_products():
    chips = [("all", "Everything"), ("cat-40k", "Warhammer 40,000"), ("cat-aos", "Age of Sigmar"),
             ("cat-uw", "Underworlds"), ("cat-hh", "Horus Heresy"), ("cat-pkmn", "Pok&eacute;mon"),
             ("cat-book", "Books &amp; Cards")]
    chip_html = "\n          ".join(
        f'<button class="chip{" is-on" if v == "all" else ""}" data-value="{v}">{l}</button>' for v, l in chips)
    cards = "\n        ".join(product_card(p, tagged=True) for p in PRODUCTS)

    body = phead("Shop", "The Armoury", "Everything on the shelves",
                 "Boxed sets, single models, paints, sleeves and the card case. Stock counts are per hall. If it says Rocklin, that&rsquo;s where it is. Ring ahead and we&rsquo;ll hold it for you until close.",
                 "plate-40k") + """

  <section class="section" id="shelves" data-filterable>
    <div class="wrap">
      <div style="display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;margin-bottom:22px">
        <div class="filters" data-filter-group="cat" style="margin:0">
          CHIPS
        </div>
        <p class="form-note" style="margin:0"><span data-tally></span> items shown</p>
      </div>

      <div class="grid grid--4">
        CARDS
      </div>

      <p class="panel center mt-l is-hidden" data-empty>Nothing in that category right now. Try another, or <a href="visit.html#contact">ask us to order it in</a>.</p>

      <div class="ornament" aria-hidden="true"><i></i></div>

      <div class="grid grid--2" id="card-case" style="align-items:center;gap:clamp(24px,4vw,48px)">
        <div>
          <p class="eyebrow">The Card Case</p>
          <h2>Singles, priced live</h2>
          <p>Every card in the case is listed, priced and searchable: commander staples, sealed product, the odd piece of old cardboard somebody traded in on a Tuesday. Search it from home, pick it up at the counter.</p>
          <div class="btn-row">
            <a class="btn" href="https://greatescapegamesllc.tcgplayerpro.com/" target="_blank" rel="noopener">Open the card finder</a>
          </div>
        </div>
        <div class="panel panel--dark">
          <h3>Can&rsquo;t find it?</h3>
          <p class="muted small">We order in most weeks. Tell us what you&rsquo;re after (kit, codex, box, sleeve colour) and we&rsquo;ll tell you honestly whether it&rsquo;s five days or five weeks.</p>
          <p><a class="tlink" href="visit.html#contact">Ask about a special order <span>&rarr;</span></a></p>
          <div class="ornament" style="margin-block:20px" aria-hidden="true"><i></i></div>
          <h3>Trade-ins</h3>
          <p class="muted small">Cash or store credit on cards and sealed miniatures, assessed at the counter. Credit always beats cash. That&rsquo;s the whole trick.</p>
        </div>
      </div>
    </div>
  </section>

  """ + CRIER

    body = body.replace("CHIPS", chip_html).replace("CARDS", cards)
    return page("products", "Shop | Great Escape Games",
                "Warhammer, Age of Sigmar, Pokemon, Magic singles and board games in stock across our Sacramento and Rocklin stores.",
                body)


def build_events():
    loc_buttons = "\n          ".join(
        f'<button class="chip{" is-on" if v == "all" else ""}" data-value="{v}">{l}</button>'
        for v, l in [("all", "Both halls"), ("loc-sacramento", "Sacramento"), ("loc-rocklin", "Rocklin")])
    sys_buttons = "\n          ".join(
        f'<button class="chip{" is-on" if v == "all" else ""}" data-value="{v}">{l}</button>'
        for v, l in [("all", "Everything"), ("sys-40k", "Warhammer 40,000"), ("sys-aos", "Age of Sigmar"),
                     ("sys-underworlds", "Underworlds"), ("sys-mtg", "Magic"), ("sys-pokemon", "Pok&eacute;mon"),
                     ("sys-dnd", "D&amp;D"), ("sys-board", "Board Games"), ("sys-painting", "Painting")])
    cards = "\n        ".join(event_card(e, tagged=True) for e in [FRIDAY_FNM] + MAJORS)

    body = phead("Events", "The Muster", "Every game we run",
                 "Weekly locals you can just turn up to, and the bigger days worth clearing a Saturday for. Entry fees go straight back out as prize support. Sign-ups happen at the counter or on the Discord.",
                 "plate-aos") + """

  <section class="section" data-filterable>
    <div class="wrap">
      <div class="panel panel--dark" style="margin-bottom:34px">
        <p class="eyebrow">Filter the calendar</p>
        <div class="filters" data-filter-group="loc" style="margin-bottom:14px">
          LOCS
        </div>
        <div class="filters" data-filter-group="sys" style="margin-bottom:0">
          SYSTEMS
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap;margin-bottom:20px">
        <h2 style="margin:0">Coming up</h2>
        <p class="form-note" style="margin:0"><span data-tally></span> events shown</p>
      </div>

      <div class="grid grid--2">
        CARDS
      </div>

      <p class="panel center mt-l is-hidden" data-empty>No events match that combination yet. Widen the filter, or <a href="https://discord.com/invite/QqpvvqK" target="_blank" rel="noopener">ask on the Discord</a>. Somebody&rsquo;s usually organising something.</p>
    </div>
  </section>

  <section class="section section--plate" id="sacramento">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Hall the First</p>
        <h2>Every week in Sacramento</h2>
        <p>1250 Howe Ave #3a. Turn up, put your name down, play. No entry fee unless it says so.</p>
      </div>
      WEEKLY_SAC
      <div class="btn-row mt-l">
        <a class="btn btn--ghost" href="visit.html#sacramento">Directions &amp; hours</a>
        <a class="btn btn--ghost" href="tel:19169270810">Call 916 927 0810</a>
      </div>
    </div>
  </section>

  <section class="section" id="rocklin">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Hall the Second</p>
        <h2>Every week in Rocklin</h2>
        <p>5050 Rocklin Road, Suite A22. Eight tables of terrain and the biggest 40k crowd of the two.</p>
      </div>
      WEEKLY_ROC
      <div class="btn-row mt-l">
        <a class="btn btn--ghost" href="visit.html#rocklin">Directions &amp; hours</a>
        <a class="btn btn--ghost" href="tel:19162591797">Call 916 259 1797</a>
      </div>
    </div>
  </section>

  <section class="section section--plate">
    <div class="wrap wrap--narrow">
      <div class="sec-head sec-head--center">
        <p class="eyebrow eyebrow--center">House Rules</p>
        <h2>Before you sit down</h2>
      </div>
      <div class="acc">
        <div class="acc-item">
          <button class="acc-q" type="button" aria-expanded="false">Do I need to sign up in advance? <i aria-hidden="true"></i></button>
          <div class="acc-a"><div><p>Not for weeklies. Walk in, put your name on the sheet. Tournaments with a seat cap fill up, so those are worth booking at the counter or on the Discord a few days out.</p></div></div>
        </div>
        <div class="acc-item">
          <button class="acc-q" type="button" aria-expanded="false">I&rsquo;ve never played. Can I still come? <i aria-hidden="true"></i></button>
          <div class="acc-a"><div><p>Yes, and please do. Say so when you arrive and we&rsquo;ll sit you with one of the regulars who&rsquo;s good at explaining it. Learn-to-play runs every Sunday at both halls with everything provided.</p></div></div>
        </div>
        <div class="acc-item">
          <button class="acc-q" type="button" aria-expanded="false">What does the entry fee pay for? <i aria-hidden="true"></i></button>
          <div class="acc-a"><div><p>Prize support, near enough all of it. Packs, store credit, the occasional boxed set for a first place. We&rsquo;re not making rent off tournament fees.</p></div></div>
        </div>
        <div class="acc-item">
          <button class="acc-q" type="button" aria-expanded="false">Are the tables free to use outside events? <i aria-hidden="true"></i></button>
          <div class="acc-a"><div><p>Open tables are free whenever they&rsquo;re not booked for an event. If you want a guaranteed space with a door on it, that&rsquo;s what the <a href="rooms.html">private rooms</a> are for.</p></div></div>
        </div>
        <div class="acc-item">
          <button class="acc-q" type="button" aria-expanded="false">Can I bring food and drink? <i aria-hidden="true"></i></button>
          <div class="acc-a"><div><p>Drinks with lids, yes. Food, keep it away from the cardboard and clear up after yourself. For parties in the Party Room, bring whatever you like.</p></div></div>
        </div>
      </div>
    </div>
  </section>
"""
    body = (body.replace("LOCS", loc_buttons).replace("SYSTEMS", sys_buttons).replace("CARDS", cards)
                .replace("WEEKLY_SAC", weekly_table(WEEKLY_SAC)).replace("WEEKLY_ROC", weekly_table(WEEKLY_ROC)))
    return page("events", "Events | Great Escape Games",
                "Warhammer tournaments, Friday Night Magic, Pokemon League, D&amp;D and board game nights at our Sacramento and Rocklin halls.",
                body)


def build_rooms():
    rooms = [
        ("The Dragon Room", "room-dragon", "$15", "Seats six", [
            "Six seats around one big table",
            "Whiteboard wall for the map",
            "Dimmable lighting, because of course",
            "Door shuts. That&rsquo;s the point."]),
        ("The Wolf Room", "room-wolf", "$15", "Seats six", [
            "Same size, quieter corner of the shop",
            "Shelf space for books and trays",
            "Power at the table for laptops",
            "Popular with long-running campaigns"]),
        ("The Party Room", "room-party", "$25", "Seats twelve", [
            "Twelve seats, two tables",
            "Bring your own cake and decorations",
            "Best for birthdays and big groups",
            "Book the whole afternoon if you like"]),
    ]
    cards = "\n        ".join(f"""<div class="room rev" style="background-image:url('assets/img/{img}.jpg')">
          <p class="eyebrow">{seats}</p>
          <h3>{name}</h3>
          <p class="rate">{rate} <span>/ hour</span></p>
          <ul>{"".join(f"<li>{b}</li>" for b in bullets)}</ul>
          <div class="room-foot"><a class="tlink" href="#book">Book this room <span>&rarr;</span></a></div>
        </div>""" for name, img, rate, seats, bullets in rooms)

    body = phead("Private Rooms", "The War Room", "A room with a door on it",
                 "Three private rooms at the Sacramento hall. Book one by the hour for a session, or take a half-day when the campaign needs room to breathe. Rooms are available during shop hours on the day you book.",
                 "room-dragon") + """

  <section class="section">
    <div class="wrap">
      <div class="grid grid--3">
        ROOMS
      </div>
    </div>
  </section>

  <section class="section section--plate">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow">Rates</p>
        <h2>What it costs</h2>
        <p>Hourly for a single session, blocks for anything longer. Everything below is during normal shop hours for the day you book.</p>
      </div>
      <div class="tbl-scroll">
        <table class="tbl">
          <thead><tr><th>Block</th><th>Days</th><th>Hours</th><th>Dragon / Wolf</th><th>Party Room</th></tr></thead>
          <tbody>
            <tr><td class="t-day">Hourly</td><td>Any day</td><td class="t-time">Minimum 1 hour</td><td class="t-time">$15 / hr</td><td class="t-time">$25 / hr</td></tr>
            <tr><td class="t-day">Half day</td><td>Mon, Tue, Wed, Thu, Sat</td><td class="t-time">12pm&ndash;5pm or 5pm&ndash;10pm</td><td class="t-time">$60</td><td class="t-time">$100</td></tr>
            <tr><td class="t-day">Half day</td><td>Friday</td><td class="t-time">12pm&ndash;5:30pm or 5:30pm&ndash;12am</td><td class="t-time">$60</td><td class="t-time">$100</td></tr>
            <tr><td class="t-day">Full day</td><td>Sunday</td><td class="t-time">12pm&ndash;6pm</td><td class="t-time">$80</td><td class="t-time">$140</td></tr>
          </tbody>
        </table>
      </div>
      <p class="form-note mt-l">Room bookings are valid only during the shop&rsquo;s trading hours for the day booked. Half and full-day blocks are the same price whichever room of the two you take.</p>
    </div>
  </section>

  <section class="section" id="book">
    <div class="wrap">
      <div class="grid grid--2" style="gap:clamp(28px,4vw,56px);align-items:start">
        <div>
          <p class="eyebrow">Reserve</p>
          <h2>Book a room</h2>
          <p>Tell us when and which room. We&rsquo;ll confirm by email, usually the same day, and take payment when you arrive or by card over the phone.</p>
          <div class="panel panel--dark mt-l">
            <h3 style="font-size:1.05rem">Running late?</h3>
            <p class="muted small">Call the shop. We&rsquo;ll hold the room fifteen minutes past your slot without charging for it, and longer if nobody&rsquo;s waiting.</p>
            <p class="muted small" style="margin-top:14px"><b style="color:var(--bone)">Sacramento</b>: <a href="tel:19169270810">916 927 0810</a></p>
          </div>
        </div>

        <div class="panel" data-booker>
          <form class="form-grid" data-mock>
            <div class="field">
              <label for="b-room">Room</label>
              <select id="b-room" name="room">
                <option value="Dragon">Dragon Room ($15/hr)</option>
                <option value="Wolf">Wolf Room ($15/hr)</option>
                <option value="Party">Party Room ($25/hr)</option>
              </select>
            </div>
            <div class="field">
              <label for="b-hours">Hours</label>
              <select id="b-hours" name="hours">
                <option value="1">1 hour</option>
                <option value="2">2 hours</option>
                <option value="3" selected>3 hours</option>
                <option value="4">4 hours</option>
                <option value="5">5 hours</option>
                <option value="6">6 hours</option>
              </select>
            </div>
            <div class="field">
              <label for="b-date">Date</label>
              <input id="b-date" type="date" required>
            </div>
            <div class="field">
              <label for="b-slot">Start time</label>
              <select id="b-slot">
                <option>12:00pm</option><option>1:00pm</option><option>2:00pm</option>
                <option>3:00pm</option><option>4:00pm</option><option>5:00pm</option>
                <option>6:00pm</option><option>7:00pm</option><option>8:00pm</option>
              </select>
            </div>
            <div class="field"><label for="b-first">First name</label><input id="b-first" required placeholder="Gary"></div>
            <div class="field"><label for="b-last">Last name</label><input id="b-last" required placeholder="Lane"></div>
            <div class="field span-2"><label for="b-email">Email</label><input id="b-email" type="email" required placeholder="you@example.com"></div>
            <div class="field span-2"><label for="b-phone">Phone</label><input id="b-phone" type="tel" placeholder="916 000 0000"></div>

            <div class="span-2" style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:18px;gap:16px;flex-wrap:wrap">
              <span class="form-note">Estimated total</span>
              <span class="price" style="font-size:1.7rem" data-total>$45</span>
            </div>
            <div class="span-2"><button class="btn btn--block" type="submit">Request this booking</button></div>
          </form>
          <p class="form-said">Booking requested. We&rsquo;ll confirm by email, usually the same day. Nothing has been charged.</p>
          <p class="form-note" style="margin-top:14px">Concept build: this form doesn&rsquo;t submit anywhere yet.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--plate">
    <div class="wrap wrap--narrow">
      <div class="sec-head sec-head--center">
        <p class="eyebrow eyebrow--center">Questions</p>
        <h2>The usual asks</h2>
      </div>
      <div class="acc">
        <div class="acc-item">
          <button class="acc-q" type="button" aria-expanded="false">Can we bring food in? <i aria-hidden="true"></i></button>
          <div class="acc-a"><div><p>In the Party Room, absolutely: cake, pizza, whatever the occasion calls for. In the Dragon and Wolf Rooms keep it to snacks and drinks with lids, and clear the table before you go.</p></div></div>
        </div>
        <div class="acc-item">
          <button class="acc-q" type="button" aria-expanded="false">How far ahead can I book? <i aria-hidden="true"></i></button>
          <div class="acc-a"><div><p>Up to three months out. Recurring campaign slots can be set up at the counter. A lot of groups hold the same Thursday every fortnight.</p></div></div>
        </div>
        <div class="acc-item">
          <button class="acc-q" type="button" aria-expanded="false">What if we need to cancel? <i aria-hidden="true"></i></button>
          <div class="acc-a"><div><p>Give us twenty-four hours and there&rsquo;s nothing to pay. Less than that and we&rsquo;ll ask for the first hour, because the room sat empty.</p></div></div>
        </div>
        <div class="acc-item">
          <button class="acc-q" type="button" aria-expanded="false">Do you have rooms at Rocklin? <i aria-hidden="true"></i></button>
          <div class="acc-a"><div><p>Not yet. Rocklin runs open tables only. If you need a private space, Sacramento is the one, twenty-five minutes down the 80.</p></div></div>
        </div>
      </div>
    </div>
  </section>
"""
    return page("rooms", "Private Rooms | Great Escape Games",
                "Book a private gaming room at our Sacramento store. Dragon and Wolf Rooms from $15/hour, Party Room $25/hour, hourly or half-day blocks.",
                body.replace("ROOMS", cards))


def build_about():
    body = phead("About", "Our Tale", "Thirty years of other people&rsquo;s campaigns",
                 "Great Escape Games opened in 1996 because Sacramento needed somewhere to play. That is still the whole idea, only now there are two of us.",
                 "plate-dnd") + """

  <section class="section">
    <div class="wrap">
      <div class="grid grid--2" style="gap:clamp(28px,5vw,64px);align-items:start">
        <div class="stack-lg">
          <div>
            <p class="eyebrow">How it started</p>
            <h2>One shop, one idea</h2>
            <p>Great Escape Games was founded in 1996 by Gary Lane, out of a straightforward want: somewhere dedicated for gamers to meet, dig into a system, and stay a while. An actual hall, with actual tables in it.</p>
            <p>The shelves have changed a lot since. The reason for them hasn&rsquo;t.</p>
          </div>
          <div>
            <p class="eyebrow">What we&rsquo;re for</p>
            <h2>More than a counter</h2>
            <p>We aim to be a hub as much as a store: a room where a family trying a board game on a Sunday and a player grinding for championship points on a Saturday both feel like they&rsquo;re in the right place.</p>
            <p>That means teaching tables, loaner armies, patient staff, and events priced so that turning up costs you an evening and not much else.</p>
          </div>
          <div>
            <p class="eyebrow">Two halls</p>
            <h2>Sacramento &amp; Rocklin</h2>
            <p>Sacramento on Howe Ave is the older of the two, with the private rooms and the deeper card case. Rocklin has the bigger miniatures crowd and eight tables of permanent terrain. Plenty of regulars play at both, twenty-five minutes apart down the 80.</p>
            <div class="btn-row" style="margin-top:20px">
              <a class="btn btn--ghost" href="visit.html">Find both halls</a>
              <a class="btn btn--ghost" href="events.html">See what&rsquo;s running</a>
            </div>
          </div>
        </div>

        <div class="stack-lg">
          <div class="panel">
            <p class="eyebrow">Since 1996</p>
            <h3>The short version</h3>
            <div class="tbl-scroll" style="border:0;background:none">
              <table class="tbl">
                <tbody>
                  <tr><td class="t-time">1996</td><td>Gary Lane opens the first Great Escape Games in Sacramento.</td></tr>
                  <tr><td class="t-time">2000s</td><td>Miniatures take over a wall. Then two. Then a room.</td></tr>
                  <tr><td class="t-time">2010s</td><td>Weekly TCG nights become the backbone of the calendar.</td></tr>
                  <tr><td class="t-time">Today</td><td>Two halls, seven days a week, and a Discord that never sleeps.</td></tr>
                </tbody>
              </table>
            </div>
          </div>

          <div class="panel panel--dark">
            <h3>What you&rsquo;ll find behind the counter</h3>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:12px">
              <li class="muted small">Staff who play the systems they sell, and will tell you when a box isn&rsquo;t worth it</li>
              <li class="muted small">Loaner armies and starter decks for anyone who wants to try before buying</li>
              <li class="muted small">A trade-in counter for cards and sealed miniatures</li>
              <li class="muted small">Special orders most weeks, with an honest estimate on timing</li>
            </ul>
          </div>

          <div class="room" style="background-image:url('assets/img/plate-neutral.jpg')">
            <p class="eyebrow">Come and see</p>
            <h3>Whether you&rsquo;re seasoned or curious</h3>
            <p class="muted small">Check out the shop in Sacramento or Rocklin, meet a few people, and start something. That invitation has been open for thirty years.</p>
            <div class="room-foot"><a class="tlink" href="visit.html">Plan a visit <span>&rarr;</span></a></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--plate">
    <div class="wrap wrap--narrow center">
      <div class="ornament" style="margin-top:0" aria-hidden="true"><i></i></div>
      <p class="lede" style="font-style:italic">&ldquo;Thank you for choosing Great Escape Games as your tabletop gaming destination.&rdquo;</p>
      <p class="form-note">The same line that&rsquo;s been on our About page for years, and we meant it then too</p>
      <div class="ornament" aria-hidden="true"><i></i></div>
    </div>
  </section>

  """ + CRIER
    return page("about", "About | Great Escape Games",
                "Founded in 1996 by Gary Lane, Great Escape Games is Sacramento and Rocklin's home for tabletop gaming, miniatures and trading card games.",
                body)


def build_visit():
    def hall_block(anchor, name, phone, tel, addr, maps, hours, note):
        rows = "\n".join(f"<div class='foot-hours'><span>{d}</span><b>{h}</b></div>" for d, h in hours)
        return f"""<div class="panel" id="{anchor}">
          <p class="eyebrow">{name}</p>
          <h2 style="margin-bottom:14px">{name} Hall</h2>
          <p class="muted">{note}</p>
          <div class="ornament" style="margin-block:22px" aria-hidden="true"><i></i></div>
          <p><svg width="16" height="16" style="vertical-align:-3px;color:var(--brass)"><use href="#i-pin"/></svg>
             <span style="color:var(--bone)">{addr}</span></p>
          <p><a href="tel:{tel}">{phone}</a></p>
          <div style="margin:18px 0">{rows}</div>
          <div class="btn-row">
            <a class="btn btn--sm" href="{maps}" target="_blank" rel="noopener">Open in Maps</a>
            <a class="btn btn--sm btn--ghost" href="events.html#{anchor}">What&rsquo;s on here</a>
          </div>
        </div>"""

    sac = hall_block("sacramento", "Sacramento", "916 927 0810", "19169270810",
                     "1250 Howe Ave #3a, Sacramento, CA 95825",
                     "https://www.google.com/maps/search/?api=1&query=1250+Howe+Ave+%233a+Sacramento+CA+95825",
                     [("Mon&ndash;Thu", "12pm&ndash;10pm"), ("Fri", "12pm&ndash;12am"), ("Sat", "12pm&ndash;10pm"), ("Sun", "12pm&ndash;6pm")],
                     "The older hall. Private rooms, the deeper card case, and the Friday night that runs till midnight.")
    roc = hall_block("rocklin", "Rocklin", "916 259 1797", "19162591797",
                     "5050 Rocklin Road, Suite A22, Rocklin, CA 95677",
                     "https://www.google.com/maps/search/?api=1&query=5050+Rocklin+Road+Suite+A22+Rocklin+CA+95677",
                     [("Mon&ndash;Tue", "12pm&ndash;7pm"), ("Wed", "12pm&ndash;9pm"), ("Thu", "12pm&ndash;10pm"), ("Fri", "12pm&ndash;11pm"), ("Sat", "12pm&ndash;10pm"), ("Sun", "12pm&ndash;6pm")],
                     "Eight tables of permanent terrain and the bigger miniatures crowd. Saturday is the day to come.")

    body = phead("Visit", "Find Us", "Two doors, both open",
                 "Twenty-five minutes apart. Same welcome at either. Below you&rsquo;ll find addresses, hours, a way to reach us, and the sign-in for order history and event registrations.",
                 "plate-neutral") + f"""

  <section class="section">
    <div class="wrap">
      <div class="grid grid--2">
        {sac}
        {roc}
      </div>
    </div>
  </section>

  <section class="section section--plate" id="contact">
    <div class="wrap">
      <div class="grid grid--2" style="gap:clamp(28px,4vw,56px);align-items:start">
        <div>
          <p class="eyebrow">Send word</p>
          <h2>Ask us anything</h2>
          <p>Special orders, event questions, trade-in valuations, or telling us we got something wrong. It all comes to the same inbox and a person reads it.</p>
          <p class="muted">If it&rsquo;s urgent, the phone is quicker. Somebody&rsquo;s behind the counter from noon every day.</p>
          <div class="ornament" aria-hidden="true"><i></i></div>
          <h3>Prefer to shout?</h3>
          <p class="muted small">The Discord is where most of the day-to-day happens: pick-up games, list feedback, and the occasional argument about rules interpretations.</p>
          <p><a class="tlink" href="https://discord.com/invite/QqpvvqK" target="_blank" rel="noopener">Join the Discord <span>&rarr;</span></a></p>
        </div>

        <div class="panel">
          <form class="form-grid" data-mock>
            <div class="field"><label for="c-name">Name</label><input id="c-name" required placeholder="Your name"></div>
            <div class="field"><label for="c-email">Email</label><input id="c-email" type="email" required placeholder="you@example.com"></div>
            <div class="field span-2">
              <label for="c-topic">What&rsquo;s it about?</label>
              <select id="c-topic">
                <option>General question</option>
                <option>Special order</option>
                <option>Event or tournament</option>
                <option>Private room booking</option>
                <option>Trade-in valuation</option>
                <option>Feedback</option>
              </select>
            </div>
            <div class="field span-2">
              <label for="c-hall">Which hall?</label>
              <select id="c-hall"><option>Sacramento</option><option>Rocklin</option><option>Either / not sure</option></select>
            </div>
            <div class="field span-2"><label for="c-msg">Message</label><textarea id="c-msg" required placeholder="Tell us what you need&hellip;"></textarea></div>
            <div class="span-2"><button class="btn btn--block" type="submit">Send it</button></div>
          </form>
          <p class="form-said">Message sent. We&rsquo;ll get back to you shortly. Thank you!</p>
          <p class="form-note" style="margin-top:14px">Concept build: this form doesn&rsquo;t submit anywhere yet.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="account">
    <div class="wrap">
      <div class="grid grid--2" style="gap:clamp(28px,4vw,56px);align-items:center">
        <div>
          <p class="eyebrow">Your Account</p>
          <h2>Sign in</h2>
          <p>An account keeps your event registrations, room bookings and order history in one place, and lets you hold items at the counter without ringing ahead.</p>
          <p class="muted small">Not got one? Making one takes about twenty seconds and we only ask for an email.</p>
        </div>
        <div class="panel">
          <form class="form-grid" data-mock>
            <div class="field span-2"><label for="a-email">Email</label><input id="a-email" type="email" required placeholder="you@example.com"></div>
            <div class="field span-2"><label for="a-pass">Password</label><input id="a-pass" type="password" required placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;"></div>
            <div class="span-2"><button class="btn btn--block" type="submit">Sign in</button></div>
            <div class="span-2 center"><a class="tlink" href="#account">Create an account <span>&rarr;</span></a></div>
          </form>
          <p class="form-said">Concept build: accounts aren&rsquo;t wired up in this demo.</p>
        </div>
      </div>
    </div>
  </section>

  {CRIER}
"""
    return page("visit", "Visit &amp; Contact | Great Escape Games",
                "Addresses, opening hours, phone numbers and directions for Great Escape Games in Sacramento and Rocklin, plus a contact form.",
                body)


def build_legal():
    body = phead("The Fine Print", "The Fine Print", "Terms, privacy and the rest",
                 "The unglamorous but necessary part. Short version: be decent in the shop, we&rsquo;ll look after your data, and nothing here takes away rights you already have.",
                 "plate-neutral") + """

  <section class="section">
    <div class="wrap wrap--narrow stack-lg">
      <div id="terms">
        <p class="eyebrow">Terms &amp; Conditions</p>
        <h2>Using this site</h2>
        <p>By using the Great Escape Games website you agree to these terms. If you don&rsquo;t, please don&rsquo;t use it.</p>
        <h3>Your content</h3>
        <p>Anything you submit to the site must not violate anybody else&rsquo;s rights: copyright, trademark, privacy, publicity or otherwise.</p>
        <h3>Our content</h3>
        <p>The site and its original content, features and functionality belong to Great Escape Games Inc and are protected by copyright, trademark and other intellectual property law. Product photography and game names remain the property of their respective publishers.</p>
        <h3>Liability</h3>
        <p>Great Escape Games Inc, its directors, employees, partners, agents, suppliers and affiliates are not liable for indirect, incidental, special, consequential or punitive damages, including loss of profits, data, use or goodwill, arising from your use of the site, or from the conduct or content of any third party on it.</p>
        <h3>Changes</h3>
        <p>We may revise these terms. Where a change is material we&rsquo;ll aim to give at least thirty days&rsquo; notice before it takes effect.</p>
      </div>

      <div class="ornament" aria-hidden="true"><i></i></div>

      <div id="privacy">
        <p class="eyebrow">Privacy</p>
        <h2>What we hold, and why</h2>
        <p>We collect what we need to run the shop and nothing beyond it: your name and email for orders, event registrations and room bookings; your phone number if you give it, so we can reach you about a booking.</p>
        <h3>Who sees it</h3>
        <p>Us. We don&rsquo;t sell or rent your details. Payment processing runs through our payment provider and card numbers never touch our systems.</p>
        <h3>Email</h3>
        <p>The newsletter is opt-in and every message carries an unsubscribe link that works immediately.</p>
        <h3>Getting it removed</h3>
        <p>Ask and we&rsquo;ll delete it. <a href="visit.html#contact">Send us a message</a> or say so at the counter.</p>
      </div>

      <div class="ornament" aria-hidden="true"><i></i></div>

      <div id="conduct">
        <p class="eyebrow">In the Shop</p>
        <h2>House rules</h2>
        <p>One rule, really: everybody at these tables gets to enjoy being here. Harassment of any kind ends your day with us. Cheating in an event ends your event. Look after the terrain, don&rsquo;t leave your dice in somebody else&rsquo;s tray, and tidy your table before you go.</p>
        <p class="muted small">Staff decisions on rules disputes are final on the day. Take it up with us afterwards and we&rsquo;ll happily go through it.</p>
      </div>

      <div class="panel panel--dark">
        <h3>Concept build notice</h3>
        <p class="muted small">This page is written for a design proposal and is not the store&rsquo;s live legal text. The real terms and privacy policy should be reviewed and published by Great Escape Games before launch.</p>
      </div>
    </div>
  </section>
"""
    return page("legal", "Terms, Privacy &amp; House Rules | Great Escape Games",
                "Terms and conditions, privacy policy and in-store house rules for Great Escape Games.",
                body)


def build_proposal():
    body = phead("Proposal", "The Pitch", "A new site for Great Escape Games",
                 "Every page in the menu above is real HTML you can click through on a phone or a desktop. Here&rsquo;s what changed and why.",
                 "plate-underworlds") + """

  <section class="section">
    <div class="wrap wrap--narrow stack-lg">
      <div>
        <p class="eyebrow">Where we are</p>
        <h2>The problem with the current site</h2>
        <p>The site does its job in the narrowest sense (the address is on it), but it costs the shop customers. Working through it honestly:</p>
        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:14px">
          <li class="panel panel--dark"><b style="color:var(--bone)">It doesn&rsquo;t look like a games shop.</b><br><span class="muted small">Default type, default blue, stock React layout. Nothing about it says Warhammer, Magic, or thirty years of Saturdays. A first-time visitor can&rsquo;t tell what kind of shop this is from the homepage.</span></li>
          <li class="panel panel--dark"><b style="color:var(--bone)">Events are close to invisible.</b><br><span class="muted small">The events section shows three flyers with no titles, no times and no entry fees. Events are the reason people come in, so they should be the loudest thing on the site.</span></li>
          <li class="panel panel--dark"><b style="color:var(--bone)">Two locations, one muddle.</b><br><span class="muted small">Sacramento and Rocklin keep different hours and run different games, but the site treats them as an afterthought in the footer.</span></li>
          <li class="panel panel--dark"><b style="color:var(--bone)">Mobile is an afterthought.</b><br><span class="muted small">Most people checking &ldquo;is it open&rdquo; or &ldquo;what&rsquo;s on tonight&rdquo; are doing it on a phone in a car park.</span></li>
          <li class="panel panel--dark"><b style="color:var(--bone)">Room booking is offline.</b><br><span class="muted small">The reservation system currently reads &ldquo;down for maintenance&rdquo;: a paid service the site isn&rsquo;t selling.</span></li>
        </ul>
      </div>

      <div>
        <p class="eyebrow">The approach</p>
        <h2>What this concept does differently</h2>
        <div class="grid grid--2">
          <div class="panel"><h3>Looks like the hobby</h3><p class="muted small">Dark forged palette, inscriptional display type, hairline brass rules and bevelled panels. Restrained enough to stay professional, specific enough that you know what shop you&rsquo;re in within a second.</p></div>
          <div class="panel"><h3>Events come first</h3><p class="muted small">A real calendar you can filter by hall and by system, weekly schedules laid out as tables, and every entry showing time, cost and seats.</p></div>
          <div class="panel"><h3>Both halls, everywhere</h3><p class="muted small">A location strip on the homepage shows each hall with live open/closed status calculated from actual trading hours, plus its own events and directions.</p></div>
          <div class="panel"><h3>Built mobile-first</h3><p class="muted small">Full-screen drawer navigation, tap targets sized properly, tables that scroll sideways on a phone, and no horizontal overflow anywhere.</p></div>
          <div class="panel"><h3>Rooms you can actually book</h3><p class="muted small">Three rooms with rates, a booking form with a live running total, and the half-day blocks spelled out plainly.</p></div>
          <div class="panel"><h3>Written like a person</h3><p class="muted small">Copy that sounds like the people behind the counter, with the flavour kept just this side of pastiche.</p></div>
        </div>
      </div>

      <div>
        <p class="eyebrow">Have a look</p>
        <h2>Every page in the concept</h2>
        <div class="tbl-scroll">
          <table class="tbl">
            <thead><tr><th>Page</th><th>What it covers</th><th></th></tr></thead>
            <tbody>
              <tr><td class="t-day">Home</td><td>Hero with featured releases, both halls with live hours, categories, new stock, this week&rsquo;s events, rooms, newsletter</td><td><a class="tlink" href="index.html">Open <span>&rarr;</span></a></td></tr>
              <tr><td class="t-day">Shop</td><td>Seventeen products, filterable by range, with stock per hall and a card-finder handoff</td><td><a class="tlink" href="products.html">Open <span>&rarr;</span></a></td></tr>
              <tr><td class="t-day">Events</td><td>Filterable calendar, weekly schedules for both halls, house rules</td><td><a class="tlink" href="events.html">Open <span>&rarr;</span></a></td></tr>
              <tr><td class="t-day">Private Rooms</td><td>Three rooms, full rate card, booking form with live total, FAQ</td><td><a class="tlink" href="rooms.html">Open <span>&rarr;</span></a></td></tr>
              <tr><td class="t-day">About</td><td>The 1996 story, what the shop is for, both halls</td><td><a class="tlink" href="about.html">Open <span>&rarr;</span></a></td></tr>
              <tr><td class="t-day">Visit</td><td>Addresses, hours, maps handoff, contact form, account sign-in</td><td><a class="tlink" href="visit.html">Open <span>&rarr;</span></a></td></tr>
              <tr><td class="t-day">Legal</td><td>Terms, privacy and in-store house rules</td><td><a class="tlink" href="legal.html">Open <span>&rarr;</span></a></td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div>
        <p class="eyebrow">Under the hood</p>
        <h2>How it&rsquo;s built</h2>
        <p>Static HTML, one stylesheet, one small script. No framework, no build step to deploy. It will run off any host, including the one you&rsquo;re on now. That keeps it fast on a phone and cheap to keep alive.</p>
        <div class="grid grid--2">
          <div class="panel panel--dark"><h3>Artwork</h3><p class="muted small">Product photography is official supplier imagery, cut off its white studio background so it sits on the dark plates. The atmospheric backdrops and heraldic plates behind the category tiles are generated for this build, so nothing needs licensing.</p></div>
          <div class="panel panel--dark"><h3>Accessibility</h3><p class="muted small">Contrast checked against the dark palette, visible focus rings, real landmarks and labels, and full support for reduced-motion preferences.</p></div>
        </div>
      </div>

      <div>
        <p class="eyebrow">Straight with you</p>
        <h2>What&rsquo;s real and what isn&rsquo;t</h2>
        <div class="panel">
          <p><b style="color:var(--bone)">Real:</b> both addresses, both phone numbers, all trading hours, the 1996 founding and Gary Lane, the private room rates and booking blocks, the social links, and the card finder link. All taken from your current site.</p>
          <p><b style="color:var(--bone)">Placeholder:</b> the event calendar, product prices and stock counts. They&rsquo;re plausible but invented, so the design could be judged with realistic content in it. Swap in the real schedule and pricing before this goes anywhere near customers.</p>
          <p><b style="color:var(--bone)">Not wired up:</b> forms confirm on screen but don&rsquo;t send. Accounts, payments and live inventory need a back end. That&rsquo;s the next conversation.</p>
        </div>
      </div>

      <div>
        <p class="eyebrow">Next</p>
        <h2>Where this could go</h2>
        <div class="tbl-scroll">
          <table class="tbl">
            <thead><tr><th>Stage</th><th>What happens</th></tr></thead>
            <tbody>
              <tr><td class="t-day">1. Sign-off</td><td>You pick the direction apart: palette, tone, structure. Changes are cheapest right now.</td></tr>
              <tr><td class="t-day">2. Real content</td><td>Your actual calendar, product feed, photography of the two halls and the people in them.</td></tr>
              <tr><td class="t-day">3. Back end</td><td>Events and inventory pulled from something you can edit without calling anyone. Room booking and payment reconnected.</td></tr>
              <tr><td class="t-day">4. Launch</td><td>Redirects from the old URLs, analytics, local SEO for both halls, and a handover doc.</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="panel" style="text-align:center">
        <h2 style="margin-bottom:12px">Have a click around</h2>
        <p class="muted">Resize the window, open it on your phone, break it if you can. Then tell me what&rsquo;s wrong with it.</p>
        <div class="btn-row" style="justify-content:center;margin-top:22px">
          <a class="btn" href="index.html">Start at the homepage</a>
          <a class="btn btn--ghost" href="events.html">Jump to the calendar</a>
        </div>
      </div>
    </div>
  </section>
"""
    return page("proposal", "Proposal | A new site for Great Escape Games",
                "Design proposal and concept build for a Great Escape Games website redesign.",
                body)


if __name__ == "__main__":
    for fn in (build_home, build_products, build_events, build_rooms,
               build_about, build_visit, build_legal, build_proposal):
        print("wrote", fn())
