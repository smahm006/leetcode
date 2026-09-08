select
s.product_id,
s.year as first_year,
s.quantity,
s.price
from
sales as s
join
(
    select
    product_id, min(year) as year
    from
    sales
    group by product_id
) as fy
on s.product_id = fy.product_id and s.year = fy.year
