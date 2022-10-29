
from tkinter import *


""" 
We create 2 lists, primes and no primes 
then we go throught all the numbers from 2 to the final number
if this number is not in the list of no primes, then it is added
to the primes list and it multiplies until the product gets bigger
than the final number and each number is added to the no primes list
and it repeat until the final
"""


primes = [1]
no_primes= []

#first, verifies if it's a number, and then runs the generate fuction
def verify():
    try:
        generate(int(nums_to_generate.get()))
        print("i can")
    except ValueError:
        label.delete(1.0,END)
        label.insert(END,"introduce a valid input")
        print("i can't")

#Here happens the magic of the generation of the primes numbers
def generate(until):
    global viterations_text
    iteration_var = int(iterations_text.get())

    primes=[1]
    current_num=2
    while current_num <= until :                            #while the current num is less or equal than the until number...
        if not(current_num in no_primes):                   #if the current number, is not in the no_primes list...    
            primes.append(current_num)                          #first of all, add it to the primes list and...
            for x in range(until+1):                            #for the numbers (called x) from 0 to the until number given
                if not((current_num * x) > until):                  #if the product of the current number multiply by x is less than the until number
                    no_primes.append(current_num*x)                     #append it to the no_primes list
                else:                                               #if the product of the current number multiply by x is MORE than the until number
                    break;                                              #stop cycle
        current_num +=1                                     #continue with the next number
        iteration_var+=1

    #in here, we clean the entry and write the primes numbers in it
    label.delete(1.0,END)
    for x in primes:
        label.insert(END,(str(x)+"\n"))

    iterations_text.set(str(iteration_var))
    
    
    

    

#------------------------------------------------------------------------------
#I use Tkinter for the graphic interface

root =Tk()
root.geometry("230x230")
root.title("primes generator")
root.config(bg="#ffffff")
root.resizable(0,0)
#===================================
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#===================================

frame =Frame(root)
frame.config(width=screen_width,height=screen_height)

title =Label(frame,text="Introduce until wich number \n you want to generate primes")

iterations_label = Label(frame,text="iterations:")
iterations_text = StringVar()
iterations_text.set("0")
iterations =Label(frame);iterations.config(textvariable=iterations_text)

#An entry that gets the final number
nums_to_generate = Entry(frame, borderwidth=2)

#A button that makes the verify fuction runs
btn = Button(frame, text="generate", command=verify)



scroll = Scrollbar(frame)
label=Text(frame,width=27, yscrollcommand=scroll.set)
label.insert(END,"---------------------------")
scroll.config(command=label.yview)




frame.grid(row=4,column=1)

title.grid(row=0,column=0,columnspan=2)
nums_to_generate.grid(row=1,column=0)
btn.grid(row=1,column=1)
iterations_label.grid(row=2,column=0, sticky="e")
iterations.grid(row=2,column=1, sticky="w")
label.grid(row=3, column=0,columnspan=2)



    


root.mainloop()
#------------------------------------------------------------------------------