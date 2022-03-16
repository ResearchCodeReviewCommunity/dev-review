# Perform code review

## Code author communicates code and context

1. Author selects an appropriate segment of code
    - Pick a snippet you estimate can be reivewed in about 30 minutes.
    - We suggest picking a piece of code that is 50-100 lines.
    - If the code you plan to review is larger than that, agree on a strategy to sequentially go through smaller segments, or prioritise the most important segment
    - Choice is helped by objectvies from MAO stage.
      - TODO add examples: e.g. if coding style is reviewed, pick recently added class or method. The more representative of the codebase the snippet is, the more widely relevant the feedback.
      - Author should be familiar with the details of the chosen snippet. The main idea here is to come prepared.

It's a good idea to share the code to review with the reviewer ahead
of the review meeting. This gives an opportunity for the reviewer to
explore the code at their own pace and form independent
opinions. Prior exposure to the code will also make it easier for
them to navigate the code during the review itself.

But sharing the code isn't enough. To build relevant opinions --and
therefore constructive feedback-- a reviewer needs to be made aware of
the local context this particular piece of code fits in. As an
illustration, picture the case where the code under review consists of
a couple class methods. These were certainly implemented for a
specific purpose, and in a way that they interact in a specific way
(or do not interact). They also play particular role within the class
itself, that is designed in its own way, to fit its own purpose. The
purpose, the design and the implementation of the methods and their
surrounding code structures is key to understand the choices and
decisions made when writing the code.

Whenever your share a piece of code with reviewers, always attach a
description of its context. Explain what problem does the code solves,
and how it solves it. Make clear the constraints you had to work with.
If the code is part of a larger codebase, describe how it fits within
the bigger logic and explicit the relationships with other parts that
use it or are used by it.

> **How to share code?**
> Ideally, revisions of your research software should be available from
> development platforms like GitHub, GitLab or Bitbucket. Simply give
> the reviewer a permalink (see figure ??) or a commit SHA-1 and
> relevant line numbers. This is the preferred option as it gives
> reviewers the opporunity to navigate the whole codebase. Another
> option is [GitHub gists](https://gist.github.com/). If you send share
> your code by email, make sure to share the relevant files and clearly
> identify the version you are sharing.

![To get a link to a particular line (permalink) on GitHub, click on the line number on the left hand side](/dev-review/images/github_permalink.png "To get a link to a particular line (permalink) on GitHub, click on the line number on the left hand sise. Most development platforms can generate links to a particular line, for a particular revision.")


> callout here about diff workflows "merge workflow", "github workflow"

      - If you are going down an async review route, then providing the reviewer with a merge/pull request will be very helpful here
    - It might not be possible to share your code openly like this, or you may not be set up with version control yet
      - in that case, consider using something like [GitHub gists](https://gist.github.com/) to share your code
      - as a last resort, share your code snippet as an attachement to email or link to a file hosting location
    - Should be done a few days before the review meeting so that the reviewer has time to look at it. Exact timing should be discussed and MAO.
    - If your code has a complex environment, it might be desirable to share a containerised version of your code/software through somethign like Binder
        - mention CODECHECK as perhaps a better option for this kind of higher level check of your code


## Reviewer reviews code

1. Reviewer reminds themselves of objectives and areas of focus from first meeting (link to Meet and Agree on Objectives section)
1. Reviewer consults guidelines/checklist for advice about how to evaluate the code
    - Create a distinct page "Reviewer Guidelines" that gives the highlights from the resources we have collected, and then link to those resources
    - Provide a very high level summary of the subject headings here
    - OxCRN guidelines: https://github.com/OxfordCodeReviewNet/forum/blob/master/guidelines_for_reviewers.md
    - maybe also http://carver.cs.ua.edu/Slides/2019/URSSI-WinterSchool/URSSI-WinterSchool-PeerCodeReview.pdf (Jeff is part of community, probably happy to share)
4. Reviewer makes notes for future discussion on code segment in light of the above two points
    - this is not meant to be in depth (~ 20 minutes)

## Author and reviewer meet
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
