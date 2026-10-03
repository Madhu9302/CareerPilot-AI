"""
Orchestrator Service
Coordinates all agents and manages state passing between them.
"""

from __future__ import annotations

from typing import Any

from agents.career_advisor import CareerAdvisorAgent
from agents.skill_gap import SkillGapAgent
from agents.roadmap import RoadmapAgent
from agents.project_recommender import ProjectRecommenderAgent
from agents.career_mentor import CareerMentorAgent


class Orchestrator:
    """
    Central coordinator that runs agents in sequence and aggregates results.

    Pipeline:
        profile
           ↓
        CareerAdvisorAgent  → career_analysis
           ↓
        SkillGapAgent       → skill_gap  (uses career_analysis)
           ↓
        RoadmapAgent        → roadmap    (uses skill_gap)
           ↓
        ProjectRecommenderAgent → projects (uses skill_gap)

    CareerMentorAgent is stateful and called separately per chat turn.
    """

    def __init__(self):
        self._career_advisor = CareerAdvisorAgent()
        self._skill_gap = SkillGapAgent()
        self._roadmap = RoadmapAgent()
        self._project_recommender = ProjectRecommenderAgent()
        self._mentor = CareerMentorAgent()

    # ------------------------------------------------------------------
    # Main pipeline
    # ------------------------------------------------------------------

    def run_analysis(self, profile: dict[str, Any]) -> dict[str, Any]:
        """
        Run the full analysis pipeline for a user profile.

        Returns
        -------
        dict with keys:
            profile, career_analysis, skill_gap, roadmap, projects
        """
        if not self._validate_profile(profile):
            return {"error": "Please fill in all required profile fields."}

        career_analysis = self._career_advisor.analyze(profile)
        skill_gap = self._skill_gap.analyze(profile, career_analysis)
        roadmap = self._roadmap.generate(profile, skill_gap)
        projects = self._project_recommender.recommend(profile, skill_gap)

        return {
            "profile": profile,
            "career_analysis": career_analysis,
            "skill_gap": skill_gap,
            "roadmap": roadmap,
            "projects": projects,
        }

    def chat(
        self,
        user_message: str,
        profile: dict[str, Any] | None = None,
        analysis: dict[str, Any] | None = None,
        history: list[dict[str, str]] | None = None,
    ) -> str:
        """Delegate a chat turn to the CareerMentorAgent."""
        return self._mentor.chat(user_message, profile, analysis, history)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _validate_profile(self, profile: dict[str, Any]) -> bool:
        required = ["name", "target_role", "skills"]
        for field in required:
            value = profile.get(field)
            if not value or (isinstance(value, list) and len(value) == 0):
                return False
        return True

    @staticmethod
    def get_available_roles() -> list[str]:
        """Return the list of roles the system supports."""
        from data.role_data import ROLE_REQUIREMENTS
        return sorted(ROLE_REQUIREMENTS.keys())
