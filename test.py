
from tkinter import *


""" 
We create 2 lists, primes and no primes 
then we go throught all the numbers from 2 to the final number
if this number is not in the list of no primes, then it is added
to the primes list and it multiplies until the product gets bigger
than the final number and each number is added to the no primes list
and it repeat until the final
"""

no_primes=[]
max_already_multiplied = 2
no_primes=[]

#first, verifies if it's a number, and then runs the generate fuction
def verify():
    global nums_to_generate
    try:    
        generate(int(nums_to_generate.get()))
        print("I can")
    except ValueError:
        label.delete(1.0,END)
        label.insert(END,"introduce a valid input")
        print("I can't")

#Here happens the magic of the generation of the primes numbers
def generate(until):
    global iteration_var
    global no_primes
    global max_already_multiplied
    global primes
    
    current_number = 2
    max_already_multiplied = 2
    while current_number <= until:
        iteration_var+=1
        if not(current_number in no_primes):
            primes.append(current_number)
            debug(current_number,(until//current_number)+1)
            max_already_multiplied = current_number
        current_number+=1
    
       
    #in here, we clean the entry and write the primes numbers in it
    label.delete(1.0,END)
    for x in primes:
        label.insert(END,(str(x)+"\n"))

    iterations_text.set(str(iteration_var))
    
    if not([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997] == primes):print("THEY ARE WRONG")
    else: print("RIGHT")
    


def debug(cn,max_multiplier):
    """this function add all multiples to
    the no_primes global list

    Args:
        cn (int): current number to debug
        max_multiplier (int): max multiplier to debug
    """
    global iteration_var
    global no_primes
    global max_already_multiplied
    for multiplier in range(max_already_multiplied,max_multiplier):
                iteration_var+=1
                no_primes.append(cn * multiplier)
    
    
    

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



    

iterations_text.set("0")
iteration_var = int(iterations_text.get())
generate(1000) #test
root.mainloop()
#------------------------------------------------------------------------------