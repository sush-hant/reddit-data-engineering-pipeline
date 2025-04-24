import pandas as pd

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
from airflow.hooks.base import BaseHook


def reddit_pipeline(file_name:str, subreddit:str, time_filter='day', limit=None):
    conn = BaseHook.get_connection('reddit_api')
    reddit_conn_params = conn.extra_dejson

    # Safely retrieve parameters with fallback values
    client_id = reddit_conn_params.get('client_id')
    client_secret = reddit_conn_params.get('client_secret')
    user_agent = reddit_conn_params.get('user_agent')


    # Connect to the Reddit instance
    instance = connect_reddit(client_id, client_secret, user_agent)

    #extraction

    posts = extract_posts(instance, subreddit, time_filter, limit)
    #transformation

    post_df = pd.DataFrame(posts)

    post_df = transform_data(post_df)
    #loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df,file_path)
    return file_path