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
--add H_Street varchar, H_City varchar not null, H_Postal_Code varchar
add primary key(H_ID)