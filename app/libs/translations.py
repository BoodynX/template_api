"""
libs.strings

By default, uses `en-gb.json` file inside the `strings` top-level folder.

If language changes, set `libs.strings.default_locale` and run `libs.strings.refresh()`.
"""
import json

default_locale = "en-us"
supported_locales = ("en-us",)
cached_strings = {}


def refresh(locale: str = default_locale):
    if locale not in supported_locales:
        raise ValueError

    global cached_strings
    with open(f"lang/{locale}.json") as file:
        cached_strings = json.load(file)


def gettext(name):
    return cached_strings[name]
