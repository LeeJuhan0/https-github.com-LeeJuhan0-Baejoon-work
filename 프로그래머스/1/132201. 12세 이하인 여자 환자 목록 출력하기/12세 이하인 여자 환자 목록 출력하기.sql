SELECT  pt_name, PT_NO, gend_cd, age, coalesce(tlno, 'NONE')
from PATIENT
where age <= 12 and gend_cd = 'W'
order by age desc, pt_name asc 
