
/*create table Request_Approval(
Ack_ID int not null, 
V_ID int not null,
Req_ID int not null,
Ack_status varchar not null,
foreign key (V_ID) references vendor,
--foreign key (Req_ID) references OnDemand_Request,
primary key (Ack_ID)
)
*/

alter table request_approval
drop constraint FK__Request_A__Req_I__395884C4
--add foreign key (req_id) references ondemand_request
--alter column ack_status varchar (15)



SELECT TABLE_NAME,
       CONSTRAINT_TYPE,CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME='request_approval';