import streamlit as st
import google.generativeai as genai

# Configure the API using the correct API key (you can load it from a JSON file or environment variable)
def load_api_key():
    """Load API key from Streamlit secrets (TOML format)"""
    return st.secrets["GEMINI_KEY"]

genai.configure(api_key=load_api_key())

def generate_campaign(club_name, event_name, event_description, guest_name, guest_title, date, venue, audience, tone):
<<<<<<< HEAD
    prompt = f"As a Marketing Specialist, craft an engaging and persuasive event invitation for {club_name} at SPJIMR. The event is titled {event_name}, focusing on {event_description}. Highlight the participation of our Chief Guest, {guest_name}, who holds the title of {guest_title}. The event will be held on {date} at {venue}, targeting {audience}. Your tone should be {tone}, ensuring it aligns perfectly with the target audience. Tone-specific nuances: - **Exciting tone**: Use at least 3-4 emojis and enthusiastic language, but keep the creativity controlled. - **Formal tone**: Keep the language concise, formal, and direct, with no unnecessary embellishments.Ensure the invitation: 1. Clearly communicates the importance and relevance of the event. 2. Emphasizes the credentials and value brought by the Chief Guest. 3. Creates a sense of urgency and excitement, motivating recipients to attend. 4. Aligns with {club_name}'s values and branding. "   
=======
    prompt = f"As a Marketing Specialist, craft an engaging and persuasive event invitation for {club_name} at SPJIMR. The event is titled {event_name}, focusing on {event_description}. Highlight the participation of our Chief Guest, {guest_name}, who holds the title of {guest_title}. The event will be held on {date} at {venue}, targeting {audience}. Your tone should be {tone}, ensuring it aligns perfectly with the target audience. Tone-specific nuances: - **Exciting tone**: Use at least 3-4 emojis and enthusiastic language, but keep the creativity controlled. - **Formal tone**: Keep the language concise, formal, and direct, with no unnecessary embellishments.Ensure the invitation: 1. Clearly communicates the importance and relevance of the event. 2. Emphasizes the credentials and value brought by the Chief Guest. 3. Creates a sense of urgency and excitement, motivating recipients to attend. 4. Aligns with {club_name}'s values and branding. "        
>>>>>>> 1462416 (Changes in prompt)
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content([prompt])

        # Output the response for debugging
        # st.write("API Response:", response)

        # Access the generated text
        if response and response.candidates and len(response.candidates) > 0:
            generated_text = ''
            for candidate in response.candidates:
                if candidate.content and candidate.content.parts:
                    for part in candidate.content.parts:
                        generated_text += part.text
            return generated_text.strip()
        else:
            return "Error: No text found in the response."

    except Exception as e:
        st.error(f"Error generating campaign: {str(e)}")
        return f"Error: {str(e)}"


# Streamlit UI for gathering input and displaying output
st.title("SPJIMR Event Campaign Generator")

# Input fields for the event campaign details
club_name = st.selectbox("Select Club", [
    "Consulting Club", 
    "Analytics Club", 
    "Product Management Club", 
    "Speak Club", 
    "OSCM Club", 
    "Marketing Club", 
    "Investment Club"
])
event_name = st.text_input("Event Name")
event_description = st.text_area("Event Description")
guest_name = st.text_input("Chief Guest Name")
guest_title = st.text_input("Chief Guest Title")
date = st.date_input("Event Date")
venue = st.text_input("Venue")
audience = st.selectbox("Target Audience", ["Students", "Faculty", "Professionals"])
tone = st.selectbox("Tone of Campaign", ["Informative", "Exciting", "Formal"])

# Generate campaign when the button is clicked
if st.button("Generate Campaign"):
    campaign = generate_campaign(club_name, event_name, event_description, guest_name, guest_title, date, venue, audience, tone)
    
    # Format and display the generated campaign using markdown
    st.markdown(f"""
        ## {event_name}
        
        **Club**: {club_name}  
        **Event Description**: {event_description}  
        **Chief Guest**: {guest_name}, {guest_title}  
        **Date**: {date}  
        **Venue**: {venue}  
        **Target Audience**: {audience}  
        **Tone**: {tone}

        ### Generated Campaign
        {campaign}
    """)
