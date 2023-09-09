# MLOps-CICD-for-ML


# CI/CD for ML

In `Traditional Software` CI/CD is triggered (Github Actions) by changes to code.

In `machine Learning` [CI/CD](https://wandb.ai/hamelsmu/model-registry/reports/What-is-CI-CD-for-Machine-Learning---VmlldzozNzk2NDg2) is triggered by changes to: `code`, `data`, and `model performance`. Also need:
* Some kind of `observability` layer that allows you to see whats happening, regardless of what triggered the testing or deployment of the model (eg. experiment tracking, model registry).
* `Workflow/orchestration` system to run all tasks regardless of where it was triggered (eg. if we change some code or data or model performance, we need a central point where we can run retraining or retesting).
* `Review process` cause ML is messy. This will interact with `A/B testing`, online/offline data tests, `canary model deployment`. 

Github Actions (GitOps) and W&B can be used together to automate your workflow for the `changing code` and `observability` steps mentioned above.


# GitHub Actions

[[Github Actions](https://docs.github.com/en/actions)] need to be located in a folder named `.github/workflows`. See example Action file with comments `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

Best way to start is with a `template`. We can Google `github actions example workflows` or use [GitHub docs](https://docs.github.com/en/actions/quickstart) (containing an example).
* Check [events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) when they are called (eg. push).
* The characters `${{ }}` are used for [special variables](https://docs.github.com/en/actions/learn-github-actions/contexts) about the context of the run.
