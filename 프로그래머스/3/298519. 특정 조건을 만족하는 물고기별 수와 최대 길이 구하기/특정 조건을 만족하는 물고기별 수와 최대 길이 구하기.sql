
select count(id) FISH_COUNT, max(length) MAX_LENGTH,	FISH_TYPE
from fish_info
group by fish_type
having avg(length) >= 33
order by fish_type asc