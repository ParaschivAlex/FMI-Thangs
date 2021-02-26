--12 a

select '01' as day, count(*)
from rental
where to_char(book_date, 'mm yyyy')=to_char(sysdate, 'mm yyyy') and to_char(book_date, 'dd')='01'
UNION
select '02' as day, count(*)
from rental
where to_char(book_date, 'mm yyyy')=to_char(sysdate, 'mm yyyy') and to_char(book_date, 'dd')='02';

--var 2

select '01' as day, count(*)
from rental
where to_char(book_date, 'dd mm yyyy')='01 10 2020'
UNION
select '02' as day, count(*)
from rental
where to_char(book_date, 'dd mm yyyy')='02 10 2020';