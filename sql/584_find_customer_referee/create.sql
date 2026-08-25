\ir ../drop_all_tables.sql

create table customer
(
    id        int primary key,
    name      varchar,
    referee_id int references customer (id)
);

insert into customer
values
(1, 'will', null),
(2, 'jane', null),
(3, 'alex', 2),
(4, 'bill', null),
(5, 'zack', 1),
(6, 'mark', 2);
