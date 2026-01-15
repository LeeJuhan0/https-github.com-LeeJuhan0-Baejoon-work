SELECT  (case when start_date between '2022-08-01' and '2022-08-31' then 8 
             when start_date between '2022-09-01' and '2022-09-30' then 9
             when start_date between '2022-10-01' and '2022-10-31' then 10  else null  end) as MONTH,
        CAR_ID, 
        count(car_id) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date between '2022-08-01' and '2022-10-31' 
        and car_id in  (select case when count(car_id) >= 5 then car_id else null end
                        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                        where start_date between '2022-08-01' and '2022-10-31' 
                        group by car_id ) 
group by car_id, (case when start_date between '2022-08-01' and '2022-08-31' then 8 
             when start_date between '2022-09-01' and '2022-09-30' then 9
             when start_date between '2022-10-01' and '2022-10-31' then 10  else null  end) 
order by month asc, car_id desc