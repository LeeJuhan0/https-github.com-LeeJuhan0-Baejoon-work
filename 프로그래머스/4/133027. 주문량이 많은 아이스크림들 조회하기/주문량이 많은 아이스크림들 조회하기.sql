with uni as (
    select flavor , sum(total_order) as total
    from (select * from july 
          union all
          select * from first_half) as cartition
    group by flavor
    order by total desc
)

select flavor
from uni
limit 3

