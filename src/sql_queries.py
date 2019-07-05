SQL={'user_statistics': """
WITH tweet_stats AS
(
  SELECT user_id_str as user_id,
         COUNT(*) AS tweets_in_db,
         SUM( CASE WHEN ((NOT is_quote_status) AND in_reply_to_status_id_str IS NULL AND t.text NOT LIKE 'RT%')
                   THEN 1
                   ELSE 0 END) AS own_tweets_in_db,
         ROUND(AVG(retweet_count),2) AS avg_retweets,
         ROUND(AVG(favorite_count),2) AS avg_favorite
    FROM tweet AS t
    JOIN twitter_user AS u ON t.user_id_str = u.id_str
GROUP BY user_id_str
)
  SELECT u.id_str AS user_id,
         u.name AS user_name,
         u.location AS user_location,
         u.screen_name,
         u.followers_count,
         u.friends_count,
         u.statuses_count AS total_tweets,
         s.tweets_in_db,
         s.own_tweets_in_db,
         ROUND(s.own_tweets_in_db::decimal/s.tweets_in_db,2) AS share_own,
         s.avg_retweets,
         s.avg_favorite
    FROM twitter_user AS u
    JOIN tweet_stats AS s ON s.user_id = u.id_str;
"""
}