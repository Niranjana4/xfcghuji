from  tkinter import*

root=Tk()
root.title("Encapsulation")
root.geometry("600x600")

label_score=Label(root,font=("Papyrus",12,"bold"))
label_score.place(relx=0.1,rely=0.1,anchor=W)
label_color=Label(root,font=("Papyrus",20))
label_color.place(relx=0.5,rely=0.3)
text_input=Entry()
text_input.place(relx=0.5,rely=0.5)

class game():
    def __init__(self):
        self.__score=0
    def __update(self):
        if(input_value==self.color[self.random_number_for_color]):
                 self.__score=self.__score+random_randint(0,10)
                 label_score["text"]="Score: "+str(self.__score)
    def get_user_value(self,input_value):
        __update()

obj=game()
def getInput():
    value=text_input.get()
    obj.get_user_value(value)
    obj.update()
    text_input.delete(0,END)
    
btn=Button(root,text="Check",command=getInput,bg="IndianRed1",fg="white",relief=FLAT,padx=10,pady=1,font=("Arial",15))
btn2=Button(root,text="Start",command=getInput,bg="IndianRed1",fg="white",relief=FLAT,padx=10,pady=1,font=("Arial",15))
btn.place(relx=0.4,rely=0.7)
btn2.place(relx=0.6,rely=0.7)
    
root.mainloop()