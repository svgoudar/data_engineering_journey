- ### DATE FUNCTIONS

- %a-Abbreviated weekday name (Sun-Sat)
- %b-Abbreviated month name (Jan-Dec)
- %c-Month, numeric (0-12)
- %D-Day of month with English suffix (0th, 1st, 2nd, 3rd)
- %d-Day of the month, numeric (00-31)
- %e-Day of the month, numeric (0-31)
- %f-Microseconds (000000-999999)
- %H-Hour (00-23)
- %h-Hour (01-12)
- %I-Hour (01-12)
- %i-Minutes, numeric (00-59)
- %j-Day of the year (001-366)
- %k-Hour (0-23)
- %l-Hour (1-12)
- %M-Month name (January-December)
- %m-Month, numeric (00-12)
- %p-AM or PM
- %r-Time, 12-hour (hh:mm: ss followed by AM or PM)
- %S-Seconds (00-59)
- %s-Seconds (00-59)
- %T-Time, 24-hour (hh:mm: ss)
- %U-Week (00-53) where Sunday is the first day of the week
- %u-Week (00-53) where Monday is the first day of the week
- %V-Week (01-53) where Sunday is the first day of the week, used with %X
- %v-Week (01-53) where Monday is the first day of the week, used with %x
- %W-Weekday name (Sunday-Saturday)
- %x-Year for the week where Monday is the first day of the week, four digits, used with %v
- %w-Day of the week (0=Sunday, 6=Saturday)
- %X-Year for the week where Sunday is the first day of the week, four digits, used with %V
- %Y-Year, numeric, four digits
- %y-Year, numeric, two digits

```sql
select current_date();
select curdate();
select current_time();
select current_timestamp();
select current_user();
select extract(year from release_date) from movie;
select date_add(release_date, interval 1 year) from movie;
SELECT DATE_ADD(release_date, INTERVAL 30 DAY)  FROM movie;
SELECT DATEDIFF('2017-01-13','2017-01-03') AS DateDiff;

    
```

- ### String Function


```sql
select ascii('A'); -- 65
select char_length(116); -- 3
select character_length('sanjeev  dds'); -- 12
select concat('Sanjeev ' ,'  dsdd','Sanju') from dual; -- 'Sanjeev   dsddSanju'
select concat_ws('_' ,'Sanjeev','Sanju') from dual; -- 'Sanjeev_Sanju'
select find_in_set('d','a,b,c,d,e,f'); -- 4
select instr('geeks for geeks','e'); -- 2
select lcase('Geeks For Feeks'); -- 'geeks for feeks'
SELECT LEFT('geeksforgeeks.org', 5); -- 'geeks'
SELECT length('geeksforgeeks.org'); -- 17
SELECT LOCATE('for', 'geeksforgeeks', 1); -- 6
SELECT LOCATE('geeks', 'geeksforgeeks', 2); -- 9
SELECT LOWER('GEEKSFORGEEKS.ORG'); -- 'geeksforgeeks.org'
select LPAD('geeks', 8, '0'); -- 000geeks
select ltrim('   123123geeks   '); -- 123123geeks   
select mid('sanjeev',1,2); -- sa
SELECT POSITION('e' IN 'geeksforgeeks'); -- 2
SELECT REPEAT('geeks', 2); -- geeksgeeks
select replace("sanjeev","sanje",2) from dual;  -- 2ev
SELECT RIGHT('geeksforgeeks.org', 4); -- .org
SELECT REVERSE('geeksforgeeks.org'); -- 'gro.skeegrofskeeg'
select RPAD('geeks', 8, '0'); -- 'geeks000'
select RTRIM('geeksxyxzyyy    '); -- 'geeksxyxzyyy'
SELECT SPACE(7); -- '       '
SELECT STRCMP('google.com', 'geeksforgeeks.com'); -- 1
SELECT STRCMP('geeksforgeeks.com', 'google.com'); -- -1
SELECT STRCMP('google.com', 'google.com'); -- 0
select SUBSTR('geeksforgeeks', 1, 5); -- geeks
SELECT SUBSTRING('GeeksForGeeks.org', 9, 2); -- Ge
SELECT SUBSTRING_INDEX('www.geeksforgeeks.org', '.', 1); -- www
select TRIM(LEADING '0' FROM '000123'); -- 123
select UCASE ("GeeksForGeeks"); -- 'GEEKSFORGEEKS'
SELECT SUBSTRING('GeeksForGeeks.org', 9, 1); -- G

```

- ### NUMERIC FUNCTION

```sql
SELECT ABS(-243.5);
SELECT ACOS(0.25);
SELECT ASIN(0.25);
SELECT CEIL(25.75);
SELECT CEILING(25.75);
SELECT COS(30);
SELECT COT(6);
SELECT DEGREES(1.5);
SELECT EXP(1);
SELECT FLOOR(25.75);
SELECT GREATEST(30, 2, 36, 81, 125);
SELECT LEAST(30, 2, 36, 81, 125);
SELECT LN(2);
SELECT LOG(2);
SELECT LOG2(6);
SELECT MOD(18, 4);
SELECT PI();
SELECT POWER(4, 2);
SELECT RADIANS(180);
SELECT TRUNCATE(7.53635, 2);
```

- ### STATISTICAL FUNCTION

```sql
select avg(votes) from movie;
select sum(votes) from movie;
select count(votes) from movie;
select max(votes) from movie;
select min(votes) from movie;
select VARIANCE(votes) from movie;
select stddev(votes) from movie;
```

- ### JSON VALIDATE

```sql
set @var='{
"Information": 
  {"SchoolDetails": 
     [{"Name": "VidhyaMandhir"}, {"Name": "Chettinad"}, {"Name":"PSSenior"}]
  }
}'
SET @document = '{}';
SELECT JSON_SCHEMA_VALID( @var,@document); -- 1 if validation successfully else 0

SELECT JSON_VALUE(@var,'$.Information.SchoolDetails[0].Name') as SchoolName;

SELECT JSON_EXTRACT(@var,'$.Information.SchoolDetails') AS LISTOFSCHOOLS
```

- ### Conversion Function

- Implicit and explicit type conversion are 2 types
- Implicit : In this type of conversion, the data is converted from one type to another implicitly (by itself/automatically).

  - Explicit:

      ```sql
        select convert(release_date, DATE) from movie;    
    
    
      ```