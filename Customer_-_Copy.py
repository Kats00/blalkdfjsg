from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB:
    
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(0 * titlespace + "Xialan Shaomai Customer Database GUI")
        self.root.geometry("1400x680+100+0")
        self.root.resizable(width = True, height = True)

        #=================================================Frame Design==========================================================

        MainFrame = Frame(self.root, bd =10, width = 1000, height = 500, relief = RIDGE, bg = 'cadet blue')
        MainFrame.grid()

        titlespace = Frame(MainFrame, bd = 7, width = 1000, height = 100, relief = RIDGE)
        titlespace.grid(row = 0, column = 0)
        
        TopFrame3 = Frame(MainFrame, bd = 5, width = 1000, height = 700, bg = 'cadet blue', relief = RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd =5, width = 1000, height = 100, padx = 2, bg = 'cadet blue', relief = RIDGE)
        LeftFrame.pack(side = LEFT)
        
        LeftFrame1 = Frame(LeftFrame, bd = 5, width = 1000, height = 100, padx = 12, pady = 24, relief = RIDGE)
        LeftFrame1.pack(side = TOP)

        RightFrame1 = Frame(TopFrame3, bd = 5, width = 800, height = 100, padx = 2, bg = 'cadet blue', relief = RIDGE)
        RightFrame1.pack(side = RIGHT)
        
        RightFrame1a = Frame(RightFrame1, bd = 5, width = 150, height = 500, padx = 2, pady = 2, bg = 'cadet blue', relief = RIDGE)
        RightFrame1a.pack(side = TOP)

        #==========================Variables Declaration=========================================

        C_ID = StringVar()
        C_LName = StringVar()
        C_FName = StringVar()
        C_Address = StringVar()
        Cell_Num = StringVar()
        C_Email = StringVar()

        #========================Functions Declaration=========================================
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Xialan Shaomai Customer Database GUI", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.entC_ID.delete(0, END)
            self.entC_LName.delete(0, END)
            self.entC_FName.delete(0, END)
            self.entC_Address.delete(0, END)
            self.entCell_Num.delete(0, END)
            self.entC_Email.delete(0, END)

        def addData():
            if C_ID.get() =="" or C_LName.get() =="" or C_FName.get() =="" or C_Address.get() =="" or Cell_Num.get() =="" or C_Email.get() =="":
                tkinter.messagebox.askyesno("Xialan Shaomai Customer Database GUI", "Enter Correct Details")
            else:
                sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
                cur = sqlCon.cursor()
                cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s)", (

                C_ID.get(),
                C_LName.get(),
                C_FName.get(),
                C_Address.get(),
                Cell_Num.get(),
                C_Email.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Xialan Shaomai Customer Database GUI", "Record Entered Successfully")

        def DisplayData():
                sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
                cur = sqlCon.cursor()
                cur.execute("select * from customer")
                result = cur.fetchall()
                if len(result) != 0:
                    self.customer_records.delete(*self.customer_records.get_children())
                    for row in result:
                        self.customer_records.insert('', END, values = row)
                    sqlCon.commit()
                sqlCon.close()

        def ascData():
            sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
            cur = sqlCon.cursor()
            cur.execute("select * from customer order by C_ID ASC")
            result = cur.fetchall()
            self.customer_records.delete(*self.customer_records.get_children())
            for row in result:
                self.customer_records.insert('', END, values = row)
            sqlCon.commit()
            sqlCon.close()

        def descData():
            sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
            cur = sqlCon.cursor()
            cur.execute("select * from customer order by C_ID DESC")
            result = cur.fetchall()
            self.customer_records.delete(*self.customer_records.get_children())
            for row in result:
                self.customer_records.insert('', END, values = row)
            sqlCon.commit()
            sqlCon.close() 

        def CustomerInfo(ev):
            viewInfo = self.customer_records.focus()
            learnerData = self.customer_records.item(viewInfo)
            row = learnerData['values']
            C_ID.set(row[0]),
            C_LName.set(row[1]),
            C_FName.set(row[2]),
            C_Address.set(row[3]),
            Cell_Num.set(row[4]),
            C_Email.set(row[5])

        def Update():
            sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
            cur = sqlCon.cursor()
            cur.execute("update customer set C_LName = %s, C_FName = %s, C_Address = %s, Cell_Num = %s, C_Email = %s where C_ID = %s", (
                     
            C_LName.get(),
            C_FName.get(),
            C_Address.get(),
            Cell_Num.get(),
            C_Email.get(),
            C_ID.get()
            ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Xialan Shaomai Customer Database GUI", "Record Updated Successfully")

        def DeleteDB():
            sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
            cur = sqlCon.cursor()
            cur.execute("delete from customer where C_ID = %s", C_ID.get())

            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Xialan Shaomai Customer Database GUI", "Record Deleted Successfully")
            Reset()

        
        
        def SearchDB():
            try:
                sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
                cur = sqlCon.cursor()
                cur.execute("select * from customer where C_ID = '%s'"%C_ID.get())

                row = cur.fetchone()
                
                C_ID.set(row[0]),
                C_LName.set(row[1]),
                C_FName.set(row[2]),
                C_Address.set(row[3]),
                Cell_Num.set(row[4]),
                C_Email.set(row[5])
                
                sqlCon.commit() 
            except:   
                tkinter.messagebox.showinfo("Xialan Shaomai Customer Database GUI", "No Such Record Found")
                Reset()
            sqlCon.close()
            
        #================================================Label Title==========================================================

        self.lbtitle = Label(titlespace, font = ('arial', 20, 'bold'), text = "Customer Database", bd = 7)
        self.lbtitle.grid(row = 0, column = 0, padx = 475)
        
        #================================================Label and Entry Widget==========================================================
        
        self.lblC_ID = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Customer ID", bd = 7)
        self.lblC_ID.grid(row = 0, column = 0, sticky = W, padx = 100)
        self.entC_ID = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = C_ID)
        self.entC_ID.grid(row = 0, column = 1, sticky = W, padx = 100)
        
        self.lblC_LName = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Customer Last Name", bd = 7)
        self.lblC_LName.grid(row = 1, column = 0, sticky = W, padx = 100)
        self.entC_LName = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = C_LName)
        self.entC_LName.grid(row = 1, column = 1, sticky = W, padx = 100)        

        self.lblC_FName = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Customer First Name", bd = 7)
        self.lblC_FName.grid(row = 2, column = 0, sticky = W, padx = 100)
        self.entC_FName = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = C_FName)
        self.entC_FName.grid(row = 2, column = 1, sticky = W, padx = 100)

        self.lblC_Address = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Customer Address", bd = 7)
        self.lblC_Address.grid(row = 3, column = 0, sticky = W, padx = 100)
        self.entC_Address = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = C_Address)
        self.entC_Address.grid(row = 3, column = 1, sticky = W, padx = 100)

        self.lblCell_Num = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Cellphone Number", bd = 7)
        self.lblCell_Num.grid(row = 4, column = 0, sticky = W, padx = 100)
        self.entCell_Num = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Cell_Num)
        self.entCell_Num.grid(row = 4, column = 1, sticky = W, padx = 100)

        self.lblC_Email = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Customer Email", bd = 7)
        self.lblC_Email.grid(row = 5, column = 0, sticky = W, padx = 100)
        self.entC_Email = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = C_Email)
        self.entC_Email.grid(row = 5, column = 1, sticky = W, padx = 100)

        #=======================================================Table Treeview Widget=============================================================

        scroll_y = Scrollbar(LeftFrame, orient = VERTICAL)
        
        self.customer_records = ttk.Treeview(LeftFrame, height = 14, columns = ("C_ID", "C_LName", "C_FName", "C_Address",
                                                                    "Cell_Num", "C_Email"), yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT, fill = Y)
        
        self.customer_records.heading("C_ID", text="Customer ID")
        self.customer_records.heading("C_LName", text="Customer Last Name")
        self.customer_records.heading("C_FName", text="Customer First Name")
        self.customer_records.heading("C_Address", text="Customer Address")
        self.customer_records.heading("Cell_Num", text="Cellphone Number")
        self.customer_records.heading("C_Email", text="Customer Email")

        self.customer_records['show'] = 'headings'

        self.customer_records.column("C_ID", width = 100)
        self.customer_records.column("C_LName", width = 100)
        self.customer_records.column("C_FName", width = 100)
        self.customer_records.column("C_Address", width = 100)
        self.customer_records.column("Cell_Num", width = 100)
        self.customer_records.column("C_Email", width = 100)

        self.customer_records.pack(fill = BOTH, expand = 1)
        self.customer_records.bind("<ButtonRelease-1>", CustomerInfo)
        #DisplayData()
        
        
        #=======================================================Buttons Widget===================================================================

        self.btnAddNew = Button(RightFrame1a, font = ('arial', 16, 'bold'), text = "Add new", bd = 1, pady = 1, padx = 10,
                                width = 8, height = 2, command = addData).grid(row = 0, column = 0, padx = 1)

        self.btnDisplayData = Button(RightFrame1a, font = ('arial', 16, 'bold'), text = "Display", bd = 1, pady = 1, padx = 10,
                                width = 8, height = 2, command = DisplayData).grid(row = 1, column = 0, padx = 1,)

        self.btnUpdate = Button(RightFrame1a, font = ('arial', 16, 'bold'), text = "Update", bd = 1, pady = 1, padx = 10,
                                width = 8, height = 2, command = Update).grid(row = 2, column = 0, padx = 1)

        self.DeleteDB = Button(RightFrame1a, font = ('arial', 16, 'bold'), text = "Delete", bd = 1, pady = 1, padx = 10,
                                width = 8, height = 2, command = DeleteDB).grid(row = 3, column = 0, padx = 1)

        self.SearchDB = Button(RightFrame1a, font = ('arial', 16, 'bold'), text = "Search", bd = 1, pady = 1, padx = 10,
                                width = 8, height = 2, command = SearchDB).grid(row = 4, column = 0, padx = 1)

        self.btnascData = Button(RightFrame1a, font = ('arial', 16, 'bold'), text = "Ascending", bd = 1, pady = 1, padx = 10,
                                width = 8, height = 2, command = ascData).grid(row = 5, column = 0, padx = 1)

        self.btndescData = Button(RightFrame1a, font = ('arial', 16, 'bold'), text = "Descending", bd = 1, pady = 1, padx = 10,
                                width = 8, height = 2, command = descData).grid(row = 6, column = 0, padx = 1) 

        self.btnReset = Button(RightFrame1a, font = ('arial', 16, 'bold'), text = "Reset", bd = 1, pady = 1, padx = 10,
                                width = 8, height = 2, command = Reset).grid(row = 7, column = 0, padx = 1)

        self.btniExit = Button(RightFrame1a, font = ('arial', 16, 'bold'), text = "Exit", bd = 1, pady = 1, padx = 10,
                                width = 8, height = 2, command = iExit).grid(row = 8, column = 0, padx = 1)      

        
if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
