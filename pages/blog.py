# pages/blog.py
import reflex as rx
from styles.theme import COLORS, SPACING
from utils.medium_feed import fetch_medium_posts, FALLBACK_POSTS


# Fetch Medium posts dynamically
def get_blog_posts():
    """Get blog posts from Medium feed or fallback to static posts."""
    posts = fetch_medium_posts("karanbhutani477", max_posts=6)
    
    if not posts:
        return FALLBACK_POSTS
    
    # Convert Medium posts to our format
    formatted_posts = []
    for i, post in enumerate(posts, 1):
        formatted_posts.append({
            "id": i,
            "title": post["title"],
            "excerpt": post["summary"],
            "date": post["date"],
            "read_time": post["read_time"],
            "url": post["url"],
            "image": post["image"],  # Add image field
            "tags": post["tags"],
        })
    
    return formatted_posts


# Get blog posts
BLOG_POSTS = get_blog_posts()


def blog_card(post: dict) -> rx.Component:
    """Component for displaying a blog post card."""
    return rx.link(
        rx.box(
            rx.box(
                # Post metadata
                rx.hstack(
                    rx.text(
                        post["date"],
                        color=COLORS["text_secondary"],
                        font_size="0.9rem",
                    ),
                    rx.text("•", color=COLORS["text_secondary"]),
                    rx.text(
                        post["read_time"],
                        color=COLORS["text_secondary"],
                        font_size="0.9rem",
                    ),
                    spacing="2",
                ),
                
                # Blog Image (if available)
                rx.cond(
                    post["image"],
                    rx.image(
                        src=post["image"],
                        alt=post["title"],
                        width="100%",
                        height="200px",
                        object_fit="cover",
                        border_radius="8px",
                        margin_bottom=SPACING["md"],
                    ),
                ),
                
                # Title
                rx.heading(
                    post["title"],
                    size="6",
                    color=COLORS["text_primary"],
                    margin_y=SPACING["sm"],
                ),
                
                # Excerpt
                rx.text(
                    post["excerpt"],
                    color=COLORS["text_secondary"],
                    line_height="1.6",
                    margin_bottom=SPACING["md"],
                ),
                
                # Tags
                rx.hstack(
                    *[
                        rx.badge(
                            tag,
                            color_scheme="purple",
                            variant="soft",
                        )
                        for tag in post["tags"]
                    ],
                    spacing="2",
                    flex_wrap="wrap",
                    margin_bottom=SPACING["lg"],
                ),
                
                padding=SPACING["md"],
                height="calc(100% - 60px)",
            ),
            
            # Read more - positioned at bottom
            rx.box(
                rx.text(
                    "Read more →",
                    color=COLORS["primary"],
                    font_weight="600",
                ),
                padding=SPACING["md"],
                border_top=f"1px solid {COLORS['border']}",
                background=COLORS["surface"],
            ),
            
            background=COLORS["surface"],
            border_radius="12px",
            border=f"1px solid {COLORS['border']}",
            _hover={"box_shadow": "lg", "transform": "translateY(-4px)"},
            transition="all 0.3s",
            width="100%",
            height="100%",
            min_height="300px",
            display="flex",
            flex_direction="column",
        ),
        href=post["url"],
        is_external=True,
        text_decoration="none",
        width="100%",
    )


def blog_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.heading(
                        "Blog",
                        size="9",
                        color=COLORS["primary"],
                        text_align="center",
                    ),
                    rx.text(
                        "Thoughts on AI, data science, and technology",
                        font_size="1.2rem",
                        color=COLORS["text_secondary"],
                        text_align="center",
                    ),
                    rx.link(
                        rx.button(
                            "View all posts on Medium",
                            size="3",
                            variant="soft",
                            color_scheme="purple",
                        ),
                        href="https://medium.com/@karanbhutani477",
                        is_external=True,
                    ),
                    spacing="4",
                    align="center",
                    text_align="center",
                    padding_y=SPACING["lg"],
                ),
                
                # Blog posts
                rx.grid(
                    *[blog_card(post) for post in BLOG_POSTS],
                    columns="1",
                    spacing="6",
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