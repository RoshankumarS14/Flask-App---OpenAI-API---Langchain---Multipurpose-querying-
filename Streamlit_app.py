import streamlit as st
from airtable import Airtable
import os

base_key = 'appDeLA2xgfphKya3'
table_name = 'Prompts'
api_key = os.getenv("AIRTABLE_API_KEY")
airtable = Airtable(base_key, table_name, api_key)

if "prompts_data" not in st.session_state:
    st.session_state["prompts_data"] = {i["fields"]["Title"]:i["fields"]["Prompt Instructions"] for i in airtable.get_all()}

if "prompts_id" not in st.session_state:
    st.session_state["prompts_id"] = {i["fields"]["Title"]:i["id"] for i in airtable.get_all()}

st.session_state["selected_prompt"] = st.selectbox("Select the prompt to modify its instructions:",st.session_state["prompts_data"].keys())

st.subheader(st.session_state["selected_prompt"])
quality_prompt = st.text_area("", st.session_state["prompts_data"][st.session_state["selected_prompt"]],height=400)
save_quality = st.button('Save Prompt')
# Display the buttons to save the prompts
if save_quality:
    st.write(st.session_state["prompts_id"][st.session_state["selected_prompt"]])
    record_id = st.session_state["prompts_id"][st.session_state["selected_prompt"]]
    update_instructions = {
        'Prompt Instructions': quality_prompt
    }
    updated_record = airtable.update(record_id, update_instructions)
    st.success('Instructions saved!')
