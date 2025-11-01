# components/navbar.py
import reflex as rx
from styles.theme import COLORS

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo/Name
            rx.link(
                rx.heading(
                    "Karan Bhutani", 
                    size=["5", "6", "7"], 
                    color=COLORS["primary"]
                ),
                href="/",
                text_decoration="none",
            ),
            
            rx.spacer(),
            
            # Navigation Links
            rx.hstack(
                rx.link(
                    "Home", 
                    href="/", 
                    color=COLORS["text_primary"], 
                    font_weight="500",
                    font_size=["0.85rem", "0.9rem", "1rem"],
                ),
                rx.link(
                    "Projects", 
                    href="/projects", 
                    color=COLORS["text_primary"], 
                    font_weight="500",
                    font_size=["0.85rem", "0.9rem", "1rem"],
                ),
                rx.link(
                    "Experience", 
                    href="/experience", 
                    color=COLORS["text_primary"], 
                    font_weight="500",
                    font_size=["0.85rem", "0.9rem", "1rem"],
                ),
                rx.link(
                    "Blog", 
                    href="/blog", 
                    color=COLORS["text_primary"], 
                    font_weight="500",
                    font_size=["0.85rem", "0.9rem", "1rem"],
                ),
                rx.link(
                    "Contact", 
                    href="/contact", 
                    color=COLORS["text_primary"], 
                    font_weight="500",
                    font_size=["0.85rem", "0.9rem", "1rem"],
                ),
                spacing=["2", "3", "6"],
                flex_wrap="wrap",
            ),
            
            width="100%",
            align="center",
            padding=["1rem", "1.5rem", "1.5rem 2rem"],
            flex_wrap="wrap",
        ),
        background=COLORS["surface"],
        border_bottom=f"1px solid {COLORS['border']}",
        position="sticky",
        top="0",
        z_index="999",
        box_shadow="sm",
    )