# components/footer.py
import reflex as rx


def footer() -> rx.Component:
    return rx.box(
        rx.box(
            height="1px",
            background="linear-gradient(90deg, transparent, rgba(0, 245, 255, 0.3), rgba(168, 85, 247, 0.3), transparent)",
        ),
        rx.box(
            rx.hstack(
                # Left — copyright + tagline
                rx.vstack(
                    rx.text(
                        "© 2025 Karan Bhutani",
                        color="rgba(148, 163, 184, 0.6)",
                        font_family="'JetBrains Mono', monospace",
                        font_size="0.78rem",
                        letter_spacing="1px",
                    ),
                    rx.text(
                        "Building the future with AI & Data",
                        color="rgba(0, 245, 255, 0.35)",
                        font_family="'JetBrains Mono', monospace",
                        font_size="0.72rem",
                        letter_spacing="0.5px",
                    ),
                    spacing="1",
                    align_items="start",
                ),

                rx.spacer(),

                # Right — social links
                rx.hstack(
                    rx.link(
                        rx.text(
                            "GitHub",
                            class_name="cyber-nav-link",
                            font_size="0.8rem",
                        ),
                        href="https://github.com/karanbhutani",
                        is_external=True,
                        text_decoration="none",
                    ),
                    rx.text("·", color="rgba(0, 245, 255, 0.25)", font_size="0.8rem"),
                    rx.link(
                        rx.text(
                            "LinkedIn",
                            class_name="cyber-nav-link",
                            font_size="0.8rem",
                        ),
                        href="https://www.linkedin.com/in/karan-bhutani/",
                        is_external=True,
                        text_decoration="none",
                    ),
                    rx.text("·", color="rgba(0, 245, 255, 0.25)", font_size="0.8rem"),
                    rx.link(
                        rx.text(
                            "Medium",
                            class_name="cyber-nav-link",
                            font_size="0.8rem",
                        ),
                        href="https://medium.com/@karanbhutani477",
                        is_external=True,
                        text_decoration="none",
                    ),
                    spacing="3",
                    align="center",
                ),

                width="100%",
                align="center",
                flex_wrap="wrap",
                gap="1rem",
            ),
            max_width="1200px",
            margin="0 auto",
            padding="1.8rem 2rem",
        ),
        class_name="cyber-footer",
        margin_top="5rem",
    )
