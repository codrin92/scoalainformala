from __future__ import print_function
from docx2pdf import convert
import os

from mailmerge import MailMerge
from datetime import date

from Application1.models import Reporting


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
        fee = int(0.001 * object.project_value * 1000000)
    elif object.building_height > 18 and object.building_type not in ['Residential', 'residential']:
        fee = int(0.0005 * object.project_value * 1000000)
    else:
        fee = int(0.0004 * object.project_value * 1000000)
    # print(duration, fee)
    Reporting.objects.filter(id=quote_number).update(project_fee=fee)

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

def mailmergefunction_reports(object, project_number):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_name = "template_report.docx"
    filepath = BASE_DIR + '/templates/Application1/testfiles/'
    document = MailMerge(filepath+template_name)
    code_guidance = "NFPA2"

    if object.building_type in ['Residential', 'residential']:
        code_guidance = "IBC400"

    document.merge(
        Project_Name=object.project_name,
        Project_Address=object.project_address,
        Author=object.assigned_engineer,
        Residential_Commercial=object.building_type,
        Building_Height=str(object.building_height),
        No_of_stairs = str(object.number_of_stairs),
        Code_guidance = code_guidance
    )
    filename = filepath + f"PRJ{project_number}-{object.project_name}.docx"
    document.write(filename)
    filename_pdf = filepath + f"PRJ{project_number}-{object.project_name}.pdf"
    return convert(filename, filename_pdf)

def mailmergefunction_invoices(object, invoice_number):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_name = "template_invoice.docx"
    filepath = BASE_DIR + '/templates/Application1/testfiles/'
    document = MailMerge(filepath+template_name)

    document.merge(
        Inv_no = str(invoice_number),
        Client_name=object.client_representative,
        Client_company=object.client_company,
        Assigned_engineer=object.assigned_engineer,
        Project_name=object.project_name,
        Project_fee=str(object.project_fee)
    )
    filename = filepath + f"INV{invoice_number}.docx"
    document.write(filename)
    filename_pdf = filepath + f"INV{invoice_number}.pdf"
    return convert(filename, filename_pdf)


