# pages/blog.py
import reflex as rx
from styles.theme import COLORS, SPACING
from utils.medium_feed import fetch_medium_posts, FALLBACK_POSTS


def get_blog_posts():
    posts = fetch_medium_posts("karanbhutani477", max_posts=6)
    if not posts:
        return FALLBACK_POSTS
    formatted = []
    for i, post in enumerate(posts, 1):
        formatted.append({
            "id": i,
            "title": post["title"],
            "excerpt": post["summary"],
            "date": post["date"],
            "read_time": post["read_time"],
            "url": post["url"],
            "image": post["image"],
            "tags": post["tags"],
        })
    return formatted


BLOG_POSTS = get_blog_posts()


def _tag_badge(tag: str) -> rx.Component:
    return rx.box(tag, class_name="cyber-badge-purple")


def blog_card(post: dict) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                # Meta row
                rx.hstack(
                    rx.text(
                        post["date"],
                        font_family="'JetBrains Mono', monospace",
                        font_size="0.75rem",
                        color="rgba(0, 245, 255, 0.5)",
                        letter_spacing="1px",
                    ),
                    rx.text("·", color="rgba(0, 245, 255, 0.25)"),
                    rx.text(
                        post["read_time"],
                        font_family="'JetBrains Mono', monospace",
                        font_size="0.75rem",
                        color="rgba(0, 245, 255, 0.5)",
                        letter_spacing="1px",
                    ),
                    spacing="2",
                    align="center",
                ),

                # Image (if any)
                rx.cond(
                    post["image"],
                    rx.image(
                        src=post["image"],
                        alt=post["title"],
                        width="100%",
                        height="180px",
                        object_fit="cover",
                        border_radius="6px",
                        border="1px solid rgba(0, 245, 255, 0.1)",
                        opacity="0.85",
                    ),
                ),

                # Title
                rx.heading(
                    post["title"],
                    size="5",
                    color=COLORS["text_primary"],
                    line_height="1.4",
                    letter_spacing="0.2px",
                ),

                # Excerpt
                rx.text(
                    post["excerpt"],
                    color="rgba(148, 163, 184, 0.75)",
                    font_size="0.9rem",
                    line_height="1.65",
                ),

                # Tags
                rx.hstack(
                    *[_tag_badge(tag) for tag in post["tags"]],
                    spacing="2",
                    flex_wrap="wrap",
                ),

                # Read more
                rx.hstack(
                    rx.text(
                        "Read on Medium",
                        font_family="'JetBrains Mono', monospace",
                        font_size="0.78rem",
                        letter_spacing="1.5px",
                        class_name="neon-text-static",
                    ),
                    rx.text("→", color="#00f5ff", font_size="0.85rem"),
                    spacing="2",
                    align="center",
                ),

                spacing="4",
                align_items="start",
                padding="1.5rem",
                height="100%",
            ),
            class_name="glass-card blog-card-hover scan-on-hover",
            width="100%",
            height="100%",
            min_height="300px",
        ),
        href=post["url"],
        is_external=True,
        text_decoration="none",
        width="100%",
        height="100%",
        display="block",
    )


def blog_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.text("// Writing", class_name="cyber-section-title"),
                    rx.heading(
                        "Blog",
                        size="9",
                        class_name="gradient-text",
                        letter_spacing="-0.5px",
                        text_align="center",
                    ),
                    rx.text(
                        "Thoughts on AI, data science, and the future of technology",
                        font_size="1.1rem",
                        color="rgba(148, 163, 184, 0.7)",
                        text_align="center",
                        max_width="600px",
                    ),
                    rx.link(
                        rx.box("[ All Posts on Medium ]", class_name="cyber-button"),
                        href="https://medium.com/@karanbhutani477",
                        is_external=True,
                        text_decoration="none",
                    ),
                    spacing="5",
                    align="center",
                    padding_y="3rem",
                ),

                # Grid
                rx.grid(
                    *[blog_card(post) for post in BLOG_POSTS],
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
