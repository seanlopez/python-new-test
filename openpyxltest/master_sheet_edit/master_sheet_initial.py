from stustu import master_sheet_operator
from stustu import master_sheet_format
import section_info
from openpyxl import Workbook
from mongo_db_operation import MongoOperation
from tqdm import tqdm


def master_sheet_all_section_create(file_path, sheet_name):
    MS = master_sheet_operator.MasterSheet(file_path, sheet_name)
    section_dic = section_info.section_detail
    #print(section_dic)
    for sec in section_dic:
        for sec_name in sec:
            MS.add_section(sec_name, sec[sec_name][0], sec[sec_name][1])
        MS.wb.save(MS.file_path)

def workbook_creation(hostname_list, workbook_path):
    wb = Workbook()
    for hostname in hostname_list:
        ws = wb.create_sheet(hostname)
    ws = wb["Sheet"]
    wb.remove(ws)
    wb.save(workbook_path)

if __name__ == "__main__":
    MO = MongoOperation.MongoOperation()
    hostname_list = MO.get_hostname("tianqi_db", "l3_interface_list")
    #print(hostname_list)
    workbook_creation(hostname_list, "C:\python-new-code\openpyxltest\master_sheet_edit\\PT_Telkom_Master_Sheet.xlsx")
    print("Master Sheet Initialization Progress: ")
    for hostname in tqdm(hostname_list):
        master_sheet_all_section_create("C:\python-new-code\openpyxltest\master_sheet_edit\\PT_Telkom_Master_Sheet.xlsx", hostname)

