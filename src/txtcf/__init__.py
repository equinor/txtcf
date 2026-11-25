"""txtcf — compare versions of a text across classes of metric.

Public API:

- Text hierarchy: :class:`Level`, :class:`TextUnit`, :func:`segment`.
- Versions: :class:`Version`, :class:`VersionSet`, :class:`AlignedPair`.
- Metrics: :class:`Dimension`, :class:`Measurement`, the metric registry
  (:func:`get_metric`, :func:`by_dimension`, :func:`metric_names`,
  :func:`higher_is`), and the
  :class:`ExtractorMetric` / :class:`JointMetric` building blocks.
- Pipeline: :class:`Pipeline`, :class:`MetricStage`.
- Stats: :func:`to_frame`, :func:`aggregate`, :func:`normalize`, :func:`agreement`,
  :func:`localize`.
"""

from __future__ import annotations

from .metrics import (
    Dimension,
    ExtractorMetric,
    JointMetric,
    Measurement,
    Metric,
    by_dimension,
    get_metric,
    higher_is,
)
from .metrics import names as metric_names
from .pipeline import MetricStage, Pipeline
from .stats import aggregate, agreement, localize, normalize, to_frame
from .units import Level, TextUnit, segment
from .version import AlignedPair, Version, VersionSet, from_frame

__all__ = [
    "Level",
    "TextUnit",
    "segment",
    "Version",
    "VersionSet",
    "AlignedPair",
    "from_frame",
    "Dimension",
    "Measurement",
    "Metric",
    "ExtractorMetric",
    "JointMetric",
    "get_metric",
    "higher_is",
    "by_dimension",
    "metric_names",
    "Pipeline",
    "MetricStage",
    "to_frame",
    "aggregate",
    "normalize",
    "agreement",
    "localize",
]
