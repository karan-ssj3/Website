"""Karan Bhutani - AI and Data Consultant Portfolio"""
import reflex as rx
from rxconfig import config

# Import components
from components.navbar import navbar
from components.footer import footer

# Import pages
from pages.home import home_page
from pages.projects import projects_page
from pages.experience import experience_page
from pages.blog import blog_page
from pages.contact import contact_page


class State(rx.State):
    """The app state."""
    pass


def create_page(content_func):
    """Wrapper to add navbar and footer to pages."""
    def wrapped_page():
        return rx.fragment(
            navbar(),
            content_func(),
            footer(),
        )
    return wrapped_page


app = rx.App()

# Add all pages with navbar and footer
app.add_page(create_page(home_page), route="/", title="Karan Bhutani - AI & Data Consultant")
app.add_page(create_page(projects_page), route="/projects", title="Projects | Karan Bhutani")
app.add_page(create_page(experience_page), route="/experience", title="Experience | Karan Bhutani")
app.add_page(create_page(blog_page), route="/blog", title="Blog | Karan Bhutani")
app.add_page(create_page(contact_page), route="/contact", title="Contact | Karan Bhutani")