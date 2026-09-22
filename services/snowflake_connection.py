"""Snowflake Connection Module for Workspace Streamlit.

Uses the embedded st.connection("snowflake") provided by the Snowflake
Workspace runtime. No secrets.toml or environment variable credentials needed.
"""

import os
import logging
from typing import Optional, Any

import streamlit as st

logger = logging.getLogger("snowflake_connection")


def get_snowflake_session() -> Optional[Any]:
    """Retrieve a Snowpark session from the Workspace Streamlit connection.

    Returns:
        Snowpark Session object if available, or None in offline mode.
    """
    try:
        conn = st.connection("snowflake", ttl=os.getenv("SNOWFLAKE_CONNECTION_TTL"))
        session = conn.session()
        if session:
            logger.info("Snowpark session acquired via st.connection('snowflake').")
            return session
    except Exception as err:
        logger.warning("Unable to initialize Snowflake session: %s. Falling back to synthetic data mode.", err)

    logger.info("Operating in standalone simulation mode with synthetic data.")
    return None
