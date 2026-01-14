select   CASE
    WHEN SUM(CASE WHEN s.category = 'Front End' THEN 1 ELSE 0 END) > 0
     AND SUM(CASE WHEN s.name = 'Python' THEN 1 ELSE 0 END) > 0 THEN 'A'
    WHEN SUM(CASE WHEN s.name = 'C#' THEN 1 ELSE 0 END) > 0 THEN 'B'
    WHEN SUM(CASE WHEN s.category = 'Front End' THEN 1 ELSE 0 END) > 0 THEN 'C'
    ELSE NULL
  END AS grade, d.id, d.email
from developers d
left join skillcodes s on (d.skill_code & s.code) = s.code
group by d.id, d.email
having  count(
    case when s.name = 'C#' 
         or (s.name = 'Python' and s.category = 'Front End')
         or (s.name <>'Python' and s.category = 'Front End') then 1 end) > 0
ORDER BY grade asc , d.id asc;

