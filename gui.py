import tkinter as tk

import cpfutils

root = tk.Tk()

def validate_cpf(stringvar: tk.StringVar, button: tk.Button):
    cpf = stringvar.get()

    if cpfutils.validate(cpf):
        button.config(text='OK',
                      activeforeground='green',
                      foreground='green')
    else:
        button.config(text='Inválido',
                      activeforeground= 'red',
                      foreground='red')

def cpf_generator(stringvar: tk.StringVar, button: tk.Button):
    cpf = cpfutils.generate()
    cpf_formatado = cpfutils.formater(cpf)
    stringvar.set(cpf_formatado)


def button_generator(master, text, command=None):
    button = tk.Button(master, text=text)
    if command:
        button.config(command=command)
    return button

def label_generator(master, text, bg:str):
    label = tk.Label(master, text=text, bg=bg)
    return label

def entry_generator(master):
    entry = tk.Entry(master)
    return entry

main_title = tk.Label(root, 
                      text='Gerador/Validador de CPF',
                      bg='#fff',
                      font=('Helvetica', 12, 'bold'))
main_title.grid(row=0, column=0, columnspan=3, pady=(0,20))

validate_string_var = tk.StringVar()
validate_entry = entry_generator(root)
validate_entry.grid(row=1, column=1, pady=10)
validate_entry.config(bd=5, relief='flat', textvariable=validate_string_var)

validate_label = label_generator(root, 'Validar CPF', bg='#fff')
validate_label.grid(row=1, column=0)

validate_button = button_generator(root,'Validar', 
                                  command=lambda:validate_cpf(validate_string_var, validate_button))
validate_button.grid(row=1, column=2, sticky='ew')

generate_stringvar = tk.StringVar()
generate_entry = entry_generator(root)
generate_entry.grid(row=2, column=1, pady=10)
generate_entry.config(bd=5, relief='flat', textvariable=generate_stringvar)

generate_label = label_generator(root, 'Gerar CPF', bg='#fff')
generate_label.grid(row=2, column=0)

generate_button = button_generator(root, 'Gerar', command=lambda:cpf_generator(generate_stringvar, generate_button))
generate_button.grid(row=2, column=2, sticky='ew')


root.title('Gerador/Validador de CPF')
root.config(background='#fff', padx=20, pady=20)
root.mainloop()
