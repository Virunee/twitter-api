import json
import re
import pandas
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

def read_json(file_path):
    results=[]
    tweets_file = open(tweets_data_path, "r")

    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue

    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

# Now format the results into columns of data
results = read_json(tweets_data_path)

# create a dataframe
statuses = pandas.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)
# store the language values
statuses['lang'] = map(lambda status: status['lang'], results)
# sometimes there may not be a 'place' associated with a Tweet, so put 'N/A' if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] else "N/A", results)

#  new DataFrame columns
statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python', status))
statuses['java']   = statuses['text'].apply(lambda status: is_token_in_tweet_text('java', status))
statuses['c#']     = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#', status))
statuses['ruby']   = statuses['text'].apply(lambda status: is_token_in_tweet_text('ruby', status))

# get each tweet language and the count of its appearance
tweets_by_lang = statuses['lang'].value_counts()
# get each tweet country of origin and the count of its appearance
tweets_by_country = statuses['country'].value_counts()

tweets_by_keyword_python = statuses['python'].value_counts()[True]
tweets_by_keyword_java = statuses['java'].value_counts()[True]
tweets_by_keyword_c = statuses['c#'].value_counts()[True]
tweets_by_keyword_ruby = statuses['ruby'].value_counts()[True]

# output the number of tweets where it is True that they contain our keywords
# output the number of tweets where it is True that they contain our keywords
# print statuses['python'].value_counts()[True]
# print statuses['java'].value_counts()[True]
# print statuses['c#'].value_counts()[True]
# print statuses['ruby'].value_counts()[True]

# Finally, we graph the data in a bar chart using Matplotlib

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'python', 'java', 'c#', 'ruby'
sizes = [tweets_by_keyword_python, tweets_by_keyword_java, tweets_by_keyword_c, tweets_by_keyword_ruby]
explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax3 = plt.subplots()
ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

# create our drawing space/window (figure)
fig = plt.figure()
# add a plot area for our data on the figure - 1,1,1 means a single chart/graph
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

# style the axes and labels of our plot
ax1.tick_params(axis='x', labelsize=15)
ax1.tick_params(axis='y', labelsize=10)
ax1.set_xlabel('Tweet Languages', fontsize=15)
ax1.set_ylabel('Number of tweets', fontsize=15)
ax1.xaxis.label.set_color('#666666')
ax1.yaxis.label.set_color('#666666')
ax1.tick_params(axis='x', colors='#666666')
ax1.tick_params(axis='y', colors='#666666')
# style the title
ax1.set_title('Top 10 languages', fontsize=15, color='#666666')

# plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_lang[:10].plot(ax=ax1, kind='bar', color='#FF7A00')

# color the spines (borders)
for spine in ax1.spines.values():
    spine.set_edgecolor('#666666')

# Second subplot
ax2.tick_params(axis='x', labelsize=15)
ax2.tick_params(axis='y', labelsize=10)
ax2.set_xlabel('Countries', fontsize=15)
ax2.set_ylabel('Number of tweets', fontsize=15)
ax2.xaxis.label.set_color('#666666')
ax2.yaxis.label.set_color('#666666')
ax2.tick_params(axis='x', colors='#666666')
ax2.tick_params(axis='y', colors='#666666')
# style the title
ax2.set_title('Top 10 Countries', fontsize=15, color='#666666')

# plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_country[:10].plot(ax=ax2, kind='bar', color='#FF7A00')

# color the spines (borders)
for spine in ax2.spines.values():
    spine.set_edgecolor('#666666')

# render the two graphs at once
plt.show()