(ref-gha)=
# GitHub Actions

Teahouse provides several Actions to make it easier to upload.

## Authentication

All authentication is handled by ephemeral token:

* You tell us what repos can access what sites
* GitHub generates an OIDC/JWT token
* Workflows use that token to authenticate with Teahouse
* Teahouse reads the token, verifies it came from GitHub, and compares it to the list of known repos.

Because of this, all actions require the `id-token: write` permission.


(ref-gha-upload)=
## `teahouse-hosting/upload`

This is an "all in one" action that covers the standard case where a single repo has exclusive access to a website, and each build is the entire website.

Inputs:

* `domain` (required): The domain name of the website to upload to.
* `root` (optional): The root directory to upload, such as your build output directory. Defaults to the project root.


This will delete old files and update everything.


(ref-gha-configure-s3)=
## `teahouse-hosting/configure-s3`

If you're doing something advanced, `configure-s3` gives you access to an S3
endpoint and allows you to bring your own S3 client.

Inputs:

* `domain` (required): The domain name of the website you want to interact with.

Outputs:

* `bucket`: The name of the bucket that contains the website.

In addition, `configure-s3` will set some number of `AWS_*` environment variables to provide credentials and configuration. Secret masking is also configured. In addition authentication data (eg, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or `AWS_SESSION_TOKEN`), this can include configuration data like `AWS_REGION` or `AWS_ENDPOINT_URL_S3`.

The provided credentials are valid for about an hour.

Note that all specifics are implementation details and may change without notice in the future. This includes bucket naming schemes, S3 endpoints, and exactly which environment variables are set.
