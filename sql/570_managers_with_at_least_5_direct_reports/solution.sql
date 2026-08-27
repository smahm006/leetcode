select name
from employee as e
join (
    select managerid, count(*) as num_reports
    from employee
    group by managerid
) as c
on e.id = c.managerid and c.count >= 5
