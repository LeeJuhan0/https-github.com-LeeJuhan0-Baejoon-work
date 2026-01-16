-- 코드를 입력하세요
SELECT p.product_id, p.product_name, sum(o.amount * p.price) as TOTAL_SALES
from food_product p
left join food_order o on p.product_id = o.product_id
where o.produce_date between '2022-05-01' and '2022-05-31'
group by p.product_id, p.product_name
order by TOTAL_SALES desc, p.product_id asc
