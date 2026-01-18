-- 코드를 입력하세요
SELECT o.ANIMAL_id, o.name
from ANIMAL_OUTS o
left join ANIMAL_INS  i on o.ANIMAL_ID = i.ANIMAL_ID
where i.ANIMAL_id is null
order by o.ANIMAL_id asc, o.name asc