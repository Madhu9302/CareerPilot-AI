# CareerPilot AI – Agentic Career Advisor

> **SDG 8 — Decent Work & Economic Growth**
> Bridging the skill-job mismatch for students and fresh graduates worldwide.

---

## Problem Statement

Every year, millions of students and fresh graduates enter the job market without a clear understanding of what skills their target role actually requires. The result is a widening **skill-job mismatch**: employers struggle to find qualified candidates while job-seekers apply for roles they are not yet prepared for.

Key issues:
- No personalised, actionable feedback on exactly which skills to develop
- Career guidance is expensive, inaccessible, or generic
- Students waste months learning the wrong things in the wrong order
- Fresh graduates lack portfolio projects that demonstrate job-readiness

---

## SDG 8 Connection

**Goal 8 – Decent Work and Economic Growth**

> *"Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all."*

CareerPilot AI directly addresses **Target 8.6**: *"Substantially reduce the proportion of youth not in employment, education or training"* by giving every student and fresh graduate — regardless of background or financial means — a free, personalised, and actionable career development plan.

By eliminating the information asymmetry between what employers need and what candidates know, CareerPilot AI accelerates productive employment and supports inclusive economic growth.

---

## Proposed Solution

CareerPilot AI is a fully local, free-to-run **Agentic AI Career Advisor** built with Streamlit. It uses five specialised AI agents coordinated by an orchestrator to:

1. **Analyse** the user's current skills against real requirements for their target role
2. **Identify** exactly which skills are matched, missing, or need deepening
3. **Generate** a personalised 3-phase learning roadmap (Beginner → Intermediate → Advanced)
4. **Recommend** hands-on portfolio projects ranked by how well they close skill gaps
5. **Mentor** the user through a conversational AI career chat — no paid API required

The entire system runs locally and requires no API keys, no subscription, and no internet connection after setup.

---

## Key Features

| Feature | Description |
|---|---|
| 📊 **Skill Match Analysis** | Transparent percentage score comparing user skills against role requirements |
| 🔍 **Skill Gap Agent** | Categorises skills into: Already Have · Need to Learn · Need to Improve, with priorities |
| 🗺️ **Career Roadmap Agent** | Personalised 3-phase roadmap with objectives, projects, and resource links |
| 🛠️ **Project Recommender Agent** | Portfolio projects ranked by how directly they close the user's skill gaps |
| 💬 **AI Career Mentor** | Intent-aware conversational mentor covering salary, resume, interviews, networking, and more |
| 🤖 **Agentic Architecture** | 5 specialised agents coordinated by a central orchestration layer |
| 🌍 **10 Supported Roles** | Data Scientist, Software Engineer, Web Developer, ML Engineer, Data Analyst, DevOps, Cybersecurity, Product Manager, UX Designer, Cloud Engineer |
| 🔒 **No API Keys** | Fully local — no paid services, no secrets, no internet required |

---

## Agentic Architecture

```
User Profile Input
       │
       ▼
  Orchestrator  (services/orchestrator.py)
       │
       │  passes profile
       ├──▶  CareerAdvisorAgent      →  skill match %, matched/missing skills, advice
       │         (agents/career_advisor.py)
       │
       │  passes career_analysis
       ├──▶  SkillGapAgent           →  skills categorised by priority + estimated learning time
       │         (agents/skill_gap.py)
       │
       │  passes skill_gap
       ├──▶  RoadmapAgent            →  3-phase roadmap with objectives, projects, resources
       │         (agents/roadmap.py)
       │
       │  passes skill_gap
       ├──▶  ProjectRecommenderAgent →  portfolio projects scored against skill gaps
       │         (agents/project_recommender.py)
       │
       │  called per chat turn (stateful)
       └──▶  CareerMentorAgent       →  intent-based conversational career mentor
                 (agents/career_mentor.py)
```

Each agent is **independent and single-responsibility**. The Orchestrator manages the data flow, passing each agent's output as input to the next where needed.

---

## Technology Stack

