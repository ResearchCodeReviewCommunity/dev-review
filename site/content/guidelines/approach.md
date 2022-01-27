# How to Have Constructive Code Review Conversations

> adapted from a [guide](http://carver.cs.ua.edu/Slides/2019/URSSI-WinterSchool/URSSI-WinterSchool-PeerCodeReview.pdf) by [Jeff Carver](http://carver.cs.ua.edu)

Many aspects of code review can occur asynchronously,
if the software is mature and the scope of the project is clearly defined.
Unfortunately, when developing code for research,
the software is not mature and the scope is not well understood,
or it wouldn't be research.
That's why code review in a research setting is much more likely
to involve one-on-one, face-to-face conversations.
How can you ensure those conversations are productive?
Here we provide some key points to keep in mind for both the
reviewer and the author of the code.

## Reviewer
* Focus on the code, not the author.
  + Use "I" statements ("Usually I approach similar situations this way...") instead of "you" statements ("You should do this...")
  + Talk about the code, not the coder
  + If you must talk about the coder, talk in terms of behavior (which can change) instead of talking about attributes
* Ask questions rather than make statements
  + Avoid "why" questions that sound accusatory ("Why would you do this?")
* Accept that there are different solutions
* Pick your battles
* Remember to praise good
* Take your time and do the review well

## Author
* Remember that the goal of code review is to improve the overall code, not evaluate the quality or worth of the developer.
  + Remember you are not your code.
* Don't be afraid to make mistakes.
  + We all make mistakes, that's how we learn.
* Keep an open mind.
  + Someone else will always know more, its ok, learn from them.
  + People bring different perspectives, that's a good thing.
* If you feel strongly about a certain approach, than you should of course defend it, but also be willing to compromise. Combatative code reviews won't help anyone.
