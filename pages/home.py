# pages/home.py
import reflex as rx
from styles.theme import COLORS, SPACING


def home_page() -> rx.Component:
    return rx.box(
        # Hero Section
        rx.box(
            rx.vstack(
                rx.heading(
                    "Karan Bhutani",
                    size="9",
                    color=COLORS["primary"],
                    text_align="center",
                ),
                rx.heading(
                    "AI and Data Consultant",
                    size="6",
                    color=COLORS["text_secondary"],
                    text_align="center",
                    font_weight="400",
                ),
                rx.text(
                    "Transforming data into actionable insights and building AI-powered solutions.",
                    font_size="1.2rem",
                    color=COLORS["text_secondary"],
                    text_align="center",
                    max_width="600px",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "View Projects",
                            size="3",
                            background=COLORS["primary"],
                            color="white",
                            _hover={"background": COLORS["primary_hover"]},
                            width=["100%", "100%", "auto"],
                        ),
                        href="/projects",
                        width=["100%", "100%", "auto"],
                    ),
                    rx.link(
                        rx.button(
                            "Contact Me",
                            size="3",
                            variant="outline",
                            color=COLORS["primary"],
                            border_color=COLORS["primary"],
                            _hover={"background": COLORS["primary"], "color": "white"},
                            width=["100%", "100%", "auto"],
                        ),
                        href="/contact",
                        width=["100%", "100%", "auto"],
                    ),
                    spacing="4",
                    justify="center",
                    flex_direction=["column", "column", "row"],
                    width="100%",
                    max_width="400px",
                ),
                spacing="5",
                align="center",
                padding_y=SPACING["xl"],
            ),
            max_width="1200px",
            padding=["1rem", "1.5rem", SPACING["lg"]],
            margin="0 auto",
            width="100%",
        ),
        
        # About Section
        rx.box(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "About Me",
                        size="8",
                        color=COLORS["text_primary"],
                        margin_bottom=SPACING["md"],
                        text_align="center",
                    ),
                    rx.text(
                        "I'm a Data and AI Consultant at Deloitte with expertise in building scalable AI solutions, "
                        "implementing advanced NLP systems, and driving data-driven decision making. With experience "
                        "working with ASX 200 clients across Australia, I specialize in RAG systems, "
                        "autonomous AI agents, and cloud technologies.",
                        font_size="1.1rem",
                        color=COLORS["text_secondary"],
                        line_height="1.8",
                        max_width="800px",
                        text_align="center",
                    ),
                    
                    # Education
                    rx.vstack(
                        rx.heading(
                            "Education",
                            size="6",
                            color=COLORS["text_primary"],
                            margin_top=SPACING["md"],
                        ),
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.heading("Masters in Data Science and Innovation", size="5", color=COLORS["primary"]),
                                    rx.spacer(),
                                    rx.text("2023 - 2025", color=COLORS["text_secondary"], font_weight="500"),
                                    width="100%",
                                    align="center",
                                ),
                                rx.text(
                                    "University of Technology Sydney",
                                    font_size="1.1rem",
                                    color=COLORS["text_secondary"],
                                ),
                                rx.text(
                                    "CGPA: 6.11/7",
                                    color=COLORS["text_secondary"],
                                ),
                                spacing="2",
                                align_items="start",
                                padding=SPACING["md"],
                            ),
                            background=COLORS["surface"],
                            border_radius="8px",
                            border=f"1px solid {COLORS['border']}",
                            width="100%",
                            max_width="800px",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    
                    # Skills
                    rx.vstack(
                        rx.heading(
                            "Core Competencies",
                            size="6",
                            color=COLORS["text_primary"],
                            margin_top=SPACING["md"],
                        ),
                        rx.hstack(
                            rx.badge("Python", size="2", color_scheme="purple"),
                            rx.badge("Autonomous AI Agents", size="2", color_scheme="purple"),
                            rx.badge("LangChain", size="2", color_scheme="purple"),
                            rx.badge("LangGraph", size="2", color_scheme="purple"),
                            rx.badge("RAG Systems", size="2", color_scheme="purple"),
                            rx.badge("Azure OpenAI", size="2", color_scheme="purple"),
                            rx.badge("FAISS", size="2", color_scheme="purple"),
                            rx.badge("Machine Learning", size="2", color_scheme="purple"),
                            rx.badge("NLP", size="2", color_scheme="purple"),
                            rx.badge("Apache Airflow", size="2", color_scheme="purple"),
                            rx.badge("dbt Cloud", size="2", color_scheme="purple"),
                            rx.badge("Strategic Consulting", size="2", color_scheme="purple"),
                            spacing="2",
                            flex_wrap="wrap",
                            max_width="800px",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    
                    spacing="4",
                    align="center",
                    text_align="center",
                ),
                max_width="1200px",
                padding=["1rem", "1.5rem", SPACING["xl"]],
                margin="0 auto",
                width="100%",
            ),
            background=COLORS["surface"],
        ),
        
        # Quick Links Section
        rx.box(
            rx.vstack(
                rx.heading(
                    "Explore",
                    size="8",
                    color=COLORS["text_primary"],
                    margin_bottom=SPACING["lg"],
                    text_align="center",
                ),
                rx.grid(
                    # Projects Card
                    rx.link(
                        rx.box(
                            rx.vstack(
                                rx.heading("Projects", size="6", color=COLORS["primary"]),
                                rx.text(
                                    "Explore my portfolio of data and AI projects",
                                    color=COLORS["text_secondary"],
                                    text_align="center",
                                ),
                                spacing="3",
                                align="center",
                                padding=SPACING["lg"],
                            ),
                            background=COLORS["surface"],
                            border_radius="12px",
                            border=f"1px solid {COLORS['border']}",
                            _hover={"box_shadow": "lg", "transform": "translateY(-4px)"},
                            transition="all 0.3s",
                        ),
                        href="/projects",
                        text_decoration="none",
                    ),
                    
                    # Experience Card
                    rx.link(
                        rx.box(
                            rx.vstack(
                                rx.heading("Experience", size="6", color=COLORS["primary"]),
                                rx.text(
                                    "View my professional journey and expertise",
                                    color=COLORS["text_secondary"],
                                    text_align="center",
                                ),
                                spacing="3",
                                align="center",
                                padding=SPACING["lg"],
                            ),
                            background=COLORS["surface"],
                            border_radius="12px",
                            border=f"1px solid {COLORS['border']}",
                            _hover={"box_shadow": "lg", "transform": "translateY(-4px)"},
                            transition="all 0.3s",
                        ),
                        href="/experience",
                        text_decoration="none",
                    ),
                    
                    # Blog Card
                    rx.link(
                        rx.box(
                            rx.vstack(
                                rx.heading("Blog", size="6", color=COLORS["primary"]),
                                rx.text(
                                    "Read my thoughts on AI, data, and technology",
                                    color=COLORS["text_secondary"],
                                    text_align="center",
                                ),
                                spacing="3",
                                align="center",
                                padding=SPACING["lg"],
                            ),
                            background=COLORS["surface"],
                            border_radius="12px",
                            border=f"1px solid {COLORS['border']}",
                            _hover={"box_shadow": "lg", "transform": "translateY(-4px)"},
                            transition="all 0.3s",
                        ),
                        href="/blog",
                        text_decoration="none",
                    ),
                    
                    columns=["1", "1", "2", "3"],
                    spacing=["4", "4", "5", "6"],
                    width="100%",
                ),
                spacing="6",
                align="center",
            ),
            max_width="1200px",
            padding=SPACING["xl"],
            margin="0 auto",
            width="100%",
        ),
        
        background=COLORS["background"],
    )