# Explain code structure

{{< admonition type="example" title="Expand for flowchart" open=false >}}

{{< mermaid >}}
%% lonecoder mermaid
graph TD;
  Link(Links to more info)
  A([Start]) --> B(Meet initial requirements)
  YouAreHere(You are here)
  B --> C(Find a reviewer)
  C --> D(Meet and agree on objectives)
  D --> E(Explain scientific context)
  E --> F(Explain code structure)
  F --> G{Is code large?}
  G -- No --> H[Select up to 400 lines to work on]
  G -- Yes --> I[Split into smaller sections and agree on a series of reviews]

  click C "https://researchcodereviewcommunity.github.io/dev-review/recipes/find_a_reviewer/" "Find a reviewer"
  click D "https://researchcodereviewcommunity.github.io/dev-review/recipes/meet_and_agree_on_objectives/" "Meet and agree on objectives"
  click F "https://researchcodereviewcommunity.github.io/dev-review/recipes/explain_code_structure/" "Explain code structure"

  classDef default fill:#8EB6DE,stroke:#162D4D,stroke-width:2px,color:#162D4D;
  classDef linkedBox fill:#FABB00,stroke:#000,stroke-width:2px,color:#000;
  classDef youAreHereBox fill:#FA3800,stroke:#000,stroke-width:2px,color:#000;
  class Link,C,D linkedBox
  class YouAreHere,F youAreHereBox
{{< /mermaid >}}

{{< /admonition >}}


## Objective

Reviewer has a good understanding of the overall structure of the
code. When reviewing a section of the code, they have an idea of its
purpose and how it relates to other parts.
If the section to review is not yet defined, they are in a position to
help the author choose it.

## Steps

1. The author describes the overall structure of the code to the reviewer(s).
2. The author highlights the section to review and describes how it
   relates to other parts of the code
   
## Description

Even if code is isolated inside a function or module, the way it is
written is influenced by its context. For the review to be useful, the
reviewer(s) must have, at the very least, a rough idea of how the code
they are looking at relates to other parts of the code. For instance,
there could be constraints on the shape of data that comes in, or the
data that comes out.

Therefore, is it important that the author takes a few minutes to
describe the overall structure of the code. The relationship between
key modules, functions or subroutines should be made clear. If the
code is too large to be outlined in less than five minutes, do not
describe its entire structure. Rather, focus on the context
surrounding the piece of code to be reviewed, answering questions such
as: from where is it called and when? What data is available and where
does is come from? What data goes out and to where?

This step can be done either by sitting together (physically or
virtually) or through written conversation (e.g. emails). Real-time
conversation is often the most efficient way to convey the most
information in the least time, but the slower pace of written
correspondence can also help building a stronger understanding of
context. This choice will often depend on your preferences and the
amount of time available.

## Examples

- Adam has been contributing to a large Fortran code. The module he's
  implementing connects to only a couple of others, and Adam isn't
  actually familiar with the rest of the code. He would like the
  review to focus on a function that they've written last week. This
  function does some complex data manipulation in order to pass it to
  another function within a separate module. Adam starts by stating
  the purpose of the module they're implementing, then moves on to
  describing how the function to be reviewed fits into this
  module. Finally, they make clear how this function depends on
  another module, and what it entails regarding data format.
  
- Sam has written an R package to automate a data analysis pipeline.
  This package is made of a main function that itself calls 4 four
  others in a sequence, representing the four steps of the pipeline.
  The review focus on the function implementing the third step. Sam
  describes the whole package and details the purpose of this specific
  function. She then explains what data goes in and in what format,
  and what data goes out and in what format.
