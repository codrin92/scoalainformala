from __future__ import print_function
from docx2pdf import convert
import os

from mailmerge import MailMerge
from datetime import date

def mailmergefunction_quotes(object, quote_number):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_name = "template.docx"
    filepath = BASE_DIR + '/templates/Application1/testfiles/'
    document = MailMerge(filepath+template_name)
    # print(document.get_merge_fields())
    duration = 6

    if object.building_type in ['Residential', 'residential']:
        duration = 4
    if object.building_height > 18 and object.building_type not in ['Residential', 'residential']:
        fee = 0.01 * object.project_value * 1000000
    elif object.building_height > 18 and object.building_type not in ['Residential', 'residential']:
        fee = 0.005 * object.project_value * 1000000
    else:
        fee = 0.004 * object.project_value * 1000000
    print(duration, fee)

    document.merge(
        Client_Name=object.client_representative,
        Project_Name=object.project_name,
        Project_Address=object.project_address,
        Project_Value=str(object.project_value),
        Residential_Commercial=object.building_type,
        Building_Height=str(object.building_height),
        Project_Duration=str(duration),
        Fee=str(fee))

    filename = filepath + f"Q{quote_number}-{object.project_name}.docx"
    document.write(filename)
    filename_pdf = filepath + f"Q{quote_number}-{object.project_name}.pdf"
    return convert(filename, filename_pdf)




