import pandas as pd
import numpy as np

class AnalystAgent:
    def run(self, csv_path, plan):
        df = pd.read_csv(csv_path)

        results = {}

        # -----------------------------
        # 1. Missing values
        # -----------------------------
        missing = df.isnull().sum()
        results['missing_values'] = {
            col: int(missing[col]) for col in df.columns if missing[col] > 0
        }

        # -----------------------------
        # 2. Numeric summary
        # -----------------------------
        numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
        if numeric_cols:
            results['numeric_summary'] = df[numeric_cols].describe().to_dict()

        # -----------------------------
        # 3. Categorical summary
        # -----------------------------
        cat_cols = [c for c in df.columns if pd.api.types.is_object_dtype(df[c])]
        cat_summary = {}
        for c in cat_cols:
            vc = df[c].value_counts().head(10)
            cat_summary[c] = vc.to_dict()
        results['categorical_summary'] = cat_summary

        # -----------------------------
        # 4. Correlations
        # -----------------------------
        if len(numeric_cols) >= 2:
            corr = df[numeric_cols].corr()
            results['correlations'] = corr.to_dict()

        # -----------------------------
        # 5. Time series detection
        # -----------------------------
        datetime_cols = [c for c in df.columns if self._is_datetime_column(df[c])]
        if datetime_cols:
            results['datetime_columns'] = datetime_cols

        return results

    def _is_datetime_column(self, series):
        if pd.api.types.is_datetime64_any_dtype(series):
            return True
        try:
            parsed = pd.to_datetime(series, errors='coerce')
            return parsed.notnull().mean() >= 0.6
        except:
            return False
