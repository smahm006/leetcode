\ir ../drop_all_tables.sql;

create table tweets
(
    tweet_id int primary key,
    content  varchar check (content ~ '^[a-zA-Z0-9! ]+$')
);

insert into tweets
values
(1, 'Let us Code'),
(2, 'More than fifteen chars are here!');
