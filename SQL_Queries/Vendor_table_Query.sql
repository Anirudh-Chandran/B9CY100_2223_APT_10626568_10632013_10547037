/*
Create table Vendor(
v_id int,
v_name varchar,
v_Location varchar,
v_associations varchar,
v_contact varchar,
Prod_ID int
)
*/
use AVA_DB_1
alter table Vendor
--drop column v_location
--add v_street varchar, v_city varchar , v_postal_code varchar
--alter column v_email varchar(30) not null
drop constraint PK__Vendor__AD3D84416252135D
--add primary key (v_id)
--add v_phone varchar, v_email varchar
--add v_website varchar(100)
add v_id int identity(1,1) primary key

--select * from vendor

--delete from vendor

insert into vendor values('Vendor-1', 1,'st 1','dublin','123','0987895643','vendor@vendor.com','We manufacture medical devices')


update vendor
set v_website='https://vendor-1.com' where v_id=1

SELECT TABLE_NAME,
       CONSTRAINT_TYPE,CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME='vendor';





