import pandas as pd
from statistics import mean
import streamlit as st

num_games_last_5 = 5
num_games_last_10 = 10
num_games_last_15 = 15

# Streamlit webapp
def main():
    st.title("0.5 Probability Predict")

home_team_input = st.text_input("Enter the home team: ")
away_team_input = st.text_input("Enter the away team: ")
home_team_input_xg = st.text_input("Enter the xG for the home team: ")
away_team_input_xg = st.text_input("Enter the xG for the away team: ")
home_team_input_odds = st.text_input("Enter the odds for the home team: ")
away_team_input_odds = st.text_input("Enter the odds for the away team: ")

#Calculate Home and Away over 0.5 goals scored

def calculate_goal_percentage(goals_scored):
    total_games = len(goals_scored)
    goals_over_05 = sum(1 for goals in goals_scored if goals > 0.5)
    goal_percentage = (goals_over_05 / total_games) * 100
    return goal_percentage

def check_last_five_home_games(home_team):
    df = pd.read_csv('https://raw.githubusercontent.com/willbadpenny/projecto/main/full_league_data_japan.csv', sep='\t', parse_dates=['Date'], dayfirst=True)

    home_team_games_last_5 = df[df['Home Team'] == home_team].head(5)
    home_team_games_last_5_sorted = home_team_games_last_5.sort_values(by='Date', ascending=False)

    home_team_games_last_10 = df[df['Home Team'] == home_team].head(10)
    home_team_games_last_10_sorted = home_team_games_last_10.sort_values(by='Date', ascending=False)

    home_team_games_last_15 = df[df['Home Team'] == home_team].head(15)
    home_team_games_last_15_sorted = home_team_games_last_15.sort_values(by='Date', ascending=False)

    if len(home_team_games_last_5_sorted) > 0:
        goal_percentage_last_5 = calculate_goal_percentage(home_team_games_last_5_sorted['Home Team Goals Scored After 90'].values)
    else:
        goal_percentage_last_5 = 0
    
    if len(home_team_games_last_10_sorted) > 0:
        goal_percentage_last_10 = calculate_goal_percentage(home_team_games_last_10_sorted['Home Team Goals Scored After 90'].values)
    else:
        goal_percentage_last_10 = 0

    if len(home_team_games_last_15_sorted) > 0:
        goal_percentage_last_15 = calculate_goal_percentage(home_team_games_last_15_sorted['Home Team Goals Scored After 90'].values)
    else:
        goal_percentage_last_15 = 0
    
    return goal_percentage_last_5, goal_percentage_last_10, goal_percentage_last_15

def check_last_five_away_games(away_team):
    df = pd.read_csv('https://raw.githubusercontent.com/willbadpenny/projecto/main/full_league_data_japan.csv', sep='\t', parse_dates=['Date'], dayfirst=True)

    away_team_games_last_5 = df[df['Away Team'] == away_team].head(5)
    away_team_games_last_5_sorted = away_team_games_last_5.sort_values(by='Date', ascending=False)

    away_team_games_last_10 = df[df['Away Team'] == away_team].head(10)
    away_team_games_last_10_sorted = away_team_games_last_10.sort_values(by='Date', ascending=False)

    away_team_games_last_15 = df[df['Away Team'] == away_team].head(15)
    away_team_games_last_15_sorted = away_team_games_last_15.sort_values(by='Date', ascending=False)

    if len(away_team_games_last_5_sorted) > 0:
        goal_percentage_last_5 = calculate_goal_percentage(away_team_games_last_5_sorted['Away Team Goals Scored After 90'].values)
    else:
        goal_percentage_last_5 = 0
    
    if len(away_team_games_last_10_sorted) > 0:
        goal_percentage_last_10 = calculate_goal_percentage(away_team_games_last_10_sorted['Away Team Goals Scored After 90'].values)
    else:
        goal_percentage_last_10 = 0

    if len(away_team_games_last_15_sorted) > 0:
        goal_percentage_last_15 = calculate_goal_percentage(away_team_games_last_15_sorted['Away Team Goals Scored After 90'].values)
    else:
        goal_percentage_last_15 = 0

    return goal_percentage_last_5, goal_percentage_last_10, goal_percentage_last_15


