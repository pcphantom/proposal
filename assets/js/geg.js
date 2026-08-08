/* ==========================================================================
   Great Escape Games front-end behaviour
   Concept build: no back end. Forms confirm locally, catalogue and calendar
   are static markup filtered in the browser.
   Each block is gated on the element it drives, so a page only runs what it has.
   ========================================================================== */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* --------------------------------------------------------- trading hours */
  /* index 0 = Sunday. [opening hour, closing hour] on a 24h clock. */
  var HOURS = {
    sacramento: [[12, 18], [12, 22], [12, 22], [12, 22], [12, 22], [12, 24], [12, 22]],
    rocklin:    [[12, 18], [12, 19], [12, 19], [12, 21], [12, 22], [12, 23], [12, 22]]
  };

  function clockLabel(h) {
    if (h === 24) return "midnight";
    var suffix = h >= 12 ? "pm" : "am";
    var display = h % 12 === 0 ? 12 : h % 12;
    return display + suffix;
  }

  function hallStatus(hall) {
    var now = new Date();
    var span = HOURS[hall][now.getDay()];
    var minutes = now.getHours() * 60 + now.getMinutes();
    var open = minutes >= span[0] * 60 && minutes < span[1] * 60;
    return {
      open: open,
      text: open
        ? "Open now, doors close at " + clockLabel(span[1])
        : "Closed, opens " + clockLabel(span[0]) + (minutes >= span[1] * 60 ? " tomorrow" : " today")
    };
  }

  document.querySelectorAll("[data-hall-status]").forEach(function (el) {
    var status = hallStatus(el.getAttribute("data-hall-status"));
    var dot = el.querySelector(".open-dot");
    var label = el.querySelector("[data-status-text]");
    if (!status.open) dot.classList.add("is-shut");
    label.textContent = status.text;
  });

  /* --------------------------------------------------------- sticky header */
  var head = document.querySelector(".site-head");
  var onScroll = function () {
    head.classList.toggle("is-stuck", window.scrollY > 24);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* --------------------------------------------------------- mobile drawer */
  var drawer = document.querySelector("[data-drawer]");
  var openDrawer = document.querySelector("[data-drawer-open]");
  var closeDrawer = document.querySelector("[data-drawer-close]");

  function setDrawer(state) {
    drawer.classList.toggle("is-open", state);
    document.body.classList.toggle("is-locked", state);
    openDrawer.setAttribute("aria-expanded", String(state));
  }
  openDrawer.addEventListener("click", function () { setDrawer(true); });
  closeDrawer.addEventListener("click", function () { setDrawer(false); });
  drawer.querySelectorAll("a").forEach(function (a) {
    a.addEventListener("click", function () { setDrawer(false); });
  });

  /* --------------------------------------------------------- search drawer */
  var search = document.querySelector("[data-search]");
  var searchToggle = document.querySelector("[data-search-open]");
  var searchInput = search.querySelector("input");

  function setSearch(state) {
    search.classList.toggle("is-open", state);
    searchToggle.setAttribute("aria-expanded", String(state));
    if (state) searchInput.focus();
  }
  searchToggle.addEventListener("click", function () {
    setSearch(!search.classList.contains("is-open"));
  });
  search.querySelector("[data-search-close]").addEventListener("click", function () {
    setSearch(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      setSearch(false);
      setDrawer(false);
    }
  });

  /* ------------------------------------------------------------- reveals */
  var revealables = document.querySelectorAll(".rev");
  if (revealables.length && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    revealables.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 70 + "ms";
      io.observe(el);
    });
  } else {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ------------------------------------------------------- hero carousel */
  var hero = document.querySelector("[data-hero]");
  if (hero) {
    var slides = Array.prototype.slice.call(hero.querySelectorAll(".hero-slide"));
    var capTitle = hero.querySelector("[data-cap-title]");
    var capText = hero.querySelector("[data-cap-text]");
    var dotWrap = hero.querySelector(".dots");
    var current = 0;
    var timer = null;

    slides.forEach(function (slide, i) {
      var dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("aria-label", "Show release " + (i + 1));
      dot.addEventListener("click", function () { show(i); restart(); });
      dotWrap.appendChild(dot);
    });
    var dots = Array.prototype.slice.call(dotWrap.children);

    function show(i) {
      current = i;
      slides.forEach(function (s, n) { s.classList.toggle("is-on", n === i); });
      dots.forEach(function (d, n) { d.classList.toggle("is-on", n === i); });
      capTitle.textContent = slides[i].getAttribute("data-title");
      capText.textContent = slides[i].getAttribute("data-sub");
    }
    function restart() {
      window.clearInterval(timer);
      if (!reduceMotion) timer = window.setInterval(function () { show((current + 1) % slides.length); }, 5600);
    }
    hero.addEventListener("mouseenter", function () { window.clearInterval(timer); });
    hero.addEventListener("mouseleave", restart);

    show(0);
    restart();
  }

  /* ------------------------------------------------------ filtered lists */
  /* Used by the calendar (location + system) and the shop (category). */
  document.querySelectorAll("[data-filterable]").forEach(function (root) {
    var items = Array.prototype.slice.call(root.querySelectorAll("[data-tags]"));
    var groups = Array.prototype.slice.call(root.querySelectorAll("[data-filter-group]"));
    var tally = root.querySelector("[data-tally]");
    var empty = root.querySelector("[data-empty]");
    var picked = {};

    /* A hash such as #sys-40k arrives from the home page tiles and preselects
       that button, so the tile lands on an already-filtered calendar. */
    var fromHash = window.location.hash.slice(1);

    groups.forEach(function (group) {
      var key = group.getAttribute("data-filter-group");
      picked[key] = "all";
      group.querySelectorAll("button").forEach(function (btn) {
        var value = btn.getAttribute("data-value");
        if (value === fromHash) {
          picked[key] = value;
          group.querySelectorAll("button").forEach(function (b) {
            b.classList.toggle("is-on", b === btn);
          });
        }
        btn.addEventListener("click", function () {
          picked[key] = value;
          group.querySelectorAll("button").forEach(function (b) {
            b.classList.toggle("is-on", b === btn);
          });
          apply();
        });
      });
    });

    function apply() {
      var shown = 0;
      items.forEach(function (item) {
        var tags = item.getAttribute("data-tags").split(" ");
        var keep = Object.keys(picked).every(function (key) {
          return picked[key] === "all" || tags.indexOf(picked[key]) > -1;
        });
        item.classList.toggle("is-hidden", !keep);
        if (keep) shown++;
      });
      if (tally) tally.textContent = shown;
      if (empty) empty.classList.toggle("is-hidden", shown > 0);
    }
    apply();
  });

  /* ---------------------------------------------------------- accordions */
  document.querySelectorAll(".acc-q").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.parentElement;
      var isOpen = item.classList.contains("is-open");
      item.classList.toggle("is-open", !isOpen);
      btn.setAttribute("aria-expanded", String(!isOpen));
    });
  });

  /* ------------------------------------------------- room booking mock-up */
  var booker = document.querySelector("[data-booker]");
  if (booker) {
    var RATES = { Dragon: 15, Wolf: 15, Party: 25 };
    var roomPick = booker.querySelector("[name=room]");
    var hoursPick = booker.querySelector("[name=hours]");
    var total = booker.querySelector("[data-total]");

    function retally() {
      var rate = RATES[roomPick.value];
      total.textContent = "$" + rate * Number(hoursPick.value);
    }
    roomPick.addEventListener("change", retally);
    hoursPick.addEventListener("change", retally);
    retally();
  }

  /* ------------------------------------------------------- mock-up forms */
  document.querySelectorAll("form[data-mock]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var said = form.parentElement.querySelector(".form-said");
      said.classList.add("is-on");
      form.reset();
      said.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "center" });
    });
  });

  /* ------------------------------------------------- current page in nav */
  var here = document.body.getAttribute("data-page");
  document.querySelectorAll("[data-nav]").forEach(function (link) {
    if (link.getAttribute("data-nav") === here) link.classList.add("is-here");
  });

  /* ------------------------------------------------------------- footer */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
