# dev-review

## installation / development
This repository is automatically built from [markdown](https://commonmark.org/) files by [Hugo](https://gohugo.io/) using [GitHub Actions](https://github.com/features/actions).

This site uses the Hugo [LoveIt](https://hugoloveit.com/) theme.

This site is available here:
https://researchcodereviewcommunity.github.io/dev-review/

<!-- Removed this, pending agreement that we should. https://researchcodereviewcommunity.github.io/ -->

The following branches are important:

- `main`: the markdown files corresponding to the current live version of the website
- `gh-pages`: the static html site, automatically built by Hugo on new commits to `main` by [this script](.github/workflows/deploy.yml)

:warning: **Do not commit directly to `main` or `gh-pages`.** :warning:
Instead, commit changes to any other branch and open a pull request.
Once your changes are merged into `main` the site will be automatically built and deployed and will be live roughly 1 minute later.

## Previewing changes locally

1. Install hugo extended ([installation
   instructions](https://gohugo.io/getting-started/installing)). The
   "extended" hugo version is required to enable some features of [the
   LoveIt theme](https://hugoloveit.com/), such as mermaid diagrams.

2. Clone this repo

	```
	git clone --recurse-submodules git@github.com:ResearchCodeReviewCommunity/dev-review.git
	```
	
	If you've cloned this repo before without the `--recurse-submodules` options, initialise your local git submodule config with
	
	```
	git submodule init
	```
	
	and update:
	
	```
	git submodule update
	```
	
3. Build and serve the website locally

	```
	cd site/ && hugo serve --disableFastRender
	```
	
	The `disableFastRender` option is required to render some features
    brought by the LoveIt theme, such as mermaid diagrams. See [Launching the website locally (hugoloveit.com)](https://hugoloveit.com/theme-documentation-basics/#25-launching-the-website-locally).