home_team_goal_percentage_last_5, home_team_goal_percentage_last_10, home_team_goal_percentage_last_15 = check_last_five_home_games(home_team_input)
away_team_goal_percentage_last_5, away_team_goal_percentage_last_10, away_team_goal_percentage_last_15 = check_last_five_away_games(away_team_input)

# Calculate the average goal percentages
home_team_average_goals_scored_over = mean([home_team_goal_percentage_last_5, home_team_goal_percentage_last_10, home_team_goal_percentage_last_15])
away_team_average_goals_scored_over = mean([away_team_goal_percentage_last_5, away_team_goal_percentage_last_10, away_team_goal_percentage_last_15])

print(f"{home_team_input} scored over 0.5 goals in {home_team_goal_percentage_last_5}% of their last five home games.")
print(f"{home_team_input} scored over 0.5 goals in {home_team_goal_percentage_last_10}% of their last ten home games.")
print(f"{home_team_input} scored over 0.5 goals in {home_team_goal_percentage_last_15}% of their last fifteen home games.")
print(f"{home_team_input} scored over 0.5 goals in {home_team_average_goals_scored_over}% of games on average.")
print(f"{away_team_input} scored over 0.5 goals in {away_team_goal_percentage_last_5}% of their last five away games.")
print(f"{away_team_input} scored over 0.5 goals in {away_team_goal_percentage_last_10}% of their last ten away games.")
print(f"{away_team_input} scored over 0.5 goals in {away_team_goal_percentage_last_15}% of their last fifteen away games.")
print(f"{away_team_input} scored over 0.5 goals in {away_team_average_goals_scored_over}% of games on average.")

# Store the goal percentages for later use
home_team_average_goals_scored_over = home_team_average_goals_scored_over
away_team_average_goals_scored_over = away_team_average_goals_scored_over

#Calculate Home and Away goals over 0.5 conceded

def calculate_goal_percentage(goals_conceded):
    total_games = len(goals_conceded)
    goals_over_05 = sum(1 for goals in goals_conceded if goals > 0.5)
    goal_percentage = (goals_over_05 / total_games) * 100
    return goal_percentage

def check_last_five_home_games(home_team):
    df = pd.read_csv('https://raw.githubusercontent.com/willbadpenny/projecto/main/full_league_data_japan.csv', sep='\t', parse_dates=['Date'], dayfirst=True)

    home_team_games_last_5 = df[df['Home Team'] == home_team].head(5)
    home_team_games_last_5_sorted = home_team_games_last_5.sort_values(by='Date', ascending=False)

    home_team_games_last_10 = df[df['Home Team'] == home_team].head(10)
    home_team_games_last_10_sorted = home_team_games_last_10.sort_values(by='Date', ascending=False)

    home_team_games_last_15 = df[df['Home Team'] == home_team].head(15)
    home_team_games_last_15_sorted = home_team_games_last_15.sort_values(by='Date', ascending=False)

    if len(home_team_games_last_5_sorted) > 0:
        goal_percentage_last_5 = calculate_goal_percentage(home_team_games_last_5_sorted['Home Team Goals Conceded After 90'].values)
    else:
        goal_percentage_last_5 = 0
    
    if len(home_team_games_last_10_sorted) > 0:
        goal_percentage_last_10 = calculate_goal_percentage(home_team_games_last_10_sorted['Home Team Goals Conceded After 90'].values)
    else:
        goal_percentage_last_10 = 0

    if len(home_team_games_last_15_sorted) > 0:
        goal_percentage_last_15 = calculate_goal_percentage(home_team_games_last_15_sorted['Home Team Goals Conceded After 90'].values)
    else:
        goal_percentage_last_15 = 0
    
    return goal_percentage_last_5, goal_percentage_last_10, goal_percentage_last_15

