"""
Career Roadmap Agent
Generates a personalized, phased learning roadmap based on the user's profile
and skill gap analysis.
"""

from __future__ import annotations

from typing import Any

from data.role_data import ROLE_REQUIREMENTS


class RoadmapAgent:
    """Produces a Beginner → Intermediate → Advanced career roadmap."""

    def generate(self, profile: dict[str, Any], skill_gap: dict[str, Any]) -> dict[str, Any]:
        """
        Build a three-phase roadmap.

        Returns
        -------
        dict with keys: phases (list), total_duration, milestones, tips
        """
        target_role: str = profile.get("target_role", "")
        experience_level: str = profile.get("experience_level", "Beginner")
        need_to_learn: list[dict] = skill_gap.get("need_to_learn", [])
        need_to_improve: list[dict] = skill_gap.get("need_to_improve", [])

        role_data = ROLE_REQUIREMENTS.get(target_role, {})
        roadmap_template = role_data.get("roadmap", {})

        phases = self._build_phases(
            experience_level,
            need_to_learn,
            need_to_improve,
            roadmap_template,
            target_role,
        )

        total_weeks = sum(p.get("duration_weeks", 0) for p in phases)
        total_duration = self._weeks_to_human(total_weeks)

        milestones = [
            {"title": f"Phase {i + 1} Complete: {p['name']}", "week": sum(
                phases[j]["duration_weeks"] for j in range(i + 1)
            )}
            for i, p in enumerate(phases)
        ]

        tips = self._get_tips(experience_level, target_role)

        return {
            "phases": phases,
            "total_duration": total_duration,
            "total_weeks": total_weeks,
            "milestones": milestones,
            "tips": tips,
            "target_role": target_role,
        }

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _build_phases(
        self,
        experience_level: str,
        need_to_learn: list[dict],
        need_to_improve: list[dict],
        template: dict,
        role: str,
    ) -> list[dict]:
        high_priority = [s for s in need_to_learn if s.get("priority") == "High"]
        medium_priority = [s for s in need_to_learn if s.get("priority") == "Medium"]
        low_priority = [s for s in need_to_learn if s.get("priority") == "Low"]

        # Duration multiplier per experience level
        multiplier = {"Beginner": 1.4, "Intermediate": 1.0, "Advanced": 0.7}.get(
            experience_level, 1.0
        )

        phase1_weeks = max(4, round(len(high_priority) * 2 * multiplier))
        phase2_weeks = max(4, round((len(medium_priority) + len(need_to_improve)) * 2 * multiplier))
        phase3_weeks = max(4, round(len(low_priority) * 2 * multiplier) + 2)

        phases = [
            {
                "phase": 1,
                "name": "Foundation",
                "level": "Beginner",
                "duration_weeks": phase1_weeks,
                "skills_to_learn": [s["skill"] for s in high_priority],
                "objectives": template.get("phase1_objectives", self._default_objectives(1, role)),
                "projects": template.get("phase1_projects", [f"Build a basic {role.split()[0].lower()} starter project"]),
                "resources": self._get_resources("Beginner", high_priority),
                "icon": "🌱",
            },
            {
                "phase": 2,
                "name": "Development",
                "level": "Intermediate",
                "duration_weeks": phase2_weeks,
                "skills_to_learn": [s["skill"] for s in medium_priority]
                + [s["skill"] for s in need_to_improve],
                "objectives": template.get("phase2_objectives", self._default_objectives(2, role)),
                "projects": template.get("phase2_projects", [f"Build a complete {role.split()[0].lower()} project with real data"]),
                "resources": self._get_resources("Intermediate", medium_priority),
                "icon": "🚀",
            },
            {
                "phase": 3,
                "name": "Mastery",
                "level": "Advanced",
                "duration_weeks": phase3_weeks,
                "skills_to_learn": [s["skill"] for s in low_priority],
                "objectives": template.get("phase3_objectives", self._default_objectives(3, role)),
                "projects": template.get("phase3_projects", [f"Build a production-ready {role.split()[0].lower()} portfolio project"]),
                "resources": self._get_resources("Advanced", low_priority),
                "icon": "🏆",
            },
        ]
        return phases

    def _default_objectives(self, phase: int, role: str) -> list[str]:
        objectives = {
            1: [
                f"Understand the core concepts required for {role}",
                "Complete at least one foundational online course",
                "Build your first small project",
                "Join relevant communities and forums",
            ],
            2: [
                "Apply skills to real-world scenarios",
                "Contribute to open-source or personal projects",
                "Network with professionals in the field",
                "Earn at least one relevant certification",
            ],
            3: [
                "Develop a production-quality portfolio project",
                "Prepare resume, LinkedIn and GitHub profile",
                "Start applying for positions",
                "Practice interview skills (technical + behavioral)",
            ],
        }
        return objectives.get(phase, [])

    def _get_resources(self, level: str, skills: list[dict]) -> list[str]:
        base = {
            "Beginner": ["freeCodeCamp (freecodecamp.org)", "The Odin Project (theodinproject.com)", "Coursera (coursera.org)"],
            "Intermediate": ["Udemy courses", "YouTube tutorials", "Official documentation"],
            "Advanced": ["LeetCode (leetcode.com)", "Building real projects", "Technical blogs & research papers"],
        }
        resources = base.get(level, [])
        if skills:
            resources.append(f"Focused study on: {', '.join(s['skill'] for s in skills[:3])}")
        return resources

    def _weeks_to_human(self, weeks: int) -> str:
        if weeks <= 4:
            return f"{weeks} weeks"
        months = round(weeks / 4.3, 1)
        if months < 12:
            return f"~{months} months"
        years = round(months / 12, 1)
        return f"~{years} years"

    def _get_tips(self, experience_level: str, role: str) -> list[str]:
        general = [
            "Consistency beats intensity — study a little every day.",
            "Build projects as you learn; don't wait until you feel 'ready'.",
            "Document your work on GitHub — it's your living portfolio.",
            "Join Discord communities and LinkedIn groups for your target role.",
        ]
        level_tips = {
            "Beginner": [
                "Don't skip the basics — fundamentals pay dividends later.",
                "Use the Pomodoro technique: 25 min focus, 5 min break.",
            ],
            "Intermediate": [
                "Review job descriptions weekly to stay aligned with market needs.",
                "Start contributing to open-source projects.",
            ],
            "Advanced": [
                "Network proactively — many jobs are filled before public posting.",
                "Prepare a compelling 60-second professional pitch.",
            ],
        }
        return general + level_tips.get(experience_level, [])
