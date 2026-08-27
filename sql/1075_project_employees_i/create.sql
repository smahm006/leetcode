\ir ../drop_all_tables.sql

create table employee
(
    employee_id      int primary key,
    name             varchar,
    experience_years int not null
);

create table project
(
    project_id  int,
    employee_id int references employee (employee_id),
    primary key (project_id, employee_id)
);

insert into employee
values
(1, 'Khaled', 3),
(2, 'Ali', 2),
(3, 'John', 1),
(4, 'Doe', 2);


insert into project
values
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 4);
