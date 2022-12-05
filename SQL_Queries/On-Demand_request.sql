create table OnDemand_Request(
Req_ID int,
Req_Title varchar,
Req_Quantity int(2),
Req_Dimensions varchar,
Req_Description varchar,
Req_Need_by_Date date,
Req_Budget varchar,
H_ID int,
foreign key(H_ID)
references hospital)