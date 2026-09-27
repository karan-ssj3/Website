# styles/theme.py — Cyberpunk / Futuristic Theme

COLORS = {
    # Neon primaries
    "primary": "#00f5ff",           # Neon cyan
    "primary_hover": "#00ccdd",
    "secondary": "#a855f7",         # Neon purple
    "accent": "#ff00ff",            # Neon magenta
    "accent_green": "#00ff88",      # Neon green

    # Backgrounds
    "background": "#050510",        # Deep space
    "surface": "rgba(10, 15, 40, 0.75)",
    "surface_solid": "#0a0f28",
    "surface_hover": "rgba(15, 20, 55, 0.9)",

    # Text
    "text_primary": "#e2e8f0",
    "text_secondary": "#94a3b8",
    "text_muted": "#475569",

    # Borders
    "border": "rgba(0, 245, 255, 0.15)",
    "border_hover": "rgba(0, 245, 255, 0.5)",
    "border_secondary": "rgba(168, 85, 247, 0.25)",

    # Status
    "error": "#ff4444",
    "warning": "#ffaa00",
    "success": "#00ff88",
}

FONTS = {
    "heading": "Inter, system-ui, sans-serif",
    "body": "Inter, system-ui, sans-serif",
    "mono": "'JetBrains Mono', 'Fira Code', monospace",
}

SPACING = {
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "1rem",
    "lg": "1.5rem",
    "xl": "2rem",
    "2xl": "3rem",
    "3xl": "4rem",
}

RADIUS = {
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "xl": "16px",
    "full": "9999px",
}

SHADOWS = {
    "glow_cyan": "0 0 10px rgba(0, 245, 255, 0.4), 0 0 30px rgba(0, 245, 255, 0.15)",
    "glow_purple": "0 0 10px rgba(168, 85, 247, 0.4), 0 0 30px rgba(168, 85, 247, 0.15)",
    "glow_magenta": "0 0 10px rgba(255, 0, 255, 0.4), 0 0 30px rgba(255, 0, 255, 0.15)",
    "card": "0 8px 32px rgba(0, 0, 0, 0.4)",
}