def check_last_five_away_games(away_team):
    df = pd.read_csv('https://raw.githubusercontent.com/willbadpenny/projecto/main/full_league_data_japan.csv', sep='\t', parse_dates=['Date'], dayfirst=True)

    away_team_games_last_5 = df[df['Away Team'] == away_team].head(5)
    away_team_games_last_5_sorted = away_team_games_last_5.sort_values(by='Date', ascending=False)

    away_team_games_last_10 = df[df['Away Team'] == away_team].head(10)
    away_team_games_last_10_sorted = away_team_games_last_10.sort_values(by='Date', ascending=False)

    away_team_games_last_15 = df[df['Away Team'] == away_team].head(15)
    away_team_games_last_15_sorted = away_team_games_last_15.sort_values(by='Date', ascending=False)

    if len(away_team_games_last_5_sorted) > 0:
        goal_percentage_last_5 = calculate_goal_percentage(away_team_games_last_5_sorted['Away Team Goals Conceded After 90'].values)
    else:
        goal_percentage_last_5 = 0
    
    if len(away_team_games_last_10_sorted) > 0:
        goal_percentage_last_10 = calculate_goal_percentage(away_team_games_last_10_sorted['Away Team Goals Conceded After 90'].values)
    else:
        goal_percentage_last_10 = 0

    if len(away_team_games_last_15_sorted) > 0:
        goal_percentage_last_15 = calculate_goal_percentage(away_team_games_last_15_sorted['Away Team Goals Conceded After 90'].values)
    else:
        goal_percentage_last_15 = 0
    
    return goal_percentage_last_5, goal_percentage_last_10, goal_percentage_last_15

home_team_goal_percentage_last_5, home_team_goal_percentage_last_10, home_team_goal_percentage_last_15 = check_last_five_home_games(home_team_input)
away_team_goal_percentage_last_5, away_team_goal_percentage_last_10, away_team_goal_percentage_last_15 = check_last_five_away_games(away_team_input)

# Calculate the average goal percentages
home_team_average_goals_conceded_over = mean([home_team_goal_percentage_last_5, home_team_goal_percentage_last_10, home_team_goal_percentage_last_15])
away_team_average_goals_conceded_over = mean([away_team_goal_percentage_last_5, away_team_goal_percentage_last_10, away_team_goal_percentage_last_15])

print(f"{home_team_input} conceded over 0.5 goals in {home_team_goal_percentage_last_5}% of their last five home games.")
print(f"{home_team_input} conceded over 0.5 goals in {home_team_goal_percentage_last_10}% of their last ten home games.")
print(f"{home_team_input} conceded over 0.5 goals in {home_team_goal_percentage_last_15}% of their last fifteen home games.")
print(f"{home_team_input} conceded over 0.5 goals in {home_team_average_goals_conceded_over}% of games on average.")
print(f"{away_team_input} conceded over 0.5 goals in {away_team_goal_percentage_last_5}% of their last five away games.")
print(f"{away_team_input} conceded over 0.5 goals in {away_team_goal_percentage_last_10}% of their last ten away games.")
print(f"{away_team_input} conceded over 0.5 goals in {away_team_goal_percentage_last_15}% of their last fifteen away games.")
print(f"{away_team_input} conceded over 0.5 goals in {away_team_average_goals_conceded_over}% of games on average.")

# Store the goal percentages for later use
home_team_average_goals_conceded_over = home_team_average_goals_conceded_over
away_team_average_goals_conceded_over = away_team_average_goals_conceded_over

# Calulcate goals over 0.5 scored in the second half of games

def calculate_goal_percentage(goals_scored):
    total_games = len(goals_scored)
    goals_over_05 = sum(1 for goals in goals_scored if goals > 0.5)
    goal_percentage = (goals_over_05 / total_games) * 100
    return goal_percentage

