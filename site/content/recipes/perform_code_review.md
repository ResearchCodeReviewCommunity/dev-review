# Perform code review

The previous phases have all be about setting the best foundation possible for
the code review. Now it is time to execute and reap the benefits of code review.
We will walk through the following steps:

1. [Code author communicates code and context](#code-author-communicates-code-and-context)
1. [Reviewer reviews code](#reviewer-reviews-code)
1. [Author and reviewer meet](#author-and-reviewer-meet)
1. [Author makes changes](#code-author-implements-changes)

## Code author communicates code and context

The first step initiating the actual code review phase is for the code author to
select a segment of their code to be reviewed. The success and impact of the code
review will depend, to some degree, on how appropriate the selected segment is,
so it warrants some consideration from the code author. Here are some points to
keep in mind when selecting your code segment.

- Your choice should address the objectives set at the [Meet and Agree on
  Objectives step](../meet_and_agree_on_objectives). For example, if you want to
  get feedback on the style of your code, picking _recent additions_ to the code
  will be more reflective of your own style rather than portions that you have
  _amended_, since they might have been originally written by someone else.
  Alternatively, if you want a general overview of the readability of your code,
  pick a snippet that shares characteristics with many other areas of the code
  base so that the feedback on this particular snippet can be extrapolated more
  broadly. This applies in general: the more representative of the codebase the
  snippet is, the more widely relevant the feedback.
- We recommend selecting a snippet of code that is between **50 and 100 lines long**
  in total, and no longer than 200 lines. There is clear evidence from the
  literature of industry studies that the quality and impact of code review
  declines rapidly as the length of the code to review increases. We also make
  this recommendation from personal experience; you probably have had the
  experience yourself of being amazed at how long it takes to decipher even a
  single line of code! These numbers can be flexed depending on how familiar the
  reviewer is with your code: the less familiar, the less code you should
  select.
- As the author, you should be familiar with this segment of code. Don't select
  something that your yourself don't understand.

Next, it's a good idea to share the code to review with the reviewer ahead
of the review meeting. This gives an opportunity for the reviewer to
explore the code at their own pace and form independent
opinions. Prior exposure to the code will also make it easier for
them to navigate the code during the review itself.

To get the most out of the review, you as the author of the code
will also want to help the reviewer understand
how the particular snippet you select fits into the overall code.
This helps the reviewer provide relevant comments
and constructive feedback.
As an illustration, picture the case where the code under review consists of
a couple methods belonging to a class. The methods were implemented for a
specific purpose, and they might interact in a specific way.
The methods also play particular role within the class
itself, a class that is designed in its own way, to fit its own purpose.
The purpose, the design and the implementation of the methods and their
surrounding code structures is key to understand the choices and
decisions made when writing the code.

When you share a piece of code with reviewers, attach a
description of its context. Explain what problem the code solves,
and how it solves it. Make clear the constraints you had to work with.
If the code is part of a larger codebase, describe how it fits within
the bigger logic and make explicit the relationships with other parts that
use it or are used by it.

> **How to share code?**
> Ideally, revisions of your research software should be available from
> development platforms like GitHub, GitLab or Bitbucket. Simply give
> the reviewer a permalink (see figure below) or a commit SHA-1 and
> relevant line numbers. This is the preferred option as it gives
> reviewers the opportunity to navigate the whole codebase. Another
> option is [GitHub gists](https://gist.github.com/). If you send
> your code by email, make sure to share the relevant files and clearly
> identify the version you are sharing.
> ![To get a link to a particular line (permalink) on GitHub, click on the line number on the left hand side](/dev-review/images/github_permalink.png "To get a link to a particular line (permalink) on GitHub, click on the line number on the left hand side. Most development platforms can generate links to a particular line, for a particular revision.")
> If you are performing an asynchronous review (see callout at top of [Author
> and reviewer meet](#author-and-reviewer-meet)) then giving your reviewer a
> link to a pull/merge request is also an effective sharing mechanism.

## Reviewer reviews code

Code review can seem intimidating, even for the reviewer. 
Where do you even start? What do you look at? 
The good news is: there are a number of points that are almost always worth looking at. 
In particular, readability is often a good place from which to start a code review. 
You can start simple, for instance looking at variables' and functions' names: are they explicit? 
Do they carry intent? As you get more and more familiar with the code under review, 
move on to larger structure: can some of the functions be split into several functions? 
Do you see any complex conditional statements that you find hard to read? 
Eventually, perhaps after several iterations of the code review process, 
you may be able to criticise the code design, 
for instance its modules and the relationships between them. But don't start from there!

As discussed in the Meet and Agree on objectives phase, however, 
code reviews are most effective when a clear goal is set. 
This goal can help you as a reviewer to orient your feedback, 
and focus on what matters from the point of view of this overall objective. 
It is also good practice to calibrate your review for the author, 
keeping in mind their programing experience. 
For instance, if the code review aims at assessing readability in general, 
and you knew that the code author has limited experience, 
you would want to pay attention to variable and function names, 
parameter lists, complex conditionals, or lengthy functions. 
It would probably be best to keep away from suggesting using the latest and greatest features of the language. 
If the review is about writing more idiomatic code, however, 
the focus changes to looking specifically at how the code under review 
makes use of the language it is written in.

Given the unique goals that researchers have when writing code, 
and the existing good practices for code review developed across industry and academia, 
we suggest a workflow with two key elements.
First of all, keep the authors' objectives in mind.
To achieve this, begin your review by refreshing your memory about what you and
the author discussed when you met initially.
The second key element is to work from a checklist.
We provide a checklist [here](../guidelines/points-to-check-for-reviewers.md).
Please see also the additional resources on the [References and Related Work](../refs-related.md) page.
Of course, no checklist can perfectly capture all the dimensions of research
code review.
Our goal in providing a checklist is to give beginners somewhere to start, and
to help experts keep in mind what common issues are that frequently need
attention.
As you work through the checklist, 
make notes you can refer to during the review meeting and perhaps share
with the author afterwards. 
You will probably find, as you go through the exercise of outlining some notes,
that there are one or two key points you will want to talk about with the
author.
These key points can form the focus for when you and the author meet, as
described in the next section.

## Author and reviewer meet

Before describing the meeting phase of the code review, it is worth mentioning
that there is an alternate technique for code review.

> **Asynchronous Review:** The most common form of code review in industry is
> done _asynchronously_ through platforms like GitHub and GitLab. Authors of
> changes submit what are called _merge_ or _pull requests_ into the main or
> development branch of a code repository. Reviewers then leave their comments
> through the web interface, directly in the context of the changes made.
> The author addresses the comments, and when a consensus is reached, the changes
> are merged or rejected. This all happens through the web interface with no
> real time or face-to-face interaction. While this can be an effective form of
> review for projects, we feel strongly that researchers with less experience of code
> review benefit more from the meeting-based approach outlined by this website.

- key points:
  -  there are two ways to do code review: synchronous/in-person, and asynchronous
  -  while there is not much existing research, what does exist suggests that for research code review, the process should include face-to-face, synchronous component [Wilson 2015]
  -  This is because there are such different backgrounds that can go into code review and both the author and reviewer need to make sure they are understanding each other
- A good way to open up this meeting might be for the author and reviewer to go over the scientific context for the code review
- Reviewer drives review according to their notes. They discuss the code by giving direct feedback or asking questions challenging the code's design, implementation and documentation.
- Author responds to reviewer's comments and questions. They describe the structure, explain implementation, justify decisions.
- Live reviews help build trust and understand the other person's mindset.
- This is a conversation in which the code author has the opportunity to talk about their code out loud. By asking questions, expressing opinions and challenging assumptions a code reviewer triggers new ideas and different perspectives.
  - > [name=David] maybe "suggesting alternatives" or something a bit less aggressive than  "challenging assumptions"?
- Predefined objectives should be kept in mind. Conversation can be powerful but should be kept on a tight leash. It's okay for anyone to stop the conversation and say they feel it is losing focus. In this case it is time to move to the next topic.
-
- A code review is not an evaluation of the author's worth as a programmer. Throughout the review, participants should keep in mind
  -  Differences in levels of experience.
  -  Differences in scientific and programming backgrounds.
  -  Code quality is often subjective and context dependent.
  -  *More?*...
  -  
- By opening their work for feedback, code authors make *themselves* vulnerable. This vulnerability must be taken into account and respected by reviewers at all times. Reviewers must take caution in expressing feedback and opinions. Authors must respect reviewer's comments and questions.
- Reviewing can be mentally demanding. It can be difficult for a reviewer to be mindful of how they phrase feedback at all times. Therefore authors should also try not to take feedback personally. This is especially true for written, asynchronous reviews.
- Example of questionable reviewer's feedback:
  - You should rename this function
  - This function should be renamed
- Examples of good reviewer's feedback
  - I think this function's name is misleading
  - This function's name didn't help me understand what it does.
- Meeting should be kept short, under 60', 45' being a good target duration in most cases. This is to avoid fatigue. Two 45' review meetings will likely be more effective than a single 90' meeting. This can, however, be decided on the spot or ahead of the meeting.
- Time will likely run out. It is possible than conversations on some of the points could have been shorter. It is also possible that the corresponding points needed to be discussed in details for reasons only made clear during teh review itself. In any case, both authors and reviewers can choose to meet again to continue the review.

## Code author implements changes

## Rinse and repeat
