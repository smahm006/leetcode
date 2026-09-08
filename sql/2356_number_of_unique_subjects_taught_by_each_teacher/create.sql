\ir ../drop_all_tables.sql;

create table teacher
(
    teacher_id int,
    subject_id int,
    dept_id    int,
    primary key (subject_id, dept_id)
);

insert into teacher
values
(1, 2, 3),
(1, 2, 4),
(1, 3, 3),
(2, 1, 1),
(2, 2, 1),
(2, 3, 1),
(2, 4, 1);
