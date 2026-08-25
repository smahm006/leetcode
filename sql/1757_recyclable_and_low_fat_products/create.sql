\ir ../drop_all_tables.sql

create type low_fats as enum ('Y', 'N');
create type recyclable as enum ('Y', 'N');
create table products
(
    product_id int primary key,
    low_fats   low_fats,
    recyclable recyclable
);

insert into products
values
(0, 'Y', 'N'),
(1, 'Y', 'Y'),
(2, 'N', 'Y'),
(3, 'Y', 'Y'),
(4, 'N', 'N');
