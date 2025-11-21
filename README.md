# **Data Analysis Companion Agent (Hybrid AI Agent System)**

***Capstone Project — Google × Kaggle AI Agents Intensive***
**Developed by: Adithya E P**

---

## ✨ **Overview**

The **Data Analysis Companion Agent** is an AI-powered hybrid system that automates the full workflow of exploratory data analysis (EDA).
It can:

* Inspect and understand any structured dataset
* Generate statistical summaries
* Identify patterns and insights
* Produce charts and visualizations
* Write executive-level reports
* Evaluate report quality
* Run a complete pipeline end-to-end with a single command

This project demonstrates how **multi-agent systems + tool calling + reasoning pipelines** can significantly improve real-world data analytics workflows.

---

## 🔍 **Why This Matters**

Manual EDA is slow, repetitive, and time-intensive.
Businesses require:

* Faster insights
* Automated pipelines
* Less dependency on manual coding
* Consistency in reports

This agent solves that by behaving like a **junior data analyst**, automatically performing 80% of the typical EDA cycle.

---

## 🧠 **Hybrid Architecture (Agents + Tools)**

Below is the architecture flow (image included):

![Hybrid Flow](/flow_adk_web.png)

### **Agent Roles**

| Agent                  | Responsibility                                         |
| ---------------------- | ------------------------------------------------------ |
| **PlannerAgent**       | Inspects dataset, detects column types, proposes tasks |
| **AnalystAgent**       | Computes statistics, distributions, correlations       |
| **InsightEngine**      | Transforms raw stats into natural-language insights    |
| **VisualizerAgent**    | Creates histograms, boxplots, bar charts               |
| **ReporterAgent**      | Writes complete executive summaries                    |
| **FinalPipelineAgent** | Orchestrates the full workflow                         |

This hybrid approach combines **agent reasoning**, **direct Python tool execution**, and **LLM-generated narrative**.

---

## 🎯 **Key Features**

* 📊 **End-to-end EDA automation**
* 🔎 **Automatic column type inference**
* 📈 **Chart generation:** histogram, boxplot, bar-top-k
* 🧩 **Insight engine based on statistical heuristics**
* 🧠 **LLM-driven summary writing**
* 📝 **PDF report generation** (10-page report + chart-rich report)
* 🧪 **Evaluation module to ensure response quality**
* 🔧 **Fully modular — every agent can be used independently**

---

## 📁 **Repository Structure**

```
data-analysis-companion-agent/
│
├── README.md
├── LICENSE
├── flow_adk_web.png
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── agents.py
│   ├── analyst_agent.py
│   ├── insight_engine.py
│   ├── final_pipeline.py
│   ├── evaluator.py
│   ├── tools.py
│   ├── utils.py
│   ├── memory.py
│   ├── llm_wrapper.py
│   └── __init__.py
│
├── data/
│   ├── sample_datasets/
│   │     ├── sales.csv
│   │     └── churn.csv
│   └── memory.json
│
├── outputs/
│   ├── Report_with_charts.pdf
│   ├── Report_10page.pdf
│   └── examples/
│         ├── hist_total_revenue.png
│         ├── box_total_revenue.png
│         ├── etc...
│
├── dac_agent_submission.zip
│
├── thumbnail1.png
└── thumbnail2.png

```

---

## 🚀 **How to Run**

```python
from final_pipeline import FinalPipelineAgent

pipeline = FinalPipelineAgent()
result = pipeline.run("data/sample_datasets/sales.csv")

print(result["report"])
```

Outputs include:

* report text
* insights list
* generated charts
* evaluation score

---

## 🛠 **Technology Stack**

* **Python 3.11**
* **Pandas**, **NumPy**
* **Seaborn**, **Matplotlib**
* **ReportLab / PIL (PDF generation)**
* **LLM agent orchestration (OpenAI-compatible interface)**

---

## 🎤 **Demo (How It Works)**

1. Upload a dataset (CSV)
2. Run `FinalPipelineAgent()`
3. View the generated:

   * Summary
   * Insights
   * Charts
   * PDF Reports

Outputs are fully reproducible and interpretable.

---

## 📘 **If I Had More Time…**

* Add SQL ingestion and multi-table joining
* Add anomaly detection using ML
* Build an interactive Streamlit dashboard
* Add RAG system for domain-specific analytics
* Deploy as an enterprise internal analytics assistant

---

## 👤 **Author**

**Adithya E P**
Capstone Project for **Google × Kaggle AI Agents Intensive (2025)**
Open-source for learning, portfolio, and community contributions.

---
