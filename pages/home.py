# pages/home.py
import reflex as rx
from styles.theme import COLORS


def _stat_box(number: str, label: str, color: str, delay: str = "0s") -> rx.Component:
    return rx.vstack(
        rx.box(
            number,
            class_name="stat-number",
            style={"color": color, "textShadow": f"0 0 15px {color}80, 0 0 40px {color}30"},
        ),
        rx.box(label, class_name="stat-label"),
        spacing="1",
        align="center",
        padding="1.5rem 2rem",
        background="rgba(10, 15, 40, 0.55)",
        border=f"1px solid {color}20",
        border_radius="8px",
        backdrop_filter="blur(12px)",
        flex="1",
        min_width="140px",
        transition="all 0.3s ease",
        _hover={
            "border_color": f"{color}55",
            "box_shadow": f"0 0 25px {color}15",
            "transform": "translateY(-4px)",
        },
        style={"animation": f"fade-in-up 0.9s ease {delay} both"},
    )


def _skill_badge(skill: str, cls: str = "cyber-badge") -> rx.Component:
    return rx.box(skill, class_name=cls)


def _explore_card(title: str, desc: str, href: str, icon: str, accent: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                rx.text(icon, font_size="2.5rem", line_height="1"),
                rx.box(
                    title,
                    font_family="'JetBrains Mono', monospace",
                    font_size="1.05rem",
                    font_weight="700",
                    letter_spacing="1px",
                    style={"color": accent, "textShadow": f"0 0 8px {accent}55"},
                ),
                rx.text(
                    desc,
                    color="rgba(148, 163, 184, 0.75)",
                    font_size="0.88rem",
                    text_align="center",
                    line_height="1.6",
                ),
                rx.box(
                    "→ explore",
                    font_family="'JetBrains Mono', monospace",
                    font_size="0.75rem",
                    letter_spacing="2px",
                    style={"color": accent, "opacity": "0.65"},
                    margin_top="0.25rem",
                ),
                spacing="3",
                align="center",
                padding="2rem 1.5rem",
            ),
            class_name="explore-card",
            width="100%",
        ),
        href=href,
        text_decoration="none",
        width="100%",
    )


