# Files in Teahouse

The file model in Teahouse is like this:

* Files exist
* Files have data and arbitrary metadata (aka headers)
* Directories don't really exist, but can be implied by the existance of files within them
* A "directory" can be a file (eg, it's allowed to have `/page` and `/page/more`)
* There is no concept of wildcards or pattern matching

Note that it is possible to construct sites in Teahouse that are not directly representable on your file system

Most headers set on files are respected and served to clients, except those that can impact serving. These exceptions can include protocol impacting headers like `Connection` & `Keep-Alive` (aka hop-by-hop), cache control headers, authentication headers, and some metadata headers like `Server`.

:::{note}
Teahouse itself does not generate a `Content-Type` header, but most upload tools will implicitly set one.
:::

## The `Status-Code` Header

One header is handled special: `Status-Code`. This is Teahouse-defined, and overrides the status code returned. The syntax is either `<code>` or `<code> <reason>`. Teahouse respects this on {ref}`error-pages`.

Some uses include:

* HTTP Redirects
* Single-Page Applications
* Producing `410 Gone` or `451 Unavailable For Legal Reasons`

Note that similiar to headers, some status codes are disallowed because they would impact the connection (eg, the entire 1xx block).
