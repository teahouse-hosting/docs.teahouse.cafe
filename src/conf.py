# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Teahouse'
copyright = '2025, Teahouse Hosting'
author = 'Teahouse Hosting'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxext.opengraph",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#attributes
    # Allows adding HTML attributes to a {} annotation
    "attrs_inline",

    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#code-fences-using-colons
    # Allows use of ::: for fenced blocks
    "colon_fence",

    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#definition-lists
    # Adds syntax for definition lists
    "deflist",

    # "fieldlist",

    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#typography
    # These two add typographic post-processing
    # "replacements",
    # "smartquotes",

    # Produces a warning
    # "strikethrough",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_logo = "_static/logo.svg"

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "oklch(39.95% 0.1021 342.07)",
        # "color-brand-content": "#CC3333",
    },
}

html_theme_options = {
    "source_repository": "https://github.com/teahouse-hosting/docs.teahouse.cafe",
    "source_branch": "trunk",
    "source_directory": "src/",
}
