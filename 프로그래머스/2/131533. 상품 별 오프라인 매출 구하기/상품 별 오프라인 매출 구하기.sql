SELECT p.product_code, p.price * sum(s.sales_amount) as SALES
from product p
left join offline_sale s on p.product_id = s.product_id
group by p.product_id, p.price
having sum(s.sales_amount) is not null
order by SALES desc , p.product_code asc
