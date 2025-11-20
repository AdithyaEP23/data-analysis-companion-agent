class InsightEngine:
    def generate_insights(self, analysis):
        insights = []

        # Missing values
        mv = analysis.get('missing_values', {})
        if mv:
            for col, count in mv.items():
                insights.append(f"Column '{col}' has {count} missing values.")

        # Numeric insights
        nums = analysis.get('numeric_summary', {})
        for col, stats in nums.items():
            if 'mean' in stats:
                mean = stats['mean']
                std = stats['std']
                insights.append(f"'{col}' has a mean of {mean:.2f} and std of {std:.2f}.")

            if 'min' in stats and 'max' in stats:
                insights.append(f"'{col}' ranges from {stats['min']:.2f} to {stats['max']:.2f}.")

        # Categorical distributions
        cats = analysis.get('categorical_summary', {})
        for col, freq in cats.items():
            top = list(freq.items())[0]
            insights.append(f"Most common value in '{col}' is '{top[0]}' ({top[1]} occurrences).")

        # Correlations
        corr = analysis.get('correlations', {})
        for col, values in corr.items():
            for other, value in values.items():
                if abs(value) > 0.6 and col != other:
                    insights.append(f"'{col}' is strongly correlated with '{other}' (corr={value:.2f}).")

        return insights
