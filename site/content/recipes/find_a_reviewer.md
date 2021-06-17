# Objective

Upon completing this recipe, you as the _code author_ will have found someone
suitable to perform the role of _reviewer_ in the code review.

# Steps

1. Identify the top areas to search for candidate reviewers.
  - Your research group
  - Research Software Engineer (RSE) group at your institution
  - Language or library specific groups at your institution
  - Open source or research communities you contribute to
  - Others?
  - Last resort is to throw it up on Code Review Stack Exchange
    <https://codereview.stackexchange.com/>
2. Pre-screen candidates based on your existing knowledge and some criteria
   (below).
3. Contact candidates directly or make advertisement.
4. Repeat 1 to 3 until you get a bite.
5. Confirm candidate can fulfill minimum thresholds.

# Description

It might seem strange, but code review has something in common with partner
dancing: it takes two to tango and (at least) two to review code. Without a
reviewer, the code review cannot happen. And just as a good dance partner is
essential for a well-performed routine, a suitable reviewer ensures that the
code review will be a rewarding and valuable experience. Finding someone to
fill this important role can be one of the more difficult steps in getting a
code review off the ground — or dance floor, depending on how far you want the
analogy to go.

Perhaps the main barrier to finding a reviewer is misconceptions about what
experience a reviewer should possess. As a lone coder, you might be thinking,
"Only software developers do code review, so I should probably find someone
outside of research." Or "The reviewer definitely needs to be more experienced
than me." We want to be absolutely clear on this point: almost _any_ researcher
who codes can be a good reviewer of your research code.

That being said, there are certainly minimum criteria that a reviewer should
satisfy to make a code review worthwhile for both parties, and there are some
places to search for reviewers that have a higher chance of yielding someone
that fulfills these criteria. Let's look at these now.

## Step 1: Places to Look {#search}

When looking for a reviewer, your first port of call should almost always be
your own research group. Your colleagues are the most likely to be using the
same language and libraries as you, and they will be familiar with your
common research domain. It will be least intimidating to ask someone at the
same seniority level as you, but equally, you shouldn't feel ashamed or
intimidated to show your code to someone at a higher seniority. You already
show them your scientific results after all! However, there are many reasons
why it may not be possible to seek a reviewer in your research group. Your
group might be small and you are the only coder, or perhaps the idea of
reviewing code is perceived as a waste of time by your colleagues, and you are
hesitant to stick your neck out. If so, keep reading.

<!--
Probably need to add something about justifying time on code review to
supervisor?
--!>

There are many other places to look for code reviewers. If you are fortunate
enough to have a Research Software Engineering (RSE) group at your institution,
then any member of that team would make a great reviewer for your code.
These groups have many different ways of operating, so you will need to contact
them to find out how to set up a code review. Forewarning: it is likely the
time of the RSE will need to be covered under someone's budget, so if you were
hesitant to have the conversation about code review in your research group,
that problem will probably resurface here.

