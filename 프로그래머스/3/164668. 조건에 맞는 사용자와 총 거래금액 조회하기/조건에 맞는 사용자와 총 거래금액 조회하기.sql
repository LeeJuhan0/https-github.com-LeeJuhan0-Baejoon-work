SELECT g.USER_ID, g.NICKNAME, sum(b.price) as 'TOTAL_SALES'
from USED_GOODS_BOARD b
left join USED_GOODS_USER g on b.writer_id = g.user_id 
where b.status like '%DONE'
group by g.user_id
having sum(b.price) >= 700000
order by sum(b.price) asc