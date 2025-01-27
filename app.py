import streamlit as st
import pickle
import pandas as pd

teams = ['Liverpool', 'Arsenal', 'Nottingham Forest', 'Manchester City',
       'Newcastle United', 'Chelsea', 'Bournemouth', 'Aston Villa',
       'Brighton and Hove Albion', 'Fulham', 'Brentford',
       'Crystal Palace', 'Manchester United', 'West Ham United',
       'Tottenham Hotspur', 'Everton', 'Wolverhampton Wanderers',
       'Ipswich Town', 'Leicester City', 'Southampton', 'Luton Town',
       'Burnley', 'Sheffield United', 'Leeds United', 'Watford',
       'Norwich City', 'West Bromwich Albion', 'Cardiff City',
       'Huddersfield Town', 'Swansea City', 'Stoke City']

teams_dict = {'Arsenal': 0,
 'Aston Villa': 1,
 'Bournemouth': 2,
 'Brentford': 3,
 'Brighton and Hove Albion': 4,
 'Burnley': 5,
 'Cardiff City': 6,
 'Chelsea': 7,
 'Crystal Palace': 8,
 'Everton': 9,
 'Fulham': 10,
 'Huddersfield Town': 11,
 'Ipswich Town': 12,
 'Leeds United': 13,
 'Leicester City': 14,
 'Liverpool': 15,
 'Luton Town': 16,
 'Manchester City': 17,
 'Manchester United': 18,
 'Newcastle United': 19,
 'Norwich City': 20,
 'Nottingham Forest': 21,
 'Sheffield United': 22,
 'Southampton': 23,
 'Stoke City': 24,
 'Swansea City': 25,
 'Tottenham Hotspur': 26,
 'Watford': 27,
 'West Bromwich Albion': 28,
 'West Ham United': 29,
 'Wolverhampton Wanderers': 30}

model = pickle.load(open('model.pkl', 'rb'))

st.title("Premier League Win Predictor")

col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox("Select the home team", sorted(teams))
with col2:
    away_team = st.selectbox("Select the away team", sorted(teams))

col1, col2 = st.columns(2)

with col1:
    xg = st.number_input("Enter the Expected Goals (xG)")
with col2:
    xgA = st.number_input("Enter the Expected Goals Against (xGA)")


if st.button("Predict the winner"):
    team_code = teams_dict[home_team]
    opp_code = teams_dict[away_team]
    # predictors = ["venue_code", "opp_code","team_code","xg", "xga", "gf", "ga"]
    input_df = pd.DataFrame({'venue_code':[1], 'opp_code': [opp_code],
                             'team_code':[team_code], 'xg':[xg], 'xga': [xgA]})

    # st.table(input_df)
    result = model.predict(input_df)
    if result == 1 :
        st.subheader(f'{home_team} is likely to win!')

    else:
        st.subheader(f'{away_team} is likely to win!')