def home_page() -> rx.Component:
    return rx.box(

        # ── Hero ────────────────────────────────────────────────────────────
        rx.box(
            # Animated floating orbs
            rx.box(class_name="cyber-orb-1"),
            rx.box(class_name="cyber-orb-2"),
            rx.box(class_name="cyber-orb-3"),
            # Particle dot field
            rx.box(class_name="particle-field"),
            # Horizontal sweep line
            rx.box(class_name="hero-sweep"),
            # Shooting stars
            rx.box(class_name="shooting-star shooting-star-1"),
            rx.box(class_name="shooting-star shooting-star-2"),
            rx.box(class_name="shooting-star shooting-star-3"),
            rx.box(class_name="shooting-star shooting-star-4"),

            # ── Content ─────────────────────────────────────────────────────
            rx.vstack(
                # Label
                rx.box(
                    "// AI & Data Consultant · Deloitte · Sydney, AU",
                    class_name="cyber-section-title fade-in-1",
                    margin_bottom="0.5rem",
                ),

                # Name — rx.box instead of rx.heading to avoid Radix color override
                rx.box(
                    "Karan Bhutani",
                    class_name="hero-name fade-in-2",
                ),

                # Tagline
                rx.text(
                    "Transforming data into intelligence. Building AI systems that scale.",
                    color="rgba(148, 163, 184, 0.82)",
                    font_size=["1rem", "1.1rem", "1.25rem"],
                    text_align="center",
                    max_width="580px",
                    line_height="1.75",
                    class_name="fade-in-3",
                ),

                # CTA buttons
                rx.hstack(
                    rx.link(
                        rx.box("[ View Projects ]", class_name="cyber-button"),
                        href="/projects",
                        text_decoration="none",
                    ),
                    rx.link(
                        rx.box("[ Contact Me ]", class_name="cyber-button-purple"),
                        href="/contact",
                        text_decoration="none",
                    ),
                    spacing="4",
                    justify="center",
                    flex_wrap="wrap",
                    class_name="fade-in-4",
                ),

                spacing="6",
                align="center",
                text_align="center",
                class_name="hero-content",
            ),

            class_name="hero-section",
            width="100%",
        ),

        # ── Stats Bar ───────────────────────────────────────────────────────
        rx.box(
            rx.hstack(
                _stat_box("2+",   "years consulting",    "#00f5ff", "0.2s"),
                _stat_box("10+",  "AI systems built",    "#a855f7", "0.35s"),
                _stat_box("70%",  "manual work reduced", "#ff00ff", "0.5s"),
                _stat_box("280+", "stakeholders led",    "#00ff88", "0.65s"),
                spacing="4",
                flex_wrap="wrap",
                justify="center",
                width="100%",
            ),
            max_width="1000px",
            margin="0 auto",
            padding="0 2rem 5rem 2rem",
        ),

        # ── About ───────────────────────────────────────────────────────────
        rx.box(
            rx.box(
                rx.vstack(
                    rx.box("// About Me", class_name="cyber-section-title"),
                    rx.heading(
                        "Who I Am",
                        size="8",
                        color=COLORS["text_primary"],
                        letter_spacing="-0.5px",
                        margin_top="0.5rem",
                    ),
                    rx.text(
                        "I'm a Data and AI Consultant at Deloitte, specialising in production-ready RAG systems, "
                        "autonomous AI agents, and cloud data engineering. With experience across ASX 200 clients in "
                        "financial services, manufacturing, and technology, I bridge the gap between cutting-edge "
                        "AI research and real-world business value.",
                        color="rgba(148, 163, 184, 0.82)",
                        font_size="1.05rem",
                        line_height="1.85",
                        max_width="760px",
                        text_align="center",
                    ),
                    spacing="5",
                    align="center",
                    text_align="center",
                ),
                max_width="1200px",
                margin="0 auto",
                padding="5rem 2rem",
            ),
            background="rgba(10, 15, 40, 0.45)",
            border_top="1px solid rgba(0, 245, 255, 0.07)",
            border_bottom="1px solid rgba(0, 245, 255, 0.07)",
        ),

        # ── Education ───────────────────────────────────────────────────────
        rx.box(
            rx.vstack(
                rx.box("// Education", class_name="cyber-section-title"),
                rx.heading(
                    "Academic Background",
                    size="7",
                    color=COLORS["text_primary"],
                    margin_top="0.5rem",
                ),
                rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.box(
                                "Masters in Data Science & Innovation",
                                class_name="neon-text-static",
                                font_weight="700",
                                font_size="1.05rem",
                            ),
                            rx.text(
                                "University of Technology Sydney",
                                color="rgba(148, 163, 184, 0.8)",
                                font_size="0.95rem",
                            ),
                            rx.box(
                                "CGPA: 6.11 / 7.0",
                                color="#a855f7",
                                font_family="'JetBrains Mono', monospace",
                                font_size="0.85rem",
                                style={"textShadow": "0 0 8px rgba(168,85,247,0.5)"},
                            ),
                            spacing="1",
                            align_items="start",
                        ),
                        rx.spacer(),
                        rx.box(
                            "2023 – 2025",
                            font_family="'JetBrains Mono', monospace",
                            font_size="0.82rem",
                            color="rgba(0, 245, 255, 0.55)",
                            letter_spacing="1px",
                        ),
                        width="100%",
                        align_items="start",
                        flex_wrap="wrap",
                        gap="1rem",
                    ),
                    padding="1.5rem",
                    class_name="glass-card",
                    width="100%",
                    max_width="760px",
                ),
                spacing="5",
                align="center",
            ),
            max_width="1200px",
            margin="0 auto",
            padding="5rem 2rem",
        ),

        # ── Skills ──────────────────────────────────────────────────────────
        rx.box(
            rx.box(
                rx.vstack(
                    rx.box("// Core Competencies", class_name="cyber-section-title"),
                    rx.heading(
                        "Skills & Technologies",
                        size="7",
                        color=COLORS["text_primary"],
                        margin_top="0.5rem",
                    ),
                    rx.hstack(
                        _skill_badge("Python",              "cyber-badge"),
                        _skill_badge("LangChain",           "cyber-badge"),
                        _skill_badge("LangGraph",           "cyber-badge"),
                        _skill_badge("RAG Systems",         "cyber-badge"),
                        _skill_badge("Azure OpenAI",        "cyber-badge"),
                        _skill_badge("FAISS",               "cyber-badge"),
                        _skill_badge("Autonomous Agents",   "cyber-badge-purple"),
                        _skill_badge("Machine Learning",    "cyber-badge-purple"),
                        _skill_badge("NLP",                 "cyber-badge-purple"),
                        _skill_badge("Apache Airflow",      "cyber-badge-purple"),
                        _skill_badge("dbt Cloud",           "cyber-badge-purple"),
                        _skill_badge("Google Cloud",        "cyber-badge-magenta"),
                        _skill_badge("Azure ML",            "cyber-badge-magenta"),
                        _skill_badge("Strategic Consulting","cyber-badge-magenta"),
                        spacing="2",
                        flex_wrap="wrap",
                        justify="center",
                        max_width="900px",
                    ),
                    spacing="5",
                    align="center",
                ),
                max_width="1200px",
                margin="0 auto",
                padding="5rem 2rem",
            ),
            background="rgba(10, 15, 40, 0.45)",
            border_top="1px solid rgba(0, 245, 255, 0.07)",
            border_bottom="1px solid rgba(0, 245, 255, 0.07)",
        ),

        # ── Explore ─────────────────────────────────────────────────────────
        rx.box(
            rx.vstack(
                rx.box("// Navigate", class_name="cyber-section-title"),
                rx.heading(
                    "Explore My Work",
                    size="7",
                    color=COLORS["text_primary"],
                    margin_top="0.5rem",
                ),
                rx.grid(
                    _explore_card(
                        "Projects",
                        "Production AI systems, RAG pipelines & data engineering solutions",
                        "/projects", "⬡", "#00f5ff",
                    ),
                    _explore_card(
                        "Experience",
                        "My professional journey at Deloitte, Synogize and beyond",
                        "/experience", "◈", "#a855f7",
                    ),
                    _explore_card(
                        "Blog",
                        "Deep dives on AI, data science and emerging technology",
                        "/blog", "◉", "#ff00ff",
                    ),
                    columns="1",
                    spacing="4",
                    width="100%",
                    class_name="responsive-grid",
                ),
                spacing="6",
                align="center",
            ),
            max_width="1200px",
            margin="0 auto",
            padding="5rem 2rem",
        ),

        # Page wrapper
        class_name="cyber-grid-bg",
        background=COLORS["background"],
        min_height="100vh",
    )
