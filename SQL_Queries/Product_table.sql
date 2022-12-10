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



alter table Product
--drop constraint prod_pk;
--alter column prod_id int not null
--add primary key(prod_id)
drop constraint v_id_fk
drop constraint PK__Product__C55AC32BC19C5368
--add constraint v_id_fk foreign key (v_id) references vendor
--alter column prod_description varchar(1000) not null

add Prod_size varchar(15)

select * from product
--delete from Product

insert into product values(1,'Prod-1',9,1,'This is first product entry')


update product
set prod_man_date='2022-08-25', prod_size='10x8x25'

SELECT TABLE_NAME,
       CONSTRAINT_TYPE,CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME='product';