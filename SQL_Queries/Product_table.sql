/*
Create table Product (
Prod_id varchar(10) not null,
Prod_Name varchar(200) not null,
Prod_Man_Date date not null,
Prod_Man_By varchar(200) not null,
Prod_Dimensions varchar(200) not null, 
Prod_Quantity int not null,
Prod_Description varchar(1000) not null,
Prod_Image binary,
v_id int not null,
CONSTRAINT Prod_pk PRIMARY KEY (Prod_id),
CONSTRAINT v_id_fk foreign key (v_id)
REFERENCES Vendor (v_id)
)
*/
--insert into Product (prod_id, prod_name, prod_quantity,v_id)
--values('123','Nam', 7,4)



alter table product
Add prod_description varchar
