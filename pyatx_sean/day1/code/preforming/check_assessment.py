import csv

tcsv = open("test.csv", "w", encoding="utf-8")
tcsv = csv.writer(tcsv)
tcsv.writerow(["test1_col", "test2_col", "test3_col"])
tcsv = open("test.csv", "r", encoding="utf-8")
tcsv = csv.reader(tcsv)
print(list(tcsv))


def assessment_logic_report_interface(raw_data, policy, expectation, output_file, report_content, ignore_loop="False"):
    result = policy(expectation, raw_data, ignore_loop)
    report_result = {}

    if len(report_content) == 1:
        compliant_content = report_content[0]["compliant"]
        non_compliant_content = report_content[0]["non-compliant"]
        report = open(output_file, "w", encoding="utf-8")
        for i in range(len(result)):
            for key in result[i].keys():
                if result[i][key] == "compliant":
                    report.write(f"{key}: {compliant_content}\n")
                elif result[i][key] == "non-compliant":
                    report.write(f"{key}: {non_compliant_content}\n")
        report.close()

    elif len(report_content) == 2:
        expectation_connection = report_content[0]["connection"]
        report_key = result[0].keys()
        report_dict = {}
        compliant_content = report_content[1]["compliant"]
        non_compliant_content = report_content[1]["non-compliant"]
        for key in report_key:
            value_list = []
            for i in range(len(result)):
                value_list.append(result[i][key])
            report_dict[key] = value_list
        if expectation_connection == "or":
            for key in report_key:
                if "compliant" in report_dict[key]:
                    report_result[key] = "compliant"
                else:
                    report_result[key] = "non-compliant"
        elif expectation_connection == "and":
            for key in report_key:
                if "non-compliant" not in report_dict[key]:
                    report_result[key] = "compliant"
                else:
                    report_result[key] = "non-compliant"
        report = open(output_file, "w", encoding="utf-8")
        for key in report_result.keys():
            if report_result[key] == "compliant":
                report.write(f"{key}: {compliant_content}\n")
            elif report_result[key] == "non-compliant":
                report.write(f"{key}: {non_compliant_content}\n")
        report.close()

def assessment_logic_report_general(raw_data, policy, output_file, report_content, option=None):
    if option != None:
        result = policy(raw_data, option)
    else:
        result = policy(raw_data)
    compliant_content = report_content["compliant"]
    non_compliant_content = report_content["non-compliant"]
    report = open(output_file, "w", encoding="utf-8")
    for i in result.keys():
        if result[i] == "compliant":
            report.write(f"{i}: {compliant_content}\n")
        elif result[i] == "non-compliant":
            report.write(f"{i}: {non_compliant_content}\n")
    report.close()

class assessment_logic_report_csv(object):
    def __init__(self, csv_file, mapping_sequence):
        csv_file = open(csv_file, "r", encoding="utf-8")
        csv_content_list = list(csv.reader(csv_file))
        mapping_sequence = mapping_sequence

    def csv_raw_data_comparation(self, csv_line, raw_data_dict, mapping_sequence, report_name, report_content, header = None):
        comparation_result = {}
        comparation_result_header = {}
        for key in mapping_sequence:
            if csv_line[mapping_sequence.index(key)] == raw_data_dict[key]:
                comparation_result[key] = "compliant"
            else:
                comparation_list = ["non-compliant", csv_line[mapping_sequence.index(key)], raw_data_dict[key]]
                comparation_result[key] = comparation_list

        report = open(report_name, "w", encoding="utf-8")
        if header != None:
            comparation_result_header[header] = comparation_result
            report.write(f"{header}: \n")
            self.csv_comparation_report(comparation_result, report_content, report)
        else:
            self.csv_comparation_report(comparation_result, report_content, report)

        return comparation_result_header

    def csv_comparation_report(self, comparation_result, report_content, report_object):
        report = report_object
        for key in comparation_result.keys():
            if comparation_result[key] == "compliant":
                report.write(f"{key}: {report_content['compliant']} \n")
            else:
                report.write(f"{key}: {report_content['non-compliant']}.  the value in csv is {comparation_result[key][1]}, the value from device is {comparation_result[key][2]} \n")

def assessment_logic_pyats_sort():
    pass
