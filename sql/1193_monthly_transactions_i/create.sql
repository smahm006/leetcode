\ir ../drop_all_tables.sql;

create type state as enum ('approved', 'declined');
create table transactions
(
    id         int primary key,
    country    varchar,
    state      state,
    amount     int,
    trans_date date
);

insert into transactions
values
(121, 'US', 'approved', 1000, '2018-12-18'),
(122, 'US', 'declined', 2000, '2018-12-19'),
(123, 'US', 'approved', 2000, '2019-01-01'),
(124, 'DE', 'approved', 2000, '2019-01-07');
