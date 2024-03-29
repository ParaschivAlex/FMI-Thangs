--Laborator 2 SGBD
--1
SELECT *
FROM rental;

-- member (member_id)
--title (title_id)
--title_copy (copy_id si title_id)
--rental (book_date, copy_id, member_id, title_id)
--reservation (res_date, member_id, title_id)

--4
SELECT ti.title_id, title, copy_id
FROM title_copy ti JOIN title t ON (ti.title_id = t.title_id)
WHERE category = (SELECT category
                  FROM rental r JOIN title t ON (r.title_id = t.title_id)
                  GROUP BY category
                  HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                                     FROM rental r JOIN title t ON (r.title_id = t.title_id)
                                     GROUP BY category));

--5
SELECT *
FROM rental;

SELECT *
FROM title_copy;

SELECT title_id, COUNT(copy_id) AS "CARTI DISP"
FROM (SELECT copy_id, title_id
     FROM title_copy
     MINUS
     SELECT copy_id, title_id
     FROM rental
     WHERE act_ret_date IS NULL)
GROUP BY title_id;

--6
--metoda 1
SELECT t.title_id, title, copy_id, status, 'RENTED' status_corect
FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
WHERE (t.title_id, copy_id) IN (select title_id, copy_id
                                FROM rental
                                WHERE act_ret_date IS NULL)
UNION
SELECT t.title_id, title, copy_id, status, 'AVAILABLE' status_corect
FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
WHERE (t.title_id, copy_id) IN (SELECT title_id, copy_id
                                FROM title_copy
                                MINUS
                                SELECT title_id, copy_id
                                FROM rental
                                WHERE act_ret_date IS NULL);
--metoda 2 (CASE)

--7
--a
SELECT COUNT(*)
FROM (SELECT t.title_id, title, copy_id, status, 'RENTeD' status_corect
      FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
      WHERE (t.title_id, copy_id) IN (select title_id, copy_id
                                      FROM rental
                                      WHERE act_ret_date IS NULL)
      UNION
      SELECT t.title_id, title, copy_id, status, 'AVAIlABLE' status_corect
      FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
      WHERE (t.title_id, copy_id) IN (SELECT title_id, copy_id
                                      FROM title_copy
                                      MINUS
                                      SELECT title_id, copy_id
                                      FROM rental
                                      WHERE act_ret_date IS NULL))
WHERE status <> UPPER(status_corect);

--b
UPDATE title_copy tr
SET status = (SELECT UPPER(status_corect)
              FROM (SELECT t.title_id, title, copy_id, status, 'RENTeD' status_corect
                    FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
                    WHERE (t.title_id, copy_id) IN (select title_id, copy_id
                                                    FROM rental
                                                    WHERE act_ret_date IS NULL)
                    UNION
                    SELECT t.title_id, title, copy_id, status, 'AVAIlABLE' status_corect
                    FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
                    WHERE (t.title_id, copy_id) IN (SELECT title_id, copy_id
                                                    FROM title_copy
                                                    MINUS
                                                    SELECT title_id, copy_id
                                                    FROM rental
                                                    WHERE act_ret_date IS NULL))
                WHERE tr.title_id = title_id
                AND tr.copy_id = copy_id)
WHERE (title_id, copy_id) IN (SELECT title_id, copy_id
                              FROM (SELECT t.title_id title_id, title, copy_id, status, 'RENTeD' status_corect
                                    FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
                                    WHERE (t.title_id, copy_id) IN (select title_id, copy_id
                                                                    FROM rental
                                                                    WHERE act_ret_date IS NULL)
                                    UNION
                                    SELECT t.title_id title_id, title, copy_id, status, 'AVAIlABLE' status_corect
                                    FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
                                    WHERE (t.title_id, copy_id) IN (SELECT title_id, copy_id
                                                                    FROM title_copy
                                                                    MINUS
                                                                    SELECT title_id, copy_id
                                                                    FROM rental
                                                                    WHERE act_ret_date IS NULL))
                                WHERE status <> UPPER(status_corect));
ROLLBACK;

UPDATE  title_copy tr
SET status = (WITH tabel AS (SELECT t.title_id, title, copy_id, status, 'RENTeD' status_corect
                    FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
                    WHERE (t.title_id, copy_id) IN (select title_id, copy_id
                                                    FROM rental
                                                    WHERE act_ret_date IS NULL)
                    UNION
                    SELECT t.title_id, title, copy_id, status, 'AVAIlABLE' status_corect
                    FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
                    WHERE (t.title_id, copy_id) IN (SELECT title_id, copy_id
                                                    FROM title_copy
                                                    MINUS
                                                    SELECT title_id, copy_id
                                                    FROM rental
                                                    WHERE act_ret_date IS NULL))
              SELECT UPPER(status_corect)
              FROM tabel
              WHERE tr.title_id = title_id
              AND tr.copy_id = copy_id)
