drop database if exists tweet_fetcher_db;
create database tweet_fetcher_db;

drop user if exists tweet_fetcher;
create user tweet_fetcher with encrypted password 'tweet_fetcher';

grant all privileges on database tweet_fetcher_db to tweet_fetcher;
