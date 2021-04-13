# lone coder
## Context:
Both author and reviewer are lone coders with no previous experience
in code review.

Both authors and reviewers work within the same group or same lab. They
work on different projects but are both familiar with the scientific
field.

Nomenclature: R = reviewer, A = author

### Finding a reviewer:
Anyone can review code, even if they are not a proficient coder/software engineer.
However, in a group or lab, it may be possible to pair a more experienced author
or reviewer with a less experienced author or reviewer.
A difference in experience level is not a bad thing, and can help with knowledge transfer.

#### Requirements:
Process is as lightweight as possible. It must fit into a researcher's
already busy schedule. We hope that, once the value of code reviews is
recognised, more time will be dedicated to them.

#### Objective:
- Create readable and understandable code
- Create maintainability and extensibility
- Verify that code does what author says it does and what it should do

#### Recipe:
Meeting 0 (initialisation)

A describes scientific context to R.
A describes code overall structure

Selecting Code to Review

- If code > 400 loc, R and A agree on a portion to review.

If large codebase, portion to review can itself be > 400 loc, which is
then split into smaller blocks to review. R and A agree on a series of
review meetings to address each smaller block in a sequence.

- Outcome of meeting 0: process and expectations are clear for everyone.

for each meeting in planned meetings:

Ahead of meeting:

A makes code block available to R a couple of days before.

R has a first look at code block and takes notes of any future discussion points.
R can refer to a checklist at this stage.
This first look is not in depth (20' max)

(Ideally) R and A make their own versioned copy of the code block. This
will allow the illustration of suggested modifications with a diff.

During meeting

A walks R through the code block, telling the story of the code,
narrating
- what the code does
- why it is required
- why it is implemented in this way.

A stops regularly to give R the chance to make comments, but R should
feel comfortable interrupting A at any point.
R (or A?) keeps notes of comments and responses from A.

Optionally, both R and A can propose alternative implementations by
modifying their versioned copy of the code block.  However, this
should not be the focus of the meeting.

Author improves code outside the meeting

#### Sharing software progress with group:
Many groups have regular meetings to share scientific progress.
These should also be seen as opportunities to share software progress.
When presenting scientific progress, show the steps you have taken
to ensure your software is as good as your science,
and what has changed as a result of code reviews.

#### Checklist:
Worth adding a checklist here?
