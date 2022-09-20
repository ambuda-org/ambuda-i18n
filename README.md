`ambuda` i18n files
===================

This repository contains translation files (`.po` files) that define how to
internalize the Ambuda application (`https://github.com/ambuda-org/ambuda`). We
store these files outside of the main repo because doing makes it easier for us
to ship updates to the underlying translation files.

- Before this repo, updates require manual intervention through PRs. This
  workflow favors big & slow updates over fast & frequent updates, which
  increases the turnaround for adding new translation data.

- The webserver works fine if no translation data is found -- it just shows
  English, which is workable for development. So, the app isn't broken if that
  data is missing.

- We can use Transifex's APIs to both push new translation requests to
  Transifex and update the repo with changes. This will let us keep our
  translation data up to date without spamming the repo log.
