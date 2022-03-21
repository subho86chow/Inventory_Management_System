from tkinter import*
from tkinter import ttk,messagebox,Label,filedialog
from datetime import date
import time
import datetime
import sqlite3
import csv
import os

class ims:
    def __init__(self,root):

        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Inventory Management System | zeroGRAVITY")
        self.root.iconbitmap(r'icon.ico')


    #=====================variables======================================

        self.today = date.today()#..........date function
        self.create_db()#............database validation
        # print(self.today.strftime("%d/%m/%Y"))
        today = datetime.date.today()
        
        first = today.replace(day=1)
        self.firstdayofMonth = first - datetime.timedelta(days=30)
        # print(self.firstdayofMonth.strftime("%Y-%m-%d"))
        self.lastdayofMonth = first - datetime.timedelta(days=1)
        # print(self.lastdayofMonth.strftime("%Y-%m-%d"))
        

    #.....................add products....................................
        
        self.SNO=IntVar()
        self.var_brandname=StringVar()
        self.var_productname=StringVar()
        self.var_quantity=DoubleVar()
        self.var_price=DoubleVar()
        self.var_total=DoubleVar()
        self.var_searchbrandname=StringVar()
        self.var_searchproductname=StringVar()
        self.var_searchdate=StringVar()
        self.productquantity_now=IntVar()
        self.var_finalquantitynow=IntVar()
        self.productquantity_now1=IntVar()

    #.....................delever products....................................


        self.delevery_SNO=IntVar()
        self.delevery_SNO1=IntVar()
        self.var_deleverybrandname=StringVar()
        self.var_deleveryproductname=StringVar()
        self.var_deleveryquantity=DoubleVar()
        self.var_deleveryprice=DoubleVar()
        self.var_deleverytotal=DoubleVar()
        self.var_deleverysearchbrandname=StringVar()
        self.var_deleverysearchproductname=StringVar()
        self.var_availablequantity=DoubleVar()
        self.var_deleverysearchdate=StringVar()
        self.var_finalquantity=IntVar()
        self.var_eid=IntVar()
        self.var_gtotal=DoubleVar()
        self.deleveryproductquantity_now1=IntVar()
        self.var_finalquantitynow1=IntVar()
        self.deleveryproductquantity_now=IntVar()
        self.deleveryproductquantity_now2=IntVar()
        self.var_total1=DoubleVar()
    
    #.................details......................    

        self.datefrom=StringVar()
        self.dateto=StringVar()
        self.brandnamed=StringVar()
        self.productnamed=StringVar()
        self.var_prevmt=DoubleVar()
        self.var_thismt=DoubleVar()
        self.var_percentage=DoubleVar()

        # self.previousm_sell()
        self.thism_sell()
        # self.percentage()



    #==============top frame=================

        title=Label(self.root,bg="blue",text="Inventory Management System",fg="white",font=("roboto",30,"bold"),anchor="w",padx="40").place(x=0,y=0,relwidth=1,height=60)

        exit=Button(self.root,text="Exit",command=root.quit,font=("roboto",18,"bold"),bg="red",cursor="hand2").place(x=1350,y=10,height=40,width=140)


    #==============main menu=====================

        main_menu=Label(self.root,bg="#03b3ff",text="Main Menu :-",fg="black",font=("roboto",20,"bold"),anchor="w",padx="40",).place(x=0,y=63,relwidth=1,height=42)

        Add=Button(self.root,text="Add Stock",font=("roboto",14,"bold"),bg="#61c906",fg="white",cursor="hand2",command= lambda : swap(add)).place(x=380,y=69,height=30)

        Delever=Button(self.root,text="Delever Stock",font=("roboto",14,"bold"),bg="#bf0a0a",fg="white",cursor="hand2",command= lambda : swap(delever)).place(x=500,y=69,height=30)

        Details=Button(self.root,text="Details",font=("roboto",18,"bold"),bg="#1602b3",fg="white",cursor="hand2",command= lambda : swap(details)).place(x=655,y=69,height=30,width=100)


    #==================date time=============================

        

        self.clock=Label(self.root,bg="#ffc800",text="Welcome to Inventory Management System \t\t\tDate: dd:MM:YY \t\t\tTime: HH:MM:SS",fg="black",font=("times new roman",15))
        self.clock.place(x=0,y=107,relwidth=1,height=30)

          
        self.update_clock()
    #==================footer===============================

        footer_lbl=Label(self.root,bg="#bf1717",text="Developed by © 2020 zeroGRAVITY for any technical help contact: 8670647386 or www.zerogravity.ml",fg="white",font=("google sans",12)).pack(side="bottom",fill="x")


    #==================add frame =====================================

        add = Frame(self.root,bd="2",relief="groove",bg="#ebdfd0")
        add.place(y=140,relwidth=1,height=628)

        add_title=Label(add,bg="#61c906",text="<<<  ADD ITEMS  >>>",font=("google sans",20,"bold"),fg="white").place(x=0,relwidth=1,height=30)
        
        sno=Label(add,bg="#ebdfd0",text="SERIAL NO:",font=("roboto",16,"bold"),fg="#7d01cf").place(x=20 ,y=50)
        brand_name =Label(add,bg="#ebdfd0",textvariable=self.SNO,fg="red",font=("Consolas",14)).place(x=160,y=50)


        name_brand=Label(add,bg="#ebdfd0",text="BRAND NAME:",font=("roboto",18,"bold"),fg="#7d01cf").place(x=20 ,y=100)
        brand_name = Entry(add,bd="3",textvariable=self.var_brandname,relief="sunken",font=("Consolas",14)).place(x=230,y=100,width=250)

        name_product=Label(add,bg="#ebdfd0",text="PRODUCT NAME:",font=("roboto",18,"bold"),fg="#7d01cf").place(x=20 ,y=200)
        product_name = Entry(add,bd="3",textvariable=self.var_productname,relief="sunken",font=("Consolas",14)).place(x=250,y=200,width=250)

        quantity_product=Label(add,bg="#ebdfd0",text="QUANTITY:",font=("roboto",18,"bold"),fg="#7d01cf").place(x=20 ,y=300)
        product_quantity = Entry(add,bd="3",textvariable=self.var_quantity,relief="sunken",font=("Consolas",14)).place(x=230,y=300,width=250)

        price_product=Label(add,bg="#ebdfd0",text="PRICE:",font=("roboto",18,"bold"),fg="#7d01cf").place(x=20 ,y=400)
        product_price = Entry(add,bd="3",textvariable=self.var_price,relief="sunken",font=("Consolas",14)).place(x=230,y=400,width=250)


        save_btn=Button(add,text="SAVE",command=self.add,bg="GREEN",fg="white",font=("google sans",16,"bold")).place(x=80,y=550)

        update_btn=Button(add,text="UPDATE",command=self.update,bg="#8f8a0d",fg="white",font=("google sans",16,"bold")).place(x=175,y=550)

        delete_btn=Button(add,text="DELETE",command=self.delete,bg="#f50505",fg="white",font=("google sans",16,"bold")).place(x=300,y=550)

        clear_btn=Button(add,text="CLEAR",command=self.clear,bg="#006e65",fg="white",font=("google sans",16,"bold")).place(x=420,y=550)

        #...............searchbox for add ................................................................

        search_frame=Frame(add,bd="2",relief="groove",bg="white")
        search_frame.place(x=550,y=80,height=450,width=300)

        search_label=Label(search_frame,bg="red",text="<< SEARCH >>",font=("google sans",20,"bold"),fg="white").place(x=0,relwidth=1,height=30)

        search_brand=Label(search_frame,bg="white",text="SEARCH BRAND:",font=("google sans",14,"bold"),fg="blue").place(x=60,y=40)

        brand_search = Entry(search_frame,bd="3",textvariable=self.var_searchbrandname,bg="lightyellow",relief="sunken",font=("Consolas",14))
        brand_search.place(x=40,y=80)
        brand_search.bind("<Key>",self.search_brandname)
        
        search_product=Label(search_frame,bg="white",text="SEARCH PRODUCT:",font=("google sans",14,"bold"),fg="blue").place(x=50,y=140)

        product_search = Entry(search_frame,textvariable=self.var_searchproductname,bd="3",bg="lightyellow",relief="sunken",font=("Consolas",14))
        product_search.place(x=40,y=180)
        product_search.bind("<Key>",self.search_productname)

        
        search_date=Label(search_frame,bg="white",text="DATE:",font=("google sans",14,"bold"),fg="blue").place(x=110,y=240)

        date_search = Entry(search_frame,textvariable=self.var_searchdate,bd="3",bg="lightyellow",relief="sunken",font=("Consolas",14))
        date_search.place(x=40,y=280)
        date_search.bind("<Key>",self.search_date)

       
        clear_search=Button(search_frame,command=self.clear_search,text="RESET",bg="green",fg="white",font=("google sans",16,"bold")).place(x=104,y=350)

 

        #...............viewbox for add............................. .........................................



        desc_frame=Frame(add,bd=3,relief="sunken")
        desc_frame.place(x=900,y=30,width=630,height=595)
        
        scrolly=Scrollbar(desc_frame,orient=VERTICAL)
        scrollx=Scrollbar(desc_frame,orient=HORIZONTAL)

        self.producttable=ttk.Treeview(desc_frame,columns=("SNO","Brand_name","Product_Name","Quantity","price","Total","date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.producttable.xview)
        scrolly.config(command=self.producttable.yview)


        self.producttable.heading("SNO",text="Sl.No")
        self.producttable.heading("Brand_name",text="Brand")
        self.producttable.heading("Product_Name",text="Name")
        self.producttable.heading("Quantity",text="Quantity")
        self.producttable.heading("price",text="Price")
        self.producttable.heading("Total",text="Total")
        self.producttable.heading("date",text="Date")

        
        self.producttable["show"]="headings"

        self.producttable.column("SNO",width=50)
        self.producttable.column("Brand_name",width=100)
        self.producttable.column("Product_Name",width=100)
        self.producttable.column("Quantity",width=60)
        self.producttable.column("price",width=70)
        self.producttable.column("Total",width=120)
        self.producttable.column("date",width=100)
        self.producttable.bind("<ButtonRelease-1>",self.show_data)

        

        self.show()
        self.clear()

        
        
        self.producttable.pack(fill=BOTH,expand=1)

    #==================delever frame=====================================

        delever = Frame(self.root,bd="2",relief="groove",bg="#ebdfd0")
        delever.place(y=140,relwidth=1,height=628)

        delever_title=Label(delever,bg="#bf0a0a",text="<<<  DELEVER ITEMS  >>>",font=("google sans",20,"bold"),fg="white").place(x=0,relwidth=1,height=30)

        sno1=Label(delever,bg="#ebdfd0",text="SERIAL NO:",font=("roboto",16,"bold"),fg="#7d01cf").place(x=20 ,y=50)
        brand_name1 =Label(delever,bg="#ebdfd0",textvariable=self.delevery_SNO,fg="red",font=("Consolas",14)).place(x=160,y=50)


        
        name_brand=Label(delever,bg="#ebdfd0",text="BRAND NAME:",font=("roboto",18,"bold"),fg="#7d01cf").place(x=20 ,y=100)
        brand_name = Entry(delever,textvariable=self.var_deleverybrandname,bd="3",relief="sunken",font=("Consolas",14)).place(x=230,y=100,width=250)

        go1_btn=Button(delever,command=self.go_search,text="Go",bg="GREEN",fg="white",font=("google sans",16,"bold")).place(x=490,y=93)

        name_product=Label(delever,bg="#ebdfd0",text="PRODUCT NAME:",font=("roboto",18,"bold"),fg="#7d01cf").place(x=20 ,y=200)
        product_name = Entry(delever,textvariable=self.var_deleveryproductname,bd="3",relief="sunken",font=("Consolas",14)).place(x=250,y=200,width=250)

        go_btn=Button(delever,command=self.go2_search,text="Go",bg="GREEN",fg="white",font=("google sans",16,"bold")).place(x=510,y=193)


        quantity_product=Label(delever,bg="#ebdfd0",text="QUANTITY:",font=("roboto",18,"bold"),fg="#7d01cf").place(x=20 ,y=300)
        product_quantity = Entry(delever,textvariable=self.var_deleveryquantity,bd="3",relief="sunken",font=("Consolas",14)).place(x=230,y=300,width=250)



        current_quantity=Label(delever,bg="#ebdfd0",text="AVAILABLE \nSTOCK:",font=("roboto",16,"bold"),fg="#a80000").place(x=20 ,y=380)
        current_quantity1 = Label(delever,textvariable=self.var_availablequantity,bd="3",relief="sunken",font=("Consolas",14)).place(x=230,y=390,width=250)
        current_price=Label(delever,bg="#ebdfd0",text="BUYING \nPRICE:",font=("roboto",16,"bold"),fg="#a80000").place(x=20 ,y=440)
        current_price1=Label(delever,textvariable=self.var_deleveryprice,bd="3",relief="sunken",font=("Consolas",14)).place(x=230,y=460,width=250)
        

        save_btn=Button(delever,command=self.add_Sales,text="SAVE",bg="GREEN",fg="white",font=("google sans",16,"bold")).place(x=80,y=550)

        update_btn=Button(delever,command=self.update_saleslist,text="UPDATE",bg="#8f8a0d",fg="white",font=("google sans",16,"bold")).place(x=175,y=550)

        delete_btn=Button(delever,command=self.delete1,text="DELETE",bg="#f50505",fg="white",font=("google sans",16,"bold")).place(x=300,y=550)

        clear_btn=Button(delever,command=self.clear1,text="CLEAR",bg="#006e65",fg="white",font=("google sans",16,"bold")).place(x=420,y=550)

        #...............searchbox................................................................

        stock_btn=Button(delever,command= lambda : swap(desc_frame),text="STOCK",bg="GREEN",fg="white",font=("google sans",16,"bold")).place(x=700,y=32)
        sales_btn=Button(delever,command= lambda : swap(desc_frame1),text="SALES",bg="red",fg="white",font=("google sans",16,"bold")).place(x=800,y=32)

        search_frame=Frame(delever,bd="2",relief="groove",bg="white")
        search_frame.place(x=580,y=120,height=450,width=300)

        search_label=Label(search_frame,bg="red",text="<< SEARCH >>",font=("google sans",20,"bold"),fg="white").place(x=0,relwidth=1,height=30)

        search_brand=Label(search_frame,bg="white",text="SEARCH BRAND:",font=("google sans",14,"bold"),fg="blue").place(x=60,y=40)

        brand_search = Entry(search_frame,textvariable=self.var_deleverysearchbrandname,bd="3",bg="lightyellow",relief="sunken",font=("Consolas",14))
        brand_search.place(x=40,y=80)
        brand_search.bind("<Key>",self.search_brandname1)

        
        search_product=Label(search_frame,bg="white",text="SEARCH PRODUCT:",font=("google sans",14,"bold"),fg="blue").place(x=50,y=140)

        product_search = Entry(search_frame,bd="3",textvariable=self.var_deleverysearchproductname,bg="lightyellow",relief="sunken",font=("Consolas",14))
        product_search.place(x=40,y=180)
        product_search.bind("<Key>",self.search_productname1)

        
        search_date=Label(search_frame,bg="white",text="DATE:",font=("google sans",14,"bold"),fg="blue").place(x=110,y=240)

        date_search = Entry(search_frame,textvariable=self.var_deleverysearchdate,bd="3",bg="lightyellow",relief="sunken",font=("Consolas",14))
        date_search.place(x=40,y=280)
        date_search.bind("<Key>",self.search_date1)


        clear_search=Button(search_frame,command=self.clear_search1,text="RESET",bg="green",fg="white",font=("google sans",16,"bold")).place(x=104,y=350)

      

        #...............viewbox................................................................



        desc_frame=Frame(delever,bd=3,relief="sunken")
        desc_frame.place(x=900,y=30,width=630,height=595)
        
        scrolly=Scrollbar(desc_frame,orient=VERTICAL)
        scrollx=Scrollbar(desc_frame,orient=HORIZONTAL)

        self.delevertable=ttk.Treeview(desc_frame,columns=("SNO","Brand_name","Product_Name","Quantity","Cost","Total","Date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.delevertable.xview)
        scrolly.config(command=self.delevertable.yview)

        self.delevertable.heading("SNO",text="SNo")
        self.delevertable.heading("Brand_name",text="Brand")
        self.delevertable.heading("Product_Name",text="Name")
        self.delevertable.heading("Quantity",text="Quantity")
        self.delevertable.heading("Cost",text="Price")
        self.delevertable.heading("Total",text="Total")
        self.delevertable.heading("Date",text="Date")


        
        self.delevertable["show"]="headings"

        self.delevertable.column("SNO",width=50)
        self.delevertable.column("Brand_name",width=100)
        self.delevertable.column("Product_Name",width=100)
        self.delevertable.column("Quantity",width=60)
        self.delevertable.column("Cost",width=70)
        self.delevertable.column("Total",width=120)
        self.delevertable.column("Date",width=100)
        self.delevertable.bind("<ButtonRelease-1>",self.show_quantity)

        self.clear1()
        self.show_delever()

        
        self.delevertable.pack(fill=BOTH,expand=1)
        
#..............................viewbox stocks --------------------------------

        desc_frame1=Frame(delever,bd=3,relief="sunken")
        desc_frame1.place(x=900,y=30,width=630,height=595)
                
        scrolly=Scrollbar(desc_frame1,orient=VERTICAL)
        scrollx=Scrollbar(desc_frame1,orient=HORIZONTAL)

        self.salestable=ttk.Treeview(desc_frame1,columns=("sno","brandname","productname","quantity","price1","sum","date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.salestable.xview)
        scrolly.config(command=self.salestable.yview)

        self.salestable.heading("sno",text="SNo")
        self.salestable.heading("brandname",text="Brand")
        self.salestable.heading("productname",text="Name")
        self.salestable.heading("quantity",text="Quantity")
        self.salestable.heading("price1",text="Price")
        self.salestable.heading("sum",text="Total")
        self.salestable.heading("date",text="Date")


        
        self.salestable["show"]="headings"

        self.salestable.column("sno",width=50)
        self.salestable.column("brandname",width=100)
        self.salestable.column("productname",width=100)
        self.salestable.column("quantity",width=60)
        self.salestable.column("price1",width=70)
        self.salestable.column("sum",width=120)
        self.salestable.column("date",width=100)
        self.salestable.bind("<ButtonRelease-1>",self.show_quantity1)
        

        self.show2()
        

        
        self.salestable.pack(fill=BOTH,expand=1)



    #==================details=====================================

        details = Frame(self.root,bd="2",relief="groove",bg="lightgrey")
        details.place(y=140,relwidth=1,height=628)

        details_title=Label(details,bg="#1602b3",text="<<<  GET DETAILS AREA  >>>",font=("google sans",20,"bold"),fg="white").place(x=0,relwidth=1,height=30)

        brand_product1=Frame(details,bd=3,relief="groov",bg="lightgrey")
        brand_product1.place(x=10,y=40,height=350,width=440)


        Datewise_details=Label(brand_product1,bg="lightgrey",text="Datewise Details:",font=("roboto",20,"bold"),fg="red").place(x=10,y=10)
        Datewise_detail=Label(brand_product1,bg="lightgrey",text="From:",font=("roboto",19,"bold"),fg="black").place(x=18,y=63)
        detailss = Entry(brand_product1,textvariable=self.datefrom,bd="3",relief="sunken",font=("Consolas",14)).place(x=110,y=65,width=250)
        Datewise_detail=Label(brand_product1,bg="lightgrey",text="Upto:",font=("roboto",19,"bold"),fg="black").place(x=28,y=106)
        detailss = Entry(brand_product1,textvariable=self.dateto,bd="3",relief="sunken",font=("Consolas",14)).place(x=110,y=110,width=250)

        get_details=Button(brand_product1,command=self.totals_details,text="Total Stock Details",bg="#fc6b03",font=("gogole sans",16,"bold"),fg="white").place(x=110,y=150,width=250)

        get_details=Button(brand_product1,command=self.currents_details,text="Current Stock Details",bg="#fc6b03",font=("gogole sans",16,"bold"),fg="white").place(x=110,y=195,width=250)

        get_details=Button(brand_product1,command=self.sell_details,text="Total sell Details",bg="#fc6b03",font=("gogole sans",16,"bold"),fg="white").place(x=110,y=242,width=250)
        
        print_details1=Button(brand_product1,command=self.download_excel,text="Generate Excel",bg="green",font=("gogole sans",16,"bold"),fg="white").place(x=110,y=289,width=250)


        brand_product=Frame(details,bd=3,relief="groov",bg="lightgrey")
        brand_product.place(x=450,y=40,height=350,width=440)

        Datewise_details=Label(brand_product,bg="lightgrey",text="Brand or Product Details:",font=("roboto",20,"bold"),fg="red").place(x=10,y=10)

        Datewise_detail=Label(brand_product,bg="lightgrey",text="Brand:",font=("roboto",19,"bold"),fg="black").place(x=18,y=63)
        detailss = Entry(brand_product,textvariable=self.brandnamed,bd="3",relief="sunken",font=("Consolas",14)).place(x=110,y=65,width=250)
        Datewise_detail=Label(brand_product,bg="lightgrey",text="Product:",font=("roboto",18,"bold"),fg="black").place(x=18,y=106)
        detailss = Entry(brand_product,textvariable=self.productnamed,bd="3",relief="sunken",font=("Consolas",14)).place(x=132,y=110,width=250)

        get_details=Button(brand_product,command=self.borp_alllist,text="Total Stock Details",bg="#fc6b03",font=("gogole sans",16,"bold"),fg="white").place(x=110,y=150,width=250)

        get_details=Button(brand_product,command=self.borp_stocklist,text="Current Stock Details",bg="#fc6b03",font=("gogole sans",16,"bold"),fg="white").place(x=110,y=195,width=250)

        get_details=Button(brand_product,command=self.borp_saleslist,text="Total sell Details",bg="#fc6b03",font=("gogole sans",16,"bold"),fg="white").place(x=110,y=242,width=250)
        
        print_details1=Button(brand_product,command=self.download_excel,text="Generate Excel",bg="green",font=("gogole sans",16,"bold"),fg="white").place(x=110,y=289,width=250)


        monthly_info=Frame(details,bd=3,relief="groov",bg="lightgrey")
        monthly_info.place(x=10,y=390,height=230,width=440)
        Datewise_details=Label(monthly_info,bg="blue",text="< Monthly Summary >",font=("roboto",16,"bold"),fg="white").place(x=0,height=25,relwidth=1)

        monthly_sale=Label(monthly_info,bg="lightgrey",text="TOTAL SALE:",fg="red",font=("roboto",14,"bold")).place(x=10,y=28)

        prev_month=Label(monthly_info,bg="lightgrey",text="Previuos Month:",fg="black",font=("roboto",14)).place(x=10,y=60)
        prev_month1=Label(monthly_info,bg="lightyellow",textvariable=self.var_prevmt,bd="2",relief="sunken",font=("Consolas",13)).place(x=155,y=61,width=260)

        this_month=Label(monthly_info,bg="lightgrey",text="Current Month:",fg="black",font=("roboto",14)).place(x=22,y=95)
        prev_month1=Label(monthly_info,bg="lightyellow",textvariable=self.var_thismt,bd="2",relief="sunken",font=("Consolas",13)).place(x=155,y=97,width=260)

        stastus=Label(monthly_info,bg="lightgrey",text="MONTHLY STASTUS:",fg="red",font=("roboto",14,"bold")).place(x=10,y=134)

        this_month=Label(monthly_info,bg="lightgrey",text="Percentage(%) compared to previous month:",fg="black",font=("roboto",13)).place(x=10,y=165)
        this_month=Label(monthly_info,bg="lightyellow",textvariable=self.var_percentage,bd="2",relief="sunken",font=("Consolas",13)).place(x=345,y=166,width=80)


        monthly_info1=Frame(details,bd=3,relief="groov",bg="lightgrey")
        monthly_info1.place(x=450,y=390,height=230,width=440)

        Datewise_details=Label(monthly_info1,bg="blue",text="< Current Month Summary >",font=("roboto",16,"bold"),fg="white").place(x=0,height=25,relwidth=1)

        monthly_sale=Label(monthly_info1,bg="lightgrey",text="TOTAL SALE:",fg="red",font=("roboto",13,"bold")).place(x=10,y=33)
        prev_month1=Label(monthly_info1,bg="lightyellow",textvariable=self.var_thismt,bd="2",relief="sunken",font=("Consolas",13)).place(x=130,y=33,width=295)
        monthly_sale=Label(monthly_info1,bg="lightgrey",text="Click here to refresh →",fg="blue",font=("roboto",13,"bold")).place(x=143,y=66)

        btn_Ref=Button(monthly_info1,cursor="hand2",command=self.thism_sell,text="Refresh",bg="green",font=("gogole sans",12,"bold"),fg="white").place(x=348,y=63)

        Thankyou=Label(monthly_info1,bg="black").place(x=0,y=110,height=2,relwidth=1)

        Thankyou=Label(monthly_info1,bg="lightgrey",text="Thanks for using!!",fg="#ff4c24",font=("roboto",30,"bold")).place(x=40,y=140)



#...........................................details treeview box.............................................
        desc_frame2=Frame(details,bd=3,relief="sunken")
        desc_frame2.place(x=900,y=30,width=630,height=595)
                
        scrolly=Scrollbar(desc_frame2,orient=VERTICAL)
        scrollx=Scrollbar(desc_frame2,orient=HORIZONTAL)

        self.detailstable=ttk.Treeview(desc_frame2,columns=("sno","brandname","productname","quantity","price1","sum","date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.detailstable.xview)
        scrolly.config(command=self.detailstable.yview)

        self.detailstable.heading("sno",text="SNo")
        self.detailstable.heading("brandname",text="Brand")
        self.detailstable.heading("productname",text="Name")
        self.detailstable.heading("quantity",text="Quantity")
        self.detailstable.heading("price1",text="Price")
        self.detailstable.heading("sum",text="Total")
        self.detailstable.heading("date",text="Date")


        
        self.detailstable["show"]="headings"

        self.detailstable.column("sno",width=50)
        self.detailstable.column("brandname",width=100)
        self.detailstable.column("productname",width=100)
        self.detailstable.column("quantity",width=60)
        self.detailstable.column("price1",width=70)
        self.detailstable.column("sum",width=120)
        self.detailstable.column("date",width=100)

        self.detailstable.pack(fill=BOTH,expand=1)



    #==================frame swaping===================

        def swap(frame):
            frame.tkraise()
        
        add.tkraise()


#=====================================================================================================
# 
# .......................add products function..........................................
 
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
                if self.var_productname.get()=="" or self.var_quantity.get()=="" or self.var_price.get()=="":
                    messagebox.showerror("Error","Enter all details.",parent=self.root)

                

                else:
                        self.total()
                        cur.execute("Insert into delever_products(Brand_name,Product_Name,Quantity,Cost,Total,Date) values(?,?,?,?,?,?)",( #database_temp
                                    
                                    self.var_brandname.get(),
                                    self.var_productname.get(),
                                    self.var_quantity.get(),
                                    self.var_price.get(),
                                    self.var_total.get(),
                                    self.today.strftime("%d/%m/%Y")
                                    

                         ))

                        cur.execute("Insert into all_products(Brand_name,Product_Name,Quantity,price,Total,date) values(?,?,?,?,?,?)",( #databse_final
                                    
                                    self.var_brandname.get(),
                                    self.var_productname.get(),
                                    self.var_quantity.get(),
                                    self.var_price.get(),
                                    self.var_total.get(),
                                    self.today.strftime("%Y-%m-%d")
                                    

                            ))
                        con.commit()
                        messagebox.showinfo("Success","Details added Successfully.",parent=self.root)
                        self.show()
                        self.show1()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

#...........................show function for add...........................................


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from all_products")
            rows=cur.fetchall()
            self.producttable.delete(*self.producttable.get_children())
            for row in rows:
                self.producttable.insert('',END,value=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

#.............................show in table viewbox function for add..........................................

    def show_data(self,ev):
        f=self.producttable.focus()
        content=(self.producttable.item(f))
        row=content['values']
        self.SNO.set(row[0])
        self.var_brandname.set(row[1])
        self.var_productname.set(row[2])
        self.var_quantity.set(row[3])
        self.var_price.set(row[4])
        

#.............................update function for add..........................................



    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_productname.get()=="":
                messagebox.showerror("Error","Enter a valid product name.",parent=self.root)

            else:
                cur.execute("Select * from all_products where SNO=?",(self.SNO.get(),))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Invalid details!",parent=self.root)
                
                else:
                    self.total()

                    cur.execute("Select * from delever_products where SNO=?",(self.SNO.get(),))
                    row=cur.fetchone()
                    self.productquantity_now.set(row[3])
                    cur.execute("Select * from all_products where SNO=?",(self.SNO.get(),))
                    row1=cur.fetchone()
                    self.productquantity_now1.set(row1[3])
                    self.quantity_update()
                    cur.execute("Update delever_products set Brand_name=?,Quantity=?,Cost=?,Total=? where SNO=?",( 
                                
                                self.var_brandname.get(),
                                self.productquantity_now1.get(),
                                self.var_price.get(),
                                (float(self.productquantity_now1.get(),)*float(self.var_price.get(),)),
                                self.SNO.get(),
                                
                                ))
                    con.commit()

                    cur.execute("Update all_products set Brand_name=?,Quantity=?,price=?,Total=? where SNO=?",( 
                                
                                self.var_brandname.get(),
                                self.var_quantity.get(),
                                self.var_price.get(),
                                self.var_total.get(),
                                self.SNO.get(),
                                
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Record added Successfully.",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def quantity_update(self):#.............
        sum5 = int(self.productquantity_now1.get(),) - int(self.var_quantity.get(),)
        self.var_finalquantitynow.set(sum5)
        sum5 = int(self.productquantity_now.get(),) - int(self.var_finalquantitynow.get(),)
        self.productquantity_now1.set(sum5)

#>.........................delete function for add........................................

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_productname.get()==" ":
                messagebox.showerror("Error","Enter a valid product name.",parent=self.root)

            else:
                cur.execute("Select * from all_products where Product_Name=?",(self.var_productname.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error","Invalid Product name.",parent=self.root)
                
                else:
                    op=messagebox.askyesno("Confrim","Are you sure ?")
                    if op==True:
                        cur.execute("delete from delever_products where SNO=?",(self.SNO.get(),))

                        cur.execute("delete from all_products where SNO=?",(self.SNO.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Record deleted Successfully.",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

#.........................clear for add.......................................
    
    def clear(self):
        self.SNO.set("")
        self.var_brandname.set("")
        self.var_productname.set("")
        self.var_quantity.set("")
        self.var_price.set("")
        self.var_total.set("")
        self.show()
    
#.............................search function for add..............................

    def search_brandname(self,ev):#.............. brand name search
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                
                    cur.execute("Select * from all_products where Brand_name=?",(self.var_searchbrandname.get(),))
                    row=cur.fetchall()
                    if len(row)>0:
                        self.producttable.delete(*self.producttable.get_children())
                        for i in row:
                            self.producttable.insert('',END,values=i)
                    else:
                        
                        self.producttable.delete(*self.producttable.get_children())

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
           
    def search_productname(self,ev):#............. product search
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Select * from all_products where Product_Name=?",(self.var_searchproductname.get(),))
                row=cur.fetchall()
                if len(row)>0:
                    self.producttable.delete(*self.producttable.get_children())
                    for i in row:
                        self.producttable.insert('',END,values=i)
                else:
                    self.producttable.delete(*self.producttable.get_children())
                    

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)      
    
    def search_date(self,ev):# ...............date search
            
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Select * from all_products where date=?",(str(self.var_searchdate.get()),))
                row=cur.fetchall()
                if len(row)>0:
                    self.producttable.delete(*self.producttable.get_children())
                    for i in row:
                        self.producttable.insert('',END,values=i)
                else:
                    self.producttable.delete(*self.producttable.get_children())
                    

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def clear_search(self):#....................... clear search
        self.var_searchbrandname.set("")
        self.var_searchproductname.set("")
        self.var_searchdate.set("")
        self.show()
    

    def update_clock(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%Y-%m-%d")
        self.clock.config(text=f"Welcome to Stock Management System \t\t\tDate: {str(date_)}  \t\t\tTime: {str(time_)}")
        self.clock.after(200,self.update_clock)

 #================================total calculate===========================

    def total(self):
        res = float(self.var_quantity.get(),)*float(self.var_price.get(),)
        self.var_total.set(res)


#===========================show for delever ================================

    def show_delever(self):#------------tree view for stocks
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * from delever_products")
            rows=cur.fetchall()
            self.delevertable.delete(*self.delevertable.get_children())
            for row in rows:
                self.delevertable.insert('',END,value=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

#............................(go search)find brand and product in delever...............................
    
    def go_search(self):#.............. brand name search
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                
                    cur.execute("Select * from delever_products where Brand_name=?",(self.var_deleverybrandname.get(),))
                    row=cur.fetchall()
                    if len(row)>0:
                        self.delevertable.delete(*self.delevertable.get_children())
                        for i in row:
                            self.delevertable.insert('',END,values=i)
                    else:
                        messagebox.showerror("Error","No Results Found",parent=self.root)
                        self.delevertable.delete(*self.delevertable.get_children())

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    
    def go2_search(self):#.............. product name search
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                
                    cur.execute("Select * from delever_products where Product_name=?",(self.var_deleveryproductname.get(),))
                    row=cur.fetchall()
                    if len(row)>0:
                        self.delevertable.delete(*self.delevertable.get_children())
                        for i in row:
                            self.delevertable.insert('',END,values=i)
                        
                    else:
                        messagebox.showerror("Error","No Results Found",parent=self.root)
                        self.delevertable.delete(*self.delevertable.get_children())

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def show_quantity(self,ev):#.............for delevery stock
        f=self.delevertable.focus()
        content=(self.delevertable.item(f))
        row=content['values']
        self.delevery_SNO.set(row[0])
        self.var_deleverybrandname.set(row[1])
        self.var_deleveryproductname.set(row[2])
        self.var_availablequantity.set(row[3])
        self.var_deleveryprice.set(row[4])
       

    def show1(self):#..............show for delever
       
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from delever_products")
            rows=cur.fetchall()
            self.delevertable.delete(*self.delevertable.get_children())
            for row in rows:
                self.delevertable.insert('',END,value=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def clear1(self):#..............clear for delever
        self.delevery_SNO.set("")
        self.var_deleverybrandname.set("")
        self.var_deleveryproductname.set("")
        self.var_deleveryquantity.set("")
        self.var_deleveryprice.set("")
        self.var_availablequantity.set("")
        self.show1()
    
    def clear2(self):#..............clear for delever
        self.delevery_SNO.set("")
        self.var_deleverybrandname.set("")
        self.var_deleveryproductname.set("")
        self.var_deleveryquantity.set("")
        self.var_deleveryprice.set("")
        self.var_availablequantity.set("")
        self.show2()

    def show2(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from sales_list")
            rows=cur.fetchall()
            self.salestable.delete(*self.salestable.get_children())
            for row in rows:
                self.salestable.insert('',END,value=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to2: {str(ex)}",parent=self.root)
    
    def add_Sales(self):#...........sales add function
        self.update_quantity()
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_finalquantity.get()<0 :
                messagebox.showerror("Warning!","Not enough quantity in stock!",parent=self.root)

            else:
                if self.var_deleverybrandname.get()=="" and self.var_deleveryproductname.get()=="" and self.var_deleveryquantity.get()=="":
                    messagebox.showerror("Error","Enter all details.",parent=self.root)

                else:
                        self.sales_total()
                        self.update_quantity()
                        cur.execute("Insert into sales_list(brandname,productname,quantity,price1,sum,date,dsno) values(?,?,?,?,?,?,?)",( #databse_sales
                                    
                                    self.var_deleverybrandname.get(),
                                    self.var_deleveryproductname.get(),
                                    self.var_deleveryquantity.get(),
                                    self.var_deleveryprice.get(),
                                    self.var_deleverytotal.get(),
                                    self.today.strftime("%Y-%m-%d"),
                                    self.delevery_SNO.get(),

                                    
                            ))
                        con.commit()
                        self.update_quantity()
                        self.new_total()
                        cur.execute("Update delever_products set Quantity=?,Total=? where SNO=?",( 

                                    self.var_finalquantity.get(),
                                    self.var_gtotal.get(),
                                    self.delevery_SNO.get(),

                            ))
                        con.commit()
                        messagebox.showinfo("Success","Details added Successfully.",parent=self.root)
                        self.clear1()
                        self.show()
                        self.clear2()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def sales_total(self):
            res = float(self.var_deleveryquantity.get(),)*float(self.var_deleveryprice.get(),)
            self.var_deleverytotal.set(res)

    def new_total(self):
        res_ = float(self.var_finalquantity.get(),)*float(self.var_deleveryprice.get(),)
        self.var_gtotal.set(res_)
        
    


    def show_quantity1(self,ev):#.............for delevery
        f=self.salestable.focus()
        content=(self.salestable.item(f))
        row=content['values']
        self.delevery_SNO.set(row[0])
        self.var_deleverybrandname.set(row[1])
        self.var_deleveryproductname.set(row[2])
        self.var_deleveryquantity.set(row[3])
        self.var_deleveryprice.set(row[4])


    def delete1(self):#.............DELETE FOR SALES
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_deleveryproductname.get()=="":
                messagebox.showerror("Error","Enter a valid product name.",parent=self.root)

            else:
                cur.execute("Select * from sales_list where sno=?",(self.delevery_SNO.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error","Invalid Product name.",parent=self.root)
                
                else:
                    op=messagebox.askyesno("Confrim","Are you sure ?")
                    if op==True:
                        
                        cur.execute("delete from sales_list where sno=?",(self.delevery_SNO.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Record deleted Successfully.",parent=self.root)
                        self.clear2()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def update_quantity(self):#..............calculate availability and updating quantity
        sum_ = int(self.var_availablequantity.get(),) - int(self.var_deleveryquantity.get(),)
        self.var_finalquantity.set(sum_)

       
    
    def update_saleslist(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_deleveryproductname.get()=="":
                messagebox.showerror("Error","Enter a valid product name.",parent=self.root)

            else:
                cur.execute("Select * from sales_list where SNO=?",(self.delevery_SNO.get(),))
                row=cur.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Invalid details!",parent=self.root)
                
                else:
                    cur.execute("Select * from sales_list where sno=?",(self.delevery_SNO.get(),))
                    row1=cur.fetchone()
                    self.deleveryproductquantity_now1.set(row1[3])
                    self.delevery_SNO1.set(row1[7])
                    
                    

                    cur.execute("Select * from delever_products where SNO=?",(self.delevery_SNO1.get(),))
                    row=cur.fetchone()

                    self.deleveryproductquantity_now2.set(row[3])
                    

                    
                    

                    self.update_quantity1()
                    self.total3()
                    cur.execute("Update sales_list set Quantity=?,sum=? where sno=?",( 
                                
                                self.var_deleveryquantity.get(),
                                self.var_total1.get(),
                                self.delevery_SNO.get(),
                                
                                ))
                    
                    
                    self.total2()
                    cur.execute("Update delever_products set Quantity=?,Cost=?,Total=? where SNO=?",( 
                                
                                self.deleveryproductquantity_now1.get(),
                                self.var_deleveryprice.get(),
                                self.var_total.get(),
                                self.delevery_SNO1.get(),
                                
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Record added Successfully.",parent=self.root)
                    self.clear1()
                    self.clear2()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def update_quantity1(self):
        sum4 = int(self.deleveryproductquantity_now1.get(),) - int(self.var_deleveryquantity.get(),)
        self.var_finalquantitynow1.set(sum4)
        sum5 = int(self.deleveryproductquantity_now2.get(),) + int(self.var_finalquantitynow1.get(),)
        self.deleveryproductquantity_now1.set(sum5)

    def total3(self):
        
        res1 = float(self.var_deleveryquantity.get(),)*float(self.var_deleveryprice.get(),)
        self.var_total1.set(res1)
        print(res1)
        
    def total2(self):
        res2 = float(self.deleveryproductquantity_now1.get(),)*float(self.var_deleveryprice.get(),)
        self.var_total.set(res2)
        print(res2)
        
#==========================================end delever table functions=========================================


#.............................search function for add..............................

    def search_brandname1(self,ev):#.............. brand name search
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                
                    cur.execute("Select * from sales_list where brandname=?",(self.var_deleverysearchbrandname.get(),))
                    row=cur.fetchall()
                    if len(row)>0:
                        self.salestable.delete(*self.salestable.get_children())
                        for i in row:
                            self.salestable.insert('',END,values=i)
                    else:
                        
                        self.salestable.delete(*self.salestable.get_children())

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
           
    def search_productname1(self,ev):#............. product search
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Select * from sales_list where productname=?",(self.var_deleverysearchproductname.get(),))
                row=cur.fetchall()
                if len(row)>0:
                    self.salestable.delete(*self.salestable.get_children())
                    for i in row:
                        self.salestable.insert('',END,values=i)
                else:
                    self.salestable.delete(*self.salestable.get_children())
                    

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)      
    
    def search_date1(self,ev):# ...............date search
            
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Select * from sales_list where date=?",(str(self.var_deleverysearchdate.get()),))
                row=cur.fetchall()
                if len(row)>0:
                    self.salestable.delete(*self.salestable.get_children())
                    for i in row:
                        self.salestable.insert('',END,values=i)
                else:
                    self.salestable.delete(*self.salestable.get_children())
                    

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear_search1(self):#....................... clear search
        self.var_deleverysearchbrandname.set("")
        self.var_deleverysearchproductname.set("")
        self.var_deleverysearchdate.set("")
        self.show2()

    def create_db(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        cur=con.execute("CREATE TABLE IF NOT EXISTS all_products(SNO INTEGER PRIMARY KEY AUTOINCREMENT,Brand_name TEXT,Product_Name TEXT,Quantity INTEGER,price REAL,Total REAL,date INTEGER)")
        con.commit()

        cur=con.execute("CREATE TABLE IF NOT EXISTS delever_products(SNO INTEGER PRIMARY KEY AUTOINCREMENT,Brand_name TEXT,Product_Name TEXT,Quantity INTEGER,Cost REAL,Total REAL,Date INTEGER)")
        con.commit()

        cur=con.execute("CREATE TABLE IF NOT EXISTS sales_list(sno INTEGER PRIMARY KEY AUTOINCREMENT,brandname TEXT,productname TEXT,quantity INTEGER,price1 REAL,sum REAL,date INTEGER,dsno INTEGER)")
        con.commit()

#==============================================details functions==============================================


    def totals_details(self):#.............all product details
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from all_products where date>='" +self.datefrom.get()+ "' and date<='" +self.dateto.get()+ "'")
                rows=cur.fetchall()
                global rowss
                rowss=rows
                self.detailstable.delete(*self.detailstable.get_children())
                for row in rows:
                    self.detailstable.insert('',END,value=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def currents_details(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from delever_products where date>='" +self.datefrom.get()+ "' and date<='" +self.dateto.get()+ "'")
                rows=cur.fetchall()
                global rowss
                rowss=rows
                self.detailstable.delete(*self.detailstable.get_children())
                for row in rows:
                    self.detailstable.insert('',END,value=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def sell_details(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from sales_list where date>='" +self.datefrom.get()+ "' and date<='" +self.dateto.get()+ "'")
                rows=cur.fetchall()
                global rowss
                rowss=rows
                self.detailstable.delete(*self.detailstable.get_children())
                for row in rows:
                    self.detailstable.insert('',END,value=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def download_excel(self):#.............generate excel file name
        if len(rowss)<1:
            messagebox.showerror("Error",f"No data available to export",parent=self.root)
            return False

        fln= filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save File", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
        with open(fln, mode='w') as myfile:
            exp_writer = csv.writer(myfile, delimiter=",")
            
            for row in rowss:
                exp_writer.writerow(row)

        messagebox.showinfo("File Saved", "File saved to "+os.path.basename(fln)+" successfully.")



    def borp_alllist(self):#.............all product details
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from all_products where Brand_name=? OR Product_Name=?",(
                                self.brandnamed.get(),
                                self.productnamed.get(),
                ))
                rows=cur.fetchall()
                global rowss
                rowss=rows
                self.detailstable.delete(*self.detailstable.get_children())
                for row in rows:
                    self.detailstable.insert('',END,value=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def borp_stocklist(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from delever_products where Brand_name=? OR Product_Name=?",(
                                self.brandnamed.get(),
                                self.productnamed.get(),
                ))
                rows=cur.fetchall()
                global rowss
                rowss=rows
                self.detailstable.delete(*self.detailstable.get_children())
                for row in rows:
                    self.detailstable.insert('',END,value=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def borp_saleslist(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("select * from sales_list where brandname=? OR productname=?",(
                                self.brandnamed.get(),
                                self.productnamed.get(),
                ))
                rows=cur.fetchall()
                global rowss
                rowss=rows
                self.detailstable.delete(*self.detailstable.get_children())
                for row in rows:
                    self.detailstable.insert('',END,value=row)

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def previousm_sell(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
                cur.execute("select sum from sales_list where date>='" +self.firstdayofMonth.strftime("%Y-%m-%d")+ "' and date<='" +self.lastdayofMonth.strftime("%Y-%m-%d")+ "'")
                rows=cur.fetchall()
                global prevtotal
                prevtotal=(float(sum(list(map(sum, list(rows))))))
                print(prevtotal)
                self.var_prevmt.set(prevtotal)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def thism_sell(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
                cur.execute("select sum from sales_list where date>='" +self.lastdayofMonth.strftime("%Y-%m-%d")+ "' and date<='" +self.today.strftime("%Y-%m-%d")+ "'")
                rows=cur.fetchall()
                global prevtotal
                prevtotal=(float(sum(list(map(sum, list(rows))))))
                print(prevtotal)
                self.var_thismt.set(prevtotal)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def percentage(self):

        percentage=((float(self.var_thismt.get())- (float(self.var_prevmt.get()))))/float(self.var_prevmt.get())
        percent=(percentage*10)
        self.var_percentage.set(round (percent,3))



root = Tk()
obj=ims(root)
root.resizable(True,True)
root.mainloop()