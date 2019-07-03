drop database if exists tweefetcher_db;
create database tweefetcher_db;

drop user if exists tweefetcher;
create user tweefetcher with encrypted password 'tweefetcher';

grant all privileges on database tweefetcher_db to tweefetcher;
