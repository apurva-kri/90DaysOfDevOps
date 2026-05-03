### Task 1: The Problem
Think about a team of 5 developers all pushing code to the same repo manually deploying to production.

Write in your notes:
1. What can go wrong?
- 8 specific failure modes: merge conflicts, deployment collisions, no rollback, environment drift, no audit trail, fear-driven batching, downtime, and testing gaps.
2. What does "it works on my machine" mean and why is it a real problem? - broken down into 6 root causes (OS, runtime version, env vars, package versions, DB state, hardware) and explained why each one is a real engineering problem, not just an excuse.
3. How many times a day can a team safely deploy manually? the honest answer is 1–2, with a time breakdown showing why each deploy takes 2–3 hours manually. Contrasted with elite teams deploying 10–100+ times per day with CI/CD.

### Task 2: CI vs CD
Research and write short definitions (2-3 lines each):
1. **Continuous Integration** — what happens, how often, what it catches
- Every time a developer pushes code to a shared branch, a server automatically pulls that code, builds it, and runs the test suite — usually within minutes. The goal is to keep the main branch permanently in a known-good state and catch integration bugs (broken builds, failing tests, merge conflicts) before they pile up. Teams that do CI well merge small changes many times a day rather than batching a week's work into one risky merge.
- Real-world example: A developer on a Django web app pushes a branch that changes the user authentication logic. GitHub Actions immediately runs pytest and a linter. The linter flags a variable shadowing bug that the developer missed. The PR is blocked until it's fixed — the bug never reaches main.
2. **Continuous Delivery** — how it's different from CI, what "delivery" means
- CD picks up where CI left off. After the build and tests pass, the pipeline automatically packages the application and deploys it to a staging environment that mirrors production. At that point, the code is ready to ship — but a human still presses the button to push it live. The word "delivery" means the software is reliably delivered to the doorstep of production; someone still has to open the door.
- Real-world example: An e-commerce team merges a pricing-engine change. CI passes, the pipeline builds a Docker image, deploys it to staging, and runs smoke tests. A product manager reviews the change on staging and clicks "Deploy to prod" in the dashboard — the actual production push takes 90 seconds.
3. **Continuous Deployment** — how it differs from Delivery, when teams use it
- CD picks up where CI left off. After the build and tests pass, the pipeline automatically packages the application and deploys it to a staging environment that mirrors production. At that point, the code is ready to ship — but a human still presses the button to push it live. The word "delivery" means the software is reliably delivered to the doorstep of production; someone still has to open the door.
- Real-world example: An e-commerce team merges a pricing-engine change. CI passes, the pipeline builds a Docker image, deploys it to staging, and runs smoke tests. A product manager reviews the change on staging and clicks "Deploy to prod" in the dashboard — the actual production push takes 90 seconds.
- The key distinction to remember: CI is about merging safely, Delivery is about being always shippable, and Deployment is about actually always shipping. Here's how they compare visually:

### Task 3: Pipeline Anatomy
A pipeline has these parts — write what each one does:
- **Trigger** — what starts the pipeline
***An event that tells the CI/CD system to begin running the pipeline. The most common trigger is a git push or pull request merge, but triggers can also be a schedule (e.g. nightly), a manual button click, or another pipeline finishing. Without a trigger, nothing runs — it is the ignition switch of the whole system.***
- **Stage** — a logical phase (build, test, deploy)
***A named group of jobs that belong together conceptually. Stages run in sequence — all jobs in 'build' complete before 'test' starts, all jobs in 'test' complete before 'deploy' starts. If any job in a stage fails, the pipeline stops and later stages are skipped. Common stages: build → test → security → deploy.Analogy: Like chapters in a recipe: prep, cook, plate. You don't plate before cooking is done.***
- **Job** — a unit of work inside a stage
***A self-contained task that runs on a single runner. Jobs within the same stage can run in parallel — e.g. a 'test' stage might have separate jobs for unit tests, integration tests, and linting, all running at the same time. Each job gets a fresh environment: it starts clean, checks out the code, runs its steps, and exits.***
- **Step** — a single command or action inside a job
***The smallest unit of execution. A step is one shell command, one script, or one pre-built action. Steps inside a job run sequentially — if any step fails (non-zero exit code), the job fails immediately and subsequent steps are skipped. Steps share the same working directory and environment variables within a job. Analogy: Like individual instructions in a cooking step: 'crack egg', 'whisk', 'pour into pan' are steps inside the job 'make omelette'.***
- **Runner** — the machine that executes the job
***A server or container that picks up a job from the queue and runs it. Runners can be hosted by your CI provider (GitHub-hosted, GitLab SaaS runners) or self-hosted on your own infrastructure. Each job gets its own runner — or at least its own isolated environment. The runner sets up the OS, installs tools, clones the repo, then executes the job's steps.Analogy: Like a hired contractor. The CI system calls the agency (runner pool), a contractor arrives, does the job, and leaves — the next job gets a fresh contractor.***
- **Artifact** — output produced by a job
***A file or set of files that a job produces and explicitly saves so other jobs or humans can use them. Artifacts survive the job — they're uploaded to the CI system's storage at the end of the job and can be downloaded by later jobs or from the UI. Common artifacts: compiled binaries, Docker images, test coverage reports, and `.zip` packages ready to deploy. Analogy: Like a packaged product coming off an assembly line. The factory (job) made something; the artifact is what gets boxed up and sent to the next station — or the customer.***

### Task 4: Draw a Pipeline
Draw a CI/CD pipeline for this scenario:
> A developer pushes code to GitHub. The app is tested, built into a Docker image, and deployed to a staging server.

Include at least 3 stages. Hand-drawn and photographed is perfectly fine.
[Image]

### Task 5: Explore in the Wild
1. Open any popular open-source repo on GitHub (Kubernetes, React, FastAPI — pick one you know)
- URL: FastAPI test.yml, Repo: fastapi/fastapi → .github/workflows/test.yml
URL: https://github.com/fastapi/fastapi/blob/master/.github/workflows/test.yml 
2. Find their `.github/workflows/` folder
3. Open one workflow YAML file 
- https://github.com/fastapi/fastapi/blob/master/.github/workflows/test.yml  
4. Write in your notes:
   - What triggers it?
   ```
   The workflow is triggered by 3 events:
   Push to master branch
   Pull Request events
   when PR is opened
   when PR is updated (synchronize)
   Scheduled run (cron job)
   Runs every Monday at 00:00 UTC
   👉 So basically:
   It runs on code changes + weekly automatic check.
   ```
  - How many jobs does it have?
    ```
    There are 2 main jobs:
    changes job
    test job

    👉 Total: 2 jobs
    test job depends on changes job (needs: changes)
    Jobs in GitHub Actions represent different stages of the pipeline
    ```
   - What does it do? (best guess)
     ```
     What it does:
     Checks if relevant files changed
     Runs automated tests
     Tests across multiple OS + Python versions
     ```