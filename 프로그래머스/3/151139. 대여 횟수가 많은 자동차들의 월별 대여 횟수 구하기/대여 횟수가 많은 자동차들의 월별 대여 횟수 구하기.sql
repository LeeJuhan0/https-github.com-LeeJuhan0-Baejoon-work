select month(start_date) as month, car_id, count(*) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where (start_date between date '2022-08-01' and date '2022-10-31') and 
        car_id in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                   where start_date between date '2022-08-01' and date '2022-10-31'
                  group by car_id 
                  having count(history_id) >= 5)
group by car_id, month(start_date)
having count(*) > 0
order by month(start_date) asc, car_id desc