Another great place to search within your institution or region are language or
library-specific community groups (e.g. a Python or R User Group). This can
help ensure the reviewer has experience with the same or similar tools you use.
Before [making your advertisement](#contact), consider asking one of the
community managers or someone you know in the community whether code review is
something that has been done before or others might be interested in. Just as
in the case with colleagues, you will be relying on people to volunteer their
time, and as you are probably all to familiar with, researchers have that in
very short supply. The community simply might not have the bandwidth to take on
code review.

It might be necessary to venture outside of your institution or immediate
geographic region to find a reviewer, and it is an increasingly viable option
in the context of remote working and many people getting used to asynchronous
communication. If you are part of a research organisation, community, or
working group that spans institutions and countries, this could be a viable
avenue to search for a reviewer. Your connections in these areas might not
themselves be suitable, but you can ask if they know anyone who might be.
Open source or open science communities could similarly be leveraged,
especially if you intend to make your software open source. If you have
extended an open source library or even just made some convenient scripts to
work with it, consider opening a merge/pull request to get the maintainers to
have a look. A good example of this for more mature software is [rOpenSci's
peer review initiative](https://bssw.io/blog_posts/a-community-of-practice-around-peer-review-for-long-term-research-software-sustainability).

If none of the above options bear any fruit, then as a last resort you could
make a post on the [Code Review Stack
Exchange](https://codereview.stackexchange.com/). See the ["What questions can
I ask about here?"](https://codereview.stackexchange.com/help/on-topic) page to
determine whether it could suit your needs.

## Step 2: Criteria for Screening {#criteria}

Once you have identified a potential reviewer and before you contact them, you
should consider whether they will satisfy some minimum thresholds to be a
suitable reviewer. These criteria equally apply when deciding whether to
advertise to a larger group.

1. Do they have some level of experience with the programming language(s) of
   your code? They do not need to be experts in the language(s), but they
   should not be absolute beginners. Code review is an opportunity to learn
   _more_ about a programming language, not to learn the language itself. 
2. Do they have some degree of knowledge about your research domain? This is
   not strictly necessary, but can be desirable. Domain knowledge will help
   your reviewer more quickly grasp the context of what your code is doing and
   therefore address the code itself more directly. Researchers or developers
   outside your domain can certainly offer valuable insight, but it might just
   take a bit longer. We are all for cross-disciplinary interactions.
3. Are they familiar with the libraries or tools that you use? As for the
   previous criterion, this one isn't strictly necessary, but it can have quite
   a large impact upon the value of the review. The importance of this
   criterion scales with the extent to which your code relies on another
   library or tool and how essential it is to the functionality of your code.

## Step 3: Contact candidate or advertise {#contact}

Everyone has their own way of writing messages, and we don't want to be too
prescriptive about how you reach out to a potential reviewer. If you already
know the reviewer, this step should be straightforward, but if not, then it can
be a little stressful going out on a limb to contact someone you don't know or
advertise to a group of people, especially if they are more senior than you.
Our advice: don't overthink it, and stay concise and to the point. A casual and
less formal atmosphere for the code review is desirable, so if you find
yourself writing a stilted and overly-formal message to a candidate, then it
might be worth thinking whether it will be a good fit.

Consider including the following information in any message or advertisement
you compose:

- Context about _why_ you are looking to have your code reviewed. The
    motivations section (**TODO** add link) on this website might be helpful to
    identify the reasons that motivated you to get your code reviewed.
- A brief summary of what your code does and any particular aspects you want
    addressed.
- [Any of the criteria for a suitable reviewer](#criteria) that you weren't
    able to answer yourself before reaching out.
- An idea of the time commitment (**TODO** what is our estimate for how long the
    whole process will take?)

## Step 4: Rinse and Repeat {#repeat}

Loop through steps 1 to 3 until you get a bite. Once you have your reviewer,
proceed to the [next step](meet_and_agree_on_objectives) and arrange a meeting
to agree on objectives for the review.

# Examples

- Priya is a researcher in a small research group in a physics department, and
  she's currently writing a Python library to process her experimental data.
  She doesn't think anyone in her immediate research circle would be
  appropriate for reviewing her code because she is mostly concerned about
  whether it conforms to Pythonic standards and she knows her PI will see it as
  a waste of time. Luckily, she recalls that there is a Python User Group at
  her university that meets fairly regularly and has a Slack space. She
  privately messages one of the administrators of the Slack space, asking
  whether code review is something that the community might be able to help
  with. The administrator responds positively, and Priya posts a brief
  advertisement giving a background to her code and describing her objective to
  have it checked for "Pythonic" idioms. Funnily enough, another researcher
  from her Physics Department, who she didn't know, responds and agrees to help
  with a code review, stating he has experience developing Python packages in
  the open source community.
- Sam is a PhD student in a medium-sized bioinformatics group writing R
  scripts, who combines their own novel algorithms with libraries from their
  group and the broader community. Sam has heard many warnings about code
  reproducibility and maintainability and wants to make sure they can run their
  code later in the PhD and build upon it. They are fortunate to have a healthy
  and relaxed working relationship with one of the postdocs in the group who
  has lots of R experience. Sam brings up the idea of code review in one of
  their water cooler conversations, mentioning the points about reproducibility
  and maintainability. The postdoc enthusiastically agrees, also wondering
  aloud whether the whole group should start doing something like that.
