# dev-review

## installation / development
This repository is automatically built from [markdown](https://commonmark.org/) files by [Hugo](https://gohugo.io/) using [GitHub Actions](https://github.com/features/actions).

This site uses the Hugo [LoveIt](https://hugoloveit.com/) theme.

This site is available here:
https://researchcodereviewcommunity.github.io/

The following branches are important:

- `main`: the markdown files corresponding to the current live version of the website
- `gh-pages`: the static html site, automatically built by Hugo on new commits to `main` by [this script](.github/workflows/deploy.yml)

:warning: **Do not commit directly to `main` or `gh-pages`.** :warning:
Instead, commit changes to any other branch and open a pull request.
Once your changes are merged into `main` the site will be automatically built and deployed and will be live roughly 1 minute later.

## Previewing changes locally

Install hugo:

- macOS
  ```
  $ brew install hugo
  ```

- Windows
  ```
  $ choco install hugo -confirm
  ```
