from tkinter import *

def get_patient_symptoms():
    fever = fever_entry.get()
    cough = cough_entry.get()
    difficulty_breathing = difficulty_breathing_entry.get()
    # Aquí puede enviar los datos a CLIPS para su procesamiento.
    print("Fever: ", fever)
    print("Cough: ", cough)
    print("Difficulty Breathing: ", difficulty_breathing)

root = Tk()
root.title("Patient Symptoms")

fever_label = Label(root, text="Fever (yes/no):")
fever_label.grid(row=0, column=0, padx=5, pady=5)
fever_entry = Entry(root)
fever_entry.grid(row=0, column=1, padx=5, pady=5)

cough_label = Label(root, text="Cough (yes/no):")
cough_label.grid(row=1, column=0, padx=5, pady=5)
cough_entry = Entry(root)
cough_entry.grid(row=1, column=1, padx=5, pady=5)

difficulty_breathing_label = Label(root, text="Difficulty Breathing (yes/no):")
difficulty_breathing_label.grid(row=2, column=0, padx=5, pady=5)
difficulty_breathing_entry = Entry(root)
difficulty_breathing_entry.grid(row=2, column=1, padx=5, pady=5)

submit_button = Button(root, text="Submit", command=get_patient_symptoms)
submit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, ipadx=50)

root.mainloop()
