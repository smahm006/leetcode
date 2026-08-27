\ir ../drop_all_tables.sql

create table users
(
    user_id   int primary key,
    user_name varchar
);


create table register
(
    contest_id int,
    user_id    int,
    primary key (contest_id, user_id)
);

insert into users
values
(6, 'Alice'),
(2, 'Bob'),
(7, 'Alex');

insert into register
values
(215, 6),
(209, 2),
(208, 2),
(210, 6),
(208, 6),
(209, 7),
(209, 6),
(215, 7),
(208, 7),
(210, 2),
(207, 2),
(210, 7);
