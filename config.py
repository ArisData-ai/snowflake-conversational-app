"""Configuration settings for the Conversational Analytics Application.

All client-specific values are parameterized below. Update the defaults
or set the corresponding environment variables to adapt this template
to a new deployment.
"""

import os

# ---------------------------------------------------------------------------
# Application metadata
# ---------------------------------------------------------------------------
APP_TITLE = os.getenv("APP_TITLE", "Conversational Analytics")
APP_ICON = "📊"

# ---------------------------------------------------------------------------
# Snowflake database / schema configuration
# ---------------------------------------------------------------------------
APP_SCHEMA = os.getenv("APP_SCHEMA", "APPS")
DB = os.getenv("DB", "ARISDATA_CONVERSATIONAL_ANALYTICS")
DATA_SCHEMA = os.getenv("DATA_SCHEMA", "STAGE_DATA")
ANALYTICS_SCHEMA = os.getenv("ANALYTICS_SCHEMA", "ANALYTICS")

# ---------------------------------------------------------------------------
# Brand color palette
# ---------------------------------------------------------------------------
# BLUE #00B0F0 | GREEN #7AC943 | ORANGE #FF9316 | NAVY #192B59 | TEAL #156082
# ---------------------------------------------------------------------------
BRAND_COLORS = {
    "primary":       "#156082",   # teal — main interactive color
    "primary_light": "#00B0F0",   # blue — lighter accent / highlights
    "primary_deep":  "#192B59",   # navy — headings & strong text
    "accent_warm":   "#FF9316",   # orange
    "accent_cool":   "#00B0F0",   # blue
    "danger":        "#FF9316",   # orange — warnings / alerts
    "success":       "#7AC943",   # green
    "success_bg":    "#F0FAE9",
    "danger_bg":     "#FFF3E5",
    "bg_top":        "#F4F7FA",
    "bg_bottom":     "#FFFFFF",
    "panel":         "#F7F9FB",
    "card":          "#FFFFFF",
    "card_soft":     "#FAFBFD",
    "border":        "#E3E8EF",
    "text":          "#192B59",   # navy — body text
    "muted":         "#5C6B82",
    "flat":          "#5C6B82",
    "flat_bg":       "#F4F7FA",
    "shadow_rgb":    "25, 43, 89",  # navy for rgba()
    "track":         "#E3E8EF",
    "rule":          "#E3E8EF",
}

# Ordered categorical scale used in charts
CHART_CATEGORY_COLORS = [
    BRAND_COLORS["primary"],       # teal
    BRAND_COLORS["accent_warm"],   # orange
    BRAND_COLORS["accent_cool"],   # blue
    BRAND_COLORS["success"],       # green
    BRAND_COLORS["primary_deep"],  # navy
    BRAND_COLORS["primary_light"], # blue
    "#3D7A99",                     # mid-teal
]

