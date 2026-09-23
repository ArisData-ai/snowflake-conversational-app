# Conversational Analytics Application

An enterprise-grade Streamlit application for **Conversational Analytics**, powered by **Snowflake Cortex Agent REST API**, Snowflake Semantic Views, and database-backed application management.

This is a **reusable template** — all branding, data references, and configuration are parameterized for easy adaptation to any domain or client.

---

## Application Architecture & Data Flow

The application consists of two independent core workflows: **Conversational Analytics Chat Flow** and **Sidebar Navigation & Admin Access Control Flow**.

### Flow 1: Conversational Analytics Chat Flow

```text
User Question / Suggested Chip Click
               │
               ▼
   Snowflake Cortex Agent REST API
    (POST /api/v2/cortex/agent:run SSE Stream)
               │
               ▼
   SSE Event Collector & Delta Stream Processor
    (collect_response() in services/cortex_agent.py)
               │
               ├───────────────────────┬───────────────────────┐
               │                       │                       │
               ▼                       ▼                       ▼
    Answer Text & Badges      Vega-Lite Chart Spec      Executed SQL & Data Table
               │                       │                       │
               └───────────────────────┴───────────────────────┘
                                       │
                                       ▼
                          Streamlit Chat Interface
                                       │
                                       ▼
                          PDF Report Conversation Export
```

### Flow 2: Sidebar Navigation & Admin Access Control Flow

```text
Sidebar Navigation Radio Selection
               │
               ▼
   Admin Privilege Verification
    (check_is_admin() via SP_APP_IS_ADMIN)
               │
               ├─────────────────────────────────┐
               │                                 │
               ▼                                 ▼
   [If Admin = True]               [If Admin = False]
   Full Settings Page Access        Settings Navigation
   (ui/settings_page.py)            Hidden / Restricted
```

---

## Quick Start: Adapting This Template

1. **`config.py`** — Update `DB`, `APP_SCHEMA`, `DATA_SCHEMA`, `ANALYTICS_SCHEMA` defaults and `BRAND_COLORS` palette.
2. **`snowflake.yml`** — Set your `query_warehouse`, `compute_pool`, `database`, `schema`, and `role`.
3. **`init_settings_db.sql`** — Run this script in your target schema to create settings tables and stored procedures. Update the seed values for `SEMANTIC_VIEW`, `WAREHOUSE_NAME`, and `ANALYST_TOOL_NAME`.
4. **Logo** — Place your logo at `assets/logo.png` and uncomment the artifact line in `snowflake.yml`.
5. **Semantic View** — Configure your Cortex Analyst semantic view name on the Settings page or in the seed SQL.

---

## Key Features

### 1. Conversational Analytics via Cortex Agent
- **REST SSE Streaming Integration** with Snowflake's `/api/v2/cortex/agent:run` endpoint.
- **Live Status Feedback**: Dynamic progress indicators during query processing.
- **Sanitized Response Formatting**: Cleans encoding artifacts, formats section headers with icons, highlights metric values.

### 2. KPI Strip
- **Database View Driven**: Queries `{DB}.{ANALYTICS_SCHEMA}.VW_KPI_CARDS` via active Snowflake session (configurable).
- **Period-over-Period Comparison**: Displays current vs. previous period metrics with direction arrows and delta chips.

### 3. Database-Backed Settings & Admin Management
- **Admin Privilege Access Control** via stored procedure `SP_APP_IS_ADMIN`.
- **Tabbed Settings Page**: Suggested Questions, Logo, Connection & Agent, Header & Banner, Admin Users.

### 4. Conversation PDF Export
- Exports full conversation to PDF with company logo, banner title, charts, SQL blocks, and data tables.

### 5. Interactive Vega-Lite Charting
- Renders chart specs from Cortex Agent with multi-color categorical palettes and hover animations.

---

## File Structure

| File | Purpose |
|------|---------|
| `config.py` | Centralized configuration: DB names, schemas, brand colors |
| `streamlit_app.py` | Main entry point, page routing, CSS theme, chat UI |
| `snowflake.yml` | Snowflake deployment manifest |
| `init_settings_db.sql` | DB setup: tables, stored procedures, seed data |
| `services/cortex_agent.py` | Cortex Agent REST API integration, SSE streaming, chart rendering |
| `services/settings_service.py` | DB persistence for settings, questions, admin users |
| `services/snowflake_connection.py` | Snowflake session management |
| `services/pdf_generator.py` | ReportLab PDF export engine |
| `ui/components.py` | Custom KPI cards, sample question buttons, metric styling |
| `ui/settings_page.py` | Tabbed settings management interface |
| `ui/chart_renderer.py` | Plotly chart renderer |
| `visualization/chart_generator.py` | Dynamic fallback chart generation |

---

## Database Objects

### Tables (`{DB}.{APP_SCHEMA}`)
- **`REF_APP_QUESTIONS`** — Suggested question text, display order, active flag, audit tracking.
- **`REF_APP_SETTINGS`** — Key-value configuration strings and binary logo blobs.
- **`REF_APP_ADMIN_USERS`** — Admin usernames, active status, audit fields.

### Stored Procedures (`{DB}.{APP_SCHEMA}`)
- `SP_APP_GET_APP_SETTINGS()` — Returns settings key-value pairs and logo blobs.
- `SP_APP_SAVE_APP_SETTING(P_KEY, P_VAL, P_USER)` — Upserts a setting value.
- `SP_APP_SAVE_APP_SETTING_BLOB(P_KEY, P_BLOB, P_USER)` — Upserts binary blobs.
- `SP_APP_GET_QUESTIONS()` — Returns active suggested questions.
- `SP_APP_SAVE_QUESTION(P_ID, P_TEXT, P_ORDER, P_USER)` — Inserts or updates questions.
- `SP_APP_DELETE_QUESTION(P_ID, P_USER)` — Soft-deletes questions.
- `SP_APP_IS_ADMIN(P_USERNAME)` — Returns boolean admin check.
- `SP_APP_GET_ADMIN_USERS()` — Returns admin user records.
- `SP_APP_SAVE_ADMIN_USER(P_USERNAME, P_ACTIVE, P_USER)` — Adds or updates admin users.
- `SP_APP_DELETE_ADMIN_USER(P_USERNAME, P_USER)` — Removes an admin user.
