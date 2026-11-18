---
layout: page
title: Home
hide_title: true
end_signup: true
feed: true
og_title: Welcome to my website
description: "Jack Skidmore thinks about how people coordinate to accomplish goals."
---

<div class="home-intro" markdown="1">
- Featured: <span class="nowrap">[Why does power accumulate and corrupt?](/essays/power-part-1/)<span class="sep">|</span></span> <span class="nowrap">[Who are the gatekeepers?](/essays/gatekeepers/)<span class="sep">|</span></span> [Who is the greatest?](/prayers/who-is-the-greatest/)
- Send me an email at <span class="copy-email" data-email="hello@jackskidmore.com" role="button" tabindex="0" title="Click to copy"><!--email_off-->hello@jackskidmore.com<!--/email_off--></span>
- Otherwise, read my latest ~quarterly emails below.
</div>

{% comment %}
  Every file in updates/ with a date shows up here automatically, newest first.
  The first `per` are built into the page; the rest load from their own pages as you scroll.
{% endcomment %}
{% assign updates = site.pages | where_exp: "p", "p.url contains '/updates/'" | where_exp: "p", "p.date" | where_exp: "p", "p.exclude != true" | sort: "date" | reverse %}
{% assign per = 5 %}
<div class="feed" data-per="{{ per }}">
{% for p in updates limit: per %}
  {% unless forloop.first %}{% include feed-divider.html %}{% endunless %}
  {% comment %}
    Several updates share this page, so heading ids (and the in-update links to them,
    plus footnotes) get the update's slug as a prefix; otherwise two updates with a
    "Story time" section would collide. feed-loader.html does the same for loaded ones.
  {% endcomment %}
  {% assign slug = p.url | split: '/' | last %}
  {% assign id_prefix = 'id="' | append: slug | append: '--' %}
  {% assign href_prefix = 'href="#' | append: slug | append: '--' %}
  <section class="feed-entry" id="{{ slug }}" data-slug="{{ slug }}">
    <h1><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h1>
    <p class="page-date">{{ p.date | date: "%B, %Y" }}</p>
    {{ p.content | markdownify | replace: 'id="', id_prefix | replace: 'href="#', href_prefix }}
  </section>
{% endfor %}
</div>
{% if updates.size > per %}
<div class="feed-more" data-urls='[{% for p in updates offset: per %}"{{ p.url | relative_url }}"{% unless forloop.last %},{% endunless %}{% endfor %}]'>
  <a href="{{ '/writing/#updates' | relative_url }}">Older updates →</a>
</div>
<template id="feed-divider">{% include feed-divider.html %}</template>
{% include feed-loader.html %}
{% endif %}
