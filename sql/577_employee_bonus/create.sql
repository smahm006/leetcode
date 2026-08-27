\ir ../drop_all_tables.sql;

create table employee
(
    empid      int primary key,
    name       varchar,
    supervisor int,
    salary     float
);

create table bonus
(
    empid int primary key references employee (empid),
    bonus int
);

insert into employee
values
(3, 'Brad', null, 4000),
(1, 'John', 3, 1000),
(2, 'Dan', 3, 2000),
(4, 'Thomas', 3, 4000);

insert into bonus
values
(2, 500),
(4, 2000);
