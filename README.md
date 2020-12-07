# Authenticate to the GitHub API as an app

Quick script to request an authentication token from a GitHub app to then use to make API calls on behalf of the app.

## Why

GitHub user personal access tokens have a rate limit of 5,000 requests per hour whereas GitHub apps have a higher limit depending on your plan type and number of users [[1]][rate-limit].

## Prerequisites

- A GitHub app created and installed in your account or Organisation, with a private key created.

[rate-limit]:https://docs.github.com/en/free-pro-team@latest/developers/apps/rate-limits-for-github-apps