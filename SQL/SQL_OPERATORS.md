```sql

-- select * from movie where release_year > 2000;
-- select * from movie where release_year >= 1972;
-- select * from movie where release_year < 1972;
-- select * from movie where release_year <= 1972;
-- select * from movie where release_year = 1972;
-- select * from movie where release_year <> 2000;
-- select * from movie where release_year between 1972 and 1995;
-- select * from movie where movie_name not like 'S%';
-- select * from movie where movie_name not like '% %';
-- select * from movie where movie_name like '% %';
-- select * from movie where movie_name like 'S%';
-- select * from movie where release_year in (1971,2000);
-- select date_format( release_date,'%d %M %Y') from movie;
-- select * from movie where movie_name like 'S%' and release_year between 1980 and 2000;
-- select * from movie where movie_name like 'S%' or release_year between 1980 and 2000;
-- select * from movie where movie_name like 'S%' or ( release_year between 1980 and 2000 and metascore < 100);
-- select * from movie where movie_name like 'S%' or ( release_year between 1980 and 2000 and metascore < 100);
-- select * from movie where release_year <> -- 1982;
-- select * from movie where release_year != 1982;
-- select * from movie where release_year is null;
-- select * from movie where release_year is not null;
-- select count(*) from  (select * from movie union all select * from movie_copy) as t;
-- select count(*) from  (select * from movie union all select * from movie_copy) as t;
-- alter  table movie_copy add column `sl_id` INT primary key auto_increment;
-- alter table movie_copy rename column `date` to `release_date`;
-- select * from (select movie_name from movie except select * from movie_copy)
-- select movie_name from movie except all select movie_name from movie_copy;
-- select movie_name from movie except select movie_name from movie_copy;
-- select all movie_name from movie;
-- select * from movie where movie_name = ANY ( select movie_name from movie_copy where movie_name  like 'S%');
-- select * from movie where movie_name = ALL ( select movie_name from movie_copy where movie_name  like 'S%');
-- select *,sum(votes) from movie group by release_year;

-- alter table movie change column `votes` `votes` int(2) default null;
-- delete from movie where votes is null;
-- select * from movie;

-- select movie_name from movie where movie_name like 's%' INTERSECT select movie_name from movie_copy where movie_name like 's%';
-- select * from movie where exists (select * from movie where release_year = 2025);
-- select * from movie where not exists (select * from movie where release_year = 2024); 

-- select movie_name, release_year , case when release_year between 1970 and 1980 THEN 'Oldest Movie' when release_year between 1980 and 2000 then 'old movie' else 'New movie' end as movie_old from movie;

```