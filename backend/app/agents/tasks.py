from crewai import Task

from app.agents.agents import (
    log_analyzer_agent,
    root_cause_agent,
    remediation_agent
)


log_analysis_task = Task(
    description="""
    Analyze the following log summary:

    {log_summary}

    Identify:
    - Important errors
    - Important warnings
    - Overall incident summary
    """,
    expected_output="""
    A concise log analysis report.
    """,
    agent=log_analyzer_agent
)


root_cause_task = Task(
    description="""
    Using the log analysis report generated previously,
    determine the most probable root cause.

    Include confidence level.
    """,
    expected_output="""
    Root cause with confidence level.
    """,
    agent=root_cause_agent
)


remediation_task = Task(
    description="""
    Based on the identified root cause,
    provide remediation steps and preventive measures.
    """,
    expected_output="""
    Actionable remediation plan.
    """,
    agent=remediation_agent
)