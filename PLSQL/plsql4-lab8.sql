--Laborator PL/SQL 4

SELECT *
FROM USER_OBJECTS
WHERE OBJECT_TYPE IN ('PROCEDURE','FUNCTION');

SELECT TEXT
FROM USER_SOURCE
WHERE NAME =UPPER('TO_NUMBER_OR_NULL');

SELECT LINE, POSITION, TEXT
FROM USER_ERRORS
WHERE NAME = UPPER('TO_NUMBER_OR_NULL');

--1
DECLARE
    v_nume employees.last_name%TYPE := Initcap('&p_nume');
    FUNCTION f1 
    RETURN NUMBER 
    IS
        salariu employees.salary%type;
    BEGIN
        SELECT salary INTO salariu
        FROM employees
        WHERE last_name = v_nume;
        RETURN salariu;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('Nu exista angajati cu numele dat');
        WHEN TOO_MANY_ROWS THEN
            DBMS_OUTPUT.PUT_LINE('Exista mai multi angajati '||
                'cu numele dat');
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Alta eroare!');
    END f1;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Salariul este '|| f1);
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Eroarea are codul = '||SQLCODE
            || ' si mesajul = ' || SQLERRM);
END;
/

--2
CREATE OR REPLACE FUNCTION f2_prof
    (v_nume employees.last_name%TYPE DEFAULT 'Bell')
RETURN NUMBER IS
    salariu employees.salary%type;
BEGIN
    SELECT salary INTO salariu
    FROM employees
    WHERE last_name = v_nume;
    RETURN salariu;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20000,
            'Nu exista angajati cu numele dat');
    WHEN TOO_MANY_ROWS THEN
        RAISE_APPLICATION_ERROR(-20001,
            'Exista mai multi angajati cu numele dat');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002,'Alta eroare!');
END f2_prof;
/

-- metode de apelare
-- 1. bloc plsql
BEGIN
    DBMS_OUTPUT.PUT_LINE('Salariul este '|| f2_prof);
END;
/
BEGIN
    DBMS_OUTPUT.PUT_LINE('Salariul este '|| f2_prof('King'));
END;
/

-- 2. SQL
SELECT f2_prof FROM DUAL;
SELECT f2_prof('King') FROM DUAL;

-- 3. SQL*PLUS CU VARIABILA HOST
VARIABLE nr NUMBER
EXECUTE :nr := f2_prof('King');
PRINT nr

--3
-- varianta 1
DECLARE
    v_nume employees.last_name%TYPE := Initcap('&p_nume');
    PROCEDURE p3
    IS
        salariu employees.salary%TYPE;
    BEGIN
        SELECT salary INTO salariu
        FROM employees
        WHERE last_name = v_nume;
        DBMS_OUTPUT.PUT_LINE('Salariul este '|| salariu);
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('Nu exista angajati cu numele dat');
        WHEN TOO_MANY_ROWS THEN
            DBMS_OUTPUT.PUT_LINE('Exista mai multi angajati '||
                'cu numele dat');
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Alta eroare!');
    END p3;
BEGIN
    p3;
END;
/

-- varianta 2
DECLARE
    v_nume employees.last_name%TYPE := Initcap('&p_nume');
    v_salariu employees.salary%type;
    PROCEDURE p3(salariu OUT employees.salary%type) 
    IS
    BEGIN
        SELECT salary INTO salariu
        FROM employees
        WHERE last_name = v_nume;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20000,
                'Nu exista angajati cu numele dat');
        WHEN TOO_MANY_ROWS THEN
            RAISE_APPLICATION_ERROR(-20001,
                'Exista mai multi angajati cu numele dat');
        WHEN OTHERS THEN
            RAISE_APPLICATION_ERROR(-20002,'Alta eroare!');
    END p3;
BEGIN
    p3(v_salariu);
    DBMS_OUTPUT.PUT_LINE('Salariul este '|| v_salariu);
END;
/

--4
-- varianta 1
CREATE OR REPLACE PROCEDURE p4_prof (v_nume employees.last_name%TYPE)
IS
    salariu employees.salary%TYPE;
