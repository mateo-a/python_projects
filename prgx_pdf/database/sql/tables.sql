/*
*  SQL instruction to create the table to store the data extracted
*/

CREATE TABLE IF NOT EXISTS EXTRACTION(
    Vendor_Name TEXT,
    Fiscal_Number TEXT,
    Contract TEXT,
    Start_Date TEXT,
    End_Date TEXT,
    Comments TEXT
)