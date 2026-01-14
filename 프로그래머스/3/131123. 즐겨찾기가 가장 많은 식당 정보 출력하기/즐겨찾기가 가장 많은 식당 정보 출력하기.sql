-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, max(FAVORITES)
from rest_info
where favorites in (select max(favorites) from rest_info group by food_type)
group by food_type
order by food_type desc