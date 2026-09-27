# components/navbar.py
import reflex as rx


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo
            rx.link(
                rx.hstack(
                    rx.text(
                        "KB",
                        class_name="cyber-logo-text",
                    ),
                    rx.text(
                        "// Karan Bhutani",
                        color="rgba(148, 163, 184, 0.6)",
                        font_family="'JetBrains Mono', monospace",
                        font_size="0.8rem",
                        letter_spacing="1px",
                        display=["none", "none", "block"],
                    ),
                    spacing="2",
                    align="center",
                ),
                href="/",
                text_decoration="none",
            ),

            rx.spacer(),

            # Nav links
            rx.hstack(
                rx.link("Home",       href="/",           class_name="cyber-nav-link"),
                rx.link("Projects",   href="/projects",   class_name="cyber-nav-link"),
                rx.link("Experience", href="/experience", class_name="cyber-nav-link"),
                rx.link("Blog",       href="/blog",       class_name="cyber-nav-link"),
                rx.link("Contact",    href="/contact",    class_name="cyber-nav-link"),
                spacing="6",
                flex_wrap="wrap",
            ),

            width="100%",
            align="center",
            padding="1.1rem 2rem",
        ),
        class_name="cyber-navbar",
        position="sticky",
        top="0",
        z_index="999",
    )
