from tkinter import *

""" 
We create 2 lists, primes and no primes 
then we go throught al the numbers from 2 to the final number
if this number is not in the list of no primes, then it is added
to the primes list and it multiplies until the product gets bigger
than the final number and each number is added to the no primes
and it repeat until the final
"""


primes = [1]
no_primes= []

def verify():
    try:
        generate(int(nums_to_generate.get()))
    except ValueError:
        label.config(text="invalid input", bg="#fa0000")

def generate(until):
    current_num=2
    while current_num <= until :
        if not(current_num in no_primes):
            primes.append(current_num)
            for x in range(until+1):
                if not((current_num * x) > until):
                    no_primes.append(current_num*x)
                else:
                    break;
        current_num +=1
    label.config(text=primes)

    

#------------------------------------------------------------------------------


root = Tk()
root.geometry("200x200")
root.title("primes generator")
root.config(bg="#ffffff")
root.resizable(height = None, width = None) #doesn't works ._.
#===================================
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#===================================

frame = Frame(root)
frame.config(width=screen_width,height=screen_height)
frame.grid(row=1,column=1)


nums_to_generate = Entry(frame, borderwidth=2)
nums_to_generate.grid(row=1,column=1)

btn = Button(frame, text="generate", command=verify)
btn.grid(row=1,column=2)


label=Label(frame, text="---", )
label.grid(row=2, column=1, columnspan=2)





    


root.mainloop()
#------------------------------------------------------------------------------