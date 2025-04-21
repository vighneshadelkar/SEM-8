# hashtag analysis
import re
from wordcloud import WordCloud
df['hashtags']=df['title'].apply(lambda x: re.findall(r"#(\w+)",x))
df_sorted=df.sort_values(by=['hashtags'],key=lambda x: x.str.len()>0,ascending=False)
df_sorted.head()

from collections import Counter

# Flatten the list of hashtags from all titles
all_hashtags = [tag.lower() for tags in df['hashtags'] for tag in tags]

# Count frequencies
hashtag_counts = Counter(all_hashtags)

# Convert to DataFrame
hashtag_df = pd.DataFrame(hashtag_counts.items(), columns=['Hashtag', 'Count'])
hashtag_df = hashtag_df.sort_values(by='Count', ascending=False)

# top 15 hashtags
top_n = 15
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(hashtag_df['Hashtag'][:top_n][::-1], hashtag_df['Count'][:top_n][::-1], color='skyblue')
ax.set_title(f'Top {top_n} Hashtags in Stream Titles')
ax.set_xlabel('Frequency')
ax.set_ylabel('Hashtag')
plt.show()

# wordcloud of hashtags
wordcloud = WordCloud(width=600, height=400, background_color='white').generate_from_frequencies(hashtag_counts)

fig_wc, ax_wc = plt.subplots(figsize=(12, 6))
ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis('off')
ax_wc.set_title('Hashtag Word Cloud')
plt.show()

