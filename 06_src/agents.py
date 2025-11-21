import os
import re
from typing import Dict, Any

import pandas as pd
import numpy as np

# Safe datetime detection
def _is_datetime_series(series: pd.Series) -> bool:
    if pd.api.types.is_numeric_dtype(series):
        return False
    vals = series.dropna()
    if len(vals) == 0:
        return False
    try:
        sample = vals.sample(min(50, len(vals)), random_state=0).astype(str)
    except Exception:
        sample = vals.astype(str)
    sep_hits = 0
    iso_hits = 0
    for v in sample:
        if any(sep in v for sep in ['-', '/', '.']):
            sep_hits += 1
        if re.match(r'^\d{4}[-/]\d{1,2}[-/]\d{1,2}', v):
            iso_hits += 1
    if (sep_hits + iso_hits) < max(1, len(sample) * 0.2):
        return False
    parsed = pd.to_datetime(sample, errors='coerce')
    return parsed.notnull().mean() >= 0.6


class PlannerAgent:
    def __init__(self, sample_rows: int = 200):
        self.sample_rows = sample_rows

    def inspect(self, csv_path_or_df) -> Dict[str, Any]:
        if isinstance(csv_path_or_df, str):
            df = pd.read_csv(csv_path_or_df, nrows=self.sample_rows)
        else:
            df = csv_path_or_df.copy()

        cols = df.columns.tolist()
        dtypes = {c: str(df[c].dtype) for c in cols}
        unique_counts = {c: int(df[c].nunique(dropna=True)) for c in cols}

        numeric_cols = [c for c in cols if pd.api.types.is_numeric_dtype(df[c])]
        categorical_cols = [c for c in cols if pd.api.types.is_object_dtype(df[c])]
        datetime_cols = [c for c in cols if _is_datetime_series(df[c])]

        suggestions = []
        for c in cols:
            if unique_counts[c] == 2:
                suggestions.append({'column': c, 'reason': 'binary target candidate'})

        plan = [
            {'task': 'overview_summary', 'priority': 1},
            {'task': 'missing_values', 'priority': 1},
        ]
        if numeric_cols:
            plan.append({'task': 'univariate_numeric', 'priority': 2})
        if categorical_cols:
            plan.append({'task': 'univariate_categorical', 'priority': 2})
        if datetime_cols:
            plan.append({'task': 'time_series', 'priority': 2})
        if len(numeric_cols) >= 2:
            plan.append({'task': 'correlations', 'priority': 3})
        if suggestions:
            plan.append({'task': 'target_suggestion', 'priority': 1})

        charts = []
        for c in numeric_cols:
            charts.append({'type': 'hist', 'col': c})
            charts.append({'type': 'box', 'col': c})
        for c in categorical_cols:
            charts.append({'type': 'bar_topk', 'col': c})

        return {
            'columns': cols,
            'dtypes': dtypes,
            'numeric_cols': numeric_cols,
            'categorical_cols': categorical_cols,
            'datetime_cols': datetime_cols,
            'suggestions': suggestions,
            'plan': sorted(plan, key=lambda x: x['priority']),
            'charts': charts
        }


class VisualizerAgent:
    def generate(self, csv_path, charts, out_dir='outputs/examples'):
        import matplotlib.pyplot as plt
        import seaborn as sns
        df = pd.read_csv(csv_path)
        os.makedirs(out_dir, exist_ok=True)
        paths = []
        for ch in charts[:8]:
            col = ch.get('col')
            t = ch.get('type')
            try:
                fig = plt.figure(figsize=(6,4))
                if t == 'hist':
                    sns.histplot(df[col].dropna(), kde=False)
                    plt.title(f"Histogram — {col}")
                elif t == 'box':
                    sns.boxplot(x=df[col].dropna())
                    plt.title(f"Box Plot — {col}")
                elif t == 'bar_topk':
                    vc = df[col].value_counts().head(10)
                    sns.barplot(x=vc.values, y=vc.index)
                    plt.title(f"Top categories — {col}")
                else:
                    plt.close()
                    continue
                out = os.path.join(out_dir, f"{t}_{col}.png")
                plt.savefig(out, bbox_inches='tight')
                plt.close()
                paths.append(out)
            except Exception:
                try:
                    plt.close()
                except Exception:
                    pass
        # add correlation heatmap if numeric
        num = df.select_dtypes(include='number')
        if num.shape[1] >= 2:
            try:
                fig = plt.figure(figsize=(7,5))
                sns.heatmap(num.corr(), annot=True, cmap='coolwarm')
                p = os.path.join(out_dir, 'correlation_heatmap.png')
                fig.savefig(p, bbox_inches='tight')
                plt.close()
                paths.append(p)
            except Exception:
                pass
        return paths


class ReporterAgent:
    def compose(self, metadata, analysis_results, chart_paths, memory):
        try:
            from llm_wrapper import call_llm
        except Exception:
            def call_llm(prompt): return "[LLM_PLACEHOLDER] " + (prompt[:1200] if isinstance(prompt, str) else str(prompt))
        insights = analysis_results.get('insights', [])
        insights_text = "\n".join(f"- {i}" for i in insights) if insights else "No insights."
        prompt = (
            "You are a senior data analyst. Produce a concise executive summary (600-900 words).\n\n" +
            f"Columns: {metadata.get('columns')}\n" +
            f"Numeric columns: {metadata.get('numeric_cols')}\n" +
            f"Categorical columns: {metadata.get('categorical_cols')}\n" +
            f"Datetime columns: {metadata.get('datetime_cols')}\n\n" +
            "Top insights:\n" + insights_text + "\n\n" +
            f"Charts: {chart_paths}\n" +
            f"Tone: {memory.get('preferred_tone', 'business')}\n"
        )
        return call_llm(prompt)
