# MLOps-CICD-for-ML


# CI/CD for ML

In `Traditional Software` CI/CD is triggered (Github Actions) by changes to code.

In `machine Learning` [CI/CD](https://wandb.ai/hamelsmu/model-registry/reports/What-is-CI-CD-for-Machine-Learning---VmlldzozNzk2NDg2) is triggered by changes to: `code`, `data`, and `model performance`. Also need:
* Some kind of `observability` layer that allows you to see whats happening, regardless of what triggered the testing or deployment of the model (eg. experiment tracking, model registry).
* `Workflow/orchestration` system to run all tasks regardless of where it was triggered (eg. if we change some code or data or model performance, we need a central point where we can run retraining or retesting).
* `Review process` cause ML is messy. This will interact with `A/B testing`, online/offline data tests, `canary model deployment`. 

Github Actions (GitOps) and W&B can be used together to automate your workflow for the `changing code` and `observability` steps mentioned above.


# GitHub Actions

[[Github Actions](https://docs.github.com/en/actions)] need to be located in a folder named `.github/workflows`. See example [Action file](.github/workflows/ci.yaml) with comments.

Best way to start is with a `template`. We can Google `github actions example workflows` or use the [Github docs example](https://docs.github.com/en/actions/quickstart). Some details about the action file are:
* If we create new files locally and want to run them through a Github actions workflow, we won't have access to it directly. `Third party actions` allow you to use pre-defined worfklows, to do things like cloning contents of the current repo (see [Github checkout action](https://github.com/actions/checkout)), which is on of the most commonly use cases. In the [workflow file](.github/workflows/ci.yaml), third party actions are called with the `uses` command.
* Github Actions are triggerd by specific commands. Check [events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows), to know which commands  can trigger Github Actions (eg. git push).
* The characters `${{ }}` are used for [special variables](https://docs.github.com/en/actions/learn-github-actions/contexts) about the context of the run.

## Action Secrets

Allow to use sensitive information (eg. passwords or tokens) inside Github action workflows without having to store it in the open where everyone can see them. We can define new `Secrets` in: `repo > Settings > Secrets and Variables > Actions > New Repository Secret`.

To access the secret, we need to reference it in your workflow