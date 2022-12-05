/*
Create table Hospital(
H_ID int,
H_Name varchar,
H_Location varchar,
H_website varchar,
H_Contact varchar
)
*/

alter table hospital
--alter column H_Id int not null
--alter column h_city varchar(30) not null
--drop column h_contact
--rename column Phome to H_Phone
--add primary key(H_ID)
alter column h_email varchar (50) not null
--select * from Hospital

insert into Hospital (h_id,h_name,h_city)
values (1,'hospital-1','dublin')