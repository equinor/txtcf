# txtcf

Compare *versions* of a text (draft → edit1 → … → final) across classes of metric.

`txtcf` treats each metric as a noisy, indirect indicator of an unknown "distortion"
signal, so it keeps everything as tidy long-form rows, summarises with uncertainty, and
can localise a score back to the sentence that drives it.

## Concepts

- **Hierarchy** — `segment()` builds a `TextUnit` tree: sentence < paragraph < document < corpus.
- **Versions** — a `Version` is one revision; a `VersionSet` enumerates comparison
  `AlignedPair`s (`consecutive`, `vs_base`, `all`).
- **Metrics** — grouped by `Dimension` (lexical, stylistic, semantic, … ). Each is either an
  `ExtractorMetric` (`text → feature` + `feature,feature → score`, so features are cached and
  batched) or a `JointMetric` (reads both texts together). Look them up via the registry.
- **Pipeline** — `MetricStage`s run metrics over pairs at chosen granularities and emit
  `Measurement`s.
- **Stats** — `to_frame`, `aggregate` (bootstrap CIs), `normalize` (z-score), `agreement`
  (do metrics co-vary?), `localize` (which unit moved most).

## Metrics in v1

| Dimension | Metric | Computes |
|-----------|--------|----------|
| lexical | `levenshtein_distance`, `levenshtein_ratio` | character edit distance |
| stylistic | `readability_*` | `textstat` readability components (signed delta) |
| semantic | `embedding_cosine` | cosine distance of `all-MiniLM-L6-v2` embeddings |

Syntactic, pragmatic and factual dimensions are named and will be added behind the same contract.

## Quick start

```python
from txtcf import Pipeline, MetricStage, Level, get_metric, to_frame, aggregate, localize
from txtcf.data import example_version_set

vs = example_version_set()  # draft -> edit1 -> final, sentence-aligned
metrics = [get_metric("levenshtein_ratio"), get_metric("embedding_cosine")]

pipe = Pipeline([MetricStage(metrics, levels=[Level.DOCUMENT, Level.SENTENCE])])
frame = to_frame(pipe.run([vs]))

aggregate(frame[frame.level == "DOCUMENT"], by=["dimension", "metric"], ci=0.95)
localize(frame, "embedding_cosine", top=2)  # which sentence moved most
```

## Development

```sh
uv sync
uv run pytest
```
