# Code Review During Development

From small data analysis scripts to large simulation software, quality
software is essential to quality research. Code readability,
maintainability and extensibility are key to research outputs that
can be reproduced and built upon.

But how can you assess the readability of your code? Have someone else
read it!  Whether your are an advanced programmer or a beginner, code
reviews will greatly improve the quality of your software by giving
you access to human feedback on your code and programming
practices. Code reviews are also opportunities for knowledge
transfer. Whether you participate as a reviewer or reviewee, code
reviews are opportunities to learn from your colleagues .. or teach
them a few tricks!

This website aims at providing a clear, opinionated workflow
for code reviews among researchers in academia. It is designed to be
accessible by researchers at all levels, from research students to
senior professors, whether they are new to programming or software
engineering experts.

{{< mermaid >}}
graph TD;
  A(Initial reviewer-author meeting) --> B(Reviewer examines code)
  B --> C(Reviewer compiles suggestions)
  C --> D(Author and reviewer go over code)
  D --> E(Author improves code)
  E --> B
{{< /mermaid >}}

## Developer Profiles
* [Single Developer](flowcharts/lonecoder)

## Resources
* [Glossary](glossary)
* [References and Related Work](refs-related)
