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
--alter column h_email varchar (50) not null
--select * from Hospital
--drop constraint PK__Hospital__61F3893D7851B133
add H_ID int identity(1,1) primary key

insert into Hospital 
values ('hospital-3','https://hospital-3.com','street-3','Dublin 3','1230986','0812376321','hospital-3@hospital3.com')

SELECT TABLE_NAME,
CONSTRAINT_TYPE,CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME='hospital';

select * from hospital