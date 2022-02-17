# Perform code review

## Code author communicates code and context

1. Author selects an appropriate segment of code
    - Pick a snippet you estimate can be reivewed in about 30 minutes.
    - We suggest picking a piece of code that is 50-100 lines.
    - If the code you plan to review is larger than that, agree on a strategy to sequentially go through smaller segments, or prioritise the most important segment
    - Choice is helped by objectvies from MAO stage.
      - TODO add examples: e.g. if coding style is reviewed, pick recently added class or method. The more representative of the codebase the snippet is, the more widely relevant the feedback.
      - Author should be familiar with the details of the chosen snippet. The main idea here is to come prepared.

1. Author shares the code through an appropriate medium
   - When sharing the code snippet before meeting to review, the author should provide local context for the code selected
      - the **overall** context and structure of your code will be discussed at the [Meet and Agree on Objectives stage](meet_and_agree_on_objectives.md)
      - e.g. For instance if you share a couple of class methods, it's useful for a reviewer to know about the class itself, its purpose, design and structure. Then how do the functions fit within the class and interact with each other.

- We recommend writing up this information in a short blurb and sending it to your reviewer in the same email or message where you share a link to the code itself (next step)

> this should be a callout "How to Share Code"

- We strongly recommend that you use a version control platform (like GitHub.com or GitLab.com) to share your code
      - Not only are these the locations where most code review happens, but they also gives your reviewer the opportunity to poke around the rest of your codebase should they need some broader context.
      - This will require the repository to be open, or perhaps you can give temporary permission to the reviewer if it is private
      - Share the URL to your file and the relevant line numbers you would like reviewed

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
