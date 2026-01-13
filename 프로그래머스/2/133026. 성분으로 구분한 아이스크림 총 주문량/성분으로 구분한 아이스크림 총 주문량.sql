-- 코드를 입력하세요
SELECT i.INGREDIENT_TYPE, sum(f.TOTAL_ORDER) as TOTAL_ORDER
from first_half as f
left join icecream_info as i on i.flavor = f.flavor
group by i.INGREDIENT_TYPE