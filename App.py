import flet
from flet import (ElevatedButton, Text,Markdown,Theme, Container,theme,TextField ,colors,TextButton, padding,PopupMenuButton, PopupMenuItem,Row,icons,Icon ,Column, border_radius,alignment)
import pandas as pd
from pytablewriter import MarkdownTableWriter
from prettytable import PrettyTable
from datetime import date
from datetime import datetime
import backend
import MakePdf
import os





def main(page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "dark"
    page.title = "برنامج حفظ الحسابات"
    def get_data_fro_input(e):
        #save data in sqlit3 file
        now =datetime.now()
        backend.insert(txt1.value,txt2.value,txt3.value,txt4.value, now.strftime("%d/%m/%Y %H:%M:%S"))
        page.add(chukِAdd)


    def showdel(e):
        #show page del data
        page.clean()
        page.add(deldata,delsdata,hadedel)


    def del_data(e):

        #del data by id
        chukdel=ElevatedButton(deldata.value+": تم مسح ايدي  ", on_click=backmain  ,width=200,height=50,)
        page.add(chukdel)
        backend.deleteitem(deldata.value)
    def del_by_numbers(e):
        for number in range(int(del_from_number.value),int(del_to_number.value)):
            backend.deleteitem(number)
    def del_all_data(e):
        os.remove("./mydata.db")
        page.clean()
        page.add(Row([ElevatedButton("تم مسح كل بيانات و الان اخرج من برنامج و شغله مره اخرى", on_click=backmain,width=400,height=80)],alignment="center"))
    def btn_click(e):
        #table data show
        page.clean()
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.title =  "برنامج حفظ الحسابات"
        page.theme = Theme(font_family="Kanit")
        def main1():
            writer = MarkdownTableWriter(
            #table_name="جدول بيانات",
            headers=["id","الايميل", "الرمز", "النوع","الملاحظات","تاريخ الاضافه"],
            value_matrix=backend.View(),
            )
            return writer.dumps()
        number_all_table=0
        for xn in backend.View():
            number_all_table+=1
        #print(number_all_table)
        page.add(Row([ElevatedButton(str(number_all_table)+" : عدد البريد المحفوظ",width=200,height=50),savepdfs,ElevatedButton("الرجوع الى قائمه الرئيسية", on_click=backmain,width=200,height=50),del_all_table,del_one_table],alignment="center"))
        page.add(Row([del_to_number,del_from_number,del_all_bynumber],alignment="center"))
        page.add(
        Markdown(
           main1(),
            extension_set="gitHubWeb",
            expand=True,
            selectable=True,
            
            
            
        ))

    def save_pdf(e):
        MakePdf.savepdfs()
    def input_data(e):
        #page input data
        page.clean()
        page.add(txt_name4,savedata,hudedata)
    def backmain(e):
        #home page
        page.clean()
        page.theme = Theme(font_family="Kanit")
        bat1=ElevatedButton("جدول البيانات المحفوضه", on_click=btn_click  ,width=200,height=120)
        bat2=ElevatedButton("اضافة بيانات جديده", on_click=input_data  ,width=200,height=120,)
        bat3=ElevatedButton("مسح البيانات", on_click=showdel  ,width=200,height=120,)
        page.add( Row([ElevatedButton("مرحبا بكم في نظام حفظ الحسابات اختر احدي الخيارات",width=500,height=100,),],width=500,height=100,alignment="center",spacing=42,),Row([bat1,bat2,bat3] ,alignment="center",spacing=40,) )


    backmain("e")
    #page save data
    txt1=TextField(label="البريد",width=300,height=100  ,multiline=True,text_align='center',text_size=20  ,border_radius=border_radius.all(5))
    txt2=TextField(label="الرمز",width=300,height=100  ,multiline=True,text_align='center',text_size=20 , )
    txt3= TextField(label="النوع",width=300,height=100  ,multiline=True,text_align='center',text_size=20 )
    txt4= TextField(label="الملاحظات",width=300,height=100  ,multiline=True,text_align='center',text_size=20 )
    txt_name4 = Column([txt1,txt2,txt3,txt4  ],alignment="center")

    savedata=ElevatedButton("حفظ بيانات", on_click=get_data_fro_input  ,width=200,height=50,)
    hudedata=ElevatedButton("الرجوع الى قائمه الرئيسية", on_click=backmain  ,width=200,height=50,)
    #del data page
    deldata=TextField(label="ادخل ايدي",width=300,height=80  ,multiline=True,text_align='center',text_size=20  ,)
    delsdata=ElevatedButton("مسح", on_click=del_data  ,width=200,height=50,)
    hadedel=ElevatedButton("الرجوع الى قائمه الرئيسية", on_click=backmain  ,width=200,height=50,)
    chukdel=ElevatedButton(" تم مسح ايدي  ", on_click=backmain  ,width=200,height=50,)
    chukِAdd=ElevatedButton(" تم اضافة الحساب بنجاح اضغط للذهاب للجدول و التحقق", on_click=btn_click  ,width=400,height=50,)
    savepdfs=ElevatedButton("pdf طباعة كامل جدول", on_click=save_pdf,width=200,height=50,)
    del_all_table=ElevatedButton("حذف كل البيانات"  ,on_click=del_all_data,width=200,height=50,)
    del_one_table=ElevatedButton("حذف  بريد واحد"  ,on_click=showdel,width=200,height=50,)
    del_from_number=TextField(label="حذف من رقم ",width=200,height=60  ,multiline=True,text_align='center',text_size=16  ,)
    del_to_number=TextField(label="حذف الى رقم ",width=200,height=60 ,multiline=True,text_align='center',text_size=16  ,)
    del_all_bynumber=ElevatedButton("حذف بيانات محدده"  ,on_click=del_by_numbers,width=200,height=50,)
#Run
flet.app(target=main)