import praw
import pandas as pd
import streamlit as st

reddit = praw.Reddit(
    client_id="j8gdAce89Q-pcDslkhOICA",
    client_secret="sLqxY5feXASuiyncMMBspc4MzbVdvg",
    user_agent="test"
)


def fetch_posts(subreddit_name, query, limit=10):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        posts = []

        for submit in subreddit.search(query, limit=limit):
            posts.append(
                {
                    'Title': submit.title,
                    'Score': submit.score,
                    'id': submit.id,
                    'Url': submit.url,
                    'Comments': submit.num_comments,
                    'created': submit.created,
                    'Body': submit.selftext,
                    'subreddit': subreddit_name
                }
            )
        if not posts:
            return pd.DataFrame()
        df = pd.DataFrame(posts)
        df = df.sort_values(by="Score",ascending=False)

        return df
    except Exception as e:
        st.error(f"An error occured : {e}")
        return pd.DataFrame()


st.title("Reddit Search Engine")
st.write("Enter a subreddit and a search query to find relevant posts.")

subreddit_name = st.text_input("Subreddit")
query = st.text_input("Search Query")
limit = st.slider("Number of posts to retrieve", 1, 50, 10)

if st.button("Search"):
    with st.spinner("Fetching results..."):
        posts_df = fetch_posts(subreddit_name, query, limit)
        if not posts_df.empty:
            st.write(f"Found {len(posts_df)} posts")
            st.write(posts_df)
        else:
            st.write("No posts found.")
