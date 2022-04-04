## Code Review Workflow

Here's a high-level view of a workflow researchers can follow to make code
review part of their development process.

```{mermaid}
%% codereview mermaid
graph TD;
  Link(Click on orange boxes for more detail)
  A([Start]) --> B(Find a reviewer)
  B --> C(Meet and agree on objectives)
  C --> D(Author prepares code segment)
  D --> E(Reviewer makes initial comments)
  E --> F(Realtime review meeting)
  F --> G(Improvements and follow up)
  G --> H{More review needed?}
  H -- Yes --> D
  H -- No --> I([Finish])

  click B "./high-level.html#find-a-reviewer" "Find a reviewer"
  click C "./high-level.html#meet-and-agree-on-objectives" "Meet and agree on objectives"
  click D,E,F,G "./high-level.html#perform-code-review" "Perform Code Review"
  click I "./high-level.html#finish" "Finish"

  classDef default fill:#8EB6DE,stroke:#162D4D,stroke-width:2px,color:#162D4D;
  classDef linkedBox fill:#FABB00,stroke:#000,stroke-width:2px,color:#000;
  class Link,B,C,D,E,F,G,I linkedBox
```

### Find a reviewer

There is no code review without a reviewer or reviewers. The good news is,
almost any researcher who codes is a good candidate for being
one.

Potential reviewers are not far: in your own research group, others
you collaborate with or your local Research Software Engineering
group. They can also be found in communities outside your institution
or specific research domain. In the [Find a reviewer](../../recipes/find_a_reviewer) phase, we look at
different pools of potential reviewers, what makes a suitable
reviewer, and ways of getting in touch.

### Meet and agree on objectives

A code review can improve code in a lot of different ways, but trying
to do everything at once is rarely effective. In the
[Meet and agree on objectives](../../recipes/meet_and_agree_on_objectives/)
phase, participants make it clear to others people involved why they are
are pariticpating.

The goal of this second phase is for all the participants to agree on
the purpose of the review. This is critical to a constructive and
useful discussion during the actual review process. Key questions are:
- What is the author expecting from the review?
- What should the review enable? Better readability? Knowledge
  transfer? Better performance?
- What part of the code should we look at?


### Perform code review

This is the core of the process. The code author and reviewer(s) meet
(in person or virtually) to discuss the code. Although the subject is
technical, everyone involved must remember that they are interacting
with humans. Empathy, humbleness and non-confrontational communication are
key to a successful code review.

The [Perform code review](../../recipes/perform_code_review/) phase
is an iterative process, itself made of 5 phases:
- Code author communicates the code and its context to reviewer(s) in advance and
  with context.
- Reviewer(s) review code in light of objectives and areas of focus,
  agreed upon during the [Meet and agree on objectives](../../recipes/meet_and_agree_on_objectives/) phase.
- Author and reviewer(s) meet and discuss the code.
- Code author implements changes.
- Rinse and repeat.

### Finish

Ideally, the code review cycle ends when both the code author and
reviewer(s) agree that the objectives set at the [Meet and agree
on](../../recipes/meet_and_agree_on_objectives/)
objectives phase are met. In case both parties do not agree, the code
author has decision power on whether or not to end the code review
process.
