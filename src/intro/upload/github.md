(with-github)=
# ... GitHub

If you're using Git and a static site generator (or want to use them), Teahouse supports uploading directly from GitHub Actions.


## 1. Create & configure your site

1. [Create your site](#create-site)
2. Configure your repo on the site page, set it to `github.com/YOURNAME/YOURPROJECT` (making the appropriate substitions)


## 2. Add Teahouse to your pipeline

We have written several actions to make it as easy as possible to upload from GitHub Actions

### Use the `teahouse-hosting/upload` Action

[`teahouse-hosting/upload`](#ref-gha-upload) is our legacy action: it's stable, will be supported forever, but is not receiving new features.

A minimal (no build step) sample might look like:

```yaml
name: Publish

on:
  push:
    branches:
      - trunk # SUBSTITUTE

env:
  DOMAIN: example.teahouse.page # SUBSTITUTE

permissions:
  id-token: write # This is required for requesting the JWT
  contents: read  # This is required for actions/checkout

concurrency:
  group: "teahouse"
  cancel-in-progress: false

jobs:
  publish:
    environment:
      name: teahouse
      url: "https://${{ env.DOMAIN }}"
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v4
    - name: Upload
      uses: teahouse-hosting/upload@trunk
      with:
        domain: ${{ env.DOMAIN }}
        root: .

```

Note that this only attempts a build on your main branch and does not handle forks. A more full-featured example can be found in [this site's own repo](https://github.com/teahouse-hosting/docs.teahouse.cafe/blob/trunk/.github/workflows/publish.yml). More details about how the action works can be found in the [reference docs](#ref-gha).

### Use Swiss Army Upload

[Swiss Army Upload](inv:sau#index) is our up-and-coming upload tool that's more flexible and offers more features (such as uploading to subfolders). It is, however, under active development and beta quality.

Compared to the above, the upload step becomes:

```yaml
    - name: Upload
      uses: teahouse-hosting/swiss-army-upload@trunk
      with:
        src: .
        dest: tea://${{ env.DOMAIN }}/
```

:::{seealso}

* [Swiss Army Upload: Teahouse Hosting](inv:sau#backend-teahouse)
* [Swiss Army Upload: Using in Actions](inv:sau#guides/actions)

:::
