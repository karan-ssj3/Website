# pages/contact.py
import reflex as rx
from styles.theme import COLORS, SPACING
from utils.form_handler import save_contact_submission


class ContactState(rx.State):
    name: str = ""
    email: str = ""
    phone: str = ""
    company: str = ""
    message: str = ""

    form_submitted: bool = False
    submit_error: bool = False
    validation_errors: dict = {}

    def validate_name(self, value: str):
        import re
        if not re.match(r'^[a-zA-Z\s]+$', value):
            return "Name can only contain letters and spaces"
        return ""

    def validate_email(self, value: str):
        import re
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            return "Please enter a valid email address"
        return ""

    def validate_phone(self, value: str):
        import re
        clean = re.sub(r'[^\d]', '', value)
        if not clean.isdigit() or len(clean) < 10:
            return "Phone must contain at least 10 digits"
        return ""

    def set_name(self, value: str):
        self.name = value
        err = self.validate_name(value)
        if err:
            self.validation_errors["name"] = err
        else:
            self.validation_errors.pop("name", None)

    def set_email(self, value: str):
        self.email = value
        err = self.validate_email(value)
        if err:
            self.validation_errors["email"] = err
        else:
            self.validation_errors.pop("email", None)

    def set_phone(self, value: str):
        self.phone = value
        err = self.validate_phone(value)
        if err:
            self.validation_errors["phone"] = err
        else:
            self.validation_errors.pop("phone", None)

    def set_company(self, value: str):
        self.company = value

    def set_message(self, value: str):
        self.message = value

    def submit_form(self):
        self.validation_errors = {}

        name_err  = self.validate_name(self.name)
        email_err = self.validate_email(self.email)
        phone_err = self.validate_phone(self.phone)

        if name_err:  self.validation_errors["name"]  = name_err
        if email_err: self.validation_errors["email"] = email_err
        if phone_err: self.validation_errors["phone"] = phone_err

        if not self.name or not self.email or not self.phone or not self.message:
            self.submit_error = True
            return

        if self.validation_errors:
            self.submit_error = True
            return

        try:
            save_contact_submission(self.name, self.email, self.phone, self.company, self.message)
            self.form_submitted = True
            self.submit_error = False
            self.name = self.email = self.phone = self.company = self.message = ""
        except Exception as e:
            print(f"Error saving submission: {e}")
            self.submit_error = True

    def reset_form(self):
        self.form_submitted = False
        self.submit_error = False
        self.validation_errors = {}


def _field_label(text: str) -> rx.Component:
    return rx.text(
        text,
        font_family="'JetBrains Mono', monospace",
        font_size="0.78rem",
        letter_spacing="2px",
        text_transform="uppercase",
        color="rgba(0, 245, 255, 0.65)",
    )


def _field_error(key: str) -> rx.Component:
    return rx.cond(
        ContactState.validation_errors[key],
        rx.text(
            ContactState.validation_errors[key],
            color="#ff4444",
            font_size="0.8rem",
            font_family="'JetBrains Mono', monospace",
        ),
    )