def check_last_games(home_team, away_team, num_games):
    df = pd.read_csv('https://raw.githubusercontent.com/willbadpenny/projecto/main/full_league_data_japan.csv', sep='\t', parse_dates=['Date'], dayfirst=True)

    home_team_games = df[df['Home Team'] == home_team].sort_values(by='Date', ascending=False).head(num_games)
    away_team_games = df[df['Away Team'] == away_team].sort_values(by='Date', ascending=False).head(num_games)

    if len(home_team_games) > 0:
        goals_scored_after_45_home = home_team_games['Home Team Goals Scored After 45'].values
        goals_scored_after_90_home = home_team_games['Home Team Goals Scored After 90'].values
        goals_scored_second_half_home = [goals_after_90 - goals_after_45 > 0.5 for goals_after_45, goals_after_90 in zip(goals_scored_after_45_home, goals_scored_after_90_home)]
        goal_percentage_home = calculate_goal_percentage(goals_scored_second_half_home)
    else:
        goal_percentage_home = 0

    if len(away_team_games) > 0:
        goals_scored_after_45_away = away_team_games['Away Team Goals Scored After 45'].values
        goals_scored_after_90_away = away_team_games['Away Team Goals Scored After 90'].values
        goals_scored_second_half_away = [goals_after_90 - goals_after_45 > 0.5 for goals_after_45, goals_after_90 in zip(goals_scored_after_45_away, goals_scored_after_90_away)]
        goal_percentage_away = calculate_goal_percentage(goals_scored_second_half_away)
    else:
        goal_percentage_away = 0

    return goal_percentage_home, goal_percentage_away

home_team_goal_percentage_last_5, away_team_goal_percentage_last_5 = check_last_games(home_team_input, away_team_input, num_games_last_5)
home_team_goal_percentage_last_10, away_team_goal_percentage_last_10 = check_last_games(home_team_input, away_team_input, num_games_last_10)
home_team_goal_percentage_last_15, away_team_goal_percentage_last_15 = check_last_games(home_team_input, away_team_input, num_games_last_15)

home_team_average_goals_scored_over_2nd_half = mean([home_team_goal_percentage_last_5, home_team_goal_percentage_last_10, home_team_goal_percentage_last_15])
away_team_average_goals_scored_over_2nd_half = mean([away_team_goal_percentage_last_5, away_team_goal_percentage_last_10, away_team_goal_percentage_last_15])

print(f"{home_team_input} scored over 0.5 goals in the second half in {home_team_goal_percentage_last_5}% of their last 5 home games.")
print(f"{home_team_input} scored over 0.5 goals in the second half in {home_team_goal_percentage_last_10}% of their last 10 home games.")
print(f"{home_team_input} scored over 0.5 goals in the second half in {home_team_goal_percentage_last_15}% of their last 15 home games.")
print(f"{home_team_input} scored over 0.5 goals in the second half in {home_team_average_goals_scored_over_2nd_half}% of games on average.")
print(f"{away_team_input} scored over 0.5 goals in the second half in {away_team_goal_percentage_last_5}% of their last 5 away games.")
print(f"{away_team_input} scored over 0.5 goals in the second half in {away_team_goal_percentage_last_10}% of their last 10 away games.")
print(f"{away_team_input} scored over 0.5 goals in the second half in {away_team_goal_percentage_last_15}% of their last 15 away games.")
print(f"{away_team_input} scored over 0.5 goals in the second half in {away_team_average_goals_scored_over_2nd_half}% of games on average.")

# Store the goal percentages for later use
home_team_average_goals_scored_over_2nd_half = home_team_average_goals_scored_over_2nd_half
away_team_average_goals_scored_over_2nd_half = away_team_average_goals_scored_over_2nd_half

# Calulcate goals over 0.5 conceded in the second half of games

def calculate_goal_percentage(goals_conceded):
    total_games = len(goals_conceded)
    goals_over_05 = sum(1 for goals in goals_conceded if goals > 0.5)
    goal_percentage = (goals_over_05 / total_games) * 100
    return goal_percentage

def check_last_games(home_team, away_team, num_games):
    df = pd.read_csv('https://raw.githubusercontent.com/willbadpenny/projecto/main/full_league_data_japan.csv', sep='\t', parse_dates=['Date'], dayfirst=True)

    home_team_games = df[df['Home Team'] == home_team].sort_values(by='Date', ascending=False).head(num_games)
    away_team_games = df[df['Away Team'] == away_team].sort_values(by='Date', ascending=False).head(num_games)

    if len(home_team_games) > 0:
        goals_conceded_after_45_home = home_team_games['Home Team Goals Conceded After 45'].values
        goals_conceded_after_90_home = home_team_games['Home Team Goals Conceded After 90'].values
        goals_conceded_second_half_home = [goals_after_90 - goals_after_45 > 0.5 for goals_after_45, goals_after_90 in zip(goals_conceded_after_45_home, goals_conceded_after_90_home)]
        goal_percentage_home = calculate_goal_percentage(goals_conceded_second_half_home)
    else:
        goal_percentage_home = 0

    if len(away_team_games) > 0:
        goals_conceded_after_45_away = away_team_games['Away Team Goals Conceded After 45'].values
        goals_conceded_after_90_away = away_team_games['Away Team Goals Conceded After 90'].values
        goals_conceded_second_half_away = [goals_after_90 - goals_after_45 > 0.5 for goals_after_45, goals_after_90 in zip(goals_conceded_after_45_away, goals_conceded_after_90_away)]
        goal_percentage_away = calculate_goal_percentage(goals_conceded_second_half_away)
    else:
        goal_percentage_away = 0

    return goal_percentage_home, goal_percentage_away

