
show databases;
show tables;
desc emaillist;

insert into emaillist values (null, "YI", "DINGDONG", "gudboy@naver.com");
insert into emaillist values (null, "OH", "MAY", "maymay55@naver.com");


select no, first_name, last_name, email from emaillist order by no desc;

delete from emaillist where email="gudboy@naver.com";

select * from emaillist order by no desc;

desc guestbook;
insert into guestbook values(null, "DINGDING","1234","HELLO there",now());

-- select 
select no, name, message,date_format(reg_date, "%Y-%m-%d %p %h:%i:%s") as reg_date
from guestbook
order by reg_date desc;

-- delete
delete from guestbook 
where no=1 and password= "1234";

