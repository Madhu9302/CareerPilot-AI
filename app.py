"""
CareerPilot AI – Agentic Career Advisor
========================================
Main Streamlit application entry point.

Run with:
    streamlit run app.py
"""

from __future__ import annotations

import streamlit as st

# ── Page config (must be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

from services.orchestrator import Orchestrator  # noqa: E402 (after set_page_config)

# ── Constants ───────────────────────────────────────────────────────────────
EXPERIENCE_LEVELS = ["Beginner", "Intermediate", "Advanced"]
EDUCATION_OPTIONS = [
    "High School / Secondary",
    "Associate Degree",
    "Bachelor's Degree",
    "Master's Degree",
    "PhD / Doctorate",
    "Bootcamp / Self-taught",
    "Other",
]

# ── Custom CSS ───────────────────────────────────────────────────────────────
def inject_css():
    st.markdown(
        """
        <style>
        /* ── Global ── */
        .main .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
        h1, h2, h3 { font-weight: 700; }
        a { color: #3b82d4; text-decoration: none; }

        /* ── Card ── */
        .cp-card {
            background: #f7f8fa;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 1.2rem 1.4rem;
            margin-bottom: 1rem;
        }
        .cp-card-title {
            font-size: 0.85rem;
            font-weight: 600;
            color: #57606a;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.3rem;
        }
        .cp-card-value {
            font-size: 2rem;
            font-weight: 800;
            color: #1f2328;
        }

        /* ── Skill badges ── */
        .skill-badge {
            display: inline-block;
            padding: 0.25rem 0.65rem;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 600;
            margin: 0.2rem;
        }
        .badge-have   { background: #dcfce7; color: #166534; border: 1px solid #86efac; }
        .badge-learn  { background: #fef9c3; color: #854d0e; border: 1px solid #fde047; }
        .badge-improve{ background: #e0f2fe; color: #0c4a6e; border: 1px solid #7dd3fc; }
        .badge-high   { background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }

        /* ── Phase cards ── */
        .phase-card {
            border-left: 4px solid #3b82d4;
            background: #f7f8fa;
            padding: 1rem 1.2rem;
            border-radius: 0 8px 8px 0;
            margin-bottom: 1rem;
        }
        .phase-beginner  { border-left-color: #22c55e; }
        .phase-intermediate { border-left-color: #f59e0b; }
        .phase-advanced  { border-left-color: #ef4444; }

        /* ── Project card ── */
        .proj-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 1rem 1.2rem;
            margin-bottom: 0.8rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .proj-title { font-size: 1.05rem; font-weight: 700; color: #1f2328; }
        .proj-meta  { font-size: 0.8rem; color: #57606a; margin-top: 0.2rem; }

        /* ── Chat ── */
        .chat-user {
            background: #3b82d4;
            color: #ffffff;
            padding: 0.6rem 1rem;
            border-radius: 14px 14px 4px 14px;
            margin: 0.4rem 0 0.4rem 20%;
            font-size: 0.9rem;
        }
        .chat-bot {
            background: #f7f8fa;
            border: 1px solid #e5e7eb;
            padding: 0.6rem 1rem;
            border-radius: 14px 14px 14px 4px;
            margin: 0.4rem 20% 0.4rem 0;
            font-size: 0.9rem;
        }

        /* ── Progress bar override ── */
        div[data-testid="stProgress"] > div { height: 12px; border-radius: 6px; }

        /* ── Main-area radio navigation bar ── */
        /* Scope tightly to the main block container so sidebar is unaffected */
        .main div[data-testid="stHorizontalBlock"] div[data-testid="stRadio"] > div,
        .main .stRadio > div[role="radiogroup"] {
            display: flex !important;
            flex-direction: row !important;
            gap: 4px !important;
            background: #f7f8fa !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 10px !important;
            padding: 4px !important;
        }
        /* Each radio option label — make it look like a nav pill */
        .main .stRadio label,
        div[data-testid="stForm"] .stRadio label {
            display: flex !important;
            align-items: center !important;
            padding: 0.45rem 1rem !important;
            border-radius: 7px !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            cursor: pointer !important;
            pointer-events: auto !important;
            color: #57606a !important;
            transition: background 0.15s, color 0.15s !important;
            white-space: nowrap !important;
            user-select: none !important;
        }
        .main .stRadio label:hover {
            background: #e9ecef !important;
            color: #1f2328 !important;
        }
        /* Hide the actual radio circle dots */
        .main .stRadio input[type="radio"] {
            display: none !important;
        }
        /* Active (checked) pill */
        .main .stRadio input[type="radio"]:checked + div,
        .main .stRadio input[type="radio"]:checked ~ div,
        .main .stRadio label:has(input[type="radio"]:checked) {
            background: #3b82d4 !important;
            color: #ffffff !important;
            border-radius: 7px !important;
        }
        /* BaseWeb radio group used by st.radio horizontal */
        .main [data-testid="stRadio"] [role="radiogroup"] {
            flex-wrap: nowrap !important;
            gap: 4px !important;
        }
        .main [data-testid="stRadio"] [data-baseweb="radio"] {
            margin: 0 !important;
        }

        /* ── Sidebar shell ── */
        section[data-testid="stSidebar"] { background: #161b22; }
        section[data-testid="stSidebar"] hr { border-color: #30363d; }

        /* ── Sidebar: all text / labels ── */
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] div,
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] small,
        section[data-testid="stSidebar"] .stMarkdown,
        section[data-testid="stSidebar"] .stSelectbox label,
        section[data-testid="stSidebar"] .stTextInput label,
        section[data-testid="stSidebar"] .stTextArea label,
        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
            color: #e6edf3 !important;
        }

        /* ── Sidebar: text_input ── */
        section[data-testid="stSidebar"] input,
        section[data-testid="stSidebar"] input[type="text"],
        section[data-testid="stSidebar"] .stTextInput input {
            background-color: #21262d !important;
            color: #e6edf3 !important;
            caret-color: #e6edf3 !important;
            border: 1px solid #30363d !important;
            border-radius: 6px !important;
        }
        section[data-testid="stSidebar"] input:focus,
        section[data-testid="stSidebar"] .stTextInput input:focus {
            border-color: #3b82d4 !important;
            box-shadow: 0 0 0 2px rgba(59,130,212,0.3) !important;
            outline: none !important;
        }
        section[data-testid="stSidebar"] input::placeholder,
        section[data-testid="stSidebar"] .stTextInput input::placeholder {
            color: #8b949e !important;
            opacity: 1 !important;
        }

        /* ── Sidebar: text_area ── */
        section[data-testid="stSidebar"] textarea,
        section[data-testid="stSidebar"] .stTextArea textarea {
            background-color: #21262d !important;
            color: #e6edf3 !important;
            caret-color: #e6edf3 !important;
            border: 1px solid #30363d !important;
            border-radius: 6px !important;
            resize: vertical;
        }
        section[data-testid="stSidebar"] textarea:focus,
        section[data-testid="stSidebar"] .stTextArea textarea:focus {
            border-color: #3b82d4 !important;
            box-shadow: 0 0 0 2px rgba(59,130,212,0.3) !important;
            outline: none !important;
        }
        section[data-testid="stSidebar"] textarea::placeholder,
        section[data-testid="stSidebar"] .stTextArea textarea::placeholder {
            color: #8b949e !important;
            opacity: 1 !important;
        }

        /* ── Sidebar: selectbox ── */
        section[data-testid="stSidebar"] .stSelectbox > div > div,
        section[data-testid="stSidebar"] [data-baseweb="select"] > div,
        section[data-testid="stSidebar"] [data-baseweb="select"] div[class*="ValueContainer"],
        section[data-testid="stSidebar"] [data-baseweb="select"] div[class*="singleValue"] {
            background-color: #21262d !important;
            color: #e6edf3 !important;
            border-color: #30363d !important;
        }
        section[data-testid="stSidebar"] [data-baseweb="select"] svg {
            fill: #8b949e !important;
        }
        /* Dropdown menu panel */
        [data-baseweb="popover"] [data-baseweb="menu"],
        [data-baseweb="popover"] ul {
            background-color: #21262d !important;
            border: 1px solid #30363d !important;
        }
        [data-baseweb="popover"] li,
        [data-baseweb="popover"] [role="option"] {
            background-color: #21262d !important;
            color: #e6edf3 !important;
        }
        [data-baseweb="popover"] li:hover,
        [data-baseweb="popover"] [role="option"]:hover,
        [data-baseweb="popover"] [aria-selected="true"] {
            background-color: #30363d !important;
            color: #ffffff !important;
        }

        /* ── Sidebar: primary button ── */
        section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background-color: #3b82d4 !important;
            color: #ffffff !important;
            border: none !important;
            font-weight: 700 !important;
        }
        section[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
            background-color: #2563b0 !important;
        }
        /* Secondary / default sidebar buttons */
        section[data-testid="stSidebar"] .stButton > button:not([kind="primary"]) {
            background-color: #21262d !important;
            color: #e6edf3 !important;
            border: 1px solid #30363d !important;
        }
        section[data-testid="stSidebar"] .stButton > button:not([kind="primary"]):hover {
            background-color: #30363d !important;
            color: #ffffff !important;
        }

        /* ── Sidebar: help tooltip icon ── */
        section[data-testid="stSidebar"] [data-testid="stTooltipIcon"] svg {
            fill: #8b949e !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ── Helpers ──────────────────────────────────────────────────────────────────

def metric_card(label: str, value: str, sub: str = "") -> None:
    sub_html = f'<div style="font-size:0.78rem;color:#57606a;margin-top:0.1rem">{sub}</div>' if sub else ""
    st.markdown(
        f"""
        <div class="cp-card">
            <div class="cp-card-title">{label}</div>
            <div class="cp-card-value">{value}</div>
            {sub_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def skill_badge(skill: str, badge_class: str) -> str:
    return f'<span class="skill-badge {badge_class}">{skill}</span>'


def badge_row(skills: list, badge_class: str) -> None:
    if not skills:
        st.markdown("_None_")
        return
    st.markdown(
        " ".join(skill_badge(s, badge_class) for s in skills),
        unsafe_allow_html=True,
    )


def difficulty_color(difficulty: str) -> str:
    colors = {"Beginner": "#22c55e", "Intermediate": "#f59e0b", "Advanced": "#ef4444"}
    return colors.get(difficulty, "#3b82d4")


def render_match_gauge(pct: float) -> None:
    """Render a visual skill-match percentage bar."""
    color = "#22c55e" if pct >= 70 else "#f59e0b" if pct >= 40 else "#ef4444"
    label = "Strong" if pct >= 70 else "Moderate" if pct >= 40 else "Early Stage"
    st.markdown(
        f"""
        <div style="margin: 0.5rem 0 1.2rem 0;">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
                <span style="font-weight:700;font-size:1.1rem;color:{color}">{pct}%</span>
                <span style="font-size:0.85rem;color:#57606a">{label} match</span>
            </div>
            <div style="background:#e5e7eb;border-radius:6px;height:14px;">
                <div style="background:{color};width:{pct}%;height:14px;border-radius:6px;
                     transition:width 0.5s ease;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Session state initializer ─────────────────────────────────────────────────

def init_state() -> None:
    defaults = {
        "analysis_done": False,
        "results": None,
        "chat_history": [],
        "profile": {},
        "nav_tab": "📊 Overview",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ── Sidebar ───────────────────────────────────────────────────────────────────

def render_sidebar(orchestrator: Orchestrator) -> dict | None:
    """Render sidebar navigation and profile form. Returns profile dict on submit."""
    available_roles = orchestrator.get_available_roles()

    with st.sidebar:
        st.markdown("## 🧭 CareerPilot AI")
        st.markdown("*Agentic Career Advisor*")
        st.markdown("---")

        st.markdown("### 👤 Your Profile")

        name = st.text_input("Full Name", placeholder="e.g. Alex Johnson", key="sb_name")

        education = st.selectbox("Education Level", EDUCATION_OPTIONS, key="sb_education")

        target_role = st.selectbox(
            "Target Job Role",
            available_roles,
            key="sb_role",
            help="Select the role you want to work towards",
        )

        experience_level = st.selectbox(
            "Experience Level",
            EXPERIENCE_LEVELS,
            key="sb_exp",
        )

        skills_input = st.text_area(
            "Current Skills",
            placeholder="e.g. Python, SQL, Excel, Git\n(comma or newline separated)",
            height=100,
            key="sb_skills",
        )

        interests_input = st.text_area(
            "Interests",
            placeholder="e.g. Data Analysis, Machine Learning, Problem Solving",
            height=70,
            key="sb_interests",
        )

        st.markdown("---")
        analyze_btn = st.button("🚀 Analyze My Career", use_container_width=True, type="primary")

        if analyze_btn:
            if not name.strip():
                st.error("Please enter your name.")
                return None
            if not skills_input.strip():
                st.error("Please enter at least one skill.")
                return None

            # Parse skills/interests
            raw_skills = [s.strip() for s in skills_input.replace("\n", ",").split(",") if s.strip()]
            raw_interests = [i.strip() for i in interests_input.replace("\n", ",").split(",") if i.strip()]

            profile = {
                "name": name.strip(),
                "education": education,
                "skills": raw_skills,
                "interests": raw_interests,
                "target_role": target_role,
                "experience_level": experience_level,
            }
            return profile

        # Quick-fill demo
        st.markdown("---")
        st.markdown("##### 🎯 Quick Demo")
        if st.button("Load Sample Profile", use_container_width=True):
            st.session_state["sb_name"] = "Alex Johnson"
            st.session_state["sb_skills"] = "Python, SQL, Excel, Statistics, Git, Data Analysis"
            st.session_state["sb_interests"] = "Machine Learning, Data Visualization, Problem Solving"
            st.rerun()

        st.markdown("---")
        st.markdown(
            "<div style='font-size:0.75rem;color:#8b949e;text-align:center'>"
            "CareerPilot AI · SDG 8<br>Decent Work & Economic Growth"
            "</div>",
            unsafe_allow_html=True,
        )

    return None


# ── Tab: Overview ─────────────────────────────────────────────────────────────

def render_overview(results: dict) -> None:
    profile = results["profile"]
    ca = results["career_analysis"]
    sg = results["skill_gap"]

    st.markdown(f"## Welcome, {profile['name']}! 👋")
    st.markdown(
        f"Here's your personalized career analysis for **{ca['target_role']}**. "
        f"Follow the roadmap and project recommendations below to close your skill gaps."
    )

    # ── Top metrics ──
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("Skill Match", f"{ca['match_percentage']}%", "vs. role requirements")
    with col2:
        metric_card("Skills You Have", str(len(ca["matching_skills"])), "matched skills")
    with col3:
        metric_card("Skills to Gain", str(len(ca["missing_skills"])), "gap skills")
    with col4:
        metric_card("Job Demand", ca.get("job_demand", "N/A"), ca["target_role"])

    # ── Match gauge ──
    st.markdown("### 📊 Skill Match Overview")
    render_match_gauge(ca["match_percentage"])

    # ── Role info ──
    if ca.get("role_description"):
        with st.expander("ℹ️ About this role", expanded=False):
            cols = st.columns([2, 1])
            with cols[0]:
                st.markdown(ca["role_description"])
            with cols[1]:
                st.markdown(f"**💰 Avg. Salary**\n\n{ca.get('avg_salary', 'N/A')}")
                st.markdown(f"**📈 Demand**\n\n{ca.get('job_demand', 'N/A')}")

    # ── Advisor advice ──
    st.info(f"💡 **Career Advisor:** {ca['advice']}")

    # ── Skills summary ──
    st.markdown("### 🎯 Skills Summary")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**✅ Skills You Already Have**")
        badge_row([s.title() for s in ca["matching_skills"]], "badge-have")
    with col_b:
        st.markdown("**📌 Skills to Learn**")
        badge_row([s.title() for s in ca["missing_skills"]], "badge-learn")

    # ── Gap chart (matplotlib-free, pure HTML) ──
    total = max(len(ca["required_skills"]), 1)
    have = len(ca["matching_skills"])
    missing = len(ca["missing_skills"])
    improve = len(sg.get("need_to_improve", []))

    st.markdown("### 📉 Skill Gap Visualization")
    cols = st.columns(3)
    for col, label, count, color in [
        (cols[0], "Already Have", have, "#22c55e"),
        (cols[1], "Need to Learn", missing, "#f59e0b"),
        (cols[2], "Need to Improve", improve, "#3b82d4"),
    ]:
        bar_pct = round(count / total * 100)
        with col:
            st.markdown(
                f"""
                <div style="text-align:center;padding:1rem;background:#f7f8fa;
                     border:1px solid #e5e7eb;border-radius:10px;">
                    <div style="font-size:1.8rem;font-weight:800;color:{color}">{count}</div>
                    <div style="font-size:0.8rem;color:#57606a;margin-bottom:8px">{label}</div>
                    <div style="background:#e5e7eb;border-radius:4px;height:8px;">
                        <div style="background:{color};width:{bar_pct}%;height:8px;border-radius:4px;"></div>
                    </div>
                    <div style="font-size:0.75rem;color:#57606a;margin-top:4px">{bar_pct}% of required</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ── Tab: Skill Gap ────────────────────────────────────────────────────────────

def render_skill_gap(results: dict) -> None:
    sg = results["skill_gap"]

    st.markdown("## 🔍 Skill Gap Analysis")
    st.markdown(
        "Your skills have been categorized to give you a clear, actionable view of "
        "where you stand and what to focus on next."
    )

    summary = sg["gap_summary"]
    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Already Have", str(summary["already_have_count"]), "skills matched")
    with col2:
        metric_card("Need to Learn", str(summary["need_to_learn_count"]), "skills missing")
    with col3:
        metric_card("Need to Improve", str(summary["need_to_improve_count"]), "skills to deepen")

    # ── High-priority gaps ──
    high_priority = summary.get("high_priority_gaps", [])
    if high_priority:
        st.warning(
            f"⚠️ **High Priority Gaps:** You're missing "
            + ", ".join(f"**{s['skill']}**" for s in high_priority)
            + " — these are core requirements for this role. Focus on these first."
        )

    # ── Already Have ──
    st.markdown("### ✅ Skills You Already Have")
    if sg["already_have"]:
        cols = st.columns(3)
        for i, skill in enumerate(sg["already_have"]):
            with cols[i % 3]:
                priority_badge = (
                    "<span style='background:#dcfce7;color:#166534;padding:2px 8px;"
                    "border-radius:10px;font-size:0.7rem;font-weight:600'>"
                    f"Core</span>" if skill["priority"] == "Core"
                    else "<span style='background:#e0f2fe;color:#0c4a6e;padding:2px 8px;"
                    "border-radius:10px;font-size:0.7rem;font-weight:600'>Advanced</span>"
                    if skill["priority"] == "Advanced"
                    else ""
                )
                st.markdown(
                    f"""
                    <div style="background:#f7f8fa;border:1px solid #e5e7eb;border-radius:8px;
                         padding:0.6rem 0.8rem;margin-bottom:0.5rem;">
                        <strong>{skill['skill']}</strong> {priority_badge}<br>
                        <span style="font-size:0.78rem;color:#57606a">{skill['level']}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
    else:
        st.info("No matching skills found yet. That's okay — we all start somewhere! 🌱")

    # ── Need to Learn ──
    st.markdown("### 📚 Skills to Learn")
    if sg["need_to_learn"]:
        for skill in sg["need_to_learn"]:
            priority_color = {"High": "#ef4444", "Medium": "#f59e0b", "Low": "#22c55e"}.get(
                skill["priority"], "#3b82d4"
            )
            st.markdown(
                f"""
                <div style="background:#ffffff;border:1px solid #e5e7eb;border-left:4px solid {priority_color};
                     border-radius:0 8px 8px 0;padding:0.7rem 1rem;margin-bottom:0.5rem;">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <strong>{skill['skill']}</strong>
                        <span style="background:{priority_color}22;color:{priority_color};
                              padding:2px 10px;border-radius:10px;font-size:0.75rem;font-weight:700">
                            {skill['priority']} Priority
                        </span>
                    </div>
                    <div style="font-size:0.82rem;color:#57606a;margin-top:3px">
                        {skill['reason']} · ⏱ Est. {skill['estimated_time']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.success("🎉 You have all the required skills for this role!")

    # ── Need to Improve ──
    if sg["need_to_improve"]:
        st.markdown("### 🔧 Skills to Improve")
        for skill in sg["need_to_improve"]:
            st.markdown(
                f"""
                <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;
                     padding:0.6rem 1rem;margin-bottom:0.5rem;">
                    <strong>{skill['skill']}</strong> —
                    <span style="font-size:0.82rem;color:#57606a">
                        {skill['current_level']} → {skill['target_level']}: {skill['reason']}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ── Tab: Roadmap ──────────────────────────────────────────────────────────────

def render_roadmap(results: dict) -> None:
    roadmap = results["roadmap"]
    profile = results["profile"]

    st.markdown(f"## 🗺️ Career Roadmap — {profile['target_role']}")
    st.markdown(
        f"Your personalized **{profile['experience_level']}** learning path. "
        f"Estimated total duration: **{roadmap['total_duration']}**."
    )

    # ── Timeline milestones ──
    st.markdown("### 📍 Milestones")
    mile_cols = st.columns(len(roadmap["milestones"]))
    for i, (col, m) in enumerate(zip(mile_cols, roadmap["milestones"])):
        with col:
            icon = ["🌱", "🚀", "🏆"][i % 3]
            st.markdown(
                f"""
                <div style="text-align:center;padding:0.8rem;background:#f7f8fa;
                     border:1px solid #e5e7eb;border-radius:10px;">
                    <div style="font-size:1.5rem">{icon}</div>
                    <div style="font-weight:700;font-size:0.85rem;color:#1f2328">{m['title']}</div>
                    <div style="font-size:0.75rem;color:#57606a">Week {m['week']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")

    # ── Phases ──
    level_class = {"Beginner": "phase-beginner", "Intermediate": "phase-intermediate", "Advanced": "phase-advanced"}
    level_color = {"Beginner": "#22c55e", "Intermediate": "#f59e0b", "Advanced": "#ef4444"}

    for phase in roadmap["phases"]:
        level = phase["level"]
        color = level_color.get(level, "#3b82d4")
        css_cls = level_class.get(level, "")

        with st.expander(
            f"{phase['icon']} Phase {phase['phase']}: {phase['name']} ({level}) — {phase['duration_weeks']} weeks",
            expanded=(phase["phase"] == 1),
        ):
            col_left, col_right = st.columns([3, 2])

            with col_left:
                st.markdown("**🎯 Learning Objectives**")
                for obj in phase["objectives"]:
                    st.markdown(f"- {obj}")

                if phase.get("skills_to_learn"):
                    st.markdown("**📚 Skills Focus**")
                    badge_row(phase["skills_to_learn"], "badge-learn")

            with col_right:
                st.markdown("**🛠️ Projects to Build**")
                for proj in phase.get("projects", []):
                    st.markdown(f"- {proj}")

                st.markdown("**📖 Resources**")
                for res in phase.get("resources", []):
                    st.markdown(f"- {res}")

            st.markdown(
                f"""
                <div style="margin-top:0.5rem;padding:0.5rem 1rem;background:{color}11;
                     border:1px solid {color}44;border-radius:6px;">
                    <span style="font-size:0.82rem;color:{color};font-weight:600">
                        ⏱ Duration: {phase['duration_weeks']} weeks
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ── Tips ──
    st.markdown("### 💡 Career Tips")
    cols = st.columns(2)
    for i, tip in enumerate(roadmap["tips"]):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div style="background:#f7f8fa;border:1px solid #e5e7eb;border-radius:8px;
                     padding:0.6rem 0.8rem;margin-bottom:0.5rem;font-size:0.85rem;">
                    💡 {tip}
                </div>
                """,
                unsafe_allow_html=True,
            )


# ── Tab: Projects ─────────────────────────────────────────────────────────────

def render_projects(results: dict) -> None:
    projects = results["projects"]

    st.markdown("## 🛠️ Project Recommendations")
    st.markdown(
        "Hands-on projects are the fastest way to bridge skill gaps and build a portfolio. "
        "Here are the best projects matched to your profile and skill gaps."
    )

    # ── Quick wins ──
    if projects["quick_wins"]:
        st.markdown("### ⚡ Quick Wins — Start Here")
        st.markdown("Projects you can start **right now** with your current skills.")
        for proj in projects["quick_wins"]:
            _render_project_card(proj, highlight=True)

    # ── All recommended projects ──
    st.markdown("### 📋 All Recommended Projects")
    all_projs = projects["projects"]
    if all_projs:
        for proj in all_projs:
            _render_project_card(proj, highlight=False)
    else:
        st.info("No projects found for this role. Please check the role data.")

    # ── Stretch goals ──
    if projects["stretch_goals"]:
        st.markdown("### 🏆 Stretch Goals — Future Challenges")
        st.markdown("More advanced projects to aim for after completing Phase 1–2.")
        for proj in projects["stretch_goals"]:
            _render_project_card(proj, highlight=False)


def _render_project_card(proj: dict, highlight: bool = False) -> None:
    diff = proj.get("difficulty", "")
    diff_color = difficulty_color(diff)
    border_style = "border: 2px solid #22c55e;" if highlight else "border: 1px solid #e5e7eb;"
    skills = proj.get("skills_developed", [])
    skills_html = " ".join(
        f'<span style="background:#e0f2fe;color:#0c4a6e;padding:2px 8px;border-radius:10px;'
        f'font-size:0.72rem;font-weight:600;margin:2px">{s}</span>'
        for s in skills
    )
    st.markdown(
        f"""
        <div style="background:#ffffff;{border_style}border-radius:10px;
             padding:1rem 1.2rem;margin-bottom:0.8rem;
             box-shadow:0 1px 3px rgba(0,0,0,0.05);">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                <div style="font-size:1.05rem;font-weight:700;color:#1f2328">{proj['title']}</div>
                <span style="background:{diff_color}22;color:{diff_color};padding:3px 12px;
                      border-radius:10px;font-size:0.75rem;font-weight:700;white-space:nowrap">
                    {diff}
                </span>
            </div>
            <div style="font-size:0.85rem;color:#57606a;margin:0.4rem 0">
                {proj.get('description', '')}
            </div>
            <div style="margin-top:0.4rem">{skills_html}</div>
            <div style="font-size:0.78rem;color:#57606a;margin-top:0.5rem">
                ⏱ {proj.get('duration', 'N/A')} &nbsp;|&nbsp;
                📦 Deliverable: {proj.get('deliverable', 'N/A')}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Tab: Career Mentor ────────────────────────────────────────────────────────

def render_career_mentor(orchestrator: Orchestrator, results: dict | None) -> None:
    st.markdown("## 💬 AI Career Mentor")
    st.markdown(
        "Ask me anything about your career: salary, resume tips, interview prep, "
        "job hunting, networking, skills, motivation, and more."
    )

    profile = results["profile"] if results else {}
    analysis = results["career_analysis"] if results else {}

    # ── Chat history display ──
    chat_container = st.container()
    with chat_container:
        if not st.session_state.chat_history:
            # Greeting message on first load
            greeting = orchestrator.chat(
                "hello",
                profile=profile,
                analysis=analysis,
                history=[],
            )
            st.session_state.chat_history.append({"role": "assistant", "content": greeting})

        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(
                    f'<div class="chat-user">👤 {msg["content"]}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div class="chat-bot">🤖 {msg["content"]}</div>',
                    unsafe_allow_html=True,
                )

    # ── Input ──
    st.markdown("---")
    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_input = st.text_input(
            "Your message",
            placeholder="Ask me about resumes, salary, interviews, skills...",
            label_visibility="collapsed",
            key="mentor_input",
        )
    with col_btn:
        send_btn = st.button("Send", use_container_width=True, type="primary")

    if send_btn and user_input.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
        response = orchestrator.chat(
            user_input.strip(),
            profile=profile,
            analysis=analysis,
            history=st.session_state.chat_history,
        )
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        st.rerun()

    # ── Quick prompt chips ──
    st.markdown("**Quick questions:**")
    cols = st.columns(4)
    quick_prompts = [
        ("💰 Salary?", "What is the expected salary for my role?"),
        ("📄 Resume tips", "Give me resume tips for my target role"),
        ("🎯 Interview prep", "How should I prepare for interviews?"),
        ("🔍 Job search", "How do I find job opportunities?"),
    ]
    for col, (label, prompt) in zip(cols, quick_prompts):
        with col:
            if st.button(label, key=f"qp_{label}", use_container_width=True):
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                response = orchestrator.chat(
                    prompt,
                    profile=profile,
                    analysis=analysis,
                    history=st.session_state.chat_history,
                )
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                st.rerun()

    if st.button("🗑️ Clear chat", key="clear_chat"):
        st.session_state.chat_history = []
        st.rerun()


# ── Welcome screen (no analysis yet) ────────────────────────────────────────

def render_welcome() -> None:
    st.markdown(
        """
        <div style="text-align:center;padding:3rem 1rem 1rem 1rem;">
            <div style="font-size:4rem">🧭</div>
            <h1 style="font-size:2.5rem;font-weight:800;margin-bottom:0.5rem">CareerPilot AI</h1>
            <p style="font-size:1.1rem;color:#57606a;max-width:540px;margin:0 auto 2rem auto">
                Your agentic AI career advisor. Beat the skill-job mismatch and land your
                dream role with a personalized roadmap, skill gap analysis, and project guidance.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    features = [
        ("🎯", "Skill Gap Analysis", "Know exactly which skills you have, need to learn, and need to improve."),
        ("🗺️", "Career Roadmap", "Phase-by-phase personalized learning plan with clear objectives."),
        ("🛠️", "Project Recommendations", "Hands-on projects that directly develop the skills you need."),
        ("💬", "AI Career Mentor", "Chat with an AI mentor for advice on jobs, resumes, and more."),
        ("📊", "Match Analytics", "Visual skill-match percentage with transparent breakdown."),
        ("🚀", "Agentic Architecture", "5 specialized agents working together to advise your career path."),
    ]
    all_cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(features):
        with all_cols[i % 3]:
            st.markdown(
                f"""
                <div style="background:#f7f8fa;border:1px solid #e5e7eb;border-radius:10px;
                     padding:1.2rem;margin-bottom:1rem;text-align:center;">
                    <div style="font-size:2rem;margin-bottom:0.5rem">{icon}</div>
                    <div style="font-weight:700;font-size:1rem;color:#1f2328;margin-bottom:0.4rem">{title}</div>
                    <div style="font-size:0.83rem;color:#57606a">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.info(
        "👈 **Get started:** Fill in your profile in the sidebar and click **Analyze My Career**. "
        "Or use the **Load Sample Profile** button to see a demo instantly."
    )

    st.markdown(
        """
        <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;
             padding:1rem 1.2rem;margin-top:1rem;">
            <strong>🌍 SDG 8 — Decent Work & Economic Growth</strong><br>
            <span style="font-size:0.85rem;color:#57606a">
            CareerPilot AI tackles the global skill-job mismatch problem by giving every student
            and fresh graduate a free, personalized, and actionable career development plan.
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    inject_css()
    init_state()

    orchestrator = Orchestrator()

    # Sidebar returns profile dict when "Analyze" is clicked
    profile = render_sidebar(orchestrator)

    if profile:
        with st.spinner("🔍 Analyzing your career profile with AI agents..."):
            results = orchestrator.run_analysis(profile)

        if "error" in results:
            st.error(f"❌ {results['error']}")
        else:
            st.session_state.results = results
            st.session_state.analysis_done = True
            st.session_state.profile = profile
            # Reset chat and nav so mentor greets with new profile
            st.session_state.chat_history = []
            st.session_state.nav_tab = "📊 Overview"

    # ── Main content area ──
    if st.session_state.analysis_done and st.session_state.results:
        results = st.session_state.results

        # Radio-based navigation — writes to session_state, survives reruns
        nav_options = [
            "📊 Overview",
            "🔍 Skill Gap",
            "🗺️ Roadmap",
            "🛠️ Projects",
            "💬 Career Mentor",
        ]
        active_tab = st.radio(
            "Navigation",
            nav_options,
            horizontal=True,
            label_visibility="collapsed",
            key="nav_tab",
        )

        st.markdown("<hr style='margin:0.4rem 0 1.2rem 0;border-color:#e5e7eb'>", unsafe_allow_html=True)

        if active_tab == "📊 Overview":
            render_overview(results)
        elif active_tab == "🔍 Skill Gap":
            render_skill_gap(results)
        elif active_tab == "🗺️ Roadmap":
            render_roadmap(results)
        elif active_tab == "🛠️ Projects":
            render_projects(results)
        elif active_tab == "💬 Career Mentor":
            render_career_mentor(orchestrator, results)

    else:
        render_welcome()
        # Still allow mentor chat without analysis
        with st.expander("💬 Chat with Career Mentor (works without analysis)", expanded=False):
            render_career_mentor(orchestrator, None)


if __name__ == "__main__":
    main()
