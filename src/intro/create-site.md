(create-site)=
# Create Your Site

When initially creating your site in Teahouse, some configuration needs to happen.

This guide assumes you have a domain registrar and DNS host (often the same company).


## Own a domain

If you already own a domain, you're all set.

If you do not have a domain, you will need to purchase one from your registrar.


## Create in Teahouse

1. Have a Teahouse account with billing configured.
2. Open to <https://counter.teahouse.cafe/sites/>.
3. Follow the form to create you site.


## Configure DNS

The specifics will vary by host, but some guidance is provided below.

* `ALIAS`/`ANAME` is the preferred way. It is most compatible and most flexible to future changes we make. Unfortunately, it is not universally implemented.
* `CNAME` is acceptable, but it has caveats. It is almost always implemented, but not usable in all cases.
* `A` & `AAAA` will work in all cases, but requires more careful configuration and may require updates in the future.

:::{tab} With ALIAS/ANAME

If your host supports `ALIAS`/`ANAME` records, then use that to point your desired site domain to `ingress.teahouse.computer`.

```{warning}
AWS Route53 purports to support aliasing, but this only works if the target is also in Route53. Teahouse does not support this yet.
```
:::

:::{tab} With CNAME

If your host does not support an alias feature, and the desired site is not an apex domain, you can use a `CNAME` instead.

An apex domain is the domain actually purchased, instead of a subdomain. `mysite.com` is an apex domain, `demo.mysite.com` is not an apex.

Most DNS hosts support `CNAME`.

Create a `CNAME` record at your desired site domain pointing to `ingress.teahouse.computer`.
:::

:::{tab} With A/AAAA

If neither of the above options work for you, you can manually create the necessary `A` and `AAAA` records.

Note that while Teahouse will try to keep these IPs constant, we are an alpha service and may be forced to change these in the future.

The `A` record needs to point to `149.248.197.131`. The `AAAA` record will point to `2a09:8280:1::47:6903:0`. Please set both.
:::


## SSL/TLS

No additional configuration needs to be done for SSL/TLS. It is enabled and managed automatically for all sites.
