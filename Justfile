set windows-powershell := true

SPHINXOPTS    := ""
SOURCEDIR     := "src"
BUILDDIR      := "build"


# Show this help
@help:
  just --list


# Show sphinx help
sphinx-help:
  just build help


# Set up dev environments
install:
  poetry install
  pre-commit install


# Run sphinx autobuild against the docs.
serve:
  poetry run sphinx-autobuild --nitpicky --port 0 --open-browser "{{SOURCEDIR}}" "{{BUILDDIR}}/html"


# Do a sphinx build
build KIND="html":
  poetry run sphinx-build -M {{KIND}} "{{SOURCEDIR}}" "{{BUILDDIR}}" {{SPHINXOPTS}}


linkcheck:
  just build linkcheck


# Clean up built files
@clean:
  just build clean
