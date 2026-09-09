(with-local)=
# ... Local Files

If you're not using Git, or you'd rather just run your static site builds locally, Teahouse supports uploading from your own computer through [Swiss Army Upload](inv:sau#index). This assumes that you're familiar with terminals & shells and installing Python packages.

:::{seealso}

* [Swiss Army Upload: Running Locally](inv:sau#guides/local)

:::


## 0. Install Swiss Army Upload

Follow the [installation instructions](inv:sau#guides/install).


## 1. Create & configure your site

[Create your site](#create-site)


## 2. Log In to Teahouse

You have to give Swiss Army Upload your Teahouse credentials:

```
$ swiss-army-upload login tea://
Teahouse email:
Teahouse password:
```

Swiss Army Upload uses your platform's secure storage, so your credentials are not lying around openly.


## 3. Upload Your Files

```
$ swiss-army-upload sync ./mysite/output tea://my.site.example/
```
