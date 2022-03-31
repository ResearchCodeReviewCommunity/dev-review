# Code Review During Development

This repository is automatically built from [markdown](https://commonmark.org/) files by [Hugo](https://gohugo.io/) using [GitHub Actions](https://github.com/features/actions).
This site uses the Hugo [LoveIt](https://hugoloveit.com/) theme.
This site is available here: https://researchcodereviewcommunity.github.io/dev-review/

The following branches in this repository are important: 
- `main`: the markdown files corresponding to the current live version of the website
- `gh-pages`: the static html site, automatically built by Hugo on new commits to `main` by [this script](.github/workflows/deploy.yml)

## Dependencies
Install hugo extended dependency. 
The "extended" hugo version is required to enable some features of [the LoveIt theme](https://hugoloveit.com/), such as mermaid diagrams.
See commands to install hugo based on your Operating system.
- macOS
```
brew install hugo
```
- Windows
```
choco install hugo -confirm
```
- GNU/Linux (Debian and Ubuntu)
```
snap install hugo --channel=extended
```

See [documentation](https://gohugo.io/getting-started/installing/) for other options and furhter instructions. 

## Clone this repository
After generating your SSH keys as suggested [here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). 
You can then clone the repository by typing (or copying) the following line in a terminal at your preferred path in your machine:
```
git clone --recurse-submodules git@github.com:ResearchCodeReviewCommunity/dev-review.git
```
If you've cloned this repo without the `--recurse-submodules` options, then you can initialise your local git submodule config with

```
git submodule init
```
and update it with
```
git submodule update
```

## Development 
To preview changes locally, you can build and serve the website locally. 
The `disableFastRender` option is required to render some features brought by the LoveIt theme, such as mermaid diagrams. 
```
cd site/ && hugo serve --disableFastRender
```

Open your favorite web-browser using the following url:
```
Web Server is available at http://localhost:1313/dev-review/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```
See [Launching the website locally (hugoloveit.com)](https://hugoloveit.com/theme-documentation-basics/#25-launching-the-website-locally) for further information. 

## Contributing
Commit changes to any other branch than `main` or `gh-pages`, open a pull request and request for reviews as common practice following the [pull request workflow with git](https://medium.com/@urna.hybesis/pull-request-workflow-with-git-6-steps-guide-3858e30b5fa4).  
Once your changes are merged into `main` branch, the site will be automatically built and deployed and will be live roughly 1 minute later. 

:warning: **Do not commit directly to `main` or `gh-pages`.** :warning:
