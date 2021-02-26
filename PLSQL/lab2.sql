--1.
select *
from rental;

--member (member_id);
--title (title_id);
--title_copy(copy_id, title_id);
--rental (book_date, copy_id, member_id, title_id);
--reservation (res_date, member_id, title_id);

--4.
select tc.title_id, title, copy_id
from title_copy tc join title t on (tc.title_id=t.title_id)
where category = (select category
                  from rental r join title t on (r.title_id=t.title_id)
                  group by caterogy
                  having count(*)= (select max(count(*))
                                    from rental r join title t on (r.title_id = t.title_id)
                                    group by category));
                                    
--5.
select *
from rental
where act_ret_date is not null;

select title_id, count(copy_id) as "CASRTI DISP"
from (select copy_id, title_id
    from title_copy
    minus
    select copy_id, title_id
    from rental
    where act_ret_date is null)
group by title_id;

--6.

select title, copy_id, status, 'RENTED' status_corect
from title t join title_copy ti on t.title_id = ti.title_id
where (t.title_id, copy_id) in (select title_id, copy_id
                            from rental
                            where act_ret_date is null)
union
select t.title_id, title, copy_id, status, 'AVAILABLE' status_corect
from title t join title_copy ti on t.title_id = ti.title_id
where (t.title_id, copy_id) in (select title_id, copy_id
                                from title_copy
                                minus
                                select title_id, copy_id
                                from rental
                                where act_ret_date is null);

--7 si 6 pe drive iar


--7.b.

update 
--8.