WHERE (title_id, copy_id) IN (WITH tabel AS (SELECT t.title_id, title, copy_id, status, 'RENTeD' status_corect
                                             FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
                                             WHERE (t.title_id, copy_id) IN (select title_id, copy_id
                                                                             FROM rental
                                                                             WHERE act_ret_date IS NULL)
                                             UNION
                                             SELECT t.title_id, title, copy_id, status, 'AVAIlABLE' status_corect
                                             FROM title t JOIN title_copy ti ON t.title_id = ti.title_id
                                             WHERE (t.title_id, copy_id) IN (SELECT title_id, copy_id
                                                                             FROM title_copy
                                                                             MINUS
                                                                             SELECT title_id, copy_id
                                                                             FROM rental
                                                                             WHERE act_ret_date IS NULL))
                              SELECT title_id, copy_id
                              FROM tabel
                              WHERE status <> UPPER(status_corect));                                
ROLLBACK;

SELECT *
FROM title_copy;

--7 
--b
--Varianta Alexandra
CREATE TABLE title_copy_paa AS SELECT * FROM title_copy; 
UPDATE title_copy_nan
SET
    status = (
        CASE
            WHEN ( title_id,
                   copy_id ) NOT IN (
                SELECT
                    title_id,
                    copy_id
                FROM
                    rental
                WHERE
                    act_ret_date IS NULL
            ) THEN
                'AVAILABLE'
            ELSE
                'RENTED'
        END
    );

--8
SELECT *
FROM reservation;

SELECT r.member_id, r.title_id, DECODE(r.res_date, re.book_date, 'Da', 'Nu') imp_ac_zi
FROM reservation r JOIN rental re ON (r.title_id = re.title_id AND r.member_id = re.member_id);

SELECT r.member_id, r.title_id, CASE 
                                    WHEN r.res_date <> re.book_date THEN 'Nu'
                                    ELSE 'Da'
                                END imp_ac_zi
FROM reservation r JOIN rental re ON (r.title_id = re.title_id AND r.member_id = re.member_id);

SELECT r.member_id, r.title_id, CASE r.res_date
                                    WHEN re.book_date THEN 'Da'
                                    ELSE 'Nu'
                                END imp_ac_zi
FROM reservation r JOIN rental re ON (r.title_id = re.title_id AND r.member_id = re.member_id);

--9
--GRESIT
SELECT m.member_id, first_name, last_name, title, COUNT(r.title_id)
FROM member m JOIN rental r ON m.member_id = r.member_id
              JOIN title t ON t.title_id = r.title_id
GROUP BY m.member_id, r.title_id, first_name, last_name, title;

SELECT m.member_id, MAX(first_name), MAX(last_name), MAX(title), COUNT(r.title_id)
FROM member m JOIN rental r ON m.member_id = r.member_id
              JOIN title t ON t.title_id = r.title_id
GROUP BY m.member_id, r.title_id;

--CORECT
SELECT m.last_name, first_name, title, COUNT(r.title_id)
FROM (SELECT member_id, last_name, first_name, title_id, title
      FROM member, title) m, rental r
WHERE m.member_id = r.member_id (+)
AND m.title_id = r.title_id (+)
GROUP BY m.member_id, r.title_id, m.last_name, first_name, title
ORDER BY 1, 2, 3;


--12
--c
SELECT *
FROM rental;

--varianta 1
--nu e ok
select count(book_date)
from rental
where extract(month from book_date) = extract (month from sysdate) -- aceeasi luna ca luna curenta :D
      and extract(day from book_date) in (1, 2); -- primele doua zile din luna curenta

--varianta 2  
select '01' as day, count(*)
from rental
where to_char(book_date, 'mm yyyy')=to_char(sysdate, 'mm yyyy') and to_char(book_date, 'dd')='01'
UNION
select '02' as day, count(*)
from rental
where to_char(book_date, 'mm yyyy')=to_char(sysdate, 'mm yyyy') and to_char(book_date, 'dd')='02';

--varianta 3
--nu e ok
select '01 10 2020' as day, count(*)
from rental
where to_char(book_date, 'dd mm yyyy')='01 10 2020'
UNION
select '02 10 2020' as day, count(*)
from rental
where to_char(book_date, 'dd mm yyyy')='02 10 2020';


--TEMA 2, 3, 6 (alte rezolvari), 10, 11, 12 (fara a)
