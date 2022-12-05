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
alter column req_budget varchar (12) not null 
