from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB:
    
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(0 * titlespace + "Xialan Shaomai Transaction Database GUI")
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

        Trans_ID = StringVar()
        C_ID = StringVar()
        Prod_ID = StringVar()
        Ord_ID = StringVar()
        

        #========================Functions Declaration=========================================
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Xialan Shaomai Transaction Database GUI", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.entTrans_ID.delete(0, END)
            self.entC_ID.delete(0, END)
            self.entProd_ID.delete(0, END)
            self.entOrd_ID.delete(0, END)

        def addData():
            if Trans_ID.get() =="" or C_ID.get() =="" or Prod_ID.get() =="" or Ord_ID.get() =="":
                tkinter.messagebox.askyesno("Xialan Shaomai Transaction Database GUI", "Enter Correct Details")
            else:
                sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
                cur = sqlCon.cursor()
                cur.execute("insert into transaction values(%s,%s,%s,%s)", (

                Trans_ID.get(),
                C_ID.get(),
                Prod_ID.get(),
                Ord_ID.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Xialan Shaomai Transaction Database GUI", "Record Entered Successfully")

        def DisplayData():
                sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
                cur = sqlCon.cursor()
                cur.execute("select * from transaction")
                result = cur.fetchall()
                if len(result) != 0:
                    self.transaction_records.delete(*self.transaction_records.get_children())
                    for row in result:
                        self.transaction_records.insert('', END, values = row)
                    sqlCon.commit()
                sqlCon.close()

        def TransactionInfo(ev):
            viewInfo = self.transaction_records.focus()
            learnerData = self.transaction_records.item(viewInfo)
            row = learnerData['values']

            Trans_ID.set(row[0])
            C_ID.set(row[1]),
            Prod_ID.set(row[2]),
            Ord_ID.set(row[3]),

        def ascData():
            sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
            cur = sqlCon.cursor()
            cur.execute("select * from transaction order by Trans_ID ASC")
            result = cur.fetchall()
            self.transaction_records.delete(*self.transaction_records.get_children())
            for row in result:
                self.transaction_records.insert('', END, values = row)
            sqlCon.commit()
            sqlCon.close()

        def descData():
            sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
            cur = sqlCon.cursor()
            cur.execute("select * from transaction order by Trans_ID DESC")
            result = cur.fetchall()
            self.transaction_records.delete(*self.transaction_records.get_children())
            for row in result:
                self.transaction_records.insert('', END, values = row)
            sqlCon.commit()
            sqlCon.close()
            

        def Update():
            sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
            cur = sqlCon.cursor()
            cur.execute("update transaction set C_ID = %s, Prod_ID = %s, Ord_ID = %s, Trans_ID = %s,", (
                     
            C_ID.get(),
            Prod_ID.get(),
            Ord_ID.get(),
            Trans_ID.get()
            ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Xialan Shaomai Transaction Database GUI", "Record Updated Successfully")

        def DeleteDB():
            sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
            cur = sqlCon.cursor()
            cur.execute("delete from transaction where Trans_ID = %s", Trans_ID.get())

            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Xialan Shaomai Transaction Database GUI", "Record Deleted Successfully")
            Reset()

        
        
        def SearchDB():
            try:
                sqlCon = pymysql.connect(host = "localhost", user = "root", password = "V@no$$1012", database = "siomai")
                cur = sqlCon.cursor()
                cur.execute("select * from transaction where Trans_ID = %s"%Trans_ID.get())

                row = cur.fetchone()
                
                Trans_ID.set(row[0])
                C_ID.set(row[1]),
                Prod_ID.set(row[2]),
                Ord_ID.set(row[3]),
                
                sqlCon.commit() 
            except:   
                tkinter.messagebox.showinfo("Xialan Shaomai Transaction Database GUI", "No Such Record Found")
                Reset()
            sqlCon.close()
            
        #================================================Label Title==========================================================

        self.lbtitle = Label(titlespace, font = ('arial', 20, 'bold'), text = "Transaction Database", bd = 7)
        self.lbtitle.grid(row = 0, column = 0, padx = 475)
        
        #================================================Label and Entry Widget==========================================================
        
        self.lblTrans_ID = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Transaction ID", bd = 7)
        self.lblTrans_ID.grid(row = 0, column = 0, sticky = W, padx = 100)
        self.entTrans_ID = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Trans_ID)
        self.entTrans_ID.grid(row = 0, column = 1, sticky = W, padx = 100)
        
        self.lblC_ID = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Customer ID", bd = 7)
        self.lblC_ID.grid(row = 1, column = 0, sticky = W, padx = 100)
        self.entC_ID = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = C_ID)
        self.entC_ID.grid(row = 1, column = 1, sticky = W, padx = 100)        

        self.lblProd_ID = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Product ID", bd = 7)
        self.lblProd_ID.grid(row = 2, column = 0, sticky = W, padx = 100)
        self.entProd_ID = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Prod_ID)
        self.entProd_ID.grid(row = 2, column = 1, sticky = W, padx = 100)

        self.lblOrd_ID = Label(LeftFrame1, font = ('arial', 12, 'bold'), text = "Order ID", bd = 7)
        self.lblOrd_ID.grid(row = 3, column = 0, sticky = W, padx = 100)
        self.entOrd_ID = Entry(LeftFrame1, font = ('arial', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Ord_ID)
        self.entOrd_ID.grid(row = 3, column = 1, sticky = W, padx = 100)


        #=======================================================Table Treeview Widget=============================================================

        scroll_y = Scrollbar(LeftFrame, orient = VERTICAL)
        
        self.transaction_records = ttk.Treeview(LeftFrame, height = 14, columns = ("Trans_ID", "C_ID", "Prod_ID", "Ord_ID"), yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT, fill = Y)
        
        self.transaction_records.heading("Trans_ID", text="Transaction ID")
        self.transaction_records.heading("C_ID", text="Customer ID")
        self.transaction_records.heading("Prod_ID", text="Product ID")
        self.transaction_records.heading("Ord_ID", text="Order ID")

        self.transaction_records['show'] = 'headings'

        self.transaction_records.column("Trans_ID", width = 100)
        self.transaction_records.column("C_ID", width = 100)
        self.transaction_records.column("Prod_ID", width = 100)
        self.transaction_records.column("Ord_ID", width = 100)

        self.transaction_records.pack(fill = BOTH, expand = 1)
        self.transaction_records.bind("<ButtonRelease-1>", TransactionInfo)
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
