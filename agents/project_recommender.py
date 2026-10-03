"""
Project Recommendation Agent
Recommends practical projects tailored to the user's target role and skill gaps.
"""

from __future__ import annotations

from typing import Any

from data.role_data import ROLE_REQUIREMENTS


class ProjectRecommenderAgent:
    """Suggests hands-on projects matched to skill gaps and experience level."""

    def recommend(
        self, profile: dict[str, Any], skill_gap: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Generate project recommendations.

        Returns
        -------
        dict with keys: projects (list[dict]), quick_wins (list), stretch_goals (list)
        """
        target_role: str = profile.get("target_role", "")
        experience_level: str = profile.get("experience_level", "Beginner")
        missing_skills: list[str] = [
            s["skill"].lower() for s in skill_gap.get("need_to_learn", [])
        ]
        already_have: list[str] = [
            s["skill"].lower() for s in skill_gap.get("already_have", [])
        ]

        role_data = ROLE_REQUIREMENTS.get(target_role, {})
        role_projects: list[dict] = role_data.get("projects", [])

        scored: list[tuple[int, dict]] = []
        for project in role_projects:
            skills_developed = [s.lower() for s in project.get("skills_developed", [])]
            # Score = number of missing skills this project addresses
            score = len(set(skills_developed) & set(missing_skills))
            scored.append((score, project))

        scored.sort(key=lambda x: x[0], reverse=True)
        recommended = [p for _, p in scored]

        # Filter by difficulty level
        level_order = ["Beginner", "Intermediate", "Advanced"]
        user_idx = level_order.index(experience_level) if experience_level in level_order else 0

        quick_wins = [
            p for p in recommended
            if level_order.index(p.get("difficulty", "Beginner")) <= user_idx
        ][:3]

        stretch_goals = [
            p for p in recommended
            if level_order.index(p.get("difficulty", "Beginner")) > user_idx
        ][:2]

        return {
            "projects": recommended[:6],
            "quick_wins": quick_wins,
            "stretch_goals": stretch_goals,
            "total_projects": len(recommended),
        }
