# git-action-test-automated_workflow

This is a sample repository showcasing the use of GitHub Actions for Continuous Integration and Continuous Deployment. (CI/CD pipeline)

The repository contains a simple Python files (works with another programming languages as well), with a workflow defined in the .github/workflows directory.

The workflow is triggered on each push to the repository and runs a series of tasks, such as:

- Installing dependencies
- Building the application
- Running unit tests

If all the tasks are successful, the workflow will be marked as completed and a new version of the application will be deployed.

To use this repository as a template for your own project, simply fork the repository and modify the workflow to fit your needs. For more information on GitHub Actions, see the official documentation.

## NOTES:
- make sure `actions/checkout@v[current version number]`. Right now, it is v3. Check [actions/checkout](https://github.com/actions/checkout) repo for more info.
- refer [commitzen tool for GitHub Actions](https://commitizen-tools.github.io/commitizen/tutorials/github_actions/)
- youtube videos for references: https://youtu.be/vLDbvV2nNHw
