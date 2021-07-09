## Single Developer Workflow

Here's a high-level view of a workflow you can follow as
a single developer that would like to make code review
part of your development process.

{{< mermaid >}}
graph TD;
  A([Start]) --> B(Meet initial requirements)
  B --> C(Find a reviewer)
  C --> D(Meet and agree on objectives)
  D --> E(Explain scientific context)
  E --> F(Explain code structure)
  F --> G{Is code large?}
  G -- No --> H[Select up to 400 lines to work on]
  G -- Yes --> I[Split into smaller sections and agree on a series of reviews]
{{< /mermaid >}}

To read about this workflow in detail, please see
[single developer process](/dev-review/recipes/lonecoder)
