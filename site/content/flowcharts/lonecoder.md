## Single Developer Workflow

Here's a high-level view of a workflow you can follow as
a single developer that would like to make code review
part of your development process.

{{< mermaid >}}
%% lonecoder mermaid
graph TD;
  Link(Click on orange boxes for more detail)
  A([Start]) --> B(Find a reviewer)
  B --> C(Meet and agree on objectives)
  C --> D(Meet to review code)
  D --> E{Have objectives been met?}
  E -- No --> D
  E -- Yes --> F([Finish])

  click B "https://researchcodereviewcommunity.github.io/dev-review/recipes/find_a_reviewer/" "Find a reviewer"
  click C "https://researchcodereviewcommunity.github.io/dev-review/recipes/meet_and_agree_on_objectives/" "Meet and agree on objectives"
  click F "https://researchcodereviewcommunity.github.io/dev-review/recipes/explain_code_structure/" "Explain code structure"

  classDef default fill:#8EB6DE,stroke:#162D4D,stroke-width:2px,color:#162D4D;
  classDef linkedBox fill:#FABB00,stroke:#000,stroke-width:2px,color:#000;
  class Link,B,C,F linkedBox
{{< /mermaid >}}

To read about this workflow in detail, please see
[single developer process](/dev-review/recipes/lonecoder)