num_games_last_5 = 5
num_games_last_10 = 10
num_games_last_15 = 15

home_team_goal_percentage_last_5, away_team_goal_percentage_last_5 = check_last_games(home_team_input, away_team_input, num_games_last_5)
home_team_goal_percentage_last_10, away_team_goal_percentage_last_10 = check_last_games(home_team_input, away_team_input, num_games_last_10)
home_team_goal_percentage_last_15, away_team_goal_percentage_last_15 = check_last_games(home_team_input, away_team_input, num_games_last_15)

home_team_average_conceded_second_half = mean([home_team_goal_percentage_last_5, home_team_goal_percentage_last_10, home_team_goal_percentage_last_15])
away_team_average_conceded_second_half = mean([away_team_goal_percentage_last_5, away_team_goal_percentage_last_10, away_team_goal_percentage_last_15])

print(f"{home_team_input} conceded over 0.5 goals in the second half in {home_team_goal_percentage_last_5}% of their last {num_games_last_5} home games.")
print(f"{home_team_input} conceded over 0.5 goals in the second half in {home_team_goal_percentage_last_10}% of their last {num_games_last_10} home games.")
print(f"{home_team_input} conceded over 0.5 goals in the second half in {home_team_goal_percentage_last_15}% of their last {num_games_last_15} home games.")
print(f"{home_team_input} conceded over 0.5 goals in the second half in {home_team_average_conceded_second_half}% of games on average.")
print(f"{away_team_input} conceded over 0.5 goals in the second half in {away_team_goal_percentage_last_5}% of their last {num_games_last_5} away games.")
print(f"{away_team_input} conceded over 0.5 goals in the second half in {away_team_goal_percentage_last_10}% of their last {num_games_last_10} away games.")
print(f"{away_team_input} conceded over 0.5 goals in the second half in {away_team_goal_percentage_last_15}% of their last {num_games_last_15} away games.")
print(f"{away_team_input} conceded over 0.5 goals in the second half in {away_team_average_conceded_second_half}% of games on average.")

# Store the goal percentages for later use
home_team_average_conceded_second_half = home_team_average_conceded_second_half
away_team_average_conceded_second_half = away_team_average_conceded_second_half

# Calculate Home goals scored in second half when xG over 0.5 at half time and 0 goals scored after 45

def calculate_percentage(condition_met, total_games):
    percentage = (condition_met / total_games) * 100
    return percentage

def check_condition(home_team, df):
    home_team_games = df[df['Home Team'] == home_team]

    condition_met = len(home_team_games[(home_team_games['xg Home After 45'] > 0.5) &
                                        (home_team_games['Home Team Goals Scored After 45'] == 0) &
                                        (home_team_games['Home Team Goals Scored After 90'] > 0.5)])

    percentage = calculate_percentage(condition_met, len(home_team_games))
    return percentage

df = pd.read_csv('https://raw.githubusercontent.com/willbadpenny/projecto/main/full_league_data_japan.csv', sep='\t', parse_dates=['Date'], dayfirst=True)
home_team_percentage_over_and_xg = check_condition(home_team_input, df)

print(f"{home_team_input} scored 0 goals after 45 minutes, had xG > 0.5 after 45 minutes, and scored over 0.5 goals after 90 minutes in {home_team_percentage_over_and_xg}% of their games.")

