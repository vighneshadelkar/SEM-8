import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from collections import defaultdict

# st.set_page_config(layout="wide")
# st.title("Visualizations in Social Media Analytics Using Twitch")

# 📌 Load CSV file
df = pd.read_csv("twitch_streams.csv")

# Convert time if needed
df['started_at'] = pd.to_datetime(df['started_at'], errors='coerce')
df['started_at'] = (df['started_at'].max() - df['started_at']).dt.total_seconds() / 3600  # Hours streamed

# Viewer count by language
fig, ax = plt.subplots()
ax.bar(df['language'], df['viewer_count'])
ax.set_ylabel('Viewer Count')
ax.set_title('Viewer Count by Language')
ax.set_xlabel('Language')
plt.show()

# Viewer count by game
df_game = df.groupby(['game_name'], as_index=False)['viewer_count'].sum()
fig1, ax1 = plt.subplots(figsize=(16, 9), subplot_kw=dict(aspect="equal"))
def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"
wedges, texts, autotexts = ax1.pie(df_game['viewer_count'], autopct=lambda pct: func(pct, df_game['viewer_count']),
                                   pctdistance=1.1, colors=plt.cm.tab20.colors)
ax1.legend(wedges, df_game['game_name'], title="Game Name", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax1.set_title("Viewer Count by Game")
plt.show()

# Hours streamed vs viewer count (2D histogram)
fig2, ax2 = plt.subplots()
ax2.hist2d(df['started_at'], df['viewer_count'], bins=30)
ax2.set_xlabel('Hours Streamed')
ax2.set_ylabel('Viewer Count')
ax2.set_title('Hours Streamed vs Viewer Count')
st.pyplot(fig2)

# Scatter: Language vs Game
fig3, ax3 = plt.subplots()
scatter = ax3.scatter(df['language'], df['game_name'], s=20, c=df['viewer_count'], cmap='viridis')
ax3.set_xlabel('Language')
ax3.set_ylabel('Game Name')
ax3.set_title('Games Sorted by Language')
legend1 = ax3.legend(*scatter.legend_elements(), loc="upper right", title="Viewers")
ax3.add_artist(legend1)
plt.show()

# Word Cloud from titles
text = ' '.join(str(title) for title in df['title'])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(width=600, height=600, background_color='white', stopwords=stopwords).generate(text)
fig4, ax4 = plt.subplots()
ax4.imshow(wordcloud, interpolation='bilinear')
ax4.axis('off')
ax4.set_title('Wordcloud of Streamer Titles')
plt.show()

# Step Function
fig5, ax5 = plt.subplots()
ax5.stairs(df['viewer_count'].sort_values().values, linewidth=2.5)
ax5.set(xlim=(0, 50), ylim=(0, 100000))
ax5.set_xlabel('Streamer No.')
ax5.set_ylabel('Viewer Count')
ax5.set_title("Distribution of Viewers by Streamer using Step Function")
plt.show()

# Stem Plot by game
df1 = df_game.sort_values(by='game_name')
fig6, ax6 = plt.subplots()
ax6.stem(df1['game_name'], df1['viewer_count'])
ax6.set_xticklabels(df1['game_name'], rotation='vertical')
ax6.set_xlabel('Game Name')
ax6.set_ylabel('Viewer Count')
ax6.set_title('View Count Distribution by Game Name using Stems')
plt.show()

# Box Plot
vcbg = defaultdict(list)
for index, row in df.iterrows():
    vcbg[row['game_name']].append(row['viewer_count'])
fig7, ax7 = plt.subplots()
ax7.boxplot(vcbg.values(), patch_artist=True, labels=vcbg.keys())
ax7.set_xticklabels(vcbg.keys(), rotation='vertical')
ax7.set_xlabel('Games')
ax7.set_ylabel('Viewer Count')
ax7.set_title('Box Plot of View Count by Game')
plt.show()

# Violin Plot
fig8, ax8 = plt.subplots()
ax8.violinplot(df['viewer_count'])
ax8.set_xlabel('Streamers')
ax8.set_ylabel('Viewer Count')
ax8.set_title('Violin Plot of Streamer View Count')
plt.show()

# Hexbin Plot
fig9, ax9 = plt.subplots()
hb = ax9.hexbin(df['started_at'], df['viewer_count'], gridsize=20, bins='log', cmap='inferno')
ax9.set_xlabel('Hours Streamed')
ax9.set_ylabel('Viewer Count')
ax9.set_title('Hours Streamed vs Viewer Count using Hex Bins')
cb = fig9.colorbar(hb, ax=ax9, label='Counts')
plt.show()

# Histogram of hours streamed
fig12, ax12 = plt.subplots()
ax12.hist(df['started_at'], bins=8, edgecolor="white")
ax12.set_xlabel('Hours Streamed')
ax12.set_ylabel('Frequency')
ax12.set_title('Histogram of Hours Streamed')
plt.show()
