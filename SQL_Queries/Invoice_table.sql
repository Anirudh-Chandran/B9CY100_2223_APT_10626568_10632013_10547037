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