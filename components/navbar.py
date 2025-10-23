# components/navbar.py
import reflex as rx
from styles.theme import COLORS

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo/Name
            rx.link(
                rx.heading("Karan Bhutani", size="7", color=COLORS["primary"]),
                href="/",
                text_decoration="none",
            ),
            
            rx.spacer(),
            
            # Navigation Links
            rx.hstack(
                rx.link("Home", href="/", color=COLORS["text_primary"], font_weight="500"),
                rx.link("Projects", href="/projects", color=COLORS["text_primary"], font_weight="500"),
                rx.link("Experience", href="/experience", color=COLORS["text_primary"], font_weight="500"),
                rx.link("Blog", href="/blog", color=COLORS["text_primary"], font_weight="500"),
                rx.link("Contact", href="/contact", color=COLORS["text_primary"], font_weight="500"),
                spacing="6",
            ),
            
            width="100%",
            align="center",
            padding="1.5rem 2rem",
        ),
        background=COLORS["surface"],
        border_bottom=f"1px solid {COLORS['border']}",
        position="sticky",
        top="0",
        z_index="999",
        box_shadow="sm",
    )