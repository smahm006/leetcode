select
query_name,
round(avg(rating / position)::decimal, 2) as quality,
round(count(case when rating < 3 then 1 end)::decimal / count(rating) * 100, 2) as poor_query_percentage
from queries
group by query_name