def contact_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.text("// Connect", class_name="cyber-section-title"),
                    rx.heading(
                        "Get In Touch",
                        size="9",
                        class_name="gradient-text",
                        letter_spacing="-0.5px",
                        text_align="center",
                    ),
                    rx.text(
                        "Interested in working together? Send a transmission.",
                        font_size="1.1rem",
                        color="rgba(148, 163, 184, 0.7)",
                        text_align="center",
                    ),
                    spacing="4",
                    align="center",
                    padding_y="3rem",
                ),

                # Form container
                rx.box(
                    rx.cond(
                        ContactState.form_submitted,

                        # ── Success ─────────────────────────────────────────
                        rx.vstack(
                            rx.box(
                                rx.vstack(
                                    rx.text(
                                        "✓ Transmission Received",
                                        font_family="'JetBrains Mono', monospace",
                                        font_size="1.1rem",
                                        letter_spacing="1px",
                                        color="#00ff88",
                                        text_shadow="0 0 12px rgba(0, 255, 136, 0.5)",
                                    ),
                                    rx.text(
                                        "I'll get back to you shortly.",
                                        color="rgba(148, 163, 184, 0.8)",
                                        font_size="0.95rem",
                                    ),
                                    spacing="2",
                                    align="center",
                                ),
                                class_name="cyber-success",
                                text_align="center",
                                width="100%",
                            ),
                            rx.box(
                                "[ Send Another ]",
                                class_name="cyber-button",
                                on_click=ContactState.reset_form,
                                cursor="pointer",
                            ),
                            spacing="5",
                            align="center",
                            padding="2rem",
                        ),

                        # ── Form ────────────────────────────────────────────
                        rx.vstack(
                            rx.cond(
                                ContactState.submit_error,
                                rx.box(
                                    rx.text(
                                        "⚠ Please fill in all required fields correctly.",
                                        font_family="'JetBrains Mono', monospace",
                                        font_size="0.85rem",
                                    ),
                                    class_name="cyber-error",
                                    width="100%",
                                ),
                            ),

                            # Name
                            rx.vstack(
                                _field_label("Name *"),
                                rx.input(
                                    placeholder="Your name",
                                    value=ContactState.name,
                                    on_change=ContactState.set_name,
                                    size="3",
                                    width="100%",
                                    class_name="cyber-input",
                                ),
                                _field_error("name"),
                                spacing="2",
                                width="100%",
                            ),

                            # Email
                            rx.vstack(
                                _field_label("Email *"),
                                rx.input(
                                    placeholder="your.email@domain.com",
                                    type="email",
                                    value=ContactState.email,
                                    on_change=ContactState.set_email,
                                    size="3",
                                    width="100%",
                                    class_name="cyber-input",
                                ),
                                _field_error("email"),
                                spacing="2",
                                width="100%",
                            ),

                            # Phone
                            rx.vstack(
                                _field_label("Phone *"),
                                rx.input(
                                    placeholder="+61 400 000 000",
                                    type="tel",
                                    value=ContactState.phone,
                                    on_change=ContactState.set_phone,
                                    size="3",
                                    width="100%",
                                    class_name="cyber-input",
                                ),
                                _field_error("phone"),
                                spacing="2",
                                width="100%",
                            ),

                            # Company
                            rx.vstack(
                                _field_label("Company (Optional)"),
                                rx.input(
                                    placeholder="Your organisation",
                                    value=ContactState.company,
                                    on_change=ContactState.set_company,
                                    size="3",
                                    width="100%",
                                    class_name="cyber-input",
                                ),
                                spacing="2",
                                width="100%",
                            ),

                            # Message
                            rx.vstack(
                                _field_label("Message *"),
                                rx.text_area(
                                    placeholder="Describe your project or inquiry...",
                                    value=ContactState.message,
                                    on_change=ContactState.set_message,
                                    size="3",
                                    min_height="140px",
                                    width="100%",
                                    class_name="cyber-textarea",
                                ),
                                spacing="2",
                                width="100%",
                            ),

                            # Submit
                            rx.box(
                                "[ Send Message ]",
                                class_name="cyber-button",
                                on_click=ContactState.submit_form,
                                cursor="pointer",
                                width="100%",
                                text_align="center",
                            ),

                            spacing="5",
                            width="100%",
                            padding="2rem",
                        ),
                    ),
                    class_name="glass-card",
                    width="100%",
                ),

                # Social links
                rx.hstack(
                    rx.text(
                        "// Find me on",
                        font_family="'JetBrains Mono', monospace",
                        font_size="0.75rem",
                        letter_spacing="2px",
                        color="rgba(148, 163, 184, 0.4)",
                    ),
                    rx.link(
                        rx.box("GitHub", class_name="cyber-badge"),
                        href="https://github.com/karanbhutani",
                        is_external=True,
                        text_decoration="none",
                    ),
                    rx.link(
                        rx.box("LinkedIn", class_name="cyber-badge-purple"),
                        href="https://www.linkedin.com/in/karan-bhutani/",
                        is_external=True,
                        text_decoration="none",
                    ),
                    rx.link(
                        rx.box("Medium", class_name="cyber-badge-magenta"),
                        href="https://medium.com/@karanbhutani477",
                        is_external=True,
                        text_decoration="none",
                    ),
                    spacing="3",
                    flex_wrap="wrap",
                    justify="center",
                    margin_top="2rem",
                ),

                spacing="4",
                align="center",
                width="100%",
            ),
            max_width="700px",
            padding="2rem",
            class_name="responsive-padding",
            margin="0 auto",
            width="100%",
        ),
        class_name="cyber-grid-bg",
        background=COLORS["background"],
        min_height="100vh",
    )
