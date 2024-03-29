DECLARE
x NUMBER(1) := 5;
y x%TYPE := NULL;
BEGIN
IF x <> y THEN
DBMS_OUTPUT.PUT_LINE ('valoare <> null este = true');
ELSE
DBMS_OUTPUT.PUT_LINE ('valoare <> null este != true');
END IF;
x := NULL;
IF x = y THEN
DBMS_OUTPUT.PUT_LINE ('null = null este = true');
ELSE
DBMS_OUTPUT.PUT_LINE ('null = null este != true');
END IF;
END;
/

DECLARE
TYPE emp_record IS RECORD
(cod employees.employee_id%TYPE,
salariu employees.salary%TYPE,
job employees.job_id%TYPE);
v_ang emp_record;
BEGIN
v_ang.cod:=700;
v_ang.salariu:= 9000;
v_ang.job:='SA_MAN';
DBMS_OUTPUT.PUT_LINE ('Angajatul cu codul '|| v_ang.cod ||
' si jobul ' || v_ang.job || ' are salariul ' || v_ang.salariu);
END;
/


DECLARE
TYPE emp_record IS RECORD
(cod employees.employee_id%TYPE,
salariu employees.salary%TYPE,
job employees.job_id%TYPE);
v_ang emp_record;
BEGIN
/******** In loc de ...
* SELECT employee_id, salary, job_id
* INTO v_ang.cod, v_ang.salariu, v_ang.job
* FROM employees
* WHERE employee_id = 101;
*******************************/
SELECT employee_id, salary, job_id
INTO v_ang
FROM employees
WHERE employee_id = 101;
DBMS_OUTPUT.PUT_LINE ('Angajatul cu codul '|| v_ang.cod ||
' si jobul ' || v_ang.job || ' are salariul ' || v_ang.salariu);
END;
/

BEGIN
DELETE FROM emp_***
WHERE employee_id=100
RETURNING employee_id, salary, job_id INTO v_ang;
DBMS_OUTPUT.PUT_LINE ('Angajatul cu codul '|| v_ang.cod ||
' si jobul ' || v_ang.job || ' are salariul ' || v_ang.salariu);
END;
/
ROLLBACK;