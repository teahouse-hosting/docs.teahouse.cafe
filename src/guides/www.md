# WWW Handling

It used to be common for websites to start with `www` (eg `www.google.com`). But as time went on, we collectively dropped it (eg `reddit.com`). But its legacy lives on in user habits and browser algorithms.

Teahouse handles this intelligently. You create your sites with your preferred form (with or without `www`), and Teahouse will automatically redirect.

To be specific:

* If your site is `mysite.example`, it'll be hosted at `mysite.example` and `www.mysite.example` will redirect to it.
* If your site is `www.mysite.example`, it'll be hosted at `www.mysite.example` and `mysite.example` will redirect to it.
* If you have two sites at `mysite.example` and `www.mysite.example`, both will be served and neither will redirect.

No other subdomains are handled this way--there's no special relationship between `project.example` and `docs.project.example` for example.
