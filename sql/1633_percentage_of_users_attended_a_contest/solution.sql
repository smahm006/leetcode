select r.contest_id, round(count(r.user_id)::decimal / (select count(*) from users)  * 100, 2) as percentage
from register as r join users as u
on r.user_id = u.user_id
group by r.contest_id
order by percentage desc, contest_id asc
