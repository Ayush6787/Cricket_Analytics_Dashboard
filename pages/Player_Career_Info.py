import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Player Info", layout="wide")

# Custom CSS for background and section styling
custom_css = """
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
        url('https://i.imgur.com/l9HuE5j.jpeg') no-repeat center center fixed;
        background-size: cover;
        font-family: Arial, sans-serif;
        color: #ffffff;
    }
    h1, h2 {
        color: #ffffff;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    .section {
        margin: 20px auto;
        padding: 20px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
"""
st.write(custom_css, unsafe_allow_html=True)

import streamlit as st

# Display the cricket field GIF
st.image("Images/Wickets1.gif", use_container_width=True)


st.markdown("""
<div class="section">
    <h2>📊 About This Page</h2>
    <p>
        This section provides an in-depth analysis of a cricket player's career across all major formats including Test, ODI, T20, and IPL. 🏏
    </p>
    <p>
        You can explore key statistics like batting and bowling averages, strike rates, milestones, and format-wise performance using interactive charts and tables. 📈✨
    </p>
    <p>
        This page is designed to be dynamic, visually appealing, and insightful for cricket fans, analysts, and fantasy league strategists alike! 🔍🏆
    </p>
</div>
""", unsafe_allow_html=True)


# Title
st.markdown("""
<div class='section'>
    <h1>🏏 Cricket Player Career Info</h1>
</div>
""", unsafe_allow_html=True)

# Load dataset
df = pd.read_csv(r"C:\Users\ayush\Cricket_Face_App\Final_cleaned_Cricket.csv")
player_groups = df.groupby("Player")

# Select player
option = st.selectbox("Choose a Player", list(player_groups.groups.keys()))
player_data = df[df['Player'] == option].iloc[0]
formats = ['Test', 'ODI', 'T20', 'IPL']

# Batting Career Summary
st.markdown("<div class='section'><h2>🏏 Batting Career Statistics</h2>", unsafe_allow_html=True)
batting_summary = []
for fmt in formats:
    batting_summary.append([
        fmt,
        player_data.get(f'Matches_{fmt}', 0),
        player_data.get(f'batting_Innings_{fmt}', 0),
        player_data.get(f'batting_Runs_{fmt}', 0),
        player_data.get(f'batting_Balls_{fmt}', 0),
        player_data.get(f'batting_Highest_{fmt}', 0),
        player_data.get(f'batting_Average_{fmt}', 0),
        player_data.get(f'batting_SR_{fmt}', 0),
        player_data.get(f'batting_Not Out_{fmt}', 0),
        player_data.get(f'batting_Fours_{fmt}', 0),
        player_data.get(f'batting_Sixes_{fmt}', 0),
        player_data.get(f'batting_50s_{fmt}', 0),
        player_data.get(f'batting_100s_{fmt}', 0),
        player_data.get(f'batting_200s_{fmt}', 0)
    ])
batting_df = pd.DataFrame(batting_summary, columns=[
    'Format', 'Matches', 'Innings', 'Runs', 'Balls Faced', 'Highest', 'Average',
    'Strike Rate', 'Not Out', '4s', '6s', '50s', '100s', '200s'])
st.dataframe(batting_df.set_index("Format"))
st.markdown("</div>", unsafe_allow_html=True)

# Bowling Career Summary
st.markdown("<div class='section'><h2>🎯 Bowling Career Statistics</h2>", unsafe_allow_html=True)
bowling_summary = []
for fmt in formats:
    bowling_summary.append([
        fmt,
        player_data.get(f'bowling_{fmt}_Innings', 0),
        player_data.get(f'bowling_{fmt}_Balls', 0),
        player_data.get(f'bowling_{fmt}_Runs', 0),
        player_data.get(f'bowling_{fmt}_Wickets', 0),
        player_data.get(f'bowling_{fmt}_Avg', 0),
        player_data.get(f'bowling_{fmt}_Eco', 0),
        player_data.get(f'bowling_{fmt}_SR', 0),
        player_data.get(f'bowling_{fmt}_BBI', "0/0"),
        player_data.get(f'bowling_{fmt}_5w', 0),
        player_data.get(f'bowling_{fmt}_10w', 0)
    ])
