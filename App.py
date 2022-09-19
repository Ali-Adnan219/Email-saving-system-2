import flet
from flet import (ElevatedButton, Text,Markdown,Theme, Container,theme,TextField ,colors,TextButton, padding,PopupMenuButton, PopupMenuItem,Row,icons,Icon ,Column, border_radius,alignment)
import pandas as pd
from pytablewriter import MarkdownTableWriter
from prettytable import PrettyTable
from datetime import date
from datetime import datetime
import backend
import MakePdf





def main(page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
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
        page.add(Row([savepdfs,ElevatedButton("الرجوع الى قائمه الرئيسية", on_click=backmain,width=200,height=50)],alignment="center"))
        page.add(
        Markdown(
           main1(),
            extension_set="gitHubWeb",
            expand=True,
            selectable=True
            
            
        ))


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
        page.add( Column([ElevatedButton("مرحبا بكم في نظام حفظ الحسابات اختر احدي الخيارات",width=500,height=100,),],width=500,height=100,alignment="center",spacing=42,),Row([bat1,bat2,bat3] ,alignment="center",spacing=40,) )


    backmain("e")
    #page save data
    txt1=TextField(label="البريد",width=300,height=100  ,multiline=True,text_align='center',text_size=20  ,border_radius=border_radius.all(5))
    txt2=TextField(label="الرمز",width=300,height=100  ,multiline=True,text_align='center',text_size=20 , )
    txt3= TextField(label="النوع",width=300,height=100  ,multiline=True,text_align='center',text_size=20 )
    txt4= TextField(label="الملاحظات",width=300,height=100  ,multiline=True,text_align='center',text_size=20 )
    txt_name4 = Row([txt1,txt2,txt3,txt4  ])

    savedata=ElevatedButton("حفظ بيانات", on_click=get_data_fro_input  ,width=170,height=120,)
    hudedata=ElevatedButton("الرجوع الى قائمه الرئيسية", on_click=backmain  ,width=200,height=120,)
    #del data page
    deldata=TextField(label="ادخل ايدي",width=300,height=100  ,multiline=True,text_align='center',text_size=20  ,border_radius=border_radius.all(5))
    delsdata=ElevatedButton("مسح", on_click=del_data  ,width=170,height=100,)
    hadedel=ElevatedButton("الرجوع الى قائمه الرئيسية", on_click=backmain  ,width=200,height=100,)
    chukdel=ElevatedButton(" تم مسح ايدي  ", on_click=backmain  ,width=200,height=50,)
    chukِAdd=ElevatedButton(" تم اضافة الحساب بنجاح اضغط للذهاب للجدول و التحقق", on_click=btn_click  ,width=400,height=50,)
    savepdfs=ElevatedButton("pdf طباعة جدول", on_click=MakePdf.savepdf()  ,width=200,height=50,)

#Run
flet.app(target=main)