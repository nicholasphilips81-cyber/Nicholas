from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Halcyon Warp Cruiser",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html(
    """
    <style>
        html,
        body,
        [data-testid="stApp"],
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"] {
            height: 100%;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        #MainMenu,
        footer {
            display: none !important;
        }

        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"] {
            min-height: 100dvh;
            overflow: hidden;
        }

        [data-testid="stMain"] {
            padding-top: 0 !important;
        }

        [data-testid="stMainBlockContainer"] {
            width: 100%;
            max-width: none;
            padding: 0 !important;
        }

        [data-testid="stIFrame"] {
            height: 100dvh !important;
            min-height: 100dvh !important;
            padding: 0 !important;
        }

        [data-testid="stIFrame"] iframe {
            display: block;
            width: 100%;
            height: 100dvh !important;
            min-height: 100dvh !important;
            border: 0;
        }
    </style>
    """
)

simulation_path = Path(__file__).with_name("Halcyon Warp Cruiser.html")
if not simulation_path.is_file():
    st.error(f"Could not find the simulation file: {simulation_path.name}")
    st.stop()

st.iframe(
    simulation_path,
    width="stretch",
    height="stretch",
    alt="Interactive 3D Halcyon warp cruiser with warp controls and camera views",
)
