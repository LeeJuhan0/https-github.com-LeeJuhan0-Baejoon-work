-- 코드를 입력하세요
SELECT a.AUTHOR_ID,	a.AUTHOR_NAME,	b.CATEGORY,	sum(b.price*s.sales) as TOTAL_SALES
from book_sales as s
left join book as b on b.book_id = s.book_id
left join author as a on a.author_id = b.author_id
where s.SALES_DATE between date '2022-01-01' and date '2022-01-31'
group by a.author_id, b.category
order by a.author_id asc, b.category desc