---
layout: page
title: Projects
permalink: /projects/
description: "Jack's various projects he's working on."
---
{% assign projects = site.pages | where_exp: "p", "p.url contains '/projects/'" | where_exp: "p", "p.order" | sort: "order" %}
<ul class="file-list">
{% for p in projects %}
  {% unless p.exclude %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>: {{ p.description | slice: 0 | upcase }}{{ p.description | slice: 1, 500 }}</li>
  {% endunless %}
{% endfor %}
</ul>