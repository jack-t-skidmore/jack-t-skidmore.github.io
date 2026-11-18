---
layout: page
title: Writing
permalink: /writing/
description: "Jack's essays on how people coordinate to accomplish goals. Prayers Jack has written for church liturgy and personal devotion."
---

<div class="writing-columns">
{% assign sections = "essays,prayers,updates" | split: "," %}
{% for section in sections %}
  {% assign dir = '/' | append: section | append: '/' %}
  {% assign items = site.pages | where_exp: "p", "p.path contains section" | where_exp: "p", "p.url != dir" | where_exp: "p", "p.date" | where_exp: "p", "p.exclude != true" | sort: "date" | reverse %}
  <section id="{{ section }}" class="writing-column">
    <h2>{{ section | capitalize }}</h2>
    <ul class="file-list">
    {% for p in items %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a> <span class="file-date">({{ p.date | date: "%B, %Y" }})</span></li>
    {% endfor %}
    </ul>
  </section>
{% endfor %}

  {% assign projects = site.pages | where_exp: "p", "p.url contains '/projects/'" | where_exp: "p", "p.order" | where_exp: "p", "p.exclude != true" | sort: "order" %}
  <section id="projects" class="writing-column">
    <h2>Projects</h2>
    <ul class="file-list">
    {% for p in projects %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>: {{ p.description | slice: 0 | upcase }}{{ p.description | slice: 1, 500 }}</li>
    {% endfor %}
    </ul>
  </section>
</div>
