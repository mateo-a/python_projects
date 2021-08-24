import os
import pytesseract
import cv2
from pdf2image import convert_from_path


def pdf_to_jpg(path):
    pdfs = path
    pages = convert_from_path(pdfs, 350)

    i = 1
    for page in pages:
        image_name = "scan" + ".jpg"
        page.save(image_name, "JPEG")
        i = i+1


def extrac_info(filename):
    img = cv2.imread(filename)

    custom_config = r'--oem 3 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
    data = pytesseract.image_to_string(img, config=custom_config)
    dataSplit = data.splitlines()
    comment = ''
    dict_values = {}

    for i in range(len(dataSplit)):
        if "vendor name: " in dataSplit[i].lower():

            dict_values["Vendor_Name"] = dataSplit[i][13:]
        if "fiscal number: " in dataSplit[i].lower():

            dict_values["Fiscal_Number"] = dataSplit[i][15:]
        if "contract" in dataSplit[i].lower():

            dict_values["Contract"] = dataSplit[i].split(':')[1].rstrip()
        if "start date:" in dataSplit[i].lower():

            dict_values["Start_Date"] = dataSplit[i+2]
        if "end date: " in dataSplit[i].lower():

            dict_values["End_Date"] = dataSplit[i][10:]
        if "comments:" in dataSplit[i].lower():
            while "more info:" not in dataSplit[i+1].lower():
                if dataSplit[i+1] != "":
                    comment = comment + dataSplit[i+1] + "\n"
                i += 1
            dict_values["Comments"] = comment.rstrip()

    os.remove(filename)
    return dict_values
