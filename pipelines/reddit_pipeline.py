import pandas as pd
from datetime import datetime

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH


def reddit_pipeline(file_name: str, subreddit: str, keywords, time_filter='day', limit=None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'kpark370')
    
    # extraction with keyword filtering
    posts = extract_posts(instance, subreddit, time_filter, keywords, limit)
    post_df = pd.DataFrame(posts)
    
    # Save raw log to file
    log_file_path = f'data/input/{file_name}_raw_log.log'
    with open(log_file_path, 'w') as log_file:
        log_file.write(str(posts))
    
    # transformation
    post_df = transform_data(post_df)
    
    # loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path

