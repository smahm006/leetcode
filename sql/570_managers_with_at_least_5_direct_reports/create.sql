\ir ../drop_all_tables.sql


create table employee
(
    id         int primary key,
    name       varchar,
    department varchar,
    managerid  int
);


insert into employee
values
(101, 'John', 'A', null),
(102, 'Dan', 'A', 101),
(103, 'James', 'A', 101),
(104, 'Amy', 'A', 101),
(105, 'Anne', 'A', 101),
(106, 'Ron', 'B', 101);
