\ir ../drop_all_tables.sql;

create table sales
(
    sale_id    int,
    product_id int,
    year       int,
    quantity   int,
    price      int,
    primary key (sale_id, year)
);

insert into sales
values
(1, 100, 2008, 10, 5000),
(2, 100, 2009, 12, 5000),
(7, 200, 2011, 15, 9000);
