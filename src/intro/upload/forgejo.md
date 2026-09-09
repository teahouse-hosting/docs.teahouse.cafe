(with-forgejo)=
# ... Forejo

If you're using Git and a static site generator (or want to use them), Teahouse supports uploading directly from Forgejo Actions.


## 1. Create & configure your site

1. [Create your site](#create-site)
2. Configure your repo on the site page, set it to `INSTANCE/YOURNAME/YOURPROJECT`, making the appropriate substitions, such as: `codeberg.org/jdoe/blog-site`


## 2. Add Teahouse to your pipeline

We have written several actions to make it as easy as possible to upload from Forgejo


### Use Swiss Army Upload

[Swiss Army Upload](inv:sau#index) is our up-and-coming upload tool that's more flexible and offers more features (such as uploading to subfolders). It is, however, under active development and beta quality.

A minimal (no build step) sample might look like:

```yaml
name: Publish

on:
  push:
    branches:
      - trunk # SUBSTITUTE

concurrency:
  group: "teahouse"
  cancel-in-progress: false

jobs:
  publish:
    runs-on: my-runner # SUBSTITUTE
    enable-openid-connect: true
    steps:
    - name: Checkout
      uses: actions/checkout@v4
    - name: Upload
      uses: https://codeberg.org/teahouse/swiss-army-upload.git@trunk
      with:
        src: .
        dest: tea://example.teahouse.page/ # SUBSTITUTE
```

Note that this only attempts a build on your main branch and does not handle forks.


:::{note}

Forgejo (including actions) is under active development, and best practices may change.

:::

:::{seealso}

* [Swiss Army Upload: Teahouse Hosting](inv:sau#backend-teahouse)
* [Swiss Army Upload: Using in Actions](inv:sau#guides/actions)

:::


### Use the `teahouse-hosting/upload` Action

[`teahouse-hosting/upload`](#ref-gha-upload) is our legacy action: it's stable, will be supported forever, but is not receiving new features. While it's written for GitHub and not currently tested on Forgejo, it'll probably work.

Compared to above, the upload step becomes:

```yaml
    - name: Upload
      uses: https://github.com/teahouse-hosting/upload@trunk
      with:
        domain: example.teahouse.page # SUBSTITUTE
        root: .
```