BEGIN
    SELECT salary 
    INTO salariu
    FROM employees
    WHERE last_name = v_nume;
    DBMS_OUTPUT.PUT_LINE('Salariul este '|| salariu);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20000, 'Nu exista angajati cu numele dat');
    WHEN TOO_MANY_ROWS THEN
        RAISE_APPLICATION_ERROR(-20001,
            'Exista mai multi angajati cu numele dat');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002,'Alta eroare!');
END p4_prof;
/

-- metode apelare
-- 1. Bloc PLSQL
BEGIN
    p4_prof('King');
END;
/

-- 2. SQL*PLUS
EXECUTE p4_prof('Bell');
EXECUTE p4_prof('King');
EXECUTE p4_prof('Kimball');

-- varianta 2
CREATE OR REPLACE PROCEDURE
    p4_prof(v_nume IN employees.last_name%TYPE,
    salariu OUT employees.salary%type) IS
BEGIN
    SELECT salary 
    INTO salariu
    FROM employees
    WHERE last_name = v_nume;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20000,
            'Nu exista angajati cu numele dat');
    WHEN TOO_MANY_ROWS THEN
        RAISE_APPLICATION_ERROR(-20001,
            'Exista mai multi angajati cu numele dat');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002,'Alta eroare!');
END p4_prof;
/

-- metode apelare
-- 1. Bloc PLSQL
DECLARE
    v_salariu employees.salary%type;
BEGIN
    p4_prof('King',v_salariu);
    DBMS_OUTPUT.PUT_LINE('Salariul este '|| v_salariu);
END;
/

-- 2. SQL*PLUS
VARIABLE v_sal NUMBER
EXECUTE p4_prof ('Bell',:v_sal)
PRINT v_sal

--5
VARIABLE ang_man NUMBER 
BEGIN
    :ang_man:=200; 
END; 
/

CREATE OR REPLACE PROCEDURE p5_prof (nr IN OUT NUMBER) 
IS 
BEGIN 
    SELECT manager_id 
    INTO nr 
    FROM employees 
    WHERE employee_id=nr;
END p5_prof; 
/

EXECUTE p5_prof (:ang_man)
PRINT ang_man

--6
DECLARE 
    nume employees.last_name%TYPE; 
    PROCEDURE p6 (rezultat OUT employees.last_name%TYPE, 
                  comision IN employees.commission_pct%TYPE:=NULL, 
                  cod IN employees.employee_id%TYPE:=NULL) 
    IS 
    BEGIN 
        IF (comision IS NOT NULL) THEN 
            SELECT last_name 
            INTO rezultat 
            FROM employees 
            WHERE commission_pct= comision; 
            
            DBMS_OUTPUT.PUT_LINE('numele salariatului care are comisionul '||
                                  comision||' este '||rezultat); 
        ELSE 
            SELECT last_name 
            INTO rezultat 
            FROM employees 
            WHERE employee_id =cod; 
            
            DBMS_OUTPUT.PUT_LINE('numele salariatului avand codul '|| 
                                  cod ||' este '||rezultat); 
        END IF; 
    END p6;
BEGIN 
    p6(nume,0.4); 
    p6(nume,cod=>200); 
END;
/

--7
DECLARE 
    medie1 NUMBER(10,2); 
    medie2 NUMBER(10,2); 
    FUNCTION medie (v_dept employees.department_id%TYPE) 
        RETURN NUMBER 
    IS 
        rezultat NUMBER(10,2); 
    BEGIN 
        SELECT AVG(salary) 
        INTO rezultat 
        FROM emp_prof
        WHERE department_id = v_dept; 
        RETURN rezultat; 
    END; 
    
    FUNCTION medie (v_dept employees.department_id%TYPE, v_job employees.job_id %TYPE) 
        RETURN NUMBER 
    IS 
        rezultat NUMBER(10,2); 
    BEGIN 
        SELECT AVG(salary) 
        INTO rezultat 
        FROM emp_prof 
        WHERE department_id = v_dept 
        AND job_id = v_job; 
        RETURN rezultat; 
    END; 
