from crewai import Crew
import time

from app.agents.agents import (
    log_analyzer_agent,
    root_cause_agent,
    remediation_agent
)

from app.agents.tasks import (
    log_analysis_task,
    root_cause_task,
    remediation_task
)


incident_crew = Crew(
    agents=[
        log_analyzer_agent,
        root_cause_agent,
        remediation_agent
    ],
    tasks=[
        log_analysis_task,
        root_cause_task,
        remediation_task
    ],
    verbose=True
)

def run_analysis(log_summary: str):
    retries = 3

    for attempt in range(retries):
        try:
            return incident_crew.kickoff(
                inputs={
                    "log_summary": log_summary
                }
            )
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(10)
            else:
                raise e