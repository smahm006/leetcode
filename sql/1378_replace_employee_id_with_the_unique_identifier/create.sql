\ir ../drop_all_tables.sql;

create table employees
(
    id   int primary key,
    name varchar
);

create table employeeuni
(
    id        int references employees (id),
    unique_id int,
    primary key (id, unique_id)
);


insert into employees
values
(1, 'Alice'),
(7, 'Bob'),
(11, 'Meir'),
(90, 'Winston'),
(3, 'Jonathan');


insert into employeeuni
values
(3, 1),
(11, 2),
(90, 3);
