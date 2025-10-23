# pages/experience.py
import reflex as rx
from styles.theme import COLORS, SPACING
from data.experience import EXPERIENCE


def experience_card(exp: dict) -> rx.Component:
    """Component for displaying a single experience entry."""
    return rx.box(
        rx.vstack(
            # Title and Company
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        exp["title"],
                        size="6",
                        color=COLORS["text_primary"],
                    ),
                    rx.text(
                        exp["company"],
                        font_size="1.1rem",
                        color=COLORS["primary"],
                        font_weight="600",
                    ),
                    spacing="1",
                    align_items="start",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.text(
                        f"{exp['start_date']} - {exp['end_date']}",
                        color=COLORS["text_secondary"],
                        font_weight="500",
                    ),
                    rx.text(
                        exp["location"],
                        color=COLORS["text_secondary"],
                        font_size="0.9rem",
                    ),
                    spacing="1",
                    align_items="end",
                ),
                width="100%",
                align_items="start",
            ),
            
            # Description
            rx.vstack(
                *[
                    rx.hstack(
                        rx.text("•", color=COLORS["primary"], font_weight="bold"),
                        rx.text(
                            desc,
                            color=COLORS["text_secondary"],
                            line_height="1.6",
                        ),
                        spacing="2",
                        align_items="start",
                    )
                    for desc in exp["description"]
                ],
                spacing="2",
                align_items="start",
                width="100%",
            ),
            
            # Tech Stack
            rx.hstack(
                rx.text("Technologies:", font_weight="600", color=COLORS["text_primary"]),
                *[
                    rx.badge(
                        tech,
                        color_scheme="purple",
                        variant="soft",
                    )
                    for tech in exp["tech_stack"]
                ],
                spacing="2",
                flex_wrap="wrap",
            ),
            
            spacing="4",
            align_items="start",
            padding=SPACING["md"],
        ),
        background=COLORS["surface"],
        border_radius="12px",
        border=f"1px solid {COLORS['border']}",
        width="100%",
    )


def experience_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.heading(
                        "Professional Experience",
                        size="9",
                        color=COLORS["primary"],
                        text_align="center",
                    ),
                    rx.text(
                        "My journey in data and AI consulting",
                        font_size="1.2rem",
                        color=COLORS["text_secondary"],
                        text_align="center",
                    ),
                    spacing="3",
                    align="center",
                    text_align="center",
                    padding_y=SPACING["lg"],
                ),
                
                # Experience Timeline
                rx.vstack(
                    *[experience_card(exp) for exp in EXPERIENCE],
                    spacing="6",
                    width="100%",
                ),
                
                spacing="8",
                align="center",
            ),
            max_width="1200px",
            padding=SPACING["lg"],
            margin="0 auto",
            width="100%",
        ),
        background=COLORS["background"],
        min_height="100vh",
    )