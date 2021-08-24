# PDF Image Reader
Project to extract specifict information from PDF (image) files and store it in a SQLite database throug API endpoints.

---
## End Points
---
`/extract`

- Receive the path of the local PDF file.
> **Example:** `http://127.0.0.1:8000/extract?doc_path=C:\Users\files\Doc4.pdf`
- Extract (Vendor Name, Fiscal Number, Contract Number, Start Date, End Date, Comments paragraph) from the PDF file.
- Store the data extracted in a SQLite database.

**Returns:**
- True if it was successfully added to the data base.
- The data base id of the row.
- The extrated information.
#

`/db_data/`

- Receive the name of the table where the information extracted is stored.
> **Example:** `http://127.0.0.1:8000/db_data/?table_name=EXTRACTION`

**Returns:**
- All the extractions ordered by the newest id to the oldest.

---
**Author:** [John Alexander Urrego Sandoval](alexander.urrego@gmail.com)
