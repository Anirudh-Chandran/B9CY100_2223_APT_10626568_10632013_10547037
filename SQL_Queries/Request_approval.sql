
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
--drop constraint FK__Request_Ap__V_ID__31B762FC
--add foreign key (req_id) references ondemand_request
alter column ack_status varchar (15)