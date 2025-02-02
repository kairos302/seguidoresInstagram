import openpyxl

def WrittingPlan(listaTxtCnpj):
        
    wb = openpyxl.load_workbook("teste.xlsx")
    sheet = wb.active
    tamanhoLista =  len(listaTxtCnpj)
    for i in range(tamanhoLista):
        #Esta variavel e necessaria para começar na segunda linha*/
        cont = i + 2    
        coluna2 = sheet.cell(row=cont, column=2)
        cnpj = listaTxtCnpj[i]
        coluna2.value = cnpj
   
    wb.save("teste.xlsx")
    listaTxtCnpj.clear()

