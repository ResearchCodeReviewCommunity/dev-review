# Code Review During Development

From small data analysis scripts to large simulation software, **quality
software is essential to quality research**. Code readability,
maintainability and extensibility are key to research outputs that
can be reproduced and built upon.

But how can you assess the readability of your code? Have someone else
read it!  Whether your are an advanced programmer or a beginner, code
reviews will greatly improve the quality of your software by giving
you access to human feedback on your code and programming
practices. Code reviews are also opportunities for **knowledge
transfer**. Whether you participate as a reviewer or reviewee, code
reviews are opportunities to learn from your colleagues .. or teach
them a few tricks!

**This website aims at providing a clear, opinionated workflow
for code reviews among researchers in academia. It is designed to be
accessible by researchers at all levels, from research students to
senior professors, whether they are new to programming or software
engineering experts.**

{{< mermaid >}}
graph TD;
  A(Initial reviewer-author meeting) --> B(Reviewer examines code)
  B --> C(Reviewer compiles suggestions)
  C --> D(Author and reviewer go over code)
  D --> E(Author improves code)
  E --> B
{{< /mermaid >}}

## Getting Started
Please see [this page](flowcharts/high-level)
for an overview of how you can get started with code review.

## Resources
* [Glossary](glossary)
* [References and Related Work](refs-related)

## Why code reviews?

Code review is standard practice in the software industry, as well as
open source software communities. It is, however, very rare in
academia.  Very generally, we believe that developers of research
software, at every level or career stage, would greatly benefit from
regular human feedback on the code they write. On an individual level,
this would provide effective learning opportunities and raise the
quality of the programs they write. On a collective level, making code
review a standard practice among research software developer would
generally raise the quality of software-based research as a whole,
bringing the development of quality software at the core of a
researcher's routine.
