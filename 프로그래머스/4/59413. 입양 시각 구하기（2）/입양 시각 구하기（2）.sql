with recursive hours as (
    select 0 as time
    union all
    select time + 1
    from hours
    where time < 23
)

select h.time, count(o.animal_id)
from hours h
left join  animal_outs o on hour(o.datetime) = h.time 
group by h.time
order by h.time



