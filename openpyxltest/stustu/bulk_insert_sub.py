def insert(self, tag_row, None_row, table_index, data_row, data):
    header0_row = tag_row + 1
    header1_row = None_row+1
    header_list = []
    data_list = []

    if table_index == 0:
        for cell in self.ws[str(header0_row)]: header_list.append(cell.value)
        for col in header_list:
            try:
                data_list.append(data[col])
            except KeyError as e:
                data_list.append(None)
                continue
        for col_num in range(1, len(data_list) + 1):
            self.ws.cell(row=data_row, column=col_num, value=data_list[col_num - 1])

    elif table_index == 1:
        for cell in self.ws[str(header1_row)]: header_list.append(cell.value)
        # print(header1_list)
        for col in header_list:
            try:
                data_list.append(data[col])
            except KeyError as e:
                data_list.append(None)
                continue
        for col_num in range(1, len(data_list) + 1): self.ws.cell(row=data_row, column=col_num,
                                                                  value=data_list[col_num - 1])
    else:
        print("Warning: No such table!! table_index can be 0 or 1")