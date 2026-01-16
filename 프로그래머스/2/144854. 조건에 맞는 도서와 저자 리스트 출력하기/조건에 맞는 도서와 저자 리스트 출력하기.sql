-- 코드를 입력하세요
SELECT book_id, author_name, left (published_date,10)
from book
left join author on book.author_id = author.author_id
where category = '경제'
order by published_date asc
