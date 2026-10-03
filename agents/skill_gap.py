"""
Skill Gap Agent
Categorizes user skills into: Already Have, Need to Learn, and Improve.
"""

from __future__ import annotations

from typing import Any

from data.role_data import ROLE_REQUIREMENTS, SKILL_LEVELS


class SkillGapAgent:
    """Categorizes skills and provides gap analysis details."""

    def analyze(self, profile: dict[str, Any], career_analysis: dict[str, Any]) -> dict[str, Any]:
        """
        Categorize skills based on the career analysis output.

        Returns
        -------
        dict with keys:
            already_have, need_to_learn, need_to_improve,
            skill_categories, gap_summary
        """
        target_role: str = career_analysis.get("target_role", "")
        user_skills: list[str] = career_analysis.get("user_skills", [])
        matching_skills: list[str] = career_analysis.get("matching_skills", [])
        missing_skills: list[str] = career_analysis.get("missing_skills", [])
        experience_level: str = profile.get("experience_level", "Beginner")

        role_data = ROLE_REQUIREMENTS.get(target_role, {})
        core_skills: set[str] = {s.lower() for s in role_data.get("core_skills", [])}
        advanced_skills: set[str] = {s.lower() for s in role_data.get("advanced_skills", [])}

        already_have: list[dict] = []
        for skill in matching_skills:
            level = SKILL_LEVELS.get(skill, "Intermediate")
            priority = "Core" if skill in core_skills else "Advanced" if skill in advanced_skills else "General"
            already_have.append({"skill": skill.title(), "level": level, "priority": priority})

        need_to_learn: list[dict] = []
        for skill in missing_skills:
            if skill in core_skills:
                priority = "High"
                reason = "Core requirement for this role"
            elif skill in advanced_skills:
                priority = "Medium"
                reason = "Advanced skill that increases competitiveness"
            else:
                priority = "Low"
                reason = "Nice-to-have for this role"
            need_to_learn.append({
                "skill": skill.title(),
                "priority": priority,
                "reason": reason,
                "estimated_time": self._estimate_time(skill, experience_level),
            })

        # Skills the user has but that could be strengthened
        need_to_improve: list[dict] = []
        improve_candidates = role_data.get("improve_skills", [])
        for skill in improve_candidates:
            if skill.lower() in user_skills:
                need_to_improve.append({
                    "skill": skill.title(),
                    "current_level": "Basic",
                    "target_level": "Proficient",
                    "reason": "Deeper mastery expected for this role",
                })

        # High-level summary by category
        skill_categories = {
            "Technical Skills": [s for s in (matching_skills + missing_skills) if s in core_skills | advanced_skills],
            "Soft Skills": role_data.get("soft_skills", []),
            "Tools & Frameworks": role_data.get("tools", []),
        }

        gap_summary = {
            "total_required": len(career_analysis.get("required_skills", [])),
            "already_have_count": len(already_have),
            "need_to_learn_count": len(need_to_learn),
            "need_to_improve_count": len(need_to_improve),
            "high_priority_gaps": [s for s in need_to_learn if s["priority"] == "High"],
        }

        return {
            "already_have": already_have,
            "need_to_learn": need_to_learn,
            "need_to_improve": need_to_improve,
            "skill_categories": skill_categories,
            "gap_summary": gap_summary,
        }

    def _estimate_time(self, skill: str, experience_level: str) -> str:
        base_times = {
            "Beginner": {"easy": "1–2 weeks", "medium": "3–4 weeks", "hard": "6–8 weeks"},
            "Intermediate": {"easy": "3–5 days", "medium": "1–2 weeks", "hard": "3–4 weeks"},
            "Advanced": {"easy": "1–3 days", "medium": "1 week", "hard": "2–3 weeks"},
        }
        difficulty_map = {
            "machine learning": "hard", "deep learning": "hard", "kubernetes": "hard",
            "docker": "medium", "react": "medium", "node.js": "medium",
            "sql": "easy", "git": "easy", "html": "easy", "css": "easy",
            "python": "medium", "java": "hard", "data analysis": "medium",
            "tensorflow": "hard", "pytorch": "hard", "aws": "hard",
        }
        difficulty = difficulty_map.get(skill.lower(), "medium")
        times = base_times.get(experience_level, base_times["Beginner"])
        return times[difficulty]
