from flask import Flask, request, jsonify

from database import documents, setup
import pdfReader

app = Flask(__name__)
setup.create_tables()


@app.route('/extract', methods=['GET', 'POST'])
def add_document():
    path = request.args.get('doc_path')

    if path:
        pdfReader.pdf_to_jpg(path)

        info = pdfReader.extrac_info("scan.jpg")

        vendor = info['Vendor_Name']
        fiscal_num = info['Fiscal_Number']
        contract_num = info['Contract']
        start_date = info['Start_Date']
        end_date = info['End_Date']
        comment = info['Comments']

        data = (vendor, fiscal_num, contract_num, start_date,
                end_date, comment)

        document_id = documents.insert_document(data)

        info['Doc_Path'] = path

        if document_id:
            return jsonify([['true', document_id], info])
        return jsonify({'message': 'Internal error'})


@app.route('/db_data/', methods=['GET'])
def get_documents():

    table = request.args.get('table_name')
    data = documents.select_all_documents(table)

    if data:
        return jsonify(data)
    elif data == False:
        return jsonify({'message': 'Internal error'})
    else:
        return jsonify({'documents': {}})


if __name__ == '__main__':
    app.run(debug=True)