bowling_df = pd.DataFrame(bowling_summary, columns=[
    'Format', 'Innings', 'Balls', 'Runs', 'Wickets', 'Avg', 'Economy',
    'Strike Rate', 'BBI', '5w', '10w'])
st.dataframe(bowling_df.set_index("Format"))
st.markdown("</div>", unsafe_allow_html=True)

# Matches Played Pie Chart
match_columns = ["Matches_Test", "Matches_ODI", "Matches_T20", "Matches_IPL"]
valid_match_columns = [col for col in match_columns if col in df.columns]
match_data = player_groups.get_group(option)[valid_match_columns].iloc[0]
st.markdown("<div class='section'><h2>📊 Matches Played</h2>", unsafe_allow_html=True)
fig_matches = px.pie(values=match_data.values, 
                     names=[col.split("_")[1] for col in match_data.index],
                     title=f"Matches Played by {option}",
                     hole=0.3)
st.plotly_chart(fig_matches, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Batting Performance Bar Chart
st.markdown("<div class='section'><h2>📈 Batting Performance</h2>", unsafe_allow_html=True)
batting_stats = [f"batting_Runs_{fmt}" for fmt in formats]
batting_data = player_groups.get_group(option)[batting_stats].iloc[0]
batting_fig = px.bar(x=formats, y=batting_data.values, 
                     labels={'x': "Format", 'y': "Runs Scored"},
                     title=f"Batting Performance - {option}")
st.plotly_chart(batting_fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Bowling Performance Bar Chart
st.markdown("<div class='section'><h2>🎯 Bowling Performance</h2>", unsafe_allow_html=True)
bowling_stats = [f"bowling_{fmt}_Wickets" for fmt in formats]
bowling_data = player_groups.get_group(option)[bowling_stats].iloc[0]
bowling_fig = px.bar(x=formats, y=bowling_data.values, 
                     labels={'x': "Format", 'y': "Wickets Taken"},
                     title=f"Bowling Performance - {option}")
st.plotly_chart(bowling_fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Milestones Comparison
st.markdown("<div class='section'><h2>🏆 Milestone Achievements</h2>", unsafe_allow_html=True)
milestone_stats = [
    f"batting_50s_{fmt}" for fmt in formats] + \
    [f"batting_100s_{fmt}" for fmt in formats] + \
    [f"batting_200s_{fmt}" for fmt in formats]
milestone_data = player_groups.get_group(option)[milestone_stats].iloc[0]
milestone_df = pd.DataFrame({
    "Format": formats * 3,
    "Milestone": ["50s"] * 4 + ["100s"] * 4 + ["200s"] * 4,
    "Count": milestone_data.values
})
milestone_fig = px.bar(milestone_df, x="Format", y="Count", color="Milestone",
                       barmode="group", title=f"{option}'s 50s, 100s, 200s")
st.plotly_chart(milestone_fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Scatter Plot: Runs vs Strike Rate
st.markdown("<div class='section'><h2>⚡ Runs vs. Strike Rate</h2>", unsafe_allow_html=True)
batting_perf = pd.DataFrame({
    "Format": formats,
    "Runs": [player_data.get(f'batting_Runs_{fmt}', 0) for fmt in formats],
    "Strike Rate": [player_data.get(f'batting_SR_{fmt}', 0) for fmt in formats]
})
runs_vs_sr_fig = px.scatter(batting_perf, x="Runs", y="Strike Rate", text="Format",
                            color="Format", size="Runs",
                            title=f"{option}'s Runs vs. Strike Rate")
runs_vs_sr_fig.update_traces(textposition="top center")
st.plotly_chart(runs_vs_sr_fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Additional Analysis
st.markdown("<div class='section'><h2>📉 Trends Overview</h2>", unsafe_allow_html=True)
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
sns.barplot(x="Format", y="Runs", data=batting_perf, ax=ax[0], palette="magma")
ax[0].set_title("Batting Runs Trend")
bowling_wickets = pd.DataFrame({
    "Format": formats,
    "Wickets": [player_data.get(f'bowling_{fmt}_Wickets', 0) for fmt in formats]
})
bowling_wickets.plot(kind='bar', x="Format", y="Wickets", ax=ax[1], color="orange")
ax[1].set_title("Bowling Wickets Trend")
st.pyplot(fig)
st.markdown("</div>", unsafe_allow_html=True)
