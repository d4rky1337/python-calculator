import tkinter as tk
calculation = ""
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"error")
def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

root = tk.Tk(className='Calculator')
root.geometry("450x380")
root.resizable(False, False)
root.configure(bg='#2C2C2C')

text_result = tk.Text(root,bg='#2C2C2C', height=2,width=25,fg='#FFFFFF', font=("Arial",25))
text_result.grid(columnspan=5)

#adding the buttons
#bg = background color ; fg = text color ; activebackgroud = color when pressing the button

btn_1=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="1", command=lambda: add_to_calculation(1),width=9,height=2,font=("Arial",14))
btn_1.grid(row=2,column=1)
btn_2=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="2", command=lambda: add_to_calculation(2),width=9,height=2,font=("Arial",14))
btn_2.grid(row=2,column=2)
btn_3=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="3", command=lambda: add_to_calculation(3),width=9,height=2,font=("Arial",14))
btn_3.grid(row=2,column=3)
btn_4=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="4", command=lambda: add_to_calculation(4),width=9,height=2,font=("Arial",14))
btn_4.grid(row=3,column=1)
btn_5=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="5", command=lambda: add_to_calculation(5),width=9,height=2,font=("Arial",14))
btn_5.grid(row=3,column=2)
btn_6=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="6", command=lambda: add_to_calculation(6),width=9,height=2,font=("Arial",14))
btn_6.grid(row=3,column=3)
btn_7=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="7", command=lambda: add_to_calculation(7),width=9,height=2,font=("Arial",14))
btn_7.grid(row=4,column=1)
btn_8=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="8", command=lambda: add_to_calculation(8),width=9,height=2,font=("Arial",14))
btn_8.grid(row=4,column=2)
btn_9=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="9", command=lambda: add_to_calculation(9),width=9,height=2,font=("Arial",14))
btn_9.grid(row=4,column=3)
btn_0=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="0", command=lambda: add_to_calculation(0),width=9,height=2,font=("Arial",14))
btn_0.grid(row=5,column=2)
btn_plus=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="+", command=lambda: add_to_calculation("+"),width=9,height=2,font=("Arial",14))
btn_plus.grid(row=2,column=4)
btn_minus=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="-", command=lambda: add_to_calculation("-"),width=9,height=2,font=("Arial",14))
btn_minus.grid(row=3,column=4)
btn_multiplication=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="x", command=lambda: add_to_calculation("*"),width=9,height=2,font=("Arial",14))
btn_multiplication.grid(row=4,column=4)
btn_division=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="/", command=lambda: add_to_calculation("/"),width=9,height=2,font=("Arial",14))
btn_division.grid(row=5,column=4)
btn_leftbracket=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text="(", command=lambda: add_to_calculation("("),width=9,height=2,font=("Arial",14))
btn_leftbracket.grid(row=5,column=1)
btn_rightbracket=tk.Button(root,bg='#3D3D3D',fg="#FFFFFF",activebackground='#FFFFFF', text=")", command=lambda: add_to_calculation(")"),width=9,height=2,font=("Arial",14))
btn_rightbracket.grid(row=5,column=3)
btn_equals=tk.Button(root,bg='#FF841E',activebackground='#FFFFFF', text="=", command=lambda: evaluate_calculation(),width=19,height=2,font=("Arial",14))
btn_equals.grid(row=6,column=3,columnspan=2)
btn_clear=tk.Button(root,bg='#FF841E',activebackground='#FFFFFF', text="C", command=lambda: clear_field(),width=19,height=2,font=("Arial",14))
btn_clear.grid(row=6,column=1,columnspan=2)

root.bind('<Escape>', lambda e, w=root: w.destroy()) #binded esc to exit window
root.mainloop()
