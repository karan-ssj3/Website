# styles/theme.py

# Color palette for the portfolio website
COLORS = {
    # Primary colors
    "primary": "#3B82F6",  # Blue
    "primary_hover": "#2563EB",  # Darker blue
    "secondary": "#64748B",  # Slate
    
    # Background colors
    "background": "#FFFFFF",  # White
    "surface": "#F8FAFC",  # Light gray
    "surface_hover": "#F1F5F9",  # Slightly darker gray
    
    # Text colors
    "text_primary": "#1E293B",  # Dark slate
    "text_secondary": "#64748B",  # Medium slate
    "text_muted": "#94A3B8",  # Light slate
    
    # Accent colors
    "accent": "#10B981",  # Emerald green
    "accent_hover": "#059669",  # Darker emerald
    "warning": "#F59E0B",  # Amber
    "error": "#EF4444",  # Red
    
    # Border colors
    "border": "#E2E8F0",  # Light gray border
    "border_hover": "#CBD5E1",  # Medium gray border
    
    # Dark mode colors
    "dark_background": "#0F172A",  # Dark slate
    "dark_surface": "#1E293B",  # Medium dark slate
    "dark_text_primary": "#F8FAFC",  # Light text
    "dark_text_secondary": "#CBD5E1",  # Medium light text
    "dark_border": "#334155",  # Dark border
}

# Typography
FONTS = {
    "heading": "Inter, system-ui, sans-serif",
    "body": "Inter, system-ui, sans-serif",
    "mono": "JetBrains Mono, monospace",
}

# Spacing scale
SPACING = {
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "1rem",
    "lg": "1.5rem",
    "xl": "2rem",
    "2xl": "3rem",
    "3xl": "4rem",
}

# Border radius
RADIUS = {
    "sm": "0.25rem",
    "md": "0.5rem",
    "lg": "0.75rem",
    "xl": "1rem",
    "full": "9999px",
}

# Shadows
SHADOWS = {
    "sm": "0 1px 2px 0 rgb(0 0 0 / 0.05)",
    "md": "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)",
    "lg": "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)",
    "xl": "0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)",
}