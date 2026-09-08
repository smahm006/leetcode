\ir ../drop_all_tables.sql;

create table delivery
(
    delivery_id                 int primary key,
    customer_id                 int,
    order_date                  date,
    customer_pref_delivery_date date
);

insert into delivery
values
(1, 1, '2019-08-01', '2019-08-02'),
(2, 2, '2019-08-02', '2019-08-02'),
(3, 1, '2019-08-11', '2019-08-12'),
(4, 3, '2019-08-24', '2019-08-24'),
(5, 3, '2019-08-21', '2019-08-22'),
(6, 2, '2019-08-11', '2019-08-13'),
(7, 4, '2019-08-09', '2019-08-09');
