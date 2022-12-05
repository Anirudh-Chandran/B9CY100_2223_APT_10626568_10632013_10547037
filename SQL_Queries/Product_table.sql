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
--drop constraint FK__Product__v_id__3A4CA8FD
--add constraint v_id_fk foreign key (v_id) references vendor
alter column prod_description varchar(1000) not null

select * from product
--delete from Product

insert into product values(1,'Prod-1',9,1,'This is first product entry')


