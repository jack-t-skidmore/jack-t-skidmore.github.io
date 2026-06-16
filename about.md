---
layout: page
title: About
permalink: /about/
description: "Jack works on and writes about how people coordinate to accomplish goals."
---

This is a place to think out loud. Having a place to share my thoughts helps me complete them. I am curious about how people coordinate to accomplish goals. This is what I work on and write about.

There are a few ways to **[support my work](/support/)**.

You're welcome to email me: hello@jackskidmore.com

# Projects {#projects}

What I work on:

{% assign projects = site.pages | where_exp: "p", "p.url contains '/projects/'" | sort: "date" | reverse %}
<ul class="file-list">
{% for p in projects %}
  {% unless p.url == '/projects/' or p.exclude %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a> — {{ p.description }}</li>
  {% endunless %}
{% endfor %}
</ul>