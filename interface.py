import tkinter as tk
import pickle


# Obtener los datos del formulario
def get_data():
    fever = fever_var.get()
    cough = cough_var.get()
    breathing = breathing_var.get()
    data = {"fever": fever, "cough": cough, "breathing": breathing}
    return data

# Guardar los datos en un archivo
def save_data():
    data = get_data()
    with open("patient_data.txt", "w") as f:
        f.write(str(data))
    print("Data saved to patient_data.txt")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("COVID-19 Diagnosis Form")

# Crear las variables de los checkboxes
fever_var = tk.StringVar()
cough_var = tk.StringVar()
breathing_var = tk.StringVar()

# Crear los checkboxes
tk.Checkbutton(root, text="Fever", variable=fever_var, onvalue="yes", offvalue="no").grid(row=0, column=0)
tk.Checkbutton(root, text="Cough", variable=cough_var, onvalue="yes", offvalue="no").grid(row=1, column=0)
tk.Checkbutton(root, text="Difficulty Breathing", variable=breathing_var, onvalue="yes", offvalue="no").grid(row=2, column=0)

# Crear el botón para guardar los datos
tk.Button(root, text="Save Data", command=save_data).grid(row=3, column=0)

root.mainloop()
