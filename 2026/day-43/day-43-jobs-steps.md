# Day 43: Jobs, Steps, Env Vars & Conditionals

Today's focus was on controlling the pipeline flow. Instead of just running a sequence of commands, I learned how to create dependencies, manage data across different scopes, and implement "smart" logic using conditionals.

## Task 1: Multi-Job Workflow
I created a workflow where jobs are linked sequentially. By default, GitHub Actions runs jobs in parallel; the `needs` keyword is what creates the chain.

- [**Workflow File:Multi-job.yml**](https://github.com/apurva-kri/github-actions-practice/blob/main/.github/workflows/multi-job.yml)

- **Key Concept:** `needs: [job_name]` creates a dependency.

---

## Task 2: Environment Variables & Contexts
Variables can be defined at different levels of "scope." I tested three levels to see how they override or complement each other.

| Level | Variable Name | Purpose |
| :--- | :--- | :--- |
| **Workflow** | `APP_NAME` | Global settings for the entire run. |
| **Job** | `ENVIRONMENT` | Specific to a set of steps (e.g., staging vs prod). |
| **Step** | `VERSION` | Temporary variable for a single task. |

**GitHub Contexts used:**
- `github.sha`: `${{ github.sha }}` (The unique ID of the commit)
- `github.actor`: `${{ github.actor }}` (The person who pushed the code)

- [**Workflow File:Env-variable.yml**](https://github.com/apurva-kri/github-actions-practice/blob/main/.github/workflows/env-var.yml)

---

## Task 3: Job Outputs
**Why pass outputs between jobs?**
Jobs run on isolated runners (different virtual machines). If Job A generates a unique build ID, an artifact name, or a dynamic version number, Job B won't know about it unless we explicitly "output" it from Job A and "need" it in Job B.

**Snippet for passing data:**
```yaml
# Job 1
outputs:
  my_date: ${{ steps.date_step.outputs.date }}
# Job 2
run: echo "The date from the previous job was ${{ needs.job1.outputs.my_date }}"
```

- [**Workflow file:job-output.yml](https://github.com/apurva-kri/github-actions-practice/blob/main/.github/workflows/env-var.yml)


---

## Task 4: Conditionals & Error Handling
**Conditionals allow the pipeline to make decisions on the fly.**

Branch Filtering: if: github.ref == 'refs/heads/main' ensures deployment only happens from the main branch.

Failure Handling: if: failure() allows a cleanup step to run only if something went wrong previously.

continue-on-error: true: This tells GitHub, "If this step fails, don't stop the whole job." This is useful for non-critical tasks like experimental linters.

- [Workflow File:condional.yml](https://github.com/apurva-kri/github-actions-practice/blob/main/.github/workflows/env-var.yml)


---

## Task 5: The Smart Pipeline
I combined these concepts into smart-pipeline.yml. It runs Lint and Test in parallel (saving time), then aggregates the results in a final Summary job.

**Key Sinppet**
```
summary:
  needs: [lint, test]
  runs-on: ubuntu-latest
  steps:
    - name: Final Report
      run: |
        echo "Commit Message: ${{ github.event.head_commit.message }}"
        echo "Branch: ${{ github.ref }}"
```

[Workflow File:smart-pipeline.yml](https://github.com/apurva-kri/github-actions-practice/blob/main/.github/workflows/smart-pipeline.yml)