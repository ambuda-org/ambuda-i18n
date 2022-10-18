#!/usr/bin/env python

"""Fetch the latest translation files from Transifex.

NOTE: fetching a `message.po` file takes about 5 seconds per language.
"""

import os
from pathlib import Path

import dotenv
import requests
from transifex.api import transifex_api as api


dotenv.load_dotenv()
ALLOWED_LANGUAGES = ['sa', 'mr_IN', 'te_IN', 'hi_IN']
TRANSIFEX_API_TOKEN = os.environ['TRANSIFEX_API_TOKEN']

api.setup(auth=TRANSIFEX_API_TOKEN)


def download_messages_po(resource, language):
    code: str = language.attributes['code']
    if code not in ALLOWED_LANGUAGES:
        return

    path = Path(f'translations/{code}/LC_MESSAGES/messages.po')
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    url = api.ResourceTranslationsAsyncDownload.download(resource=resource, language=language)
    text = requests.get(url).text
    path.write_text(text)

    print(f'Wrote latest data to: {path}')


def main():
    languages = api.Project.get(organization='o:ambuda', slug='ambuda').fetch('languages')
    resources = api.Resource.filter(project='o:ambuda:p:ambuda')
    assert len(resources) == 1
    resource = resources[0]

    for lang in languages:
        code = lang.attributes['code']
        if code not in ALLOWED_LANGUAGES:
            continue

        download_messages_po(resource, lang)


main()
