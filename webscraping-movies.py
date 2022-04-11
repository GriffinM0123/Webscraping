
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##
table_rows = soup.findAll('tr')

wb = xl.Workbook()

MySheet = wb.active

MySheet.title = "Box Office Report"

wb.create_sheet(index=1, title="Box Office Report")

count = 2

for row in table_rows[1:6]:
    td = row.findAll('td')

    Rank = td[0].text
    Name = td[1].text
    Gross = int(td[5].text.replace(',','').replace('$',''))
    TotalG = int(td[7].text.replace(',','').replace('$',''))
    release_date = td[8].text
    precent_gross = round((Gross/TotalG)*100,2)

    MySheet['A' + str(count + 1)] = Rank
    MySheet['B' + str(count)] = Name
    MySheet['C' + str(count + 1)] = release_date
    MySheet['D' + str(count + 1)] = Gross
    MySheet['E' + str(count + 1)] = TotalG
    MySheet['F' + str(count + 1)] = precent_gross



    MySheet["A1"] = "No."
    MySheet["A1"].font = Font(name="Times New Roman", size=24, italic=True, bold=True)

    MySheet["B1"] = "Movie Title"
    MySheet["B1"].font = Font(name="Times New Roman", size=24, italic=True, bold=True)

    MySheet["C1"] = "Release Date"
    MySheet["C1"].font = Font(name="Times New Roman", size=24, italic=True, bold=True)

    MySheet["D1"] = "Gross"
    MySheet["D1"].font = Font(name="Times New Roman", size=24, italic=True, bold=True)

    MySheet["E1"] = "Total Gross"
    MySheet["E1"].font = Font(name="Times New Roman", size=24, italic=True, bold=True)

    MySheet["F1"] = "% of Total Gross"
    MySheet["F1"].font = Font(name="Times New Roman", size=24, italic=True, bold=True)

    fontobject = Font(name="Times New Roman", size=24, italic=True, bold=True)


  

    MySheet.column_dimensions['A'].width = 5
    MySheet.column_dimensions['B'].width = 30
    MySheet.column_dimensions['C'].width = 25
    MySheet.column_dimensions['D'].width = 16
    MySheet.column_dimensions['E'].width = 20
    MySheet.column_dimensions['F'].width = 26




    count = count + 1




    wb.save("BoxOfficeReport.xlsx")






    print(Rank)
    print(Name)
    print(Gross)
    print(TotalG)


