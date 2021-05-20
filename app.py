import tkinter as tk
from keras.models import load_model

# load the saved model
saved_model = load_model('best_model.h5')
# evaluate the model
def predict(X):
    return saved_model.predict(X)[0][0]*100

temp=predict([[0,0,0,0,0,0,0,0]])

root = tk.Tk()

vars_list = []
fields=[('Cough',(('Yes',1),('No',0))),
        ('Fever',(('Yes',1),('No',0))),
        ('Sore Throat',(('Yes',1),('No',0))),
        ('Shortness of breath',(('Yes',1),('No',0))),
        ('Headache',(('Yes',1),('No',0))),
        ('Age',(('60 and above',1),('Less than 60',0))),
        ('Gender',(('Male',1),('Female',0))),
        ('Contact with Covid positive person',(('Yes',0),('No',2),("Don't know",1)))
        ]

for field in fields:
    frame = tk.Frame(root)
    frame.pack()
    tk.Label(frame,text=field[0]).pack(side="left")
    var = tk.IntVar(value=0)
    vars_list.append(var)
    for options in field[1]:
        tk.Radiobutton(frame, text=options[0], variable=var, value=options[1]).pack(side="left")
def fetch():
    vec=list(map(lambda i:i.get(),vars_list))
    vec=[vec]
    s="Probability of testing positive is " + str(predict(vec)) + "%"
    label.config(text=s)

button_frame = tk.Frame(root)
b1 = tk.Button(button_frame, text='Show',command=fetch)
b2 = tk.Button(button_frame, text='Quit', command=root.quit)
button_frame.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)
b1.pack(side=tk.LEFT, padx=5, pady=5)
b2.pack(side=tk.LEFT, padx=5, pady=5)

label = tk.Label(root)
label.pack(side=tk.LEFT)
root.mainloop()