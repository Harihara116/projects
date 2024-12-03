from tkinter import *
top = Tk()
top.configure(bg='red')
top.geometry('1350x800')
top.title('billing software')
l = Label(top, text='BILLING SOFTWARE', bg='orange', width=700, height=1, font=("Times New Roman", 20), borderwidth=5,
          relief='sunken')
l.pack(padx=50, pady=10)

# customer detail
top.e1 = StringVar()
top.e2 = StringVar()
top.e3 = StringVar()

# cosmetics
top.e4 = IntVar()
top.e5 = IntVar()
top.e6 = IntVar()
top.e7 = IntVar()
top.e8 = IntVar()

# grocery
top.e9 = IntVar()
top.e10 = IntVar()
top.e11 = IntVar()
top.e12 = IntVar()
top.e13 = IntVar()

# others
top.e14 = IntVar()
top.e15 = IntVar()
top.e16 = IntVar()
top.e17 = IntVar()
top.e18 = IntVar()

# bill menu
top.e19 = StringVar()
top.e20 = StringVar()
top.e21 = StringVar()
top.e22 = StringVar()
top.e23 = StringVar()
top.e24 = StringVar()

# customer detail
lf = LabelFrame(top, text='customer detail', bg='orange', bd=7, width=1250, height=75).place(x=50, y=55)
cname = Label(top, text='CustomerName:', bg='orange', font=('Times New Roman', 11)).place(x=57, y=90)
e1 = Entry(top, width=30, textvariable=top.e1, font=('arial', 11), borderwidth=5, relief='sunken').place(x=160, y=87)
cphn = Label(top, text='CustomerPhoneNo:', bg='orange', font=('Times New Roman', 11)).place(x=430, y=90)
e2 = Entry(top, width=30, textvariable=top.e2, font=('arial', 11), borderwidth=5, relief='sunken').place(x=555, y=87)
billno = Label(top, text='BillNo:', bg='orange', font=('Times New Roman', 11)).place(x=820, y=90)
e3 = Entry(top, width=30, textvariable=top.e3, font=('arial', 11), borderwidth=5, relief='sunken').place(x=870, y=87)
b = Button(top, text='Enter', bg='brown', fg='white', width=10, height=1).place(x=1170, y=85)

# cosmetics
lf1 = LabelFrame(top, text='Cosmetics', bg='orange', bd=7, width=300, height=400).place(x=50, y=130)
bathsoap = Label(top, text='Bath Soap:', bg='orange', font=('Times New Roman', 11)).place(x=65, y=170)
e4 = Entry(top, width=10, textvariable=top.e4, font=('arial', 19), borderwidth=5, relief='sunken').place(x=160, y=165)
facecream = Label(top, text='Face Cream:', bg='orange', font=('Times New Roman', 11)).place(x=65, y=240)
e5 = Entry(top, width=10, textvariable=top.e5, font=('arial', 19), borderwidth=5, relief='sunken').place(x=160, y=230)
facewash = Label(top, text='Face Wash:', bg='orange', font=('Times New Roman', 11)).place(x=65, y=310)
e6 = Entry(top, width=10, textvariable=top.e6, font=('arial', 19), borderwidth=5, relief='sunken').place(x=160, y=300)
hairspray = Label(top, text='Hair Spray:', bg='orange', font=('Times New Roman', 11)).place(x=65, y=380)
e7 = Entry(top, width=10, textvariable=top.e7, font=('arial', 19), borderwidth=5, relief='sunken').place(x=160, y=370)
bodylortion = Label(top, text='Body Lortion:', bg='orange', font=('Times New Roman', 11)).place(x=65, y=460)
e8 = Entry(top, width=10, textvariable=top.e8, font=('arial', 19), borderwidth=5, relief='sunken').place(x=160, y=450)

