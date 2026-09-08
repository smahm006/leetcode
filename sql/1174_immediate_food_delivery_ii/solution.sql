with haha as (
    select
    *,
    row_number() over (partition by customer_id order by order_date )
    from
    delivery
)
select
round(count(case when order_date = customer_pref_delivery_date then 'immediate' end)::decimal /
count(*) * 100, 2) as immediate_percentage
from haha
where row_number = 1
