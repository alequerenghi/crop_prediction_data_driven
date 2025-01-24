import streamlit as st
import pandas as pd
from db_utils import get_predictions_by_username

def user_data_page():
    st.title("These are your predictions")

    results = get_predictions_by_username(st.session_state["username"])
    if results:
        df = pd.DataFrame(results, columns=["Plant", "Country", "Hectares", "Prediction (tons)"])
        st.table(df.style.format({"Prediction (tons)": "{:.2f}"}))
    else:
        st.warning(f"No predictions found, make one!")

