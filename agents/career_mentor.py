"""
Career Mentor Agent
Provides a rule-based conversational AI mentor that answers career questions
without requiring any paid external API.
"""

from __future__ import annotations

import random
import re
from typing import Any


class CareerMentorAgent:
    """Rule-based career mentor chatbot with contextual responses."""

    # ------------------------------------------------------------------
    # Intent patterns → handler methods
    # ------------------------------------------------------------------
    _INTENTS: list[tuple[list[str], str]] = [
        (["hello", "hi", "hey", "greet"], "greet"),
        (["salary", "pay", "earn", "compensation", "money"], "salary"),
        (["resume", "cv", "curriculum"], "resume"),
        (["interview", "prepare", "preparation", "question"], "interview"),
        (["skill", "learn", "study", "course", "certificate"], "skills"),
        (["job", "apply", "application", "position", "opening"], "job_search"),
        (["linkedin", "network", "connection", "profile"], "networking"),
        (["freelance", "freelancing", "remote", "contract"], "freelance"),
        (["github", "portfolio", "project", "showcase"], "portfolio"),
        (["roadmap", "plan", "path", "steps"], "roadmap"),
        (["motivation", "discourage", "stuck", "help", "advice"], "motivation"),
        (["thank", "thanks", "appreciate"], "thanks"),
    ]

    def __init__(self):
        self._context: dict[str, Any] = {}

    def chat(
        self,
        user_message: str,
        profile: dict[str, Any] | None = None,
        analysis: dict[str, Any] | None = None,
        history: list[dict[str, str]] | None = None,
    ) -> str:
        """
        Respond to a user message.

        Parameters
        ----------
        user_message : str
        profile      : user profile dict (optional, for personalization)
        analysis     : career analysis dict (optional)
        history      : list of {role, content} dicts

        Returns
        -------
        str – mentor response
        """
        if profile:
            self._context["profile"] = profile
        if analysis:
            self._context["analysis"] = analysis

        msg_lower = user_message.lower().strip()
        intent = self._detect_intent(msg_lower)
        handler = getattr(self, f"_handle_{intent}", self._handle_generic)
        return handler(user_message, msg_lower)

    # ------------------------------------------------------------------
    # Intent detection
    # ------------------------------------------------------------------

    def _detect_intent(self, text: str) -> str:
        for keywords, intent in self._INTENTS:
            if any(kw in text for kw in keywords):
                return intent
        return "generic"

    # ------------------------------------------------------------------
    # Intent handlers
    # ------------------------------------------------------------------

    def _handle_greet(self, _raw: str, _lower: str) -> str:
        profile = self._context.get("profile", {})
        name = profile.get("name", "there")
        role = profile.get("target_role", "your target role")
        return (
            f"Hi {name}! 👋 Great to have you here. I'm your AI Career Mentor.\n\n"
            f"I see you're aiming for a **{role}** position — that's a fantastic goal! "
            "I'm here to answer your career questions, give advice on job searching, "
            "resumes, interviews, skill-building and more.\n\n"
            "What would you like to know?"
        )

    def _handle_salary(self, _raw: str, _lower: str) -> str:
        analysis = self._context.get("analysis", {})
        role = analysis.get("target_role") or self._context.get("profile", {}).get("target_role", "your target role")
        avg_salary = analysis.get("avg_salary", "N/A")
        tips = [
            f"For **{role}**, the typical salary range is **{avg_salary}** depending on location and experience.",
            "",
            "💡 **Salary negotiation tips:**",
            "- Research market rates on Glassdoor, LinkedIn Salary, and Levels.fyi",
            "- Never give the first number — let the employer anchor",
            "- Consider the full package: benefits, equity, remote flexibility",
            "- Confidence matters — know your worth and articulate your value",
            "- It's always okay to ask for time to consider an offer",
        ]
        return "\n".join(tips)

    def _handle_resume(self, _raw: str, _lower: str) -> str:
        profile = self._context.get("profile", {})
        role = profile.get("target_role", "your target role")
        return (
            f"Here's how to craft a strong resume for **{role}**:\n\n"
            "📄 **Resume Best Practices:**\n"
            "- Keep it to **1 page** (2 pages max with 5+ years experience)\n"
            "- Use **action verbs**: Built, Designed, Implemented, Led, Optimized\n"
            "- **Quantify impact**: 'Improved performance by 40%' beats 'improved performance'\n"
            "- Tailor your resume for **each job description** — mirror their keywords\n"
            "- List skills from your profile prominently in a dedicated Skills section\n"
            "- Include links to your **GitHub, portfolio, or LinkedIn**\n\n"
            "🛠️ Free tools: **resume.io**, **Zety**, **Canva**, **Overleaf** (LaTeX)\n\n"
            "Would you like specific advice on any section?"
        )

    def _handle_interview(self, _raw: str, _lower: str) -> str:
        profile = self._context.get("profile", {})
        role = profile.get("target_role", "your target role")
        questions = {
            "Data Scientist": ["Explain overfitting and how to prevent it", "Walk me through a data project end-to-end"],
            "Software Engineer": ["What is Big-O notation?", "Explain the difference between REST and GraphQL"],
            "Web Developer": ["Explain the box model in CSS", "What is the difference between == and === in JavaScript?"],
            "Machine Learning Engineer": ["Explain backpropagation", "What is the bias-variance trade-off?"],
            "Data Analyst": ["How do you handle missing data?", "What is a pivot table used for?"],
            "DevOps Engineer": ["What is CI/CD?", "Explain the difference between Docker and a VM"],
            "Cybersecurity Analyst": ["What is a man-in-the-middle attack?", "Explain the CIA triad"],
            "Product Manager": ["How do you prioritize features?", "Tell me about a product you admire and why"],
            "UX Designer": ["Walk me through your design process", "How do you conduct user research?"],
            "Cloud Engineer": ["What is the difference between IaaS, PaaS, and SaaS?", "Explain auto-scaling"],
        }
        sample_qs = questions.get(role, ["Tell me about yourself", "What are your greatest strengths?"])
        return (
            f"🎯 **Interview Prep for {role}:**\n\n"
            "**General Tips:**\n"
            "- Use the **STAR method** (Situation, Task, Action, Result) for behavioral questions\n"
            "- Research the company: products, culture, recent news\n"
            "- Prepare 3–5 thoughtful questions to ask the interviewer\n"
            "- Do a mock interview out loud — recording yourself helps\n\n"
            f"**Sample technical questions for {role}:**\n"
            + "\n".join(f"- {q}" for q in sample_qs)
            + "\n\n💬 Practice these aloud. The more you explain, the more confident you'll become!"
        )

    def _handle_skills(self, _raw: str, _lower: str) -> str:
        analysis = self._context.get("analysis", {})
        missing = analysis.get("missing_skills", [])[:3]
        tips = (
            "📚 **Skill-Building Strategy:**\n\n"
            "- Follow the **80/20 rule**: focus on the 20% of skills that unlock 80% of opportunities\n"
            "- Use **spaced repetition** — revisit concepts regularly, not just once\n"
            "- Build projects *while* learning, not after\n"
            "- Free platforms: **freeCodeCamp, Coursera (audit), YouTube, edX**\n"
            "- Paid (worth it): **Udemy, Pluralsight, LinkedIn Learning**\n"
        )
        if missing:
            tips += f"\n🎯 Based on your profile, focus next on: **{', '.join(s.title() for s in missing)}**"
        return tips

    def _handle_job_search(self, _raw: str, _lower: str) -> str:
        profile = self._context.get("profile", {})
        role = profile.get("target_role", "your target role")
        return (
            f"🔍 **Job Search Strategy for {role}:**\n\n"
            "**Where to look:**\n"
            "- LinkedIn Jobs (set job alerts!)\n"
            "- Indeed, Glassdoor, Wellfound (startups)\n"
            "- Company career pages directly\n"
            "- Hackathons and meetups (hidden job market)\n\n"
            "**Approach:**\n"
            "- Apply **quality over quantity** — tailor each application\n"
            "- Reach out to **hiring managers directly** on LinkedIn\n"
            "- Track applications in a spreadsheet to stay organized\n"
            "- Follow up politely 5–7 days after applying\n\n"
            "⚡ **80% of jobs are filled through networking** — don't rely only on job boards!"
        )

    def _handle_networking(self, _raw: str, _lower: str) -> str:
        return (
            "🤝 **Networking Tips:**\n\n"
            "- Optimize your **LinkedIn headline** — include your target role and key skills\n"
            "- Post weekly: share what you're learning, projects, and insights\n"
            "- Send personalized connection requests with a short, genuine note\n"
            "- Engage genuinely with content in your target field\n"
            "- Attend virtual and in-person **meetups, conferences, and hackathons**\n"
            "- Find a **mentor** — many professionals are happy to help if you ask respectfully\n\n"
            "📌 Tip: 'Informational interviews' (15 min calls to learn about someone's role) are "
            "incredibly effective — most people say yes!"
        )

    def _handle_freelance(self, _raw: str, _lower: str) -> str:
        return (
            "💼 **Freelancing & Remote Work:**\n\n"
            "**Platforms to start:**\n"
            "- Upwork, Fiverr (general)\n"
            "- Toptal (top 3%, higher rates)\n"
            "- Gun.io (developers)\n"
            "- Contra, Braintrust (newer, lower fees)\n\n"
            "**Getting your first client:**\n"
            "- Start with your network — friends, professors, local businesses\n"
            "- Underprice slightly at first to build reviews and portfolio\n"
            "- Create clear proposals that focus on **client outcomes**, not just your skills\n\n"
            "🎯 Niche down — specialists earn 2–3× more than generalists on freelance platforms!"
        )

    def _handle_portfolio(self, _raw: str, _lower: str) -> str:
        analysis = self._context.get("analysis", {})
        role = analysis.get("target_role") or self._context.get("profile", {}).get("target_role", "your field")
        return (
            f"🗂️ **Building a Strong Portfolio for {role}:**\n\n"
            "- **Quality over quantity** — 3 excellent projects beat 10 mediocre ones\n"
            "- Each project should solve a **real problem** or replicate something real\n"
            "- Write a clear **README** for every GitHub repo: what it does, how to run it, what you learned\n"
            "- Deploy your projects — live demos are far more impressive than code alone\n"
            "  (Use: **Vercel, Netlify, Streamlit Cloud, Render, Railway**)\n\n"
            "📌 **Portfolio must-haves:**\n"
            "- A personal website/portfolio page\n"
            "- Active GitHub with green contribution graph\n"
            "- A capstone project that shows end-to-end thinking\n\n"
            "Start today — one project on GitHub is better than nothing!"
        )

    def _handle_roadmap(self, _raw: str, _lower: str) -> str:
        profile = self._context.get("profile", {})
        role = profile.get("target_role", "your target role")
        level = profile.get("experience_level", "Beginner")
        return (
            f"🗺️ **Your Career Roadmap for {role} ({level}):**\n\n"
            "Check the **Career Roadmap** tab in this app for your personalized plan!\n\n"
            "In general, the path is:\n"
            "1. **Foundation (Phase 1)** — Core skills, first projects, community\n"
            "2. **Development (Phase 2)** — Real projects, certifications, networking\n"
            "3. **Mastery (Phase 3)** — Portfolio polish, job applications, interviews\n\n"
            "💡 The roadmap updates dynamically based on your skill analysis — "
            "go to the Roadmap tab to see your specific plan!"
        )

    def _handle_motivation(self, _raw: str, _lower: str) -> str:
        quotes = [
            "\"Every expert was once a beginner.\" — The key is to keep going.",
            "\"It always seems impossible until it's done.\" — Nelson Mandela",
            "\"The secret of getting ahead is getting started.\" — Mark Twain",
        ]
        return (
            f"💪 **You've got this!**\n\n"
            f"{random.choice(quotes)}\n\n"
            "Feeling stuck is normal — it means you're growing.\n\n"
            "**Practical reset tips:**\n"
            "- Break your goal into the smallest possible next action\n"
            "- Celebrate small wins — every skill learned is progress\n"
            "- Find an accountability partner or study group\n"
            "- Remember *why* you started — revisit your target role and what it means to you\n\n"
            "I'm here whenever you need guidance. What would you like to work on next?"
        )

    def _handle_thanks(self, _raw: str, _lower: str) -> str:
        profile = self._context.get("profile", {})
        name = profile.get("name", "")
        return (
            f"You're very welcome{', ' + name if name else ''}! 😊 "
            "That's what I'm here for. Keep pushing forward — "
            "your commitment to growth is what will set you apart. "
            "Feel free to ask anything else anytime!"
        )

    def _handle_generic(self, raw: str, lower: str) -> str:
        profile = self._context.get("profile", {})
        role = profile.get("target_role", "your target role")
        analysis = self._context.get("analysis", {})
        match_pct = analysis.get("match_percentage", 0)

        suggestions = [
            f"your skill progress toward {role}",
            "resume tips",
            "interview preparation",
            "how to find job opportunities",
            "building a portfolio",
            "salary negotiation",
        ]
        suggestion = random.choice(suggestions)

        return (
            f"That's a great question! While I'm optimized for career-related guidance, "
            f"I'll do my best to help.\n\n"
            f"Based on your profile, you're working toward **{role}** "
            f"with a current match of **{match_pct}%**.\n\n"
            f"Would you like to discuss **{suggestion}**? "
            "Or feel free to ask about resumes, interviews, skills, job search, "
            "networking, or your roadmap!"
        )