| Layer | Technology |
|---|---|
| **UI Framework** | [Streamlit](https://streamlit.io) ≥ 1.32 |
| **Data Handling** | [Pandas](https://pandas.pydata.org) ≥ 2.0 |
| **Language** | Python 3.9+ |
| **Architecture** | Modular agentic pattern with central orchestrator |
| **AI / ML** | Rule-based intent detection + knowledge base (no external LLM required) |
| **Deployment** | Local · Streamlit Community Cloud · Any Python-capable host |

No paid APIs. No cloud dependencies. No environment variables required to run.

---

## Project Structure

```
CareerPilot-AI/
├── app.py                       # Main Streamlit application entry point
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── .gitignore
│
├── agents/                      # Specialised AI agents
│   ├── __init__.py
│   ├── career_advisor.py        # Skill-match analysis & career advice
│   ├── skill_gap.py             # Skill categorisation with priorities
│   ├── roadmap.py               # 3-phase personalised learning roadmap
│   ├── project_recommender.py   # Portfolio project recommendations
│   └── career_mentor.py         # Conversational AI career mentor
│
├── services/
│   └── orchestrator.py          # Agent coordination & pipeline management
│
└── data/
    ├── __init__.py
    └── role_data.py             # Role requirements, project library & skill data
```

---

## Installation

### Prerequisites
- Python 3.9 or higher
- pip

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/CareerPilot-AI.git
cd CareerPilot-AI

# 2. Create and activate a virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## How to Run

```bash
streamlit run app.py
```

The app opens automatically at **http://localhost:8501** in your default browser.

To stop the server: press `Ctrl + C` in the terminal.

---

## Example Workflow

Here is a complete walkthrough of how a user interacts with CareerPilot AI:

**1. Enter your profile** *(sidebar)*
- Name: `Alex Johnson`
- Education: `Bachelor's Degree`
- Target Role: `Data Scientist`
- Experience Level: `Beginner`
- Current Skills: `Python, SQL, Excel, Statistics, Git`

**2. Click "Analyze My Career"**
- The Orchestrator runs all 4 analysis agents in sequence
- Results appear across 5 tabs instantly

**3. Overview tab**
- Skill Match: **41.7%** against Data Scientist requirements
- Matched skills: Python, SQL, Statistics, Git
- Missing skills: Machine Learning, Scikit-learn, Pandas, Matplotlib…
- Career Advisor message: personalised advice based on match level

**4. Skill Gap tab**
- **Already Have**: Python (Proficient · Core), SQL (Intermediate · Core)…
- **High Priority gaps**: Machine Learning, Data Visualization
- **Need to Improve**: Python, SQL — deeper mastery expected

**5. Roadmap tab**
- **Phase 1 – Foundation** (6 weeks): Core Python, SQL, statistics, first Kaggle project
- **Phase 2 – Development** (8 weeks): ML models, certifications, dashboards
- **Phase 3 – Mastery** (6 weeks): Deep learning, MLflow pipeline, portfolio
- Total estimated duration: **~7 months**

**6. Projects tab**
- ⚡ Quick Win: *Customer Churn Predictor* (Beginner · 1–2 weeks)
- ⚡ Quick Win: *Sales Analytics Dashboard* (Beginner · 1 week)
- Full list of 6 ranked projects with skills developed and deliverables

**7. Career Mentor tab** *(chat)*
- Ask: *"What salary can I expect?"* → market salary ranges + negotiation tips
- Ask: *"How do I prepare for interviews?"* → STAR method + sample DS interview questions
- Ask: *"How do I build a portfolio?"* → GitHub tips, deployment platforms, what to include

---

## Adding a New Role

Edit [`data/role_data.py`](data/role_data.py) and add a new entry to the `ROLE_REQUIREMENTS` dictionary following the existing schema. The application picks it up automatically — no other changes required.

---

## Security

- **No API keys** are hard-coded or required anywhere in the project
- **No external network calls** are made at runtime
- All user data stays in browser session memory only — nothing is persisted or transmitted

---

## License

MIT License — free to use, modify, and distribute.
