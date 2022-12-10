/*
CREATE TABLE Invoice(
Inv_ID		INT			NOT NULL,
Prod_Name VARCHAR  		NOT NULL,
Prod_ID 	INT			NOT NULL,
Quantity	INT			NOT NULL,
Price		INT			NOT NULL,
V_ID		INT			NOT NULL,
H_ID		INT			NOT NULL,
);
*/

alter table invoice
--add primary key (inv_id)
--add foreign key (V_ID) references vendor
add foreign key (h_ID) references hospital
--drop constraint FK__Invoice__Prod_ID__37703C52
--drop column v_id
--add foreign key (Prod_id) references product
--alter column prod_name varchar (200)

add Inv_id int identity(1,1) primary key


SELECT TABLE_NAME,
       CONSTRAINT_TYPE,CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME='invoice';
