/*
create table OnDemand_Request(
Req_ID int not null,
Req_Title varchar not null,
Req_Quantity int,
Req_Dimensions varchar,
Req_Description varchar not null,
Req_Need_by_Date date,
Req_Budget varchar not null,
primary key (Req_ID)
--H_ID int,
--foreign key(H_ID)
--references hospital
)
*/
--select * from OnDemand_Request

alter table ondemand_request
--add H_ID int not null
--add foreign key (h_id) references hospital
--alter column req_title varchar(30) not null,
alter column req_title varchar (100) not null 

select * from ondemand_request

insert into ondemand_request values(1,'Request-1',12,'10x5x34','This is the first request from Hospital-1 and we need a medical device with mentioned dimensions. If any vendor can fulfill then please contact.','2023-08-23','80000',1)