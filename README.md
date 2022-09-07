# Code Review During Development

This repository is automatically built from [markdown](https://commonmark.org/) files by [Sphinx](https://www.sphinx-doc.org/) and the [MyST parser](https://myst-parser.readthedocs.io)
using [ReadTheDocs](https://readthedocs.org/).
This site uses the [Sphinx Book](https://sphinx-book-theme.readthedocs.io) theme.
This site is available here: https://dev-review.readthedocs.io/en/latest/

The content of the website is contained in markdown files located in the `docs/` folder and are structured like so

~~~text
docs/
├── flowcharts    <-- any mermaid flowcharts used in multiple locations
│   └── high-level.md
├── glossary.md    <-- a glossary of important terms for code review
├── guidelines    <-- more general guidelines for code review apart from the more prescriptive recipes
│   ├── approach.md
│   └── points-to-check-for-reviewers.md
├── index.md    <-- the landing page of the website
├── recipes    <-- our suggested steps to follow during the code review process
│   ├── explain_code_structure.md
│   ├── find_a_reviewer.md
│   ├── lonecoder.md
│   ├── meet_and_agree_on_objectives.md
│   ├── perform_code_review.md
│   └── recipe_template.md
└── refs-related.md    <-- references for material related to code review
~~~

## Dependencies
We use [`nox`](https://nox.thea.codes/en/stable/)
as a task-runner to create development environments
and to build the docs.
There are many ways to install but we recommend the following:
1. use a system package manager to install `pipx`
2. use `pipx` to install `nox` so you can use it across projects
3. finally ask `nox` to create a development environment

- macOS/Linux
```
brew install pipx  # or `python3 -m pip install --user pipx`
pipx install nox
nox -s dev
```
- Windows
```
choco install pipx -confirm
pipx install nox
nox -s dev
```

## Clone this repository
After generating your SSH keys as suggested [here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
You can then clone the repository by typing (or copying) the following line in a terminal at your preferred path in your machine:
```
git clone git@github.com:ResearchCodeReviewCommunity/dev-review.git
```

## Development
To preview changes, you can build and serve the website locally.

```
nox -s docs -- serve
```

Open your favorite web-browser using the following url:
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

## Contributing
Commit changes to any other branch than `main`, open a pull request and request for reviews as common practice following the [pull request workflow with git](https://medium.com/@urna.hybesis/pull-request-workflow-with-git-6-steps-guide-3858e30b5fa4).  
Once your changes are merged into `main` branch, the site will be automatically built and deployed and will be live roughly 1 minute later.

:warning: **Do not commit directly to `main`.** :warning:
