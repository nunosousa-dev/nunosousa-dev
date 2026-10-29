# Writing plan

Status: planning. No articles have been published as part of this update.

## Focus

Practical notes on building and operating AI platforms. Start with the tools used in current work; older DevOps experience and homelab experiments can provide background rather than lead the series.

Write for engineers who want to try something themselves. Each article should answer one question, include a small reproducible example, and explain what can go wrong.

## First three articles

Write these in order, without setting publication dates until the examples work. All three are independent tutorials, not accounts of an employer's implementation.

### 1. Argo Workflows and Ray: what each one does

**Question:** Where does workflow orchestration end and distributed execution begin?

- Build a small pipeline that generates synthetic CSV data and aggregates it with Ray.
- Explain what Argo Workflows coordinates and what Ray executes. Don't frame them as interchangeable competitors.
- Include one intentional failure and show where it appears, what a retry repeats, and how to clean up.
- Keep the example CPU-only, with pinned versions and no employer cloud dependencies. Specify local hardware requirements before recommending a local Kubernetes setup.

**Ready when:** a reader can reproduce a successful run and a failed run, explain which component owns each step, and remove every demo resource.

**Public starting points:** [Argo Workflows overview](https://argo-workflows.readthedocs.io/en/latest/) and [Ray overview](https://docs.ray.io/en/latest/ray-overview/index.html).

### 2. Useful workflow metrics without too many time series

**Question:** What should a dashboard show, and which labels make metrics unnecessarily expensive?

- Generate a bounded set of synthetic workflow outcomes and durations.
- Build an original Prometheus/Grafana demo showing run counts, failures, and duration distributions.
- Compare a small set of useful labels with a deliberately bad run-ID label in a tightly bounded experiment.
- Explain which questions belong in metrics and which need logs or another source. Keep per-run history separate from aggregate metrics.

**Ready when:** the dashboard answers a few stated operational questions and the example demonstrates how label choices affect the number of time series.

**Public starting points:** [Prometheus metric and label naming](https://prometheus.io/docs/practices/naming/) and [Grafana documentation](https://grafana.com/docs/grafana/latest/).

### 3. From an MLflow model version to a Ray Serve endpoint

**Question:** How can a serving application load a specific registered model version?

- Train a tiny model using synthetic data, track the run, and register the model in a local MLflow setup.
- Load an explicit model version into a disposable Ray Serve application.
- Show a request/response smoke test and what happens when the requested version doesn't exist.
- Distinguish a local demonstration from production concerns. Do not copy deployment topology, access controls, or configuration from work.

**Ready when:** a reader can identify which model version is serving, reproduce the prediction, and shut down the demo. This is a new personal experiment, not a claim about a production deployment.

**Public starting points:** [MLflow documentation](https://mlflow.org/docs/latest/ml/) and [Ray Serve documentation](https://docs.ray.io/en/latest/serve/index.html).

## Approach

- Start with a problem, not a list of product features.
- Use a small standalone project with invented names and data.
- Explain the choices and limits of the example.
- Include commands, expected results, and cleanup steps where relevant.
- Link to public, official documentation for technical claims.
- Keep the language direct. Use hyphens instead of em dashes.

## Before publishing

- Verify the example from a clean environment and record the tool versions.
- Use a personal sandbox, never an employer account or environment.
- Do not reuse internal code, manifests, diagrams, screenshots, logs, tickets, or URLs.
- Do not describe production topology, account arrangements, access policies, capacity, incidents, or unreleased work.
- Check that mentioning a technology or practice does not disclose confidential information. Follow the employer's publication and review requirements.
- Label experiments as experiments. Do not present an approach as production-proven unless there is public evidence for that claim.
- Add an article link to the README only after the article is published.
