# Code Review During Research

What is *code review*?
If you're a researcher, why should you care about it?
For many researchers, the term may not be familiar, 
even for scientists that routinely write code.
For software engineers in industry and academia, 
the term "code review" brings to mind an established series of 
good practices.

At its core, code review consists of  
**someone else reading code you wrote,
and providing feedback**.
When it works, this process makes code
**easier to read, easier to maintain,
and easier to extend**.

This set of practices that software engineers call "code review"
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


{{< mermaid >}}
graph TD;
A(Initial reviewer-author meeting) --> B(Reviewer examines code)
B --> C(Reviewer compiles suggestions)
C --> D(Author and reviewer go over code)
D --> E(Author improves code)
E --> B
{{< /mermaid >}}


## Resources
* [Review Guidelines, References and Related Work](guidelines-refs-related)
* [Glossary](glossary)
