# pages/projects.py
import reflex as rx
from styles.theme import COLORS, SPACING
from data.projects import PROJECTS


def project_card(project: dict) -> rx.Component:
    """Component for displaying a single project card."""
    return rx.box(
        rx.vstack(
            # Project Image Placeholder
            rx.box(
                rx.center(
                    rx.text(
                        "Project Image",
                        color=COLORS["text_secondary"],
                        font_size="1.2rem",
                    ),
                    height="200px",
                    background=COLORS["border"],
                    border_radius="8px 8px 0 0",
                ),
            ),
            
            # Project Content
            rx.vstack(
                rx.heading(
                    project["title"],
                    size="6",
                    color=COLORS["text_primary"],
                ),
                rx.text(
                    project["description"],
                    color=COLORS["text_secondary"],
                    line_height="1.6",
                ),
                
                # Tech Stack
                rx.hstack(
                    *[
                        rx.badge(
                            tech,
                            color_scheme="purple",
                            variant="soft",
                        )
                        for tech in project["tech_stack"]
                    ],
                    spacing="2",
                    flex_wrap="wrap",
                ),
                
                # Links
                rx.hstack(
                    rx.cond(
                        project["demo_link"],
                        rx.link(
                            rx.button(
                                "Live Demo",
                                size="2",
                                variant="soft",
                                color_scheme="purple",
                            ),
                            href=project["demo_link"],
                            is_external=True,
                        ),
                    ),
                    rx.cond(
                        project["github_link"],
                        rx.link(
                            rx.button(
                                "GitHub",
                                size="2",
                                variant="outline",
                                color_scheme="purple",
                            ),
                            href=project["github_link"],
                            is_external=True,
                        ),
                    ),
                    spacing="3",
                ),
                
                spacing="4",
                padding=SPACING["md"],
                align_items="start",
            ),
            
            spacing="0",
            width="100%",
        ),
        background=COLORS["surface"],
        border_radius="12px",
        border=f"1px solid {COLORS['border']}",
        overflow="hidden",
        _hover={"box_shadow": "lg", "transform": "translateY(-4px)"},
        transition="all 0.3s",
    )


def projects_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.heading(
                        "Projects",
                        size="9",
                        color=COLORS["primary"],
                        text_align="center",
                    ),
                    rx.text(
                        "A showcase of my data and AI projects",
                        font_size="1.2rem",
                        color=COLORS["text_secondary"],
                        text_align="center",
                    ),
                    spacing="3",
                    align="center",
                    text_align="center",
                    padding_y=SPACING["lg"],
                ),
                
                # Projects Grid
                rx.grid(
                    *[project_card(project) for project in PROJECTS],
                    columns=["1", "1", "2", "3"],
                    spacing=["4", "4", "5", "6"],
                    width="100%",
                ),
                
                spacing="8",
                align="center",
            ),
            max_width="1200px",
            padding=["1rem", "1.5rem", SPACING["lg"]],
            margin="0 auto",
            width="100%",
        ),
        background=COLORS["background"],
        min_height="100vh",
    )