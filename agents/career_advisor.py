"""
Career Advisor Agent
Analyzes the user profile against the target role requirements and produces
a structured career analysis report.
"""

from __future__ import annotations

from typing import Any

from data.role_data import ROLE_REQUIREMENTS


class CareerAdvisorAgent:
    """Compares user skills to target-role requirements and produces a report."""

    def analyze(self, profile: dict[str, Any]) -> dict[str, Any]:
        """
        Run the career analysis.

        Parameters
        ----------
        profile : dict
            Keys: name, education, skills (list[str]), interests (list[str]),
                  target_role (str), experience_level (str)

        Returns
        -------
        dict with keys:
            target_role, required_skills, user_skills,
            matching_skills, missing_skills, match_percentage, advice
        """
        target_role: str = profile.get("target_role", "").strip()
        user_skills: list[str] = [s.strip().lower() for s in profile.get("skills", [])]
        experience_level: str = profile.get("experience_level", "Beginner")

        role_data = ROLE_REQUIREMENTS.get(target_role, {})
        required_skills: list[str] = [s.lower() for s in role_data.get("required_skills", [])]

        matching_skills = [s for s in required_skills if s in user_skills]
        missing_skills = [s for s in required_skills if s not in user_skills]

        match_percentage = (
            round(len(matching_skills) / len(required_skills) * 100, 1)
            if required_skills
            else 0.0
        )

        advice = self._generate_advice(
            match_percentage, experience_level, target_role, len(missing_skills)
        )

        return {
            "target_role": target_role,
            "required_skills": required_skills,
            "user_skills": user_skills,
            "matching_skills": matching_skills,
            "missing_skills": missing_skills,
            "match_percentage": match_percentage,
            "advice": advice,
            "role_description": role_data.get("description", ""),
            "avg_salary": role_data.get("avg_salary", "N/A"),
            "job_demand": role_data.get("job_demand", "N/A"),
        }

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _generate_advice(
        self,
        match_pct: float,
        experience: str,
        role: str,
        missing_count: int,
    ) -> str:
        if match_pct >= 80:
            return (
                f"Excellent! You have a strong match for the {role} role. "
                "Focus on the few remaining skills to become a top candidate. "
                "Start applying for positions and build portfolio projects to stand out."
            )
        if match_pct >= 60:
            return (
                f"You have a solid foundation for the {role} role. "
                f"You need to develop {missing_count} more key skills. "
                "With 3–6 months of focused learning, you can be job-ready."
            )
        if match_pct >= 40:
            return (
                f"You're on the right track for the {role} role. "
                f"There are {missing_count} important skills to develop. "
                "Follow the roadmap below and dedicate 6–9 months to skill building."
            )
        return (
            f"Starting your journey toward the {role} role. "
            f"You have {missing_count} core skills to acquire. "
            "This is completely normal — follow the structured roadmap and you'll get there!"
        )
