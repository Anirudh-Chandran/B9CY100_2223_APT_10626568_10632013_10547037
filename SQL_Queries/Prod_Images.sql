/*
create table Prod_Images (
Prod_Image varbinary
)

*/

--select * from Prod_Images

Alter table prod_images
--add Prod_ID int foreign key (Prod_ID) references Product
--drop constraint FK__Prod_Imag__Prod___2BFE89A6
--Alter table prod_images
--add primary key(Img_id)
--add img_id int identity(1,1) primary key
add foreign key (prod_id) references product

select * from prod_images

delete from prod_images

SELECT TABLE_NAME,
       CONSTRAINT_TYPE,CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME='prod_images';