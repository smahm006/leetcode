\ir ../drop_all_tables.sql

create table queries
(
    query_name varchar,
    result     varchar,
    position   int check (position between 1 and 500),
    rating     int check (rating between 1 and 5)
);


insert into queries
values
(' Dog', 'Golden Retriever', 1, 5),
(' Dog', 'German Shepherd', 2, 5),
(' Dog', 'Mule', 200, 1),
(' Cat', 'Shirazi', 5, 2),
(' Cat', 'Siamese', 3, 3),
(' Cat', 'Sphynx', 7, 4);
