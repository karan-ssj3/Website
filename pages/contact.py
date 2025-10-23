# pages/contact.py
import reflex as rx
from styles.theme import COLORS, SPACING
from utils.form_handler import save_contact_submission


class ContactState(rx.State):
    """State for the contact form."""
    
    name: str = ""
    email: str = ""
    phone: str = ""
    company: str = ""
    message: str = ""
    
    form_submitted: bool = False
    submit_error: bool = False
    validation_errors: dict = {}
    
    def validate_name(self, value: str):
        """Validate name field - only letters and spaces allowed."""
        import re
        if not re.match(r'^[a-zA-Z\s]+$', value):
            return "Name can only contain letters and spaces"
        return ""
    
    def validate_email(self, value: str):
        """Validate email field - must contain @ and proper format."""
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, value):
            return "Please enter a valid email address"
        return ""
    
    def validate_phone(self, value: str):
        """Validate phone field - only digits allowed."""
        import re
        # Remove common phone formatting characters
        clean_phone = re.sub(r'[^\d]', '', value)
        if not clean_phone.isdigit() or len(clean_phone) < 10:
            return "Phone number must contain at least 10 digits"
        return ""
    
    def set_name(self, value: str):
        """Set name with validation."""
        self.name = value
        error = self.validate_name(value)
        if error:
            self.validation_errors["name"] = error
        else:
            self.validation_errors.pop("name", None)
    
    def set_email(self, value: str):
        """Set email with validation."""
        self.email = value
        error = self.validate_email(value)
        if error:
            self.validation_errors["email"] = error
        else:
            self.validation_errors.pop("email", None)
    
    def set_phone(self, value: str):
        """Set phone with validation."""
        self.phone = value
        error = self.validate_phone(value)
        if error:
            self.validation_errors["phone"] = error
        else:
            self.validation_errors.pop("phone", None)
    
    def set_company(self, value: str):
        """Set company (optional field)."""
        self.company = value
    
    def set_message(self, value: str):
        """Set message."""
        self.message = value
    
    def submit_form(self):
        """Handle form submission with validation."""
        # Clear previous errors
        self.validation_errors = {}
        
        # Validate all fields
        name_error = self.validate_name(self.name)
        email_error = self.validate_email(self.email)
        phone_error = self.validate_phone(self.phone)
        
        if name_error:
            self.validation_errors["name"] = name_error
        if email_error:
            self.validation_errors["email"] = email_error
        if phone_error:
            self.validation_errors["phone"] = phone_error
        
        # Check for required fields
        if not self.name or not self.email or not self.phone or not self.message:
            self.submit_error = True
            return
        
        # If there are validation errors, don't submit
        if self.validation_errors:
            self.submit_error = True
            return
        
        # Save to CSV
        try:
            save_contact_submission(
                self.name,
                self.email,
                self.phone,
                self.company,
                self.message
            )
            self.form_submitted = True
            self.submit_error = False
            
            # Clear form
            self.name = ""
            self.email = ""
            self.phone = ""
            self.company = ""
            self.message = ""
            
        except Exception as e:
            print(f"Error saving submission: {e}")
            self.submit_error = True
    
    def reset_form(self):
        """Reset form state."""
        self.form_submitted = False
        self.submit_error = False
        self.validation_errors = {}


def contact_page() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                # Header
                rx.vstack(
                    rx.heading(
                        "Get In Touch",
                        size="9",
                        color=COLORS["primary"],
                        text_align="center",
                    ),
                    rx.text(
                        "Interested in working together? Let's connect!",
                        font_size="1.2rem",
                        color=COLORS["text_secondary"],
                        text_align="center",
                    ),
                    spacing="3",
                    align="center",
                    text_align="center",
                    padding_y=SPACING["lg"],
                ),
                
                # Contact Form
                rx.box(
                    rx.cond(
                        ContactState.form_submitted,
                        # Success Message
                        rx.vstack(
                            rx.callout(
                                "Thank you for reaching out! I'll get back to you soon.",
                                icon="check",
                                color_scheme="green",
                                size="3",
                            ),
                            rx.button(
                                "Submit Another Message",
                                on_click=ContactState.reset_form,
                                size="3",
                                variant="soft",
                                color_scheme="purple",
                            ),
                            spacing="4",
                            align="center",
                            padding=SPACING["xl"],
                        ),
                        # Contact Form
                        rx.vstack(
                            rx.cond(
                                ContactState.submit_error,
                                rx.callout(
                                    "Please fill in all required fields.",
                                    icon="alert_triangle",
                                    color_scheme="red",
                                    size="2",
                                ),
                            ),
                            
                            rx.vstack(
                                rx.text("Name *", font_weight="600", color=COLORS["text_primary"]),
                                rx.input(
                                    placeholder="Your name",
                                    value=ContactState.name,
                                    on_change=ContactState.set_name,
                                    size="3",
                                    width="100%",
                                ),
                                rx.cond(
                                    ContactState.validation_errors["name"],
                                    rx.text(
                                        ContactState.validation_errors["name"],
                                        color=COLORS["error"],
                                        font_size="0.9rem",
                                    ),
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            
                            rx.vstack(
                                rx.text("Email *", font_weight="600", color=COLORS["text_primary"]),
                                rx.input(
                                    placeholder="your.email@example.com",
                                    type="email",
                                    value=ContactState.email,
                                    on_change=ContactState.set_email,
                                    size="3",
                                    width="100%",
                                ),
                                rx.cond(
                                    ContactState.validation_errors["email"],
                                    rx.text(
                                        ContactState.validation_errors["email"],
                                        color=COLORS["error"],
                                        font_size="0.9rem",
                                    ),
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            
                            rx.vstack(
                                rx.text("Phone *", font_weight="600", color=COLORS["text_primary"]),
                                rx.input(
                                    placeholder="+1 (555) 123-4567",
                                    type="tel",
                                    value=ContactState.phone,
                                    on_change=ContactState.set_phone,
                                    size="3",
                                    width="100%",
                                ),
                                rx.cond(
                                    ContactState.validation_errors["phone"],
                                    rx.text(
                                        ContactState.validation_errors["phone"],
                                        color=COLORS["error"],
                                        font_size="0.9rem",
                                    ),
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            
                            rx.vstack(
                                rx.text("Company (Optional)", font_weight="600", color=COLORS["text_primary"]),
                                rx.input(
                                    placeholder="Your company name",
                                    value=ContactState.company,
                                    on_change=ContactState.set_company,
                                    size="3",
                                    width="100%",
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            
                            rx.vstack(
                                rx.text("Message *", font_weight="600", color=COLORS["text_primary"]),
                                rx.text_area(
                                    placeholder="Tell me about your project or inquiry...",
                                    value=ContactState.message,
                                    on_change=ContactState.set_message,
                                    size="3",
                                    min_height="150px",
                                    width="100%",
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            
                            rx.button(
                                "Send Message",
                                on_click=ContactState.submit_form,
                                size="3",
                                width="100%",
                                background=COLORS["primary"],
                                color="white",
                                _hover={"background": COLORS["primary_hover"]},
                            ),
                            
                            spacing="5",
                            width="100%",
                        ),
                    ),
                    background=COLORS["surface"],
                    padding=SPACING["xl"],
                    border_radius="12px",
                    border=f"1px solid {COLORS['border']}",
                    width="100%",
                ),
                
                spacing="8",
                align="center",
            ),
            max_width="800px",
            padding=SPACING["lg"],
            margin="0 auto",
            width="100%",
        ),
        background=COLORS["background"],
        min_height="100vh",
    )