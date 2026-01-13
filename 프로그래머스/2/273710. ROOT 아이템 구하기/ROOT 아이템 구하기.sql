-- 코드를 작성해주세요
select t.ITEM_ID, i.item_name
from ITEM_TREE as t
left join item_info as i on i.item_id = t.item_id
where t.PARENT_ITEM_ID is Null