import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(page_title="IPL Predictor", page_icon="🏏", layout="centered")

# Background (IPL style)
# c:\Users\ELCOT\Downloads\backgrounds.jpg
import base64

def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# CALL FUNCTION
set_bg("backgrounds.jpg")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.markdown(
    "<h1 style='text-align:center; color:white; text-shadow: 2px 2px 10px black;'>🏏 IPL Match Winner Predictor</h1>",
    unsafe_allow_html=True
)

# Teams
teams = [
    "Chennai Super Kings",
    "Mumbai Indians",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Sunrisers Hyderabad",
    "Delhi Capitals",
    "Rajasthan Royals",
    "Punjab Kings",
    "Gujarat Titans",
    "Lucknow Super Giants",
    "Deccan Chargers",
    "Gujarat Lions",
    "Rising Pune Supergiants"
]

# Venues
venues = [
    "Wankhede Stadium",
    "Eden Gardens",
    "M Chinnaswamy Stadium",
    "MA Chidambaram Stadium",
    "Feroz Shah Kotla"
]

# Mapping
team_mapping = {team: i for i, team in enumerate(teams)}
reverse_mapping = {v: k for k, v in team_mapping.items()}
venue_mapping = {venue: i for i, venue in enumerate(venues)}

# Team slogans 🔥
slogans = {
    "Chennai Super Kings": "Whistle Podu! 🦁💛",
    "Mumbai Indians": "Duniya Hila Denge! 🔵",
    "Royal Challengers Bangalore": "Ee Sala Cup Namde! 🔴",
    "Kolkata Knight Riders": "Korbo Lorbo Jeetbo! 🟣",
    "Sunrisers Hyderabad": "Orange Army Rising! 🧡",
    "Delhi Capitals": "Roar Macha! 🔵",
    "Rajasthan Royals": "Halla Bol! 💗",
    "Punjab Kings": "Sadda Punjab! ❤️",
    "Gujarat Titans": "Aava De! 🔷",
    "Lucknow Super Giants": "Ab Apni Baari Hai! 💙"
}

# Layout
col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Team 1", teams)
    toss_winner = st.selectbox("Toss Winner", teams)

with col2:
    team2 = st.selectbox("Team 2", teams)
    venue = st.selectbox("Venue", venues)

# Validation
if team1 == team2:
    st.error("Team 1 and Team 2 cannot be same")

# Prediction
if st.button("Predict Winner 🚀"):
    data = np.array([[
        team_mapping[team1],
        team_mapping[team2],
        team_mapping[toss_winner],
        venue_mapping[venue]
    ]])

    prediction = model.predict(data)
    winner_name = reverse_mapping.get(prediction[0], "Unknown")

    st.success(f"🏆 Predicted Winner: {winner_name}")
    st.balloons()
    # Show slogan
    if winner_name in slogans:
        st.markdown(f"<h3 style='text-align:center; color:yellow;'>{slogans[winner_name]}</h3>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color:white;'>Made by ❤️ by MOHAMMED HAFID K</p>", unsafe_allow_html=True)