# components/footer.py
import reflex as rx
from styles.theme import COLORS

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.divider(border_color=COLORS["border"]),
            rx.hstack(
                rx.text(
                    "© 2025 Karan Bhutani. All rights reserved.",
                    color=COLORS["text_secondary"],
                    font_size="0.9rem",
                ),
                rx.spacer(),
                rx.hstack(
                    rx.link(
                        "GitHub",
                        href="https://github.com/karanbhutani",
                        color=COLORS["primary"],
                        is_external=True,
                    ),
                    rx.link(
                        "LinkedIn",
                        href="https://www.linkedin.com/in/karan-bhutani/",
                        color=COLORS["primary"],
                        is_external=True,
                    ),
                    rx.link(
                        "Medium",
                        href="https://medium.com/@karanbhutani477",
                        color=COLORS["primary"],
                        is_external=True,
                    ),
                    spacing="4",
                ),
                width="100%",
                align="center",
            ),
            padding="2rem",
            spacing="3",
        ),
        background=COLORS["surface"],
        margin_top="4rem",
    )