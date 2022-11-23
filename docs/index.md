# Code Review During Research
## A lightweight workflow for researchers

What is *code review*?
Even scientists that routinely write code for analysis
may not be familiar with the term.
At its core, code review consists of
someone else reading code you wrote
and providing feedback.
For software engineers in industry and academia,
code review has come to represent a standardized process,
carried out according to an established set of good practices.
When it works, this process makes code
easier to read, easier to maintain,
and easier to extend.
Although code review is a standard practice
in the software industry and in open source software communities, it is still comparatively rare in academia.

The goal of this website is to provide you,
a researcher, with a way to do code review.
We provide a lightweight process
meant to be easy for all to use.
In particular, this workflow is designed
to be accessible to
a single researcher working
independently, such as a graduate student
developing code for their own thesis project.
Although code review in a research context
has not been studied as well as code review in industry,
the guidelines we provide are based
on existing studies,
notably [Petre and Wilson 2014](https://arxiv.org/abs/1407.5648).
For additional literature,
please see the [references and related work](./refs-related.md) page.
The guidelines are also based on the experience
of the authors running
the [Oxford Code Review Network](https://github.com/OxfordCodeReviewNet/forum),
and on their experiences carrying out code review
in academia and in the private sector.

## Getting Started

The core workflow that we suggest
is presented below.
To find out about how you can
get started with code review,
and a high-level overview of
this lightweight workflow,
please see [this page](flowcharts/high-level)
for an overview of how you can get started with code review.

```{mermaid}
graph TD;
  A(Initial reviewer-author meeting) --> B(Reviewer examines code)
  B --> C(Reviewer compiles suggestions)
  C --> D(Author and reviewer go over code)
  D --> E(Author improves code)
  E --> B
```

## Resources
* [Review Guidelines, References and Related Work](refs-related)
* [Glossary](glossary)

```{toctree}
:hidden: true
:maxdepth: 2

flowcharts/high-level
refs-related
glossary
```

## About

This site is one of the products of
the [Research Code Review Community](https://github.com/ResearchCodeReviewCommunity),
that formed to open up dialogues and build bridges across efforts to integrate code review into research.
