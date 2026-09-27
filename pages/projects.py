# pages/projects.py
import reflex as rx
from styles.theme import COLORS, SPACING
from data.projects import PROJECTS


def _tech_badge(tech: str) -> rx.Component:
    return rx.box(tech, class_name="cyber-badge")


def project_card(project: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Image / banner area
            rx.box(
                rx.text(
                    project["title"][:2].upper(),
                    font_family="'JetBrains Mono', monospace",
                    font_size="2.5rem",
                    font_weight="900",
                    color="rgba(0, 245, 255, 0.15)",
                    letter_spacing="4px",
                    user_select="none",
                ),
                class_name="project-image-area",
                width="100%",
            ),

            # Content
            rx.vstack(
                rx.heading(
                    project["title"],
                    size="5",
                    color=COLORS["text_primary"],
                    letter_spacing="0.2px",
                ),

                rx.text(
                    project["description"],
                    color="rgba(148, 163, 184, 0.8)",
                    font_size="0.9rem",
                    line_height="1.65",
                ),

                # Tech stack
                rx.vstack(
                    rx.text(
                        "// stack",
                        font_family="'JetBrains Mono', monospace",
                        font_size="0.68rem",
                        letter_spacing="2px",
                        color="rgba(0, 245, 255, 0.4)",
                    ),
                    rx.hstack(
                        *[_tech_badge(tech) for tech in project["tech_stack"]],
                        spacing="2",
                        flex_wrap="wrap",
                    ),
                    spacing="2",
                    align_items="start",
                    width="100%",
                ),

                # Links
                rx.hstack(
                    rx.cond(
                        project["demo_link"],
                        rx.link(
                            rx.box("[ Live Demo ]", class_name="cyber-button"),
                            href=project["demo_link"],
                            is_external=True,
                            text_decoration="none",
                        ),
                    ),
                    rx.cond(
                        project["github_link"],
                        rx.link(
                            rx.box("[ GitHub ]", class_name="cyber-button-purple"),
                            href=project["github_link"],
                            is_external=True,
                            text_decoration="none",
                        ),
                    ),
                    spacing="3",
                    flex_wrap="wrap",
                ),

                spacing="4",
                padding="1.25rem",
                align_items="start",
                width="100%",
            ),

            spacing="0",
            width="100%",
        ),
        class_name="glass-card scan-on-hover",
        overflow="hidden",
        width="100%",
    )


def projects_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.text("// Portfolio", class_name="cyber-section-title"),
                    rx.heading(
                        "Projects",
                        size="9",
                        class_name="gradient-text",
                        letter_spacing="-0.5px",
                        text_align="center",
                    ),
                    rx.text(
                        "AI systems, RAG pipelines, and data engineering at scale",
                        font_size="1.1rem",
                        color="rgba(148, 163, 184, 0.7)",
                        text_align="center",
                        max_width="600px",
                    ),
                    spacing="4",
                    align="center",
                    padding_y="3rem",
                ),

                # Grid
                rx.grid(
                    *[project_card(project) for project in PROJECTS],
                    columns="1",
                    spacing="5",
                    width="100%",
                    class_name="responsive-grid",
                ),

                spacing="4",
                align="center",
                width="100%",
            ),
            max_width="1200px",
            padding="2rem",
            class_name="responsive-padding",
            margin="0 auto",
            width="100%",
        ),
        class_name="cyber-grid-bg",
        background=COLORS["background"],
        min_height="100vh",
    )