# grocery
lf2 = LabelFrame(top, text='Grocery', bg='orange', bd=7, width=300, height=400).place(x=350, y=130)
Rice = Label(top, text='Rice:', bg='orange', font=('Times New Roman', 11)).place(x=370, y=170)
e9 = Entry(top, width=10, textvariable=top.e9, font=('arial', 19), borderwidth=5, relief='sunken').place(x=450, y=165)
foodoil = Label(top, text='Food Oil:', bg='orange', font=('Times New Roman', 11)).place(x=370, y=240)
e10 = Entry(top, width=10, textvariable=top.e10, font=('arial', 19), borderwidth=5, relief='sunken').place(x=450, y=230)
jaggery = Label(top, text='Jaggery:', bg='orange', font=('Times New Roman', 11)).place(x=370, y=310)
e11 = Entry(top, width=10, textvariable=top.e11, font=('arial', 19), borderwidth=5, relief='sunken').place(x=450, y=300)
uraddal = Label(top, text='Urad Dal:', bg='orange', font=('Times New Roman', 11)).place(x=370, y=380)
e12 = Entry(top, width=10, textvariable=top.e12, font=('arial', 19), borderwidth=5, relief='sunken').place(x=450, y=370)
wheat = Label(top, text='Wheat:', bg='orange', font=('Times New Roman', 11)).place(x=370, y=460)
e13 = Entry(top, width=10, textvariable=top.e13, font=('arial', 19), borderwidth=5, relief='sunken').place(x=450, y=450)

# others
lf3 = LabelFrame(top, text='Others', bg='orange', bd=7, width=300, height=400).place(x=650, y=130)
biscuits = Label(top, text='Biscuits:', bg='orange', font=('Times New Roman', 11)).place(x=670, y=170)
e14 = Entry(top, width=10, textvariable=top.e14, font=('arial', 19), borderwidth=5, relief='sunken').place(x=750, y=165)
slice = Label(top, text='Slice:', bg='orange', font=('Times New Roman', 11)).place(x=670, y=240)
e15 = Entry(top, width=10, textvariable=top.e15, font=('arial', 19), borderwidth=5, relief='sunken').place(x=750, y=240)
coke = Label(top, text='Coke:', bg='orange', font=('Times New Roman', 11)).place(x=670, y=310)
e16 = Entry(top, width=10, textvariable=top.e16, font=('arial', 19), borderwidth=5, relief='sunken').place(x=750, y=300)
mazaa = Label(top, text='Mazaa:', bg='orange', font=('Times New Roman', 11)).place(x=670, y=380)
e17 = Entry(top, width=10, textvariable=top.e17, font=('arial', 19), borderwidth=5, relief='sunken').place(x=750, y=370)
tilo = Label(top, text='Tilo:', bg='orange', font=('Times New Roman', 11)).place(x=670, y=460)
e18 = Entry(top, width=10, textvariable=top.e18, font=('arial', 19), borderwidth=5, relief='sunken').place(x=750, y=450)

