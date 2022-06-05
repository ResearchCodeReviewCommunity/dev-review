# Meet and agree on objectives

## Objective

Set the code review up for success by making sure the reviewer and author are on the same page.

## Steps

1. The author describes the overall structure and scientific context of the code
   to the reviewer(s).
1. If they have some, the code author states their expectation for the code review.
1. If they have some, reviewer(s) state their expectation for the code review.
1. Author and reviewers agree on the focus of the review

## Description

Code review can be a powerful tool to improve code quality, provided
that participants agree on what "improve" means. Should you focus on
code readability? Or performance? For a code review to be productive,
both the author and the reviewer(s) must agree on the direction to
follow.

To kick off the startup meeting, we recommend that the code author provide some
context for their code base. Here are some questions the code author might want
to consider:

- What scientific problem or area does this computer program address?
- What are the programs inputs and outputs?
- How is the program used? Is is a library called by other programs or is it
  compiled directly itself to produce results?
- What is the overall structure of the code? Its main modules, classes, functions?

Then, during the remainder of the startup meeting, all participants in the
review state their expectations and agree on what the objective of the review
should be.  As the code author, you could plan to receive feedback on a
particular design choice you made last week.  Or maybe you're planning to pick
the reviewer's brain about optimising the performance of that sluggish
subroutine. As a reviewer, you could be motivated by learning new features of a
programming language. You could also want to put the focus on readability,
because you think there is room for improvement in this direction. These
expectations must be made clear during the startup meeting, before the review
itself starts.

As a rule of thumb, we recommend that the review focuses on one of the
following themes, ordered by priority:

- Code readability
- Code maintainability
- Code extensability (can the code be extended or added to)
- Performance

Particularly, we do not recommend focusing on performance unless it is
justified from a scientific perspective. Optimising for performance
often makes code harder to read and maintain.

Another special case is a "debugging session". The code author is looking
for help to fix a specific problem, and code quality may not be the primary
focus of the code review.

## Examples

-   R is familiar with the basics of C++, but never used it
    frequently. They would like to learn what kind of features their C++
    programmers colleagues use, and learn a few tricks along the way.  A
    has been working on a C++ analysis pipeline on their own for the
    past few weeks and is about to share it with their team. Before they
    do so, they would like to check that the code is easy to read and
    the structure easy to understand, even by colleagues with little
    experience in C++. R and A decide

-   A is looking is unsure about a the design of a module their wrote
    last week.  It works, but it is complicated and contains a lot of
    duplicated code. They would like somebody else to assess
    readability and potentially suggest alternative design choices.  R
    is keen on helping a colleague improving their code, but doesn't
    have specific expectations. they find the code easy to read although
    they agree that the structure is odd.  A and R decide to have a look
    at the module, looking to better define the issue, assess current
    maintainability and, if time allows, draft a few solutions to
    improve code structure.

-   A's numerical experiments are running much slower than
    expected. They identified a specific function performing poorly, and
    they're looking for help in investigating the root cause. R previously
    had a look at the function and the surrounding code, but found it
    very hard to read. R suggests that they focus on identifying what
    makes the code difficult to read and, if time allows, think of some
    options that would improve its structure. They agree that they could
    look into performance in a follow up review, once the code is easier
    to read.
