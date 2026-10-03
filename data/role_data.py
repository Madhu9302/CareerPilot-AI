"""
Role Data
=========
Comprehensive skill and role definitions used by all agents.
Add more roles by following the same schema.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Skill → typical proficiency level mapping
# ---------------------------------------------------------------------------
SKILL_LEVELS: dict[str, str] = {
    "python": "Proficient", "javascript": "Proficient", "java": "Proficient",
    "sql": "Intermediate", "html": "Basic", "css": "Basic",
    "react": "Intermediate", "node.js": "Intermediate", "django": "Intermediate",
    "flask": "Intermediate", "fastapi": "Intermediate",
    "machine learning": "Advanced", "deep learning": "Advanced",
    "data analysis": "Intermediate", "data visualization": "Intermediate",
    "tensorflow": "Advanced", "pytorch": "Advanced", "scikit-learn": "Intermediate",
    "docker": "Intermediate", "kubernetes": "Advanced", "aws": "Advanced",
    "git": "Basic", "linux": "Intermediate", "bash": "Intermediate",
    "statistics": "Intermediate", "mathematics": "Intermediate",
    "excel": "Basic", "tableau": "Intermediate", "power bi": "Intermediate",
    "mongodb": "Intermediate", "postgresql": "Intermediate", "mysql": "Basic",
    "typescript": "Intermediate", "vue.js": "Intermediate",
    "ci/cd": "Advanced", "terraform": "Advanced", "jenkins": "Intermediate",
    "figma": "Intermediate", "ui/ux design": "Intermediate",
    "agile": "Basic", "scrum": "Basic", "jira": "Basic",
    "networking": "Intermediate", "cryptography": "Advanced",
    "penetration testing": "Advanced", "linux administration": "Intermediate",
    "product management": "Intermediate", "user research": "Intermediate",
    "wireframing": "Intermediate", "prototyping": "Intermediate",
    "a/b testing": "Intermediate", "user interviews": "Intermediate",
}

# ---------------------------------------------------------------------------
# Role definitions
# ---------------------------------------------------------------------------
ROLE_REQUIREMENTS: dict[str, dict] = {

    # ── Data Scientist ──────────────────────────────────────────────────────
    "Data Scientist": {
        "description": (
            "Data Scientists extract insights from large datasets using statistical "
            "analysis, machine learning, and storytelling to drive business decisions."
        ),
        "avg_salary": "$90,000 – $140,000 / year",
        "job_demand": "Very High",
        "required_skills": [
            "Python", "SQL", "Statistics", "Machine Learning", "Data Analysis",
            "Data Visualization", "Scikit-learn", "Pandas", "Matplotlib",
            "Git", "Mathematics", "Communication",
        ],
        "core_skills": ["Python", "SQL", "Statistics", "Machine Learning", "Data Analysis"],
        "advanced_skills": ["Deep Learning", "TensorFlow", "PyTorch", "Big Data"],
        "improve_skills": ["Python", "SQL", "Statistics", "Data Visualization"],
        "soft_skills": ["Communication", "Critical Thinking", "Storytelling", "Collaboration"],
        "tools": ["Jupyter Notebook", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn"],
        "roadmap": {
            "phase1_objectives": [
                "Learn Python fundamentals and data structures",
                "Master SQL for data querying and aggregation",
                "Understand descriptive and inferential statistics",
                "Complete an intro to Data Science course (Coursera/edX)",
            ],
            "phase1_projects": [
                "EDA (Exploratory Data Analysis) on a public Kaggle dataset",
                "SQL data cleaning and reporting project",
            ],
            "phase2_objectives": [
                "Build and evaluate ML models with Scikit-learn",
                "Learn feature engineering and model selection",
                "Create compelling data visualizations with Matplotlib / Seaborn",
                "Earn Google or IBM Data Science Certificate",
            ],
            "phase2_projects": [
                "House price prediction ML model",
                "Customer churn analysis with classification",
                "Dashboard with Plotly / Streamlit",
            ],
            "phase3_objectives": [
                "Explore deep learning with TensorFlow or PyTorch",
                "Participate in Kaggle competitions",
                "Build end-to-end ML pipeline with MLflow",
                "Prepare a portfolio of 3 strong DS projects",
            ],
            "phase3_projects": [
                "End-to-end NLP sentiment analysis app",
                "Time series forecasting project",
                "Capstone: Full ML pipeline with deployment",
            ],
        },
        "projects": [
            {
                "title": "Customer Churn Predictor",
                "description": "Build a classification model to predict customer churn from telecom data.",
                "skills_developed": ["Python", "Machine Learning", "Scikit-learn", "Data Analysis"],
                "difficulty": "Beginner",
                "duration": "1–2 weeks",
                "deliverable": "Jupyter notebook + Streamlit demo",
            },
            {
                "title": "Housing Price Regression",
                "description": "Predict house prices using feature engineering and regression models.",
                "skills_developed": ["Python", "Machine Learning", "Statistics", "Pandas"],
                "difficulty": "Beginner",
                "duration": "1–2 weeks",
                "deliverable": "GitHub repo with full EDA",
            },
            {
                "title": "Sales Analytics Dashboard",
                "description": "Analyze sales data and build an interactive Plotly/Streamlit dashboard.",
                "skills_developed": ["Python", "SQL", "Data Visualization", "Pandas"],
                "difficulty": "Beginner",
                "duration": "1 week",
                "deliverable": "Live Streamlit app",
            },
            {
                "title": "NLP Sentiment Analysis",
                "description": "Classify sentiment of product reviews using NLP techniques.",
                "skills_developed": ["Python", "Machine Learning", "Deep Learning", "NLP"],
                "difficulty": "Intermediate",
                "duration": "2–3 weeks",
                "deliverable": "API + demo UI",
            },
            {
                "title": "Recommendation System",
                "description": "Build a collaborative filtering recommendation engine.",
                "skills_developed": ["Python", "Machine Learning", "Mathematics", "SQL"],
                "difficulty": "Intermediate",
                "duration": "2–3 weeks",
                "deliverable": "Deployed recommendation API",
            },
            {
                "title": "Real-time ML Pipeline",
                "description": "End-to-end ML pipeline with data ingestion, training, and deployment.",
                "skills_developed": ["Python", "Machine Learning", "Docker", "MLflow"],
                "difficulty": "Advanced",
                "duration": "4–6 weeks",
                "deliverable": "Production-ready pipeline on GitHub",
            },
        ],
    },

    # ── Software Engineer ───────────────────────────────────────────────────
    "Software Engineer": {
        "description": (
            "Software Engineers design, develop, and maintain software systems "
            "using principles of computer science and engineering."
        ),
        "avg_salary": "$85,000 – $145,000 / year",
        "job_demand": "Very High",
        "required_skills": [
            "Python", "Java", "JavaScript", "SQL", "Git",
            "Data Structures", "Algorithms", "System Design",
            "REST APIs", "Linux", "Agile",
        ],
        "core_skills": ["Python", "Java", "JavaScript", "SQL", "Git", "Data Structures", "Algorithms"],
        "advanced_skills": ["System Design", "Docker", "Kubernetes", "Microservices"],
        "improve_skills": ["Python", "JavaScript", "SQL", "Git"],
        "soft_skills": ["Problem Solving", "Communication", "Teamwork", "Time Management"],
        "tools": ["Git", "VS Code", "IntelliJ IDEA", "Docker", "Postman", "Jira"],
        "roadmap": {
            "phase1_objectives": [
                "Master a primary language: Python or Java",
                "Learn data structures and algorithms fundamentals",
                "Understand Git version control",
                "Build basic CRUD applications",
            ],
            "phase1_projects": [
                "To-do list app with CRUD (Python/Flask or Node.js)",
                "LeetCode Easy problems (aim for 20+)",
            ],
            "phase2_objectives": [
                "Design and build REST APIs",
                "Learn databases: SQL + one NoSQL",
                "Understand software design patterns",
                "Contribute to an open-source project",
            ],
            "phase2_projects": [
                "Blog platform with auth and CRUD API",
                "Chat application with WebSockets",
                "LeetCode Medium problems (aim for 30+)",
            ],
            "phase3_objectives": [
                "Learn system design fundamentals",
                "Understand CI/CD and DevOps basics",
                "Build a production-deployed application",
                "Practice mock technical interviews",
            ],
            "phase3_projects": [
                "Microservices-based e-commerce backend",
                "Full-stack app deployed with Docker on cloud",
                "System design case studies on GitHub",
            ],
        },
        "projects": [
            {
                "title": "REST API with Authentication",
                "description": "Build a secure REST API with JWT auth, CRUD operations, and database integration.",
                "skills_developed": ["Python", "REST APIs", "SQL", "Git"],
                "difficulty": "Beginner",
                "duration": "1–2 weeks",
                "deliverable": "GitHub repo with Postman collection",
            },
            {
                "title": "Full-Stack Task Manager",
                "description": "Complete task management app with React front-end and Python/Node back-end.",
                "skills_developed": ["JavaScript", "React", "Python", "REST APIs"],
                "difficulty": "Intermediate",
                "duration": "2–4 weeks",
                "deliverable": "Live deployed app",
            },
            {
                "title": "Algorithm Visualizer",
                "description": "Web app that visualizes sorting and graph algorithms.",
                "skills_developed": ["JavaScript", "Algorithms", "Data Structures"],
                "difficulty": "Beginner",
                "duration": "1–2 weeks",
                "deliverable": "Live web app",
            },
            {
                "title": "Microservices Chat App",
                "description": "Real-time chat app built with microservices, Docker, and message queues.",
                "skills_developed": ["Docker", "Microservices", "System Design", "Linux"],
                "difficulty": "Advanced",
                "duration": "4–6 weeks",
                "deliverable": "Docker Compose deployment",
            },
            {
                "title": "CLI DevOps Tool",
                "description": "Command-line tool that automates a dev workflow (e.g., project scaffolding).",
                "skills_developed": ["Python", "Linux", "Bash", "Git"],
                "difficulty": "Intermediate",
                "duration": "1–2 weeks",
                "deliverable": "Published PyPI package",
            },
        ],
    },

    # ── Web Developer ───────────────────────────────────────────────────────
    "Web Developer": {
        "description": (
            "Web Developers build and maintain websites and web applications, "
            "covering front-end (UI), back-end (server/API), or both (full-stack)."
        ),
        "avg_salary": "$65,000 – $115,000 / year",
        "job_demand": "High",
        "required_skills": [
            "HTML", "CSS", "JavaScript", "React", "Node.js",
            "SQL", "Git", "REST APIs", "Responsive Design", "TypeScript",
        ],
        "core_skills": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Git"],
        "advanced_skills": ["TypeScript", "Next.js", "PostgreSQL", "Docker"],
        "improve_skills": ["HTML", "CSS", "JavaScript", "React"],
        "soft_skills": ["Attention to Detail", "Creativity", "Communication", "Problem Solving"],
        "tools": ["VS Code", "Git", "Chrome DevTools", "Figma", "Postman", "Vercel"],
        "roadmap": {
            "phase1_objectives": [
                "Master HTML5 & CSS3 (Flexbox, Grid, responsive design)",
                "Learn JavaScript fundamentals and DOM manipulation",
                "Understand version control with Git",
                "Build static websites and deploy to Netlify/Vercel",
            ],
            "phase1_projects": [
                "Personal portfolio website",
                "Responsive landing page clone (Netflix, Spotify)",
            ],
            "phase2_objectives": [
                "Learn React.js: components, hooks, state management",
                "Build a Node.js/Express back-end with REST API",
                "Connect front-end to back-end with fetch/axios",
                "Learn SQL database integration",
            ],
            "phase2_projects": [
                "Weather app with external API integration",
                "Full-stack blog with React + Node.js + SQLite",
                "E-commerce product page",
            ],
            "phase3_objectives": [
                "Learn TypeScript for type safety",
                "Explore Next.js for SSR/SSG",
                "Performance optimization and accessibility",
                "Deploy full-stack app to a cloud provider",
            ],
            "phase3_projects": [
                "Full-stack Next.js e-commerce with Stripe payments",
                "Real-time collaborative tool (Google Docs-like)",
                "Portfolio with 3+ deployed projects",
            ],
        },
        "projects": [
            {
                "title": "Personal Portfolio Website",
                "description": "Build a responsive personal portfolio showcasing skills and projects.",
                "skills_developed": ["HTML", "CSS", "JavaScript", "Responsive Design"],
                "difficulty": "Beginner",
                "duration": "3–5 days",
                "deliverable": "Live on Netlify/Vercel",
            },
            {
                "title": "Weather Dashboard App",
                "description": "Fetch and display weather data from a public API with a clean UI.",
                "skills_developed": ["JavaScript", "React", "REST APIs", "CSS"],
                "difficulty": "Beginner",
                "duration": "1 week",
                "deliverable": "Deployed React app",
            },
            {
                "title": "Full-Stack Blog Platform",
                "description": "CRUD blog with user authentication, React frontend, and Express backend.",
                "skills_developed": ["React", "Node.js", "SQL", "REST APIs", "Git"],
                "difficulty": "Intermediate",
                "duration": "3–4 weeks",
                "deliverable": "Deployed full-stack app",
            },
            {
                "title": "Real-time Chat Application",
                "description": "Chat app with Socket.io, React, and Node.js.",
                "skills_developed": ["React", "Node.js", "JavaScript", "TypeScript"],
                "difficulty": "Intermediate",
                "duration": "2 weeks",
                "deliverable": "Live chat app",
            },
            {
                "title": "Next.js E-commerce Store",
                "description": "Full-featured online store with SSR, cart, and payment integration.",
                "skills_developed": ["TypeScript", "Node.js", "React", "SQL", "REST APIs"],
                "difficulty": "Advanced",
                "duration": "4–6 weeks",
                "deliverable": "Production-ready store",
            },
        ],
    },

    # ── Machine Learning Engineer ────────────────────────────────────────────
    "Machine Learning Engineer": {
        "description": (
            "ML Engineers design, build, and deploy scalable machine learning systems "
            "and models, bridging data science and software engineering."
        ),
        "avg_salary": "$110,000 – $170,000 / year",
        "job_demand": "Very High",
        "required_skills": [
            "Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
            "SQL", "Docker", "Git", "Statistics", "Mathematics",
            "REST APIs", "Linux", "MLOps",
        ],
        "core_skills": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Statistics"],
        "advanced_skills": ["MLOps", "Kubernetes", "Spark", "Distributed Training"],
        "improve_skills": ["Python", "Machine Learning", "TensorFlow", "PyTorch"],
        "soft_skills": ["Research Mindset", "Problem Solving", "Communication", "Collaboration"],
        "tools": ["Jupyter", "MLflow", "Docker", "Kubernetes", "Weights & Biases", "DVC"],
        "roadmap": {
            "phase1_objectives": [
                "Strengthen Python: NumPy, Pandas, Matplotlib",
                "Learn ML fundamentals: regression, classification, clustering",
                "Understand linear algebra and calculus for ML",
                "Complete Andrew Ng's ML course on Coursera",
            ],
            "phase1_projects": [
                "Iris classification with Scikit-learn",
                "Housing price prediction end-to-end",
            ],
            "phase2_objectives": [
                "Master TensorFlow and/or PyTorch",
                "Build and train neural networks",
                "Learn model evaluation, tuning, and deployment",
                "Experiment with CNNs, RNNs, and Transformers",
            ],
            "phase2_projects": [
                "Image classifier (CNN) with TensorFlow/Keras",
                "Text classifier with Hugging Face Transformers",
                "Model served as a REST API with FastAPI",
            ],
            "phase3_objectives": [
                "Learn MLOps: MLflow, DVC, model monitoring",
                "Containerize models with Docker",
                "Deploy to cloud: AWS SageMaker / GCP Vertex AI",
                "Build full ML platform pipeline",
            ],
            "phase3_projects": [
                "End-to-end ML pipeline: data → training → deployment",
                "Real-time inference microservice",
                "Capstone: LLM fine-tuning or diffusion model project",
            ],
        },
        "projects": [
            {
                "title": "Image Classification API",
                "description": "Train a CNN model and serve it as a REST API.",
                "skills_developed": ["Python", "Deep Learning", "TensorFlow", "REST APIs"],
                "difficulty": "Intermediate",
                "duration": "2–3 weeks",
                "deliverable": "Deployed API with demo",
            },
            {
                "title": "NLP Text Classifier",
                "description": "Fine-tune a transformer model for text classification with Hugging Face.",
                "skills_developed": ["Python", "Deep Learning", "PyTorch", "Machine Learning"],
                "difficulty": "Intermediate",
                "duration": "2–3 weeks",
                "deliverable": "Hugging Face model card + demo",
            },
            {
                "title": "MLOps Pipeline",
                "description": "Build a CI/CD pipeline for ML models with MLflow and Docker.",
                "skills_developed": ["MLOps", "Docker", "Python", "Machine Learning"],
                "difficulty": "Advanced",
                "duration": "4–6 weeks",
                "deliverable": "GitHub Actions pipeline",
            },
            {
                "title": "Recommendation Engine",
                "description": "Collaborative + content-based recommendation system.",
                "skills_developed": ["Python", "Machine Learning", "SQL", "Mathematics"],
                "difficulty": "Intermediate",
                "duration": "2–3 weeks",
                "deliverable": "Deployed recommendation service",
            },
        ],
    },

    # ── Data Analyst ────────────────────────────────────────────────────────
    "Data Analyst": {
        "description": (
            "Data Analysts collect, process, and analyze data to help organizations "
            "make informed decisions using SQL, Excel, and visualization tools."
        ),
        "avg_salary": "$60,000 – $95,000 / year",
        "job_demand": "High",
        "required_skills": [
            "SQL", "Excel", "Python", "Data Visualization", "Statistics",
            "Tableau", "Power BI", "Data Analysis", "Communication", "Git",
        ],
        "core_skills": ["SQL", "Excel", "Data Analysis", "Data Visualization", "Statistics"],
        "advanced_skills": ["Python", "Tableau", "Power BI", "A/B Testing"],
        "improve_skills": ["SQL", "Excel", "Data Visualization"],
        "soft_skills": ["Analytical Thinking", "Communication", "Attention to Detail", "Storytelling"],
        "tools": ["Excel", "Google Sheets", "Tableau", "Power BI", "SQL", "Jupyter Notebook"],
        "roadmap": {
            "phase1_objectives": [
                "Master SQL: SELECT, JOIN, GROUP BY, subqueries, CTEs",
                "Learn Excel: PivotTables, VLOOKUP, charts",
                "Understand basic descriptive statistics",
                "Learn data cleaning techniques",
            ],
            "phase1_projects": [
                "Sales analysis in Excel with PivotTables",
                "SQL analysis of a public database (e.g., Northwind)",
            ],
            "phase2_objectives": [
                "Build dashboards in Tableau or Power BI",
                "Learn Python with Pandas for data manipulation",
                "Understand A/B testing and hypothesis testing",
                "Tell stories with data (chart selection, annotations)",
            ],
            "phase2_projects": [
                "Interactive Tableau/Power BI sales dashboard",
                "Python EDA on a real-world dataset",
                "Marketing campaign A/B test analysis",
            ],
            "phase3_objectives": [
                "Learn advanced SQL (window functions, optimization)",
                "Build automated reporting pipelines",
                "Earn Google Data Analytics or similar certification",
                "Create a portfolio of 3 analysis case studies",
            ],
            "phase3_projects": [
                "End-to-end data pipeline with Python + SQL",
                "Multi-dashboard analytics platform",
                "Business case study with recommendations report",
            ],
        },
        "projects": [
            {
                "title": "Sales Performance Dashboard",
                "description": "Analyze sales data and create an interactive dashboard in Tableau or Power BI.",
                "skills_developed": ["SQL", "Tableau", "Power BI", "Data Visualization"],
                "difficulty": "Beginner",
                "duration": "1 week",
                "deliverable": "Published Tableau Public dashboard",
            },
            {
                "title": "COVID-19 Data Analysis",
                "description": "Analyze public COVID-19 datasets and tell a data-driven story.",
                "skills_developed": ["Python", "Data Analysis", "Data Visualization", "Statistics"],
                "difficulty": "Beginner",
                "duration": "1–2 weeks",
                "deliverable": "Jupyter notebook with narrative",
            },
            {
                "title": "Customer Segmentation",
                "description": "Segment customers using SQL and Python clustering analysis.",
                "skills_developed": ["SQL", "Python", "Data Analysis", "Statistics"],
                "difficulty": "Intermediate",
                "duration": "2 weeks",
                "deliverable": "Report with actionable insights",
            },
            {
                "title": "Automated Report Pipeline",
                "description": "Build a Python script that auto-generates weekly business reports.",
                "skills_developed": ["Python", "SQL", "Data Analysis", "Excel"],
                "difficulty": "Intermediate",
                "duration": "2 weeks",
                "deliverable": "Scheduled script on GitHub",
            },
        ],
    },

    # ── DevOps Engineer ──────────────────────────────────────────────────────
    "DevOps Engineer": {
        "description": (
            "DevOps Engineers bridge development and operations, building CI/CD pipelines, "
            "managing infrastructure as code, and ensuring system reliability."
        ),
        "avg_salary": "$100,000 – $155,000 / year",
        "job_demand": "Very High",
        "required_skills": [
            "Linux", "Bash", "Docker", "Kubernetes", "CI/CD", "Git",
            "AWS", "Terraform", "Python", "Networking", "Monitoring",
        ],
        "core_skills": ["Linux", "Docker", "Git", "CI/CD", "AWS", "Bash"],
        "advanced_skills": ["Kubernetes", "Terraform", "Ansible", "Prometheus", "Grafana"],
        "improve_skills": ["Linux", "Docker", "Git", "Python"],
        "soft_skills": ["Problem Solving", "Reliability Mindset", "Communication", "On-Call Discipline"],
        "tools": ["Docker", "Kubernetes", "Terraform", "Jenkins", "GitHub Actions", "Prometheus"],
        "roadmap": {
            "phase1_objectives": [
                "Master Linux command line and Bash scripting",
                "Learn Git and branching strategies",
                "Understand Docker: images, containers, compose",
                "Set up a basic CI/CD pipeline with GitHub Actions",
            ],
            "phase1_projects": [
                "Dockerize a Python/Node.js web app",
                "GitHub Actions CI pipeline for a sample repo",
            ],
            "phase2_objectives": [
                "Learn Kubernetes: pods, deployments, services, ingress",
                "Understand infrastructure as code with Terraform",
                "Learn AWS/GCP/Azure fundamentals",
                "Implement monitoring with Prometheus + Grafana",
            ],
            "phase2_projects": [
                "Deploy a multi-container app on Kubernetes (Minikube)",
                "Provision cloud infra with Terraform",
                "Full monitoring stack for a sample service",
            ],
            "phase3_objectives": [
                "Implement GitOps with ArgoCD or Flux",
                "Earn AWS Solutions Architect Associate cert",
                "Build a complete DevOps platform for a project",
                "Practice incident management and post-mortems",
            ],
            "phase3_projects": [
                "Full DevOps pipeline: code → build → test → deploy",
                "Multi-env deployment (dev/staging/prod) with Terraform",
                "Site Reliability Engineering (SRE) runbook",
            ],
        },
        "projects": [
            {
                "title": "Dockerized Web App",
                "description": "Package a web application into Docker containers with docker-compose.",
                "skills_developed": ["Docker", "Linux", "Bash", "Git"],
                "difficulty": "Beginner",
                "duration": "1 week",
                "deliverable": "Docker Compose setup on GitHub",
            },
            {
                "title": "CI/CD Pipeline with GitHub Actions",
                "description": "Automated build, test, and deploy pipeline for a web app.",
                "skills_developed": ["CI/CD", "Git", "Linux", "Bash"],
                "difficulty": "Beginner",
                "duration": "1 week",
                "deliverable": "GitHub Actions workflow file",
            },
            {
                "title": "Kubernetes Cluster Deployment",
                "description": "Deploy a microservices app on a local Kubernetes cluster.",
                "skills_developed": ["Kubernetes", "Docker", "Linux", "Networking"],
                "difficulty": "Intermediate",
                "duration": "2–3 weeks",
                "deliverable": "K8s manifests on GitHub",
            },
            {
                "title": "Infrastructure as Code with Terraform",
                "description": "Provision and manage cloud infrastructure using Terraform.",
                "skills_developed": ["Terraform", "AWS", "Linux", "CI/CD"],
                "difficulty": "Advanced",
                "duration": "3–4 weeks",
                "deliverable": "Terraform modules on GitHub",
            },
        ],
    },

    # ── Cybersecurity Analyst ────────────────────────────────────────────────
    "Cybersecurity Analyst": {
        "description": (
            "Cybersecurity Analysts protect systems and networks from threats, "
            "monitoring for attacks and implementing security measures."
        ),
        "avg_salary": "$80,000 – $130,000 / year",
        "job_demand": "Very High",
        "required_skills": [
            "Networking", "Linux", "Python", "Cryptography",
            "Penetration Testing", "SIEM Tools", "Firewalls",
            "Incident Response", "Git", "Bash",
        ],
        "core_skills": ["Networking", "Linux", "Cryptography", "Incident Response"],
        "advanced_skills": ["Penetration Testing", "Malware Analysis", "Reverse Engineering"],
        "improve_skills": ["Networking", "Linux", "Python"],
        "soft_skills": ["Attention to Detail", "Analytical Thinking", "Ethics", "Communication"],
        "tools": ["Wireshark", "Nmap", "Metasploit", "Burp Suite", "Splunk", "Kali Linux"],
        "roadmap": {
            "phase1_objectives": [
                "Understand networking fundamentals (TCP/IP, DNS, HTTP)",
                "Master Linux command line for security",
                "Learn cryptography basics (encryption, hashing, PKI)",
                "Complete CompTIA Security+ study material",
            ],
            "phase1_projects": [
                "Home lab: set up a virtual network with VirtualBox",
                "Capture and analyze network traffic with Wireshark",
            ],
            "phase2_objectives": [
                "Learn ethical hacking basics with Kali Linux",
                "Understand web application security (OWASP Top 10)",
                "Set up and use a SIEM tool (Splunk free tier)",
                "Earn CompTIA Security+ certification",
            ],
            "phase2_projects": [
                "CTF (Capture the Flag) challenges on HackTheBox/TryHackMe",
                "Vulnerability assessment report on a test environment",
            ],
            "phase3_objectives": [
                "Learn penetration testing methodology",
                "Study incident response and forensics",
                "Earn CEH or OSCP certification",
                "Build a cybersecurity portfolio",
            ],
            "phase3_projects": [
                "Full penetration testing report on a lab environment",
                "SIEM dashboard and alerting setup",
                "Python security tool (port scanner, log analyzer)",
            ],
        },
        "projects": [
            {
                "title": "Network Traffic Analyzer",
                "description": "Build a Python tool to capture and analyze network packets.",
                "skills_developed": ["Python", "Networking", "Linux", "Bash"],
                "difficulty": "Beginner",
                "duration": "1–2 weeks",
                "deliverable": "Python CLI tool on GitHub",
            },
            {
                "title": "CTF Challenges Portfolio",
                "description": "Document solutions to 10+ CTF challenges with write-ups.",
                "skills_developed": ["Penetration Testing", "Cryptography", "Linux", "Networking"],
                "difficulty": "Intermediate",
                "duration": "Ongoing",
                "deliverable": "GitHub write-ups repository",
            },
            {
                "title": "Web Vulnerability Scanner",
                "description": "Build a basic Python script to test for common OWASP Top 10 issues.",
                "skills_developed": ["Python", "Penetration Testing", "Networking"],
                "difficulty": "Intermediate",
                "duration": "2–3 weeks",
                "deliverable": "CLI scanner tool",
            },
            {
                "title": "SIEM Dashboard",
                "description": "Set up Splunk or ELK Stack to monitor and alert on security events.",
                "skills_developed": ["SIEM Tools", "Linux", "Networking", "Incident Response"],
                "difficulty": "Advanced",
                "duration": "3–4 weeks",
                "deliverable": "Dashboard screenshots + runbook",
            },
        ],
    },

    # ── Product Manager ──────────────────────────────────────────────────────
    "Product Manager": {
        "description": (
            "Product Managers define product vision, work with engineering and design, "
            "prioritize features, and drive products from idea to launch."
        ),
        "avg_salary": "$95,000 – $155,000 / year",
        "job_demand": "High",
        "required_skills": [
            "Product Management", "User Research", "Agile", "Scrum",
            "Data Analysis", "SQL", "Communication", "Wireframing",
            "A/B Testing", "Jira",
        ],
        "core_skills": ["Product Management", "User Research", "Agile", "Communication", "Data Analysis"],
        "advanced_skills": ["SQL", "A/B Testing", "Wireframing", "Prototyping"],
        "improve_skills": ["Communication", "Data Analysis", "User Research"],
        "soft_skills": ["Leadership", "Empathy", "Strategic Thinking", "Communication", "Prioritization"],
        "tools": ["Jira", "Figma", "Google Analytics", "Mixpanel", "Notion", "Miro"],
        "roadmap": {
            "phase1_objectives": [
                "Understand core PM frameworks (Jobs-to-be-Done, Lean Startup)",
                "Learn Agile and Scrum methodology",
                "Practice writing user stories and acceptance criteria",
                "Read: 'Inspired' by Marty Cagan",
            ],
            "phase1_projects": [
                "Write a PRD (Product Requirements Document) for a product you use",
                "Conduct 3 user interviews for a product concept",
            ],
            "phase2_objectives": [
                "Learn wireframing with Figma",
                "Understand metrics: DAU, MAU, retention, NPS",
                "Learn SQL for product analytics",
                "Run an A/B test analysis (can be simulated)",
            ],
            "phase2_projects": [
                "End-to-end PRD with wireframes for a mobile app",
                "Product teardown and improvement analysis",
                "A/B test design and results analysis",
            ],
            "phase3_objectives": [
                "Build a PM portfolio with case studies",
                "Prepare for PM interviews: product sense + estimation",
                "Network with PMs on LinkedIn",
                "Apply for APM (Associate PM) programs",
            ],
            "phase3_projects": [
                "Full product case study (problem → solution → metrics)",
                "Mock PM interview recordings with feedback",
                "PM portfolio website",
            ],
        },
        "projects": [
            {
                "title": "Product Requirements Document",
                "description": "Write a comprehensive PRD for a new feature or product.",
                "skills_developed": ["Product Management", "Communication", "User Research"],
                "difficulty": "Beginner",
                "duration": "1 week",
                "deliverable": "Google Doc PRD",
            },
            {
                "title": "User Research Study",
                "description": "Conduct 5 user interviews, analyze findings, and present insights.",
                "skills_developed": ["User Research", "Communication", "Data Analysis"],
                "difficulty": "Beginner",
                "duration": "2 weeks",
                "deliverable": "Research report + insights deck",
            },
            {
                "title": "Wireframe Prototype",
                "description": "Design a clickable prototype for a mobile app feature in Figma.",
                "skills_developed": ["Wireframing", "Prototyping", "User Research"],
                "difficulty": "Intermediate",
                "duration": "2 weeks",
                "deliverable": "Figma prototype link",
            },
            {
                "title": "Product Case Study",
                "description": "Full product case study: identify a problem, design a solution, define metrics.",
                "skills_developed": ["Product Management", "Data Analysis", "A/B Testing", "Communication"],
                "difficulty": "Advanced",
                "duration": "3–4 weeks",
                "deliverable": "Portfolio case study",
            },
        ],
    },

    # ── UX Designer ─────────────────────────────────────────────────────────
    "UX Designer": {
        "description": (
            "UX Designers create intuitive and engaging user experiences through "
            "research, prototyping, and iterative design."
        ),
        "avg_salary": "$70,000 – $120,000 / year",
        "job_demand": "High",
        "required_skills": [
            "UI/UX Design", "Figma", "User Research", "Wireframing", "Prototyping",
            "User Interviews", "Usability Testing", "HTML", "CSS", "Communication",
        ],
        "core_skills": ["UI/UX Design", "Figma", "User Research", "Wireframing", "Prototyping"],
        "advanced_skills": ["User Interviews", "Usability Testing", "HTML", "CSS"],
        "improve_skills": ["Figma", "User Research", "Prototyping"],
        "soft_skills": ["Empathy", "Creativity", "Communication", "Attention to Detail", "Collaboration"],
        "tools": ["Figma", "Adobe XD", "Maze", "Hotjar", "Notion", "Miro"],
        "roadmap": {
            "phase1_objectives": [
                "Learn UX design fundamentals and design thinking",
                "Master Figma: components, auto-layout, prototyping",
                "Understand user research methods",
                "Complete Google UX Design Certificate on Coursera",
            ],
            "phase1_projects": [
                "Redesign an existing app's onboarding flow",
                "Low-fidelity wireframes for a mobile app concept",
            ],
            "phase2_objectives": [
                "Conduct user interviews and usability tests",
                "Create high-fidelity prototypes in Figma",
                "Learn accessibility (WCAG) guidelines",
                "Build a design system (components, colors, typography)",
            ],
            "phase2_projects": [
                "Full UX case study: research → wireframes → prototype",
                "Design system for a fictional app",
                "Usability test with 5 participants",
            ],
            "phase3_objectives": [
                "Build a UX portfolio with 3+ case studies",
                "Learn basic HTML/CSS for developer collaboration",
                "Present designs to stakeholders effectively",
                "Apply for junior/associate UX roles",
            ],
            "phase3_projects": [
                "End-to-end responsive web design project",
                "Portfolio website showcasing case studies",
                "Accessibility audit of an existing product",
            ],
        },
        "projects": [
            {
                "title": "App Redesign Case Study",
                "description": "Identify usability issues in an existing app and redesign key flows.",
                "skills_developed": ["UI/UX Design", "Figma", "User Research", "Wireframing"],
                "difficulty": "Beginner",
                "duration": "2 weeks",
                "deliverable": "Figma file + case study write-up",
            },
            {
                "title": "Mobile App Prototype",
                "description": "Design a complete mobile app from research to interactive prototype.",
                "skills_developed": ["Figma", "Prototyping", "User Research", "Wireframing"],
                "difficulty": "Intermediate",
                "duration": "3–4 weeks",
                "deliverable": "Clickable Figma prototype",
            },
            {
                "title": "Usability Testing Study",
                "description": "Run a moderated usability test and synthesize findings.",
                "skills_developed": ["User Research", "User Interviews", "Communication"],
                "difficulty": "Intermediate",
                "duration": "2 weeks",
                "deliverable": "Research report + recommendations",
            },
        ],
    },

    # ── Cloud Engineer ───────────────────────────────────────────────────────
    "Cloud Engineer": {
        "description": (
            "Cloud Engineers design, build, and manage cloud infrastructure on "
            "platforms like AWS, Azure, or GCP for scalability and reliability."
        ),
        "avg_salary": "$105,000 – $160,000 / year",
        "job_demand": "Very High",
        "required_skills": [
            "AWS", "Docker", "Kubernetes", "Terraform", "Linux",
            "Python", "Networking", "CI/CD", "Git", "Bash", "Monitoring",
        ],
        "core_skills": ["AWS", "Docker", "Linux", "Python", "Networking", "Git"],
        "advanced_skills": ["Kubernetes", "Terraform", "CI/CD", "Monitoring"],
        "improve_skills": ["AWS", "Docker", "Linux", "Python"],
        "soft_skills": ["Problem Solving", "Reliability Mindset", "Communication", "Documentation"],
        "tools": ["AWS Console", "Terraform", "Kubernetes", "Docker", "CloudFormation", "Prometheus"],
        "roadmap": {
            "phase1_objectives": [
                "Learn Linux fundamentals and Bash scripting",
                "Create an AWS Free Tier account and explore core services",
                "Learn Docker: build, run, push images",
                "Understand networking: VPC, subnets, security groups",
            ],
            "phase1_projects": [
                "Deploy a static website on AWS S3 + CloudFront",
                "Containerize and deploy an app to AWS ECS",
            ],
            "phase2_objectives": [
                "Learn Infrastructure as Code with Terraform or CloudFormation",
                "Understand Kubernetes: deployments, services, ingress",
                "Set up CI/CD to AWS with GitHub Actions",
                "Earn AWS Cloud Practitioner certification",
            ],
            "phase2_projects": [
                "Provision multi-tier AWS architecture with Terraform",
                "EKS (Elastic Kubernetes Service) deployment",
            ],
            "phase3_objectives": [
                "Earn AWS Solutions Architect Associate",
                "Implement monitoring with CloudWatch + Prometheus",
                "Learn cost optimization strategies",
                "Build a well-architected cloud platform",
            ],
            "phase3_projects": [
                "Multi-region highly available AWS architecture",
                "Full platform: IaC + CI/CD + monitoring + alerting",
            ],
        },
        "projects": [
            {
                "title": "Static Site on AWS S3",
                "description": "Deploy a static website to S3 with CloudFront CDN.",
                "skills_developed": ["AWS", "Networking", "Git", "Linux"],
                "difficulty": "Beginner",
                "duration": "3–5 days",
                "deliverable": "Live website URL",
            },
            {
                "title": "Terraform AWS Infrastructure",
                "description": "Provision a complete VPC with EC2, RDS, and load balancer using Terraform.",
                "skills_developed": ["Terraform", "AWS", "Networking", "Linux"],
                "difficulty": "Intermediate",
                "duration": "2–3 weeks",
                "deliverable": "Terraform codebase on GitHub",
            },
            {
                "title": "Kubernetes on EKS",
                "description": "Deploy a microservices app to AWS EKS with autoscaling.",
                "skills_developed": ["Kubernetes", "AWS", "Docker", "CI/CD"],
                "difficulty": "Advanced",
                "duration": "4–6 weeks",
                "deliverable": "EKS cluster with Helm charts",
            },
        ],
    },
}
