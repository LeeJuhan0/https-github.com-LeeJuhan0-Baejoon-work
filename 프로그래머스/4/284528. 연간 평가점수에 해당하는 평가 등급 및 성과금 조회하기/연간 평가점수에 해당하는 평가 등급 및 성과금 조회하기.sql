select e.EMP_NO, e.EMP_NAME, case 
                                when sum(g.score)/2 >= 96 then 'S'
                                when sum(g.score)/2 >= 90 then 'A'
                                when sum(g.score)/2 >= 80 then 'B'
                                else 'C' end as GRADE, 
                             case 
                                when sum(g.score)/2 >= 96 then e.sal*0.2	
                                when sum(g.score)/2 >= 90 then e.sal*0.15
                                when sum(g.score)/2 >= 80 then e.sal*0.1
                                else 0 end as BONUS
from hr_grade g
left join hr_employees e on g.emp_no = e.emp_no
left join hr_department d on d.dept_id = e.dept_id
where g.score is not null and e.emp_no is not null and e.emp_name is not null and e.sal is not null
group by e.emp_no, e.emp_name
order by e.emp_no asc