BEGIN 
    medie1:=medie(80); 
    DBMS_OUTPUT.PUT_LINE('Media salariilor din departamentul 80' 
                          || ' este ' || medie1); 
    medie2 := medie(80,'SA_MAN'); 
    DBMS_OUTPUT.PUT_LINE('Media salariilor managerilor din' 
                          || ' departamentul 80 este ' || medie2); 
END;
/

--8
CREATE OR REPLACE FUNCTION factorial_prof(n NUMBER) 
    RETURN INTEGER 
IS 
BEGIN 
    IF (n=0) THEN 
        RETURN 1; 
    ELSE 
        RETURN n*factorial_prof(n-1); 
    END IF; 
END factorial_prof; 
/

BEGIN
    DBMS_OUTPUT.PUT_LINE(factorial_prof(5));
END;
/

SELECT factorial_prof(5)
FROM DUAL;

--9
CREATE OR REPLACE FUNCTION medie_prof 
    RETURN NUMBER 
IS 
    rezultat NUMBER; 
BEGIN 
    SELECT AVG(salary) 
    INTO rezultat 
    FROM employees; 
    RETURN rezultat; 
END; 
/ 

SELECT last_name,salary 
FROM employees 
WHERE salary >= medie_prof;

-- Exercitii
--1
CREATE TABLE info_prof(
    ID NUMBER(10, 2) PRIMARY KEY,
    utilizator VARCHAR2(50),
    data TIMESTAMP,
    comanda VARCHAR2(100),
    nr_linii NUMBER,
    eroare VARCHAR2(50));
    
--2
CREATE SEQUENCE secv_prof
INCREMENT BY 2
START WITH 5;

SELECT secv_prof.NEXTVAL
FROM DUAL;

SELECT secv_prof.CURRVAL
FROM DUAL;

SELECT USER
FROM DUAL;

SELECT SYSTIMESTAMP
FROM DUAL;

CREATE OR REPLACE FUNCTION f2_stl
    (v_nume employees.last_name%TYPE DEFAULT 'Bell')
RETURN NUMBER IS
    nr NUMBER := 0;
    salariu employees.salary%type;
    mesaj VARCHAR2(500);
    BEGIN
        SELECT salary INTO salariu
        FROM employees
        WHERE UPPER(last_name) = UPPER(v_nume);
        nr := SQL%ROWCOUNT;
        INSERT INTO info_stl
        VALUES (USER, SYSDATE, 'SELECT', nr, 'Nicio eroare');
        
        RETURN salariu;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            nr := SQL%ROWCOUNT;
            INSERT INTO info_stl
            VALUES (USER, SYSDATE, 'SELECT', nr, 'Nu exista angajati cu numele dat');
            RETURN -1;
            --RAISE_APPLICATION_ERROR(-20000, 'Nu exista angajati cu numele dat');
        
        WHEN TOO_MANY_ROWS THEN
            nr := SQL%ROWCOUNT;
            mesaj := SQLCODE || ' ' || SQLERRM;
            DBMS_OUTPUT.PUT_LINE(MESAJ);
            INSERT INTO info_stl
            VALUES (USER, SYSDATE, 'SELECT', nr, mesaj);
            RETURN -2;
            --RAISE_APPLICATION_ERROR(-20001, 'Exista mai multi angajati cu numele dat');

        WHEN OTHERS THEN
            mesaj := SQLERRM;
            INSERT INTO info_stl
            VALUES (USER, SYSDATE, 'SELECT', nr, mesaj);
            --RAISE_APPLICATION_ERROR(-20002,'Alta eroare!');
            RETURN -3;
END f2_stl;
/

--NU MERGE
SELECT f2_stl
FROM DUAL;

DECLARE 
    sal NUMBER;
BEGIN
    sal := f2_stl('King');
    DBMS_OUTPUT.PUT_LINE(sal);
END;
/

DESC info_stl;

SELECT *
FROM info_stl;