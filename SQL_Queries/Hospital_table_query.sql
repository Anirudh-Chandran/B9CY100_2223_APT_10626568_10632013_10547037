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
--alter column h_name varchar not null
--drop column h_contact
rename column Phome to H_Phone
--add primary key(H_ID)