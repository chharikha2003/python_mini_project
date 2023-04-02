from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import json
root = Tk()
root.geometry("680x600")
root.title("Quiz")
with open('questions.json') as f:
    obj = json.load(f)
q= (obj['question'])
options = (obj['options'])
a = (obj['answer'])

class Quiz:
   
    def __init__(self):
        self.q_no=0
        self.new_func()
        
    def calling(self):
         print("inside")
         label_2.destroy()
         canvas.destroy()
         
         label_0.destroy()
         label.destroy()
         label_1.destroy()
         entry_1.destroy()
         entry_2.destroy()
         btn1.destroy()
         self.maincall()
         
         
    def maincall(self):
        
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(q)
        self.correct = 0
         
       
        
    
        
    

    def display_question(self):
        # setting the Question properties
        q_no = Label(root,text=q[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        #placing the option on the screen
        q_no.place(x=70, y=100)
    def display_title(self):
        # The title to be shown
        title = Label(root,text="PYQUIZ",
        width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
        # place of the title
        title.place(x=-100, y=2)  
    def display_result(self):
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
    def check_ans(self, q_no):
        if self.opt_selected.get() == a[q_no]:
            return True
    def next_btn(self):
        if self.check_ans(self.q_no):
             
            # if the answer is correct it increments the correct by 1
            self.correct += 1
         
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1
         
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
             
            # if it is correct then it displays the score
            self.display_result()
             
            # destroys the GUI
            root.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()
            
    def buttons(self):
         
        # The first button is the Next button to move to the
        # next Question
            next_button = Button(root, text="Next",command=self.next_btn,
            width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
            
            # placing the button  on the screen
            next_button.place(x=200,y=360)
            
            # This is the second button which is used to Quit the GUI
            quit_button = Button(root, text="Quit", command=root.destroy,
            width=10,bg="black", fg="white",font=("ariel",16," bold"))
            
            # placing the Quit button on the screen
            quit_button.place(x=380,y=360)
    def new_func(self):
        global label_2,canvas,img_file,img,label_0,label,label_1,entry_1,entry_2,btn1
        print("new")
        canvas = Canvas(root, width=300, height=300)
        canvas.pack()
        img_file = Image.open("logo.jpg")
        img_file = img_file.resize((150, 150))# (width,height)
        img = ImageTk.PhotoImage(img_file)
        canvas.create_image(80, 40, anchor=NW, image=img)
        label_0 = Label(root, text="PyQuiz", width=10, font=("bold", 20))
        label_0.place(x=250, y=210)
        label = Label(root, text="Welcome to PyQuiz!\nClick below to test your python knowledge",
                      width=50, font=("bold", 15))
        label.place(x=50, y=280)
        label_1 = Label(root, text="Name", width=20,font=("bold", 10))
        label_1.place(x=150, y=350)
        entry_1 = Entry(root)
        entry_1.place(x=280, y=350)
        label_2 = Label(root, text="Email",width=20, font=("bold", 10))
        label_2.place(x=150, y=380)
        entry_2 = Entry(root)
        entry_2.place(x=280, y=380)
        
        btn1=Button(root, text='Start',command=self.calling, width=15,bg="black",fg='white',    font=("ariel",16,"bold"))
        btn1.place(x=240, y=450)
    def display_options(self):
            val=0
            
            # deselecting the options
            self.opt_selected.set(0)
            
            # looping over the options to be displayed for the
            # text of the radio buttons.
            for option in options[self.q_no]:
                self.opts[val]['text']=option
                val+=1
 
 
    # This method shows the current Question on the screen
    def display_question(self):
            
            # setting the Question properties
            q_no = Label(root, text=q[self.q_no], width=60,
            font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
            
            #placing the option on the screen
            q_no.place(x=70, y=100)
 
 
    
 
    
    def radio_buttons(self):
            
            # initialize the list with an empty list of options
            q_list = []
            
            # position of the first option
            y_pos = 150
            
            # adding the options to the list
            while len(q_list) < 4:
                
                # setting the radio button properties
                radio_btn = Radiobutton(root,text=" ",variable=self.opt_selected,
                value = len(q_list)+1,font = ("ariel",14))
                
                # adding the button to the list
                q_list.append(radio_btn)
                
                # placing the button
                radio_btn.place(x = 100, y = y_pos)
                
                # incrementing the y-axis position by 40
                y_pos += 40
            
            # return the radio buttons
            return q_list

quiz=Quiz()

root.mainloop()



