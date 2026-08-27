\ir ../drop_all_tables.sql;

create table students
(
    student_id  int primary key,
    student_name varchar
);

create table subjects
(
    subject_name varchar primary key
);


create table examinations
(
    student_id   int,
    subject_name varchar
);

insert into students
values
(1, 'Alice'),
(2, 'Bob'),
(13, 'John'),
(6, 'Alex');

insert into subjects
values
('Math'),
('Physics'),
('Programming');

insert into examinations
values
(1, 'Math'),
(1, 'Physics'),
(1, 'Programming'),
(2, 'Programming'),
(1, 'Physics'),
(1, 'Math'),
(13, 'Math'),
(13, 'Programming'),
(13, 'Physics'),
(2, 'Math'),
(1, 'Math');
