import os
import pytesseract
import cv2
from pdf2image import convert_from_path


def pdf_to_jpg(path):
    """ Function to convert PDF file to JPG creating a file named scan.jpg in
    order to be able to extract the text in the function extract_info, the file
    is deleted at the end of the process.

    path: Path received in the end point, where is located the PDF file.
    """
    pdfs = path
    pages = convert_from_path(pdfs, 350)

    for page in pages:
        page.save("scan.jpg", "JPEG")


def extrac_info(filename):
    """ Function to extract required information, in this case (Vendor_Name,
    Fiscal_Number, Contract, Start_Date, End_Date, Comments), the information 
    is extracted based on the JPEG file created in the function pdf_to_jpg.

    filename: Name of the JPEG file that will be processed.

    RETURN: A dictionary with the values requested
    """

    img = cv2.imread(filename)

    custom_config = r'--oem 3 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
    data = pytesseract.image_to_string(img, config=custom_config)
    dataSplit = data.splitlines()
    comment = ''
    dict_values = {}

    for i in range(len(dataSplit)):
        if "vendor name: " in dataSplit[i].lower():
            dict_values["Vendor_Name"] = dataSplit[i].split(':')[1].strip()

        if "fiscal number: " in dataSplit[i].lower():
            dict_values["Fiscal_Number"] = dataSplit[i].split(':')[1].strip()

        if "contract" in dataSplit[i].lower():
            dict_values["Contract"] = dataSplit[i].split(':')[1].strip()

        if "start date:" in dataSplit[i].lower():
            dict_values["Start_Date"] = dataSplit[i+2]

        if "end date: " in dataSplit[i].lower():
            dict_values["End_Date"] = dataSplit[i].split(':')[1].strip()

        if "comments:" in dataSplit[i].lower():
            while "more info:" not in dataSplit[i+1].lower():
                if dataSplit[i+1] != "":
                    comment = comment + dataSplit[i+1] + "\n"
                i += 1
            dict_values["Comments"] = comment.rstrip()

    os.remove(filename)
    return dict_values
