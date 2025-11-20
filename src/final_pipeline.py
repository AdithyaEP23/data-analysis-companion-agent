from agents import PlannerAgent, VisualizerAgent, ReporterAgent
from analyst_agent import AnalystAgent
from insight_engine import InsightEngine
from evaluator import check_outputs
from memory import load_memory

class FinalPipelineAgent:
    def __init__(self):
        self.planner = PlannerAgent()
        self.analyst = AnalystAgent()
        self.insight_engine = InsightEngine()
        self.visualizer = VisualizerAgent()
        self.reporter = ReporterAgent()
        self.memory = load_memory()

    def run(self, csv_path):
        # 1. Planner
        plan = self.planner.inspect(csv_path)

        # 2. Analyst
        analysis = self.analyst.run(csv_path, plan)

        # 3. Insights
        insights = self.insight_engine.generate_insights(analysis)
        analysis['insights'] = insights

        # 4. Visuals
        charts = self.visualizer.generate(csv_path, plan['charts'])

        # 5. Reporter
        report = self.reporter.compose(plan, analysis, charts, self.memory)

        # 6. Evaluator
        status = check_outputs(report, charts)

        return {
            'plan': plan,
            'analysis': analysis,
            'insights': insights,
            'charts': charts,
            'report': report,
            'evaluation': status
        }
