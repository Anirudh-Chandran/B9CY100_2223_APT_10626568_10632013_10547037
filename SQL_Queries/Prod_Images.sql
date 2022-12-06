/*
create table Prod_Images (
Prod_Image varbinary
)

*/

--select * from Prod_Images

Alter table prod_images
add Prod_ID int foreign key (Prod_ID) references Product


--Alter table prod_images
--add primary key(Img_id)

select * from prod_images

delete from prod_images