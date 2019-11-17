"""Contains Code to print PDF from a table.
"""

import string

import openpyxl
from pandas import DataFrame

from PyQt5.QtPrintSupport import QPrintDialog

class PrintPDF:
    def printer(self):

        Page = QPrintDialog(self)
        dec = Page.exec_()

        # Code added for creating the excel file
        if dec == 1:
            model = self.table.__model__
            data = []
            for row in range(model.rowCount()):
                data.append([])
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    data[row].append(str(model.data(index)))

            # for formatting excels
            dp = dict(enumerate(string.ascii_uppercase, 1))
            xlsFilepath = "./testing1.xlsx"

            # creating dataframes adding columns to the dataframe
            self.df = DataFrame(data)
            self.attr = list(self.FeildForm.keys())
            self.df.columns = self.attr
            self.no_of_attr = len(self.df.columns)

            # greater than  or equal to 7 no_of_attr
            if self.no_of_attr >= 7:

                self.df = self.df.transpose()

                self.df.to_excel("testing1.xlsx")

                wb = openpyxl.load_workbook("testing1.xlsx")
                sheet = wb.active

                column_len = len(max(self.df.index))
                sheet.column_dimensions[dp[1]].width = column_len + 5

                for x, y in enumerate(self.df.columns):

                    column_len = self.df[x].astype(str).str.len().max()
                    print(dp[x + 2])
                    sheet.column_dimensions[dp[x + 2]].width = column_len + 5

                wb.save(xlsFilepath)
            # for no_of_attributes <7
            else:

                self.df.to_excel("testing1.xlsx")

                wb = openpyxl.load_workbook("testing1.xlsx")
                sheet = wb.active

                for x, y in enumerate(self.df.columns):

                    column_len = len(max(self.df[self.df.columns[x]]))

                    column_attr_len = len(self.df.columns[x])

                    print("cl=", column_len, " attr=", column_attr_len)

                    column_len = (
                        column_len if column_len >= column_attr_len else column_attr_len
                    )

                    sheet.column_dimensions[dp[x + 2]].width = column_len + 5
                    print(dp[x + 1], column_len + 5)

                sheet.column_dimensions[dp[x + 2]].width = column_len + 5
                print(dp[x + 2], column_len + 5)

                wb.save(xlsFilepath)
