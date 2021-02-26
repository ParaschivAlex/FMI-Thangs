--3 v1

VARIABLE g_mesaj VARCHAR2(50)
BEGIN
:g_mesaj := 'Invat PL/SQL';
END;
/

PRINT g_mesaj

--3 v2

BEGIN
    DBMS_OUTPUT.PUT_LINE('Invat PL/SQL');
END;


--4

DECLARE
    v_dep departments.department_name%TYPE;
BEGIN
    SELECT department_name
    INTO v_dep
    FROM employees e, departments d
    WHERE e.department_id=d.department_id
    GROUP BY department_name
    HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                        FROM employees
                        GROUP BY department_id);
    DBMS_OUTPUT.PUT_LINE('Departamentul '|| v_dep);
END;


--5

VARIABLE rezultat VARCHAR2(35)
BEGIN
    SELECT department_name
    INTO :rezultat
    
    FROM employees e, departments d
    WHERE e.department_id=d.department_id
    GROUP BY department_name
    HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                        FROM employees
                        GROUP BY department_id);
    
    DBMS_OUTPUT.PUT_LINE('Departamentul '|| :rezultat);
END;
/
PRINT rezultat

--6

DECLARE
    v_dep departments.department_name%TYPE;
    v_nr NUMBER;
BEGIN
    SELECT department_name, count(*)
    INTO v_dep, v_nr
    FROM employees e, departments d
    WHERE e.department_id=d.department_id
    GROUP BY department_name
    HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                        FROM employees
                        GROUP BY department_id);
    DBMS_OUTPUT.PUT_LINE('Departamentul '|| v_dep);
    DBMS_OUTPUT.PUT_LINE(' are '|| v_nr || ' angajati');
END;
/


--7

SET VERIFY OFF
DECLARE
    v_cod employees.employee_id%TYPE:=&p_cod;
    v_bonus NUMBER(8);
    v_salariu_anual NUMBER(8);
BEGIN
    SELECT salary*12 INTO v_salariu_anual
    FROM employees
    WHERE employee_id = v_cod;
    IF v_salariu_anual>=200001
        THEN v_bonus:=20000;
    ELSIF v_salariu_anual BETWEEN 100001 AND 200000
        THEN v_bonus:=10000;
    ELSE v_bonus:=5000;
    END IF;
    DBMS_OUTPUT.PUT_LINE('Bonusul este ' || v_bonus);
END;
/
SET VERIFY ON

--8

DECLARE
    v_cod employees.employee_id%TYPE:=&p_cod;
    v_bonus NUMBER(8);
    v_salariu_anual NUMBER(8);
BEGIN
    SELECT salary*12 INTO v_salariu_anual
    FROM employees
    WHERE employee_id = v_cod;
    CASE 
        WHEN v_salariu_anual>=200001
            THEN v_bonus:=20000;
        WHEN v_salariu_anual BETWEEN 100001 AND 200000
            THEN v_bonus:=10000;
        ELSE v_bonus:=5000;
    END CASE;
    DBMS_OUTPUT.PUT_LINE('Bonusul este ' || v_bonus);
END;
/

--9
DEFINE p_cod_sal= 200
DEFINE p_cod_dept = 80
DEFINE p_procent =20
DECLARE
    v_cod_sal emp_***.employee_id%TYPE:= &p_cod_sal;
    v_cod_dept emp_***.department_id%TYPE:= &p_cod_dept;
    v_procent NUMBER(8):=&p_procent;
BEGIN
    UPDATE emp_paa
    SET department_id = v_cod_dept,
    salary=salary + (salary* v_procent/100)
    WHERE employee_id= v_cod_sal;
    IF SQL%ROWCOUNT =0 THEN
    DBMS_OUTPUT.PUT_LINE('Nu exista un angajat cu acest cod');
    ELSE DBMS_OUTPUT.PUT_LINE('Actualizare realizata');
    END IF;
END;
/
ROLLBACK;

--10.

DECLARE
    contor NUMBER(6) := 1;
    v_data DATE;
    maxim NUMBER(2) := LAST_DAY(SYSDATE)-SYSDATE;
BEGIN
    LOOP
        v_data := sysdate+contor;
        INSERT INTO zile_paa
        VALUES (contor,v_data,to_char(v_data,'Day'));
        contor := contor + 1;
        EXIT WHEN contor > maxim;
    END LOOP;  
END;
/