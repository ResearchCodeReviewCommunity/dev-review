## Single Developer Workflow

Here's a high-level view of a workflow you can follow as
a single developer that would like to make code review
part of your development process.

{{< mermaid >}}
%% lonecoder mermaid
flowchart LR
  H-->REVIEWLOOP
  I-->REVIEWLOOP
  subgraph MAIN
    direction TD;
      Link(Links to more info)
      A([Start]) --> B(Meet initial requirements)
      %%YouAreHere(You are here)
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
      class Link,C,D,F linkedBox
      class YouAreHere youAreHereBox
  end
  subgraph REVIEWLOOP
    direction TD
    A2(Review) --> B2(Keep Reviewing)
  end

{{< /mermaid >}}

To read about this workflow in detail, please see
[single developer process](/dev-review/recipes/lonecoder)
