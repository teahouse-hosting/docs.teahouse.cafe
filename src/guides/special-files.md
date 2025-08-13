# Special Files

Teahouse tries to keep its serving pretty thin--what you upload is what is served. But there are some special files that are used sometimes.

## Directory Indexing

When serving a website, Teahouse will check for several options:

* The path as-is
* The path with `index.html`
* The path with `index.txt`

## Error pages

In case that no page can be found, Teahouse will look for a `_404.html` page in your site and serve that as the error page.

If there isn't a `_404.html`, a default error page will be served.
