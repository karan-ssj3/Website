# pages/experience.py
import reflex as rx
from styles.theme import COLORS, SPACING
from data.experience import EXPERIENCE


def _tech_badge(tech: str) -> rx.Component:
    return rx.box(tech, class_name="cyber-badge-purple")


def experience_card(exp: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Header row
            rx.hstack(
                rx.vstack(
                    rx.text(
                        exp["title"],
                        font_size="1.15rem",
                        font_weight="700",
                        color=COLORS["text_primary"],
                        letter_spacing="0.3px",
                    ),
                    rx.text(
                        exp["company"],
                        font_size="1rem",
                        class_name="neon-text-static",
                        font_family="'JetBrains Mono', monospace",
                        letter_spacing="0.5px",
                    ),
                    spacing="1",
                    align_items="start",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.box(
                        rx.text(
                            f"{exp['start_date']} — {exp['end_date']}",
                            font_family="'JetBrains Mono', monospace",
                            font_size="0.8rem",
                            color="rgba(0, 245, 255, 0.65)",
                            letter_spacing="1px",
                        ),
                        background="rgba(0, 245, 255, 0.06)",
                        border="1px solid rgba(0, 245, 255, 0.18)",
                        border_radius="4px",
                        padding="0.3rem 0.7rem",
                    ),
                    rx.text(
                        exp["location"],
                        color="rgba(148, 163, 184, 0.55)",
                        font_size="0.8rem",
                        font_family="'JetBrains Mono', monospace",
                        text_align="right",
                    ),
                    spacing="1",
                    align_items="end",
                ),
                width="100%",
                align_items="start",
                flex_wrap="wrap",
                gap="1rem",
            ),

            # Divider
            rx.box(
                height="1px",
                background="linear-gradient(90deg, rgba(0, 245, 255, 0.3), transparent)",
                width="100%",
            ),

            # Bullet points
            rx.vstack(
                *[
                    rx.hstack(
                        rx.text(
                            "▸",
                            color="#00f5ff",
                            font_size="0.8rem",
                            flex_shrink="0",
                            margin_top="2px",
                        ),
                        rx.text(
                            desc,
                            color="rgba(148, 163, 184, 0.85)",
                            font_size="0.93rem",
                            line_height="1.65",
                        ),
                        spacing="3",
                        align_items="start",
                        width="100%",
                    )
                    for desc in exp["description"]
                ],
                spacing="3",
                align_items="start",
                width="100%",
            ),

            # Tech stack
            rx.vstack(
                rx.text(
                    "// tech stack",
                    font_family="'JetBrains Mono', monospace",
                    font_size="0.7rem",
                    letter_spacing="2px",
                    color="rgba(168, 85, 247, 0.5)",
                ),
                rx.hstack(
                    *[_tech_badge(tech) for tech in exp["tech_stack"]],
                    spacing="2",
                    flex_wrap="wrap",
                ),
                spacing="2",
                align_items="start",
                width="100%",
            ),

            spacing="4",
            align_items="start",
            padding="1.5rem",
        ),
        class_name="glass-card exp-card",
        width="100%",
    )


def experience_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                # Page header
                rx.vstack(
                    rx.text("// Career Journey", class_name="cyber-section-title"),
                    rx.heading(
                        "Professional Experience",
                        size="9",
                        class_name="gradient-text",
                        letter_spacing="-0.5px",
                        text_align="center",
                    ),
                    rx.text(
                        "Building AI-powered solutions for enterprise clients across Australia",
                        font_size="1.1rem",
                        color="rgba(148, 163, 184, 0.7)",
                        text_align="center",
                        max_width="600px",
                    ),
                    spacing="4",
                    align="center",
                    padding_y="3rem",
                ),

                # Timeline
                rx.vstack(
                    *[experience_card(exp) for exp in EXPERIENCE],
                    spacing="6",
                    width="100%",
                    max_width="900px",
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
