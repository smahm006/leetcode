select machine_id,
round(avg(process_sum)::decimal, 3) as processing_time
from (
select machine_id, (max(timestamp) - min(timestamp)) as process_sum
from activity
group by (machine_id, process_id)
)
group by machine_id
