import streamlit as st
from airtable import Airtable
import os

base_key = 'appDeLA2xgfphKya3'
table_name = 'Prompts'
api_key = os.getenv("AIRTABLE_API_KEY")
airtable = Airtable(base_key, table_name, api_key)

if "save_prompt" not in st.session_state:
    st.session_state["save_prompt"] = False

if "prompt_title" not in st.session_state:
    st.session_state["prompt_title"] = ""

if "new_prompt_instructions" not in st.session_state:
    st.session_state["new_prompt_instructions"] = ""

st.session_state["prompt_title"] = st.text_input("Enter the Title for the prompt:")
st.session_state["new_prompt_instructions"] = st.text_area("Enter the instructions for the prompt:",height=500)

st.session_state["save_prompt"] = st.button("Save!")

if st.session_state["save_prompt"]:

    new_record_data = {
        'Title': st.session_state["prompt_title"],
        'Prompt Instructions': st.session_state["new_prompt_instructions"],
    }

    # Creating the new record
    new_record = airtable.insert(new_record_data)
    st.success("New Prompt Instruction added successfully!")
