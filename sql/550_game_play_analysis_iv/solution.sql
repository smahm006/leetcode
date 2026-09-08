with a as (
     select player_id, min(event_date) as first_login from activity group by player_id
)
select
round(count(b.event_date) / count(*)::decimal, 2) as fraction
from
a
left join
activity as b
on a.player_id = b.player_id and b.event_date - a.first_login = 1
