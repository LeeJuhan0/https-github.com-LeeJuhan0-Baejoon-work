select E1.Y as YEAR, MAX_SIZE - size_of_colony as YEAR_DEV, id
from (select ID, PARENT_ID,	SIZE_OF_COLONY,	DIFFERENTIATION_DATE, 
      GENOTYPE,  year(DIFFERENTIATION_DATE) as Y from ECOLI_DATA) E1
left join (select year(DIFFERENTIATION_DATE) as Y, max(SIZE_OF_COLONY) as MAX_SIZE
           from ECOLI_DATA group by year(DIFFERENTIATION_DATE)) E2
            on E1.Y = E2.Y
order by YEAR asc, YEAR_DEV asc
