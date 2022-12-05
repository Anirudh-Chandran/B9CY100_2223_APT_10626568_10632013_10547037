create table OnDemand_Request(
Req_ID int(3) not null,
Req_Title varchar not null,
Req_Quantity int(2),
Req_Dimensions varchar,
Req_Description varchar not null,
Req_Need_by_Date date,
Req_Budget varchar not null,
primary key (Req_ID)
--H_ID int,
--foreign key(H_ID)
--references hospital
)