# Calculate Away goals scored in second half when xG over 0.5 at half time and 0 goals scored after 45

def calculate_percentage(condition_met, total_games):
    percentage = (condition_met / total_games) * 100
    return percentage

def check_condition(away_team, df):
    away_team_games = df[df['Away Team'] == away_team]
    try:
        condition_met = len(away_team_games[(away_team_games['xg Away After 45'] > 0.5) &
                                            (away_team_games['Away Team Goals Scored After 45'] == 0) &
                                            (away_team_games['Away Team Goals Scored After 90'] > 0.5)])
        percentage = calculate_percentage(condition_met, len(away_team_games))
    except ZeroDivisionError:
        percentage = 0
    return percentage

df = pd.read_csv('https://raw.githubusercontent.com/willbadpenny/projecto/main/full_league_data_japan.csv', sep='\t', parse_dates=['Date'], dayfirst=True)

away_team_percentage_over_and_xg = check_condition(away_team_input, df)

print(f"{away_team_input} scored 0 goals after 45 minutes, had xG > 0.5 after 45 minutes, and scored over 0.5 goals after 90 minutes in {away_team_percentage_over_and_xg}% of their games.")

# Store the goal percentages for later use

home_team_percentage_over_and_xg = home_team_percentage_over_and_xg
away_team_percentage_over_and_xg = away_team_percentage_over_and_xg

#Calculate xG input and convert to %

xg = float(home_team_input_xg)
home_team_input_xg_percentage = xg * 100

xg = float(away_team_input_xg)
away_team_input_xg_percentage = xg * 100

#Calculate averages of all data and output estimated probability

total_values = 6
average_total_home = (
    home_team_average_goals_scored_over
    + away_team_average_goals_conceded_over
    + home_team_average_goals_scored_over_2nd_half
    + away_team_average_conceded_second_half
    + home_team_percentage_over_and_xg
    + home_team_input_xg_percentage
) / total_values

total_values = 6
average_total_away = (
    away_team_average_goals_scored_over
    + home_team_average_goals_conceded_over
    + away_team_average_goals_scored_over_2nd_half
    + home_team_average_conceded_second_half
    + home_team_percentage_over_and_xg
    + away_team_input_xg_percentage
) / total_values

print(f"{home_team_input} estimated probability: {average_total_home:.2f}%")
print(f"{away_team_input} estimated probability: {average_total_away:.2f}%")

#Calculate implied probability as % and output

implied_probability_home = 1 / float(home_team_input_odds)
implied_probability_home_percentage = implied_probability_home * 100

implied_probability_away = 1 / float(away_team_input_odds)
implied_probability_away_percentage = implied_probability_away * 100

print(f"{home_team_input} implied probability from odds: {implied_probability_home_percentage:.2f}%")
print(f"{away_team_input} implied probability from odds: {implied_probability_away_percentage:.2f}%")



if st.button("Calculate"):
    total_values = 6
    average_total_home = (
    home_team_average_goals_scored_over
    + away_team_average_goals_conceded_over
    + home_team_average_goals_scored_over_2nd_half
    + away_team_average_conceded_second_half
    + home_team_percentage_over_and_xg
    + home_team_input_xg_percentage
    ) / total_values

    total_values = 6
    average_total_away = (
    away_team_average_goals_scored_over
    + home_team_average_goals_conceded_over
    + away_team_average_goals_scored_over_2nd_half
    + home_team_average_conceded_second_half
    + home_team_percentage_over_and_xg
    + away_team_input_xg_percentage
    ) / total_values

    implied_probability_home = 1 / float(home_team_input_odds)
    implied_probability_home_percentage = implied_probability_home * 100

    implied_probability_away = 1 / float(away_team_input_odds)
    implied_probability_away_percentage = implied_probability_away * 100

    st.write(f"**{home_team_input} estimated probability: {average_total_home:.2f}%**")
    st.write(f"**{away_team_input} estimated probability: {average_total_away:.2f}%**")
    st.write(f"**{home_team_input} implied probability from odds: {implied_probability_home_percentage:.2f}%**")
    st.write(f"**{away_team_input} implied probability from odds: {implied_probability_away_percentage:.2f}%**")

if __name__ == "__main__":
    main()