# bill area
f = Frame(top, bg='orange', bd=10, relief=GROOVE)
f.place(x=955, y=135, width=347, height=390)
billtitle = Label(f, text="Bill Area", bg='orange', font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
scrol_y = Scrollbar(f, orient=VERTICAL)
top.txtarea = Text(f, yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=top.txtarea.yview)
top.txtarea.pack(fill=BOTH, expand=1)

# bill menu
lf4 = LabelFrame(top, text='Bill Menu', bg='orange', bd=7, width=1250, height=145).place(x=50, y=527)
totalcosmetics = Label(lf4, text='Total Cosmetics:', bg='orange', font=('Times New Roman', 11)).place(x=57, y=555)
e19 = Entry(top, width=15, textvariable=top.e19, font=('arial', 12), borderwidth=5, relief='sunken').place(x=165, y=555)
totalgrocery = Label(lf4, text='Total grocery:', bg='orange', font=('Times New Roman', 11)).place(x=57, y=600)
e20 = Entry(top, width=15, textvariable=top.e20, font=('arial', 12), borderwidth=5, relief='sunken').place(x=165, y=595)
totalothers = Label(lf4, text='Total Others:', bg='orange', font=('Times New Roman', 11)).place(x=57, y=635)
e21 = Entry(top, width=15, textvariable=top.e21, font=('arial', 12), borderwidth=5, relief='sunken').place(x=165, y=630)

cosmeticstax = Label(lf4, text='Cosmetics Tax:', bg='orange', font=('Times New Roman', 11)).place(x=350, y=555)
e22 = Entry(top, width=15, textvariable=top.e22, font=('arial', 12), borderwidth=5, relief='sunken').place(x=455, y=555)
grocerytax = Label(lf4, text='Grocery Tax:', bg='orange', font=('Times New Roman', 11)).place(x=350, y=600)
e23 = Entry(top, width=15, textvariable=top.e23, font=('arial', 12), borderwidth=5, relief='sunken').place(x=455, y=595)
otherstax = Label(lf4, text='Others Tax:', bg='orange', font=('Times New Roman', 11)).place(x=350, y=635)
e24 = Entry(top, width=15, textvariable=top.e24, font=('arial', 12), borderwidth=5, relief='sunken').place(x=455, y=630)


def fun():
    # cosmetic
    top.c_s_p = top.e4.get() * 40
    top.c_fc_p = top.e5.get() * 80
    top.c_fw_p = top.e6.get() * 120
    top.c_hs_p = top.e7.get() * 60
    top.c_bl_p = top.e8.get() * 150
    top.total_cosmetic_price = (
            top.c_s_p +
            top.c_fc_p +
            top.c_fw_p +
            top.c_hs_p +
            top.c_bl_p
    )
    top.e19.set(str(top.total_cosmetic_price))
    top.c_tax = (top.total_cosmetic_price * 0.10)
    top.e22.set("Rs, " + str(top.c_tax))

    # grocery
    top.g_r_p = top.e9.get() * 1200
    top.g_fo_p = top.e10.get() * 300
    top.g_j_p = top.e11.get() * 250
    top.g_u_p = top.e12.get() * 60
    top.g_w_p = top.e13.get() * 450

    top.total_grocery_price = (
            top.g_r_p +
            top.g_fo_p +
            top.g_j_p +
            top.g_u_p +
            top.g_w_p
    )
    top.e20.set(str(top.total_grocery_price))
    top.g_tax = (top.total_grocery_price * 0.10)
    top.e23.set("Rs, " + str(top.g_tax))

    # other
    top.o_b_p = top.e14.get() * 20
    top.o_s_p = top.e15.get() * 70
    top.o_c_p = top.e16.get() * 80
    top.o_m_p = top.e17.get() * 50
    top.o_t_p = top.e18.get() * 80
    top.total_other_price = (
            top.o_b_p +
            top.o_s_p +
            top.o_c_p +
            top.o_m_p +
            top.o_t_p
    )
    top.e21.set(str(top.total_other_price))
    top.o_tax = (top.total_other_price * 0.02)
    top.e24.set("Rs, " + str(top.o_tax))

    # totalBill
    top.total_bill = (
            top.total_cosmetic_price +
            top.c_tax +
            top.total_grocery_price +
            top.g_tax +
            top.total_other_price +
            top.o_tax
    )


b1 = Button(top, text='Total', bg='brown', fg='white', width=10, height=2, command=fun).place(x=650, y=590)


def welcome():
    top.txtarea.delete('1.0', END)
    top.txtarea.insert(END, "\t welcome Hari Mall")
    top.txtarea.insert(END, f"\n Bill Number :{top.e3.get()}")
    top.txtarea.insert(END, f"\n Customer Name :{top.e1.get()}")
    top.txtarea.insert(END, f"\n Customer Phno :{top.e2.get()}")
    top.txtarea.insert(END, f"\n ************************************")
    top.txtarea.insert(END, f"\n Product\t\t QTY \t\tPrice")
    top.txtarea.insert(END, f"\n ************************************")


def f():
    welcome()
    # Cosmetic bill
    if top.e4.get() != 0:
        top.txtarea.insert(END, f"\n Bath Soap\t\t {top.e4.get()}\t\t{top.e4.get() * 40} ")
    if top.e5.get() != 0:
        top.txtarea.insert(END, f"\n Face Cream \t\t {top.e5.get()}\t\t{top.e5.get() * 80} ")
    if top.e6.get() != 0:
        top.txtarea.insert(END, f"\n Face Wash\t\t {top.e6.get()}\t\t{top.e6.get() * 120} ")
    if top.e7.get() != 0:
        top.txtarea.insert(END, f"\n Hair Spray\t\t {top.e7.get()}\t\t{top.e7.get() * 60} ")
    if top.e8.get() != 0:
        top.txtarea.insert(END, f"\n Body Lortion\t\t {top.e8.get()}\t\t{top.e8.get() * 150} ")

    # grocerybill
    if top.e9.get() != 0:
        top.txtarea.insert(END, f"\n Rice\t\t {top.e9.get()}\t\t{top.e9.get() * 1200} ")
    if top.e10.get() != 0:
        top.txtarea.insert(END, f"\n Food Oil \t\t {top.e10.get()}\t\t{top.e10.get() * 300} ")
    if top.e11.get() != 0:
        top.txtarea.insert(END, f"\n Jaggery\t\t {top.e11.get()}\t\t{top.e11.get() * 250} ")
    if top.e12.get() != 0:
        top.txtarea.insert(END, f"\n Urad Dal\t\t {top.e12.get()}\t\t{top.e12.get() * 60} ")
    if top.e13.get() != 0:
        top.txtarea.insert(END, f"\n Wheat\t\t {top.e13.get()}\t\t{top.e13.get() * 450} ")

    # other bill
    if top.e14.get() != 0:
        top.txtarea.insert(END, f"\n Biscuit\t\t {top.e14.get()}\t\t{top.e14.get() * 20} ")
    if top.e15.get() != 0:
        top.txtarea.insert(END, f"\n Slice \t\t {top.e15.get()}\t\t{top.e15.get() * 70} ")
    if top.e16.get() != 0:
        top.txtarea.insert(END, f"\n Coke\t\t {top.e16.get()}\t\t{top.e16.get() * 80} ")
    if top.e17.get() != 0:
        top.txtarea.insert(END, f"\n Mazaa\t\t {top.e17.get()}\t\t{top.e17.get() * 50} ")
    if top.e18.get() != 0:
        top.txtarea.insert(END, f"\n Tilo\t\t {top.e18.get()}\t\t{top.e18.get() * 80} ")
    top.txtarea.insert(END, f"\n ************************************")
    if top.e22.get() != 0:
        top.txtarea.insert(END, f"\n Cosmetic Tax\t\t {top.e22.get()} ")
    if top.e23.get() != 0:
        top.txtarea.insert(END, f"\n Grocery Tax \t\t {top.e23.get()} ")
    if top.e24.get() != 0:
        top.txtarea.insert(END, f"\n Other Tax\t\t {top.e24.get()} ")

    top.txtarea.insert(END, f"\n ************************************")
    top.txtarea.insert(END, f"\n Total Bill\t\t {str(top.total_bill)} ")


def clear():
    # customer detail
    top.e1.set("")
    top.e2.set("")
    top.e3.set("")

    # cosmetic
    top.e4.set(0)
    top.e5.set(0)
    top.e6.set(0)
    top.e7.set(0)
    top.e8.set(0)

    # grocery
    top.e9.set(0)
    top.e10.set(0)
    top.e11.set(0)


b2 = Button(top, text='Generate Bill', bg='brown', fg='white', width=17, height=2, command=f).place(x=800, y=590)
welcome()
b3 = Button(top, text='Clear', bg='brown', fg='white', command=clear, width=10, height=2).place(x=990, y=590)


def exit():
    top.destroy()


b4 = Button(top, text='Exit', bg='red', fg='white', command=exit, width=10, height=2).place(x=1150, y=590)

top.mainloop()