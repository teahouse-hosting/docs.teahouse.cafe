(with-git)=
# I Have a Git Repo

If you're using Git and a static site generator (or want to use them), Teahouse supports uploading directly from CI/CD.

Currently, we support these CI/CD providers:

* GitHub Actions


## 1. Create & configure your site

1. {ref}`Create your site <create-site>`
2. Configure your repo on the site page, set it to `github.com/YOURNAME/YOURPROJECT` (making the appropriate substitions)


## 2. Add Teahouse to your pipeline

:::{tab} GitHub Actions

We have written several actions to make it as easy as possible to upload from GitHub Actions

A minimal (no build step) sample might look like:

```yaml
name: Publish

on:
  push:
    branches:
      - trunk

env:
  DOMAIN: example.teahouse.page

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

Note that this only attempts a build on your main branch and does not handle forks. A more full-featured example can be found in [this site's own repo](https://github.com/teahouse-hosting/docs.teahouse.cafe/blob/trunk/.github/workflows/publish.yml). More details about how the action works can be found in the {ref}`reference docs <ref-gha>`

:::


:::{tab} Other

At this time, we do not have authentication options for other CI/CD sytems. We are looking to add them in the future.

:::
