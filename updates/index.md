---
layout: page
title: Updates
permalink: /updates/
description: "Jack's projects, and the email updates he sends out."
---

## Projects

{% assign projects = site.pages | where_exp: "p", "p.url contains '/projects/'" | where_exp: "p", "p.order" | where_exp: "p", "p.exclude != true" | sort: "order" %}
<ul class="file-list">
{% for p in projects %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>: {{ p.description | slice: 0 | upcase }}{{ p.description | slice: 1, 500 }}</li>
{% endfor %}
</ul>

## Updates

{% assign this_url = page.url %}
{% assign updates = site.pages | where_exp: "p", "p.url contains '/updates/'" | where_exp: "p", "p.url != this_url" | where_exp: "p", "p.exclude != true" | sort: "date" | reverse %}
{% if updates.size > 0 %}
<ul class="file-list">
{% for p in updates %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>{% if p.date %} <span class="file-date">({{ p.date | date: "%B, %Y" }})</span>{% endif %}</li>
{% endfor %}
</ul>
{% else %}
<p>Coming soon.</p>
{% endif %}
