
# Data Analysis Companion Agent (Capstone Project)

## Overview
This project is an AI-powered Data Analysis Agent capable of:
- Inspecting datasets
- Performing exploratory data analysis
- Generating insights
- Creating visualizations
- Producing executive summaries
- Running evaluation checks

## Architecture
1. PlannerAgent – understands dataset structure  
2. AnalystAgent – computes EDA statistics  
3. InsightEngine – extracts insights  
4. VisualizerAgent – generates charts  
5. ReporterAgent – writes a full data summary  
6. FinalPipelineAgent – ties everything together

## Features
- Works with any structured CSV dataset
- Automatic chart creation
- Automatic insight generation
- Memory-based personalization
- Evaluation for report quality
- Modular and extendable design

## File Structure
src/
- agents.py
- analyst_agent.py
- insight_engine.py
- final_pipeline.py
- llm_wrapper.py
- tools.py
- memory.py
- evaluator.py

data/sample_datasets/
- sales.csv
- churn.csv

outputs/examples/
- generated charts

## How to Use
from final_pipeline import FinalPipelineAgent
pipeline = FinalPipelineAgent()
result = pipeline.run("path_to_your_dataset.csv")

## Author
Generated as part of the AI Agents Intensive (Google × Kaggle) Capstone Project.
