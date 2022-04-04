# Code Review During Research
## A lightweight workflow for researchers

What is *code review*?
Even scientists that routinely write code for analysis
may not be familiar with the term.
At its core, code review consists of
**someone else reading code you wrote,
and providing feedback**.
For software engineers in industry and academia,
code review represents a process
that can be carried out according to an established set of good practices.
When it works, this process makes code
**easier to read, easier to maintain,
and easier to extend**.

**The goal of this website is to provide you,
a researcher, with just such a process.
You may be in academia or in industry,
a student or a senior professor,
new to programming or a software engineering expert.
We aim to make this process accessible to all.**

### Why should I care about *code review* if I'm a researcher, not a software engineer?

Code review is standard practice in the software industry, as well as
open source software communities. It is still comparitively rare in academia.
We think that all researchers can benefit
from frequently getting feedback on the code they write,
in the same way that we benefit by taking the time to
read and write articles, reviews, textbooks or any other scholarly work.
Regardless of whether you are a physicist modeling molecular dynamics
or a digital humanities librarian building a website for a collection of an authors' personal papers,
we think you stand to gain a thing or two
from doing just a little code review.

### Can you do code review and research at the same time?

The process that software engineers call code review
applies when software is mature and the scope of the project is clearly defined.
Unfortunately, when writing code for research,
the software is not mature, and the scope is not well understood.
If either of those were true, it wouldn't be research.
It is still unclear how well code review
translates to what is arguably the most common research setting:
a single scientist, writing analysis code,
or helping to maintain a shared set of homegrown tools used by just one lab.
Some work has been done to answer the question of how to translate code review to this setting
(please see [references and related work](./refs-related.md)).
Although there are good ideas on how to adapt code review for researchers,
many of the efforts have been disparate.
The [Research Code Review Community](https://github.com/ResearchCodeReviewCommunity)
formed to build bridges and open up dialogues across these efforts.

### A guide to a lightweight process for code review during research

One key issue is that there is no guide that describes a
clear process for code review during research.
**The goal of this website is to provide you,
a researcher in academia, with just such a process.
We aim to make the process accessible to researchers at all levels,
from students to senior professors,
whether they are new to programming or software engineering experts.**

## Getting Started

From small data analysis scripts to large simulation software, **quality
software is essential to quality research**.
Whether you are an advanced programmer or a beginner, code
reviews will greatly improve the quality of your software by giving
you access to human feedback on your code and programming
practices. Code reviews are also opportunities for **knowledge
transfer**. Whether you participate as a reviewer or reviewee, code
reviews are opportunities to learn from your colleagues ... or teach
them a few tricks!

Please see [this page](flowcharts/high-level)
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
