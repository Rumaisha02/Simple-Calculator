from tkinter import *

root=Tk()
root.title("Simple Calculator")

e=Entry(root, width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def DisplayButton(number):
  current=e.get()
  e.delete(0,END)
  e.insert(0,  str(current) + str(number))

def ClearButton():
  e.delete(0,END)

def Solve(sign):
  first_number=e.get()
  global F_num 
  F_num=int(first_number)
  e.delete(0, END)
  global operation
  operation=str(sign)
#   match sign:
#     case "+":
#        second_number=e.get()
#        e.delete(0,END)
#        e.insert(0, F_num + int(second_number))
      

def Equals_button():
  second_number=e.get()
  e.delete(0,END)
  match operation:
    case "+":
      e.insert(0, F_num + int(second_number))
    case "-":
      e.insert(0, F_num - int(second_number))
    case "*":
      e.insert(0, F_num * int(second_number))
    case "/":
      e.insert(0, F_num / int(second_number))
      
       
  
  

Button1=Button(root, text="1", command=lambda: DisplayButton(1),padx=40, pady=20)
Button2=Button(root, text="2", command=lambda: DisplayButton(2),padx=40, pady=20)
Button3=Button(root, text="3", command=lambda: DisplayButton(3),padx=40, pady=20)
Button4=Button(root, text="4", command=lambda: DisplayButton(4),padx=40, pady=20)
Button5=Button(root, text="5", command=lambda: DisplayButton(5),padx=40, pady=20)
Button6=Button(root, text="6", command=lambda: DisplayButton(6),padx=40, pady=20)
Button7=Button(root, text="7", command=lambda: DisplayButton(7),padx=40, pady=20)
Button8=Button(root, text="8", command=lambda: DisplayButton(8),padx=40, pady=20)
Button9=Button(root, text="9", command=lambda: DisplayButton(9),padx=40, pady=20)
Button0=Button(root, text="0", command=lambda: DisplayButton(0),padx=40, pady=20)

Button_clear=Button(root, text="CLEAR", command=lambda: ClearButton(),padx=25, pady=20)
Button_plus=Button(root, text="+", command=lambda: Solve("+"),padx=40, pady=20)
Button_substract=Button(root, text="-", command=lambda: Solve("-") ,padx=40, pady=20)
Button_multiply=Button(root, text="x" , command=lambda: Solve("*") ,padx=40, pady=20)
Button_divide=Button(root, text="/" , command=lambda: Solve("/") ,padx=40, pady=20)
Button_equals=Button(root, text="=" , command=Equals_button ,padx=40, pady=20)

#placing the  NUMBER buttons
Button9.grid(row=1,column=0)
Button8.grid(row=1,column=1)
Button7.grid(row=1,column=2)
Button6.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button4.grid(row=2,column=2)
Button3.grid(row=3,column=0)
Button2.grid(row=3,column=1)
Button1.grid(row=3,column=2)
Button0.grid(row=4,column=1)

#placing the Funtion buttons
Button_clear.grid(row=4,column=0)
Button_equals.grid(row=4,column=2)
Button_plus.grid(row=1,column=3)
Button_substract.grid(row=2,column=3)
Button_multiply.grid(row=3,column=3)
Button_divide.grid(row=4,column=3)

root.mainloop()