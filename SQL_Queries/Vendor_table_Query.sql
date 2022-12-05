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

alter table vendor
--drop column v_location
add v_street varchar, v_city varchar , v_postal_code varchar