select s.user_id, coalesce(round((c.per::numeric/c.total), 2), 0) as confirmation_rate
from signups as s
left join (
     select user_id, count(
     case when action = 'confirmed' then 1 end
) as per, count(*) as total
     from confirmations
     group by user_id
) as c
on s.user_id = c.user_id
