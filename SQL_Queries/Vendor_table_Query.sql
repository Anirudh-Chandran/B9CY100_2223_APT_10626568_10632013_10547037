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

alter table Vendor
--drop column v_location
--add v_street varchar, v_city varchar , v_postal_code varchar
--alter column v_city varchar not null
--drop constraint PK__Vendor__AD3D844110B23F37
--add primary key (v_id)
--add v_phone varchar, v_email varchar
add v_aboutus varchar

--select * from vendor

--delete from vendor





