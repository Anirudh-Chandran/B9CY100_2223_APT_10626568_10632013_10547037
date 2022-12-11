CREATE VIEW Vendor Name AS
SELECT v_name, v_phone, v_email, v_website
FROM Vendor.dbo
WHERE Location = 'Dublin';