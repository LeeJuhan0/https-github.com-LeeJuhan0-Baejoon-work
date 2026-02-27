SELECT year(s.SALES_DATE) as YEAR, month(SALES_DATE) as MONTH, count(DISTINCT s.user_id) as 	PURCHASED_USERS, 
        round(count(DISTINCT s.user_id)/
              (select count(DISTINCT user_id) from user_info where year(joined) = 2021),1) as PUCHASED_RATIO
from  USER_INFO i
inner join ONLINE_SALE s on i.user_id = s.user_id
where year(joined) = 2021
group by year(s.SALES_DATE), month(SALES_DATE)
order by YEAR asc, month(SALES_DATE) asc
