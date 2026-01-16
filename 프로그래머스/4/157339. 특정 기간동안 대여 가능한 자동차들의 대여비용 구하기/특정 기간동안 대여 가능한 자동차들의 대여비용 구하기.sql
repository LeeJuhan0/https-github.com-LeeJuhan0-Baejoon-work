SELECT
    c.car_id,
    c.car_type,
    ROUND(c.daily_fee * 30 * (100 - d.discount_rate) / 100) AS fee
FROM CAR_RENTAL_COMPANY_CAR c
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
  ON c.car_type = d.car_type
 AND d.duration_type = '30일 이상'
LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h
  ON c.car_id = h.car_id
 AND h.start_date <= '2022-11-30'
 AND h.end_date   >= '2022-11-01'
WHERE c.car_type IN ('세단', 'SUV')
  AND h.car_id IS NULL
  AND ROUND(c.daily_fee * 30 * (100 - d.discount_rate) / 100) >= 500000
  AND ROUND(c.daily_fee * 30 * (100 - d.discount_rate) / 100) < 2000000
ORDER BY fee DESC, c.car_type ASC, c.car_id DESC;
