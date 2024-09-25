import streamlit as st
import requests

# Function to interact with Gemini API
def generate_campaign(club_name, event_name, event_description, guest_name, guest_title, date, venue, audience, tone):
    prompt = f"Generate an invitation for the {club_name} at SPJIMR. The event is {event_name}, focused on {event_description}. Chief guest {guest_name}, {guest_title}, on {date} at {venue}. Target audience: {audience}. Tone: {tone}."
    
    api_key = "AIzaSyAQSX5N-uSJZ4dPgOjQ73IP06k0JJ-9iPo"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
        # Add any other parameters as required by the Gemini API
    }

    response = requests.post('https://api.gemini.com/generate', headers=headers, json=data)
    response_json = response.json()

    if response.status_code == 200:
        return response_json.get('generated_text', 'Campaign could not be generated.')
    else:
        return f"Error: {response_json.get('error', 'API request failed')}"

# Streamlit UI
st.title("SPJIMR Event Campaign Generator")

club_name = st.selectbox("Select Club", ["Consulting Club", "Analytics Club", "Product Management Club", "Speak Club", "OSCM Club", "Marketing Club", "Investment Club"])
event_name = st.text_input("Event Name")
event_description = st.text_area("Event Description")
guest_name = st.text_input("Chief Guest Name")
guest_title = st.text_input("Chief Guest Title")
date = st.date_input("Event Date")
venue = st.text_input("Venue")
audience = st.selectbox("Target Audience", ["Students", "Faculty", "Professionals"])
tone = st.selectbox("Tone of Campaign", ["Informative", "Exciting", "Formal"])

if st.button("Generate Campaign"):
    campaign = generate_campaign(club_name, event_name, event_description, guest_name, guest_title, date, venue, audience, tone)
    st.write(campaign)
