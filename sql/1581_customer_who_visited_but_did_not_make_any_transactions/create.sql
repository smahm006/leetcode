\ir ../drop_all_tables.sql;


create table visits
(
    visit_id   int primary key,
    customer_id int
);

create table transactions
(
    transaction_id int primary key,
    visit_id       int references visits (visit_id),
    amount         int
);

insert into visits
values
(1, 23),
(2, 9),
(4, 30),
(5, 54),
(6, 96),
(7, 54),
(8, 54);

insert into transactions
values
(2, 5, 310),
(3, 5, 300),
(9, 5, 200),
(12, 1, 910),
(13, 2, 970);
