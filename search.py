import xlrd

def get_line(file,country):
    i = country
    book = xlrd.open_workbook(file)
    number_sheets = book.nsheets
    sheet = book.sheet_by_index(0)
    names = sheet.col_values(0)
    del names[0:2]
    c = 0
    for g in names:
        if i == g:
            n_raw = c + 2
        else:
            c+=1
    value = sheet.row_values(n_raw)
    return value
    #research_main(value,bot,update,percent_level_fall)
