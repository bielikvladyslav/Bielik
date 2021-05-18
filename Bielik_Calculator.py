import tkinter as tk
from tkinter import messagebox
import re
import numpy as np
import math
from tkinter import *


hist=0

def add_digit(digit):
    '''Добавляем цифру и если перед ней стоял нолик, то нолик удаляется.
    НО если мы выполняем какую-то операцию над ноликом, то он остается.
    '''
    value = calc.get()

    if value=="":
        calc.insert(0, digit)
    elif value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete (0, tk.END)
    calc.insert(0, value+digit)

def add_operation(operation):
    """Эта функция добавляет операцию и если цифры нет, но новую операцию пользователь хочет
    добать, то операция, которая уже существует заменяеьтся нвоой
    """
    value=calc.get()
    if value[-1] in '-+*/':
        value=value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)



def eval_by_bielik(expr):
    """Решение математических операций

    """
    symb = '[()/*+-]'
    eq= re.split(symb, expr)
    numbs='[1234567890. ]'
    actions=re.split(numbs, expr)

    while '' in actions:
            actions.remove('')
    while '' in eq:
            eq.remove('')
    while ' ' in eq:
            eq.remove(' ')
    f = 0
    x = len(actions)
    while f < x:
        if len(actions[f]) > 1:
            a = actions[f]
            b = actions[f + 1:]
            actions = actions[:f]
            for j in range(len(a)):
                actions.append(a[j])
            for k in range(len(b)):
                actions.append(b[k])

        x = len(actions)
        f += 1

    while '(' in actions:
        indxsk=expr.index('(')
        indxsk2=indxsk

        while expr[indxsk2]!=')':
            indxsk2+=1

        indxa1=actions.index('(')
        indxa2=actions.index(')')

        i=indxa2-1
        while indxa2!=indxa1-1:

            actions.pop(indxa2)
            indxa2-=1
        while i!= indxa1:
            print(eq)
            eq.pop(i)
            i -= 1

        particres=expr[indxsk+1:indxsk2]
        eq[i]=eval_by_bielik(particres)
    while len(actions)>=1:
        if "*" in actions:
            indxm=actions.index('*')
            res1=float(eq[indxm])*float(eq[indxm+1])
            actions.remove('*')
            eq[indxm] = res1
            eq.pop(indxm+1)

        elif "/" in actions:
            indxd=actions.index('/')
            res1=float(eq[indxd])/float(eq[indxd+1])
            actions.remove('/')
            eq[indxd] = res1
            eq.pop(indxd+1)
        elif actions[0]=='+':
            res1=float(eq[0])+float(eq[1])
            actions.remove('+')
            eq[0] = res1
            eq.pop(1)
        elif actions[0]=='-':
            res1=float(eq[0])-float(eq[1])
            actions.remove('-')
            eq[0] = res1
            eq.pop(1)
    return eq[0]

def intenger(a):
    """Проверка целое ли число"""
    a = str(a)
    length = len(a)
    if a[length - 1] == "0" and a[length - 2] == ".":
        a = str(int(float(a)))
    return a

def calculate():
    """Выполняется расчет, если введено лишь одно число и операция то эта операция выполняется
     с этим же числом. Например, 2+ = 2+2 = 4
     если вводятся буквы, то выводится ошибка
     если выполняется деление на ноль, то выводится ошибка"""
    value = calc.get()

    if hist == 1:
        history = open('history.txt', 'a+')
        exp=str(value)

    #Перевіряємо чи однакова кількість дужок
    if '(' in value:
        x=value.count('(')
        y=value.count(')')
        if x!=y:
            messagebox.showinfo("Error!", "The number of brackets is different!")

    symb = '[()/*+-]'
    trigon = ['sin', 'cos', 'tg', 'ctg','arcsin','arccos','arctg','arcctg']
    value_trig = re.split(symb, value)
    for i in range(len(trigon)):
        for j in range(len(value_trig)):
            if trigon[i] == value_trig[j]:
                if trigon[i] == 'sin':
                    indx = value.index('n') + 2
                    while value[indx] != ')':
                        indx += 1
                        n = indx
                    N = value.index('n')
                    мalue = (value[:N - 2] + str(intenger(round(math.sin(float(value_trig[j + 1])), 3))) + value[n + 1:])

                elif trigon[i] == 'cos':
                        indx = value.index('s') + 2
                        while value[indx] != ')':
                            indx += 1
                            n = indx
                        N = value.index('s')
                        value= (value[:N - 2] + str(intenger(round(math.cos(float(value_trig[j + 1])), 1))) + value[n + 1:])
                elif trigon[i] == 'tg':
                        indx = value.index('g') + 2
                        while value[indx] != ')':
                            indx += 1
                            n = indx
                        N = value.index('g')
                        value= (value[:N - 1] + str(intenger(round(math.tan(float(value_trig[j + 1])), 1))) + value[n + 1:])
                elif trigon[i] == 'ctg':
                    indx = value.index('g') + 2
                    while value[indx] != ')':
                        indx += 1
                        n = indx
                    N = value.index('g')
                    ctg = round((math.cos(float(value_trig[j + 1])) / math.sin(float(value_trig[j + 1]))), 1)

                    value = (value[:N - 2] + str(intenger(ctg)) + value[n + 1:])
                elif trigon[i] == 'arcsin':
                    indx = value.index('n') + 2
                    while value[indx] != ')':
                        indx += 1
                        n = indx
                    N = value.index('n')
                    arcsin = round((math.asin(float(value_trig[j + 1]))), 1)


                    value = (value[:N - 5] + str(intenger(arcsin)) + value[n + 1:])
                elif trigon[i] == 'arccos':
                    indx = value.index('s') + 2
                    while value[indx] != ')':
                        indx += 1
                        n = indx
                    N = value.index('s')
                    arccos = round((math.acos(float(value_trig[j + 1]))), 1)

                    value = (value[:N - 5] + str(intenger(arccos)) + value[n + 1:])
                elif trigon[i] == 'arctg':
                    indx = value.index('g') + 2
                    while value[indx] != ')':
                        indx += 1
                        n = indx
                    N = value.index('g')
                    arctg = round((math.atan(float(value_trig[j + 1]))), 1)

                    value = (value[:N - 4] + str(intenger(arctg)) + value[n + 1:])
                elif trigon[i] == 'arcctg':
                    indx = value.index('g') + 2
                    while value[indx] != ')':
                        indx += 1
                        n = indx
                    N = value.index('g')
                    arcctg = round((math.acos(float(value_trig[j + 1])) / math.asin(float(value_trig[j + 1]))), 1)
                    value = (value[:N - 5] + str(intenger(arcctg)) + value[n + 1:])


    """Осуществляется проверка на использование статистических функций"""
    symb = '[()/*+-,]'
    stat=['sum','A','SE']
    value_2_0=re.split(symb,value)
    while '' in value_2_0:
        value_2_0.remove('')


    for i in range(len(stat)):
        for j in range(len(value_2_0)):
            if stat[i]==value_2_0[j]:
                if stat[i]=='sum':
                    sum_result=0
                    indx=value.index('m')+2  #узнаем индекс на который начинаются элементы функции
                    summa=''

                    while value[indx] != ')':
                        summa=summa+value[indx]
                        indx += 1
                        n=indx
                    summa_2=summa.split(',')
                    for k in range (len(summa_2)):
                            sum_result+=int(summa_2[k])

                    N=value.index('s')
                    value=value[:N]+str(sum_result)+value[n+1:]
                elif stat[i]=='A':
                    sredar_result=0
                    indx=value.index('A')+2  #узнаем индекс на который начинаются элементы функции
                    summa=''




                    while value[indx] != ')':
                        summa = summa + value[indx]
                        indx += 1
                        n = indx
                    summa_2 = summa.split(',')
                    for k in range(len(summa_2)):
                        sredar_result += int(summa_2[k])
                    num=len(summa_2)


                    N=value.index('A')
                    value=value[:N]+str(intenger(sredar_result/num))+value[n+1:]
                elif stat[i]=='SE':
                    sum_result=0
                    indx=value.index('E')+2  #узнаем индекс на который начинаются элементы функции
                    se=[]
                    SE_result=[]

                    summa = ''

                    while value[indx] != ')':
                        summa = summa + value[indx]
                        indx += 1
                        n = indx
                    summa_2 = summa.split(',')
                    for k in range(len(summa_2)):
                        SE_result.append(int(summa_2[k]))

                    SE=np.std(SE_result)
                    N=value.index('S')
                    value=value[:N]+str(intenger(SE))+value[n+1:]
            value=intenger(value)

    """Проверка есть ли доп операции в строке ввода"""
    symb_oper = '[()/*+-,]'
    oper = ['^','%','sqrt','!','log']
    value_oper = re.split(symb_oper, value)
    for i in range(len(oper)):
        for j in range(len(value_oper)):
            if oper[i] == value_oper[j]:

                if oper[i]=='^':
                    indx = value.index('^')
                    NDX=indx
                    n=indx
                    while value[indx]!="(":
                        indx+=-1
                    N=indx
                    while value[n] != ")":
                        n+=1
                    result=int(eval_by_bielik(value[N+1:NDX-1]))**int(eval_by_bielik(value[NDX+2:n]))
                    value=value[:N]+str(result)+value[n+1:]
                elif oper[i]=='sqrt':
                    indx = value.index('t')
                    n = indx
                    while value[n]!=')':
                        n+=1
                    N=value.index('s')
                    try:
                        result=intenger(math.sqrt(int(eval_by_bielik(value[indx+2:n]))).__round__(3))
                        value = value[:N] + str(intenger(result)) + value[n + 1:]
                    except:
                        messagebox.showinfo('Error!', "Square root of a negative number!")
                elif oper[i] == '!':
                    indx = value.index('!')
                    n = indx
                    while value[n] != '(':
                        n += -1
                    result = math.factorial(int(value_oper[j -1]))
                    value = value[:n] + str(intenger(result)) + value[indx+1:]
                elif oper[i] == '%':
                    indx=value.index('%')-2
                    number=value_oper[j-2]

                    if number=='':
                        number = value_oper[j - 3]
                    else:
                        number=number[0:len(number)-1]


                    while value[indx]!='(':
                        indx-=1
                    result=int(value_oper[j-1])/100*int(number)
                    value = value[:indx] + str(intenger(result)) + value[value.index('%')+1:]

                elif oper[i] == 'log':
                    indx = value.index('l')
                    n = indx

                    while value[n] != ')':
                        n += 1
                    try:
                        result=math.log(int(value_oper[j+1]),int(value_oper[j+2]))
                        value= value[:indx] + str(intenger(result)) + value[n+1:]
                    except ZeroDivisionError:
                        messagebox.showinfo('Error!', "Base is 1!")

            value = intenger(value)


    #Якщо строка закінчується на операцію, то ця операція виконується на останнім числом
    if value [-1] in ['/','*','-','+']:
        value= value+value[:-1]




    try:
        value = eval_by_bielik(value)
    except ZeroDivisionError:
        messagebox.showinfo("Error!", "Division by zero!")
        calc.insert(0, 0)



        # перевіряємо чи відповідь є цілим числом
    value = intenger(value)

    calc.delete(0, tk.END)
    calc.insert(0, value)

#проверка активирована ли кнопка сохранения
    if hist == 1:
        history = open('history.txt','r')
        inp=history.read()
        history = open('history.txt', 'w')
        result = str(value)
        line = str(exp + '=' + result + "\n"+inp)
        history.write(line)





def clear():
    """ Эта функция очищает всю строку"""
    calc.delete(0, tk.END)
    calc.insert(0,0)

def clearlast():
    """ Эта функция удаляет последний символ"""
    value = calc.get()
    if len(value)==1:
        calc.delete(0, tk.END)
        calc.insert(0, 0)
    else:
        value = value[:-1]
        calc.delete(0, tk.END)
        calc.insert(0, value)

def make_digit_button(digit):
    """Создаем новую кнопку с цифрой"""
    return tk.Button(text=digit, bd=5, font=('Times New Roman', 13),
                     command=lambda: add_digit(digit))



def make_operation_button(operation):
    """Создаем кнопку с операцией и направляем при нажатии к функции add_operation"""
    return tk.Button(text=operation, bd=5, font=('Times New Roman', 13), fg='red',
                     command=lambda: add_operation(operation))

def make_calc_button(operation):
    """Создаем кнопку равно"""
    return tk.Button(text = operation, bd = 5, font = ('Times New Roman', 13), fg="red",
                                 command = calculate)

def make_clear_button(operation):
    """Создаем кнопку очистки всей строки"""
    return tk.Button(text = operation, bd = 5, font = ('Times New Roman', 13), fg="red",
                                 command = clear)

def make_clearlast_button(operation):
    """Создаем кнопку удаления последнего символа"""
    return tk.Button(text = operation, bd = 5, font = ('Times New Roman', 13), fg="red",
                                 command = clearlast)


def add_trigonometry(function):
    """Добавляем тригонометрическую функцию и удаляем нолик перед ней, если такой имеется"""
    value = calc.get()
    if value [0]=='0' and len(value)==1:
        value=value[1:]
    calc.delete (0, tk.END)
    calc.insert(0, value+function)

def make_trigonometry_button(function):
    """Создаем кнопку с тригонометрической функцией"""
    TRIG = tk.Button(text=function, bd=5, font=('Times New Roman', 13), fg='green',
                     command=lambda: add_trigonometry(function))
    TRIG_ttp=CreateToolTip(TRIG,"Operaion(value)")
    return TRIG

def memory(task):
    """Эта функция выполняет задачи при нажатии на кнопки работы с памятью"""
    value = calc.get()
    memory = open('memory.txt')
    if task=='MS':
        memory = open('memory.txt', 'w')
        memory.write(value)
    elif task=='MR':
        memory = open('memory.txt', 'r')
        line=memory.read()
        calc.delete(0, tk.END)
        calc.insert(0,line )
    elif task=='MC':
        memory = open('memory.txt', 'w')
        memory.write('0')

    elif task=='M+':
        memory = open('memory.txt', 'r')
        line = memory.read()
        memory = open('memory.txt', 'w')
        num=int(line)+int(value)
        memory.write(str(num))
    elif task == 'M-':
        memory = open('memory.txt', 'r')
        line = memory.read()
        memory = open('memory.txt', 'w')
        num = int(line) - int(value)
        memory.write(str(num))
    memory.close()

def make_memory_button(name):
    '''Осуществляется работа с памятью а именно: запись, чтение, очистка,
    добавление или отнимание к числу в ячейке памяти'''
    return tk.Button(text=name, bd=5, font=('Times New Roman', 13), fg="blue",
                     command=lambda: memory(name))

def statisticcalc(statistic):
    '''эта функция добавляет в строку калькулятора статистическую функцию'''
    value = calc.get()
    calc.delete(0, tk.END)
    if value [0]=='0' and len(value)==1:
        value=value[1:]
    if statistic=="Sum":
        calc.insert(0, value + 'sum(')

    elif statistic=='Average':
        calc.insert(0, value + 'A(')
    elif statistic=='Standart deviation':
        calc.insert(0, value + 'SE(')

def make_static_button(statistic):
    """Эта функция создает статистические кнопки и коментарий к ним"""
    STATISTIC=tk.Button(text=statistic, bd=5, font=('Times New Roman', 13), fg="blue",
                     command=lambda: statisticcalc(statistic))
    STATISTIC_ttp=CreateToolTip(STATISTIC,"Function(value1,value2,value3)")
    return STATISTIC

def constant_button():
    """Эта функция создает новое окно при добавлении константы в строку ввода"""
    fhandle = open('constant.txt')
    OPTIONS  = []
    constants = {}
    for line in fhandle:
       lst = line.split('=')
       OPTIONS.append(lst[0])
       constants[lst[0]]=str(lst[1]).strip()

    master = Tk()
    master.geometry(f'230x200+100+200')
    master.title('Constants')

    variable = StringVar(master)
    variable.set(OPTIONS[0])

    w = OptionMenu(master, variable, *OPTIONS)
    w.pack()

    def ok():
        value = calc.get()
        if value[0] == '0' and len(value) == 1:
            value = value[1:]
        calc.delete(0, tk.END)
        calc.insert(0, value + constants[variable.get()])

    button = Button(master, text="Add", command= ok)
    button.pack()

    master.grid_columnconfigure(0, minsize=60)
    master.grid_columnconfigure(1, minsize=60)
    master.grid_rowconfigure(0, minsize=60)
    master.grid_rowconfigure(1, minsize=60)


    mainloop()

def add_constant_button():
    """Эта функция создает новое окно для создания новой константы """
    constant = Tk()
    constant.geometry(f'300x100+100+200')
    constant.title('Create new constant')
    constant_name = tk.Entry(constant, justify=tk.LEFT, font=('Times New Roman', 15), width=15)  # строка ввода
    constant_name.insert(0, 'Constant:value')
    constant_name.grid(row=0, column=0, columnspan=3, stick='we', padx=5)

    def add_button():
        fhandle = open('constant.txt', 'a+')
        constnew = str(constant_name.get()).split(':')
        line = '\n'+constnew[0] + "=" + constnew[1]
        fhandle.write(line)
        fhandle.close()


    button = Button(constant, text="Add constant", font=('Times New Roman', 13), fg="black",
                    command=lambda: add_button()).grid(row=1, column=(0), columnspan=2, stick='wens', padx=5, pady=5)

    constant.grid_columnconfigure(0, minsize=60)
    constant.grid_columnconfigure(1, minsize=60)
    constant.grid_columnconfigure(2, minsize=60)
    constant.grid_rowconfigure(0, minsize=40)
    constant.grid_rowconfigure(1, minsize=40)
    mainloop()



def history_button(name):
    """Выполняется проверка активирована ли история, если да,
     то она отключается и наоборот"""
    global hist
    if name=='Save calculations':
        if hist==0:
            hist=1
            tk.Button(text='Save calculationsв', bd=5, font=('Times New Roman', 13), fg="green",
                      command=lambda: history_button('Save calculations')).grid(row=1, column=(7), columnspan=2, stick='wens', padx=5, pady=5)
        elif hist==1:
            hist=0
            tk.Button(text='Save calculations', bd=5, font=('Times New Roman', 13), fg="black",
                      command=lambda: history_button('Save calculations')).grid(row=1, column=(7), columnspan=2, stick='wens', padx=5, pady=5)
    else:
        history = open('history.txt', 'w')
        history.write('')


def file_button():
    """Создается окно для записи названия файла и чтение
    выражения из этого файла"""
    file = Tk()
    file.geometry(f'300x100+100+200')
    file.title('Read data')
    file_name = tk.Entry(file, justify=tk.LEFT, font=('Times New Roman', 15), width=15)  # строка ввода
    file_name.insert(0, 'File_name.txt')
    file_name.grid(row=0, column=0, columnspan=3, stick='we', padx=5)
    def read_button():
        name = file_name.get()
        fhandle = open(name, 'r')
        line = fhandle.read()
        calc.delete(0, tk.END)
        calc.insert(0, line)

    button = Button(file, text="Read",font=('Times New Roman', 13), fg="black",
                    command=lambda : read_button()).grid(row=1, column=(0), columnspan=2, stick='wens', padx=5, pady=5)


    mainloop()

win=tk.Tk()
win.geometry(f'700x435+100+200')#размеры окна
win.title('Calculator')

class CreateToolTip(object):
    '''
    Создается всплывающее окно при наведении на кнопки
    '''
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background='grey', relief='solid', borderwidth=1,
                       font=("times", "8", "normal"), fg='white')
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()

calc=tk.Entry(win, justify=tk.RIGHT, font=('Times New Roman', 15), width=15)#строка ввода
calc.insert(0,'0')
calc.grid(row=0, column=0, columnspan=9, stick='we',padx=5)

#цифры
make_digit_button('1').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=5, column=1, stick='wens', padx=5, pady=5)
make_digit_button('.').grid(row=4, column=4, stick='wens', padx=5, pady=5)
make_digit_button('(').grid(row=5, column=0, stick='wens', padx=5, pady=5)
make_digit_button(')').grid(row=5, column=2, stick='wens', padx=5, pady=5)
make_digit_button(',').grid(row=5, column=4, stick='wens', padx=5, pady=5)

#стіорюємо кнопки для додаткових операцій
PERCENT=tk.Button(text='%', bd=5, font=('Times New Roman', 13),
                     command=lambda: add_digit('%'))
PERCENT.grid(row=2, column=5, stick='wens', padx=5, pady=5)
PERCENT_ttp=CreateToolTip(PERCENT,'number+-*/(percent)%')
SQRT=tk.Button(text='sqrt', bd=5, font=('Times New Roman', 13),
                     command=lambda: add_digit('sqrt'))
SQRT.grid(row=3, column=5, stick='wens', padx=5, pady=5)
SQRT_ttp=CreateToolTip(SQRT, "sqrt(value)")
FACTORIAL=tk.Button(text='!', bd=5, font=('Times New Roman', 13),
                     command=lambda: add_digit('!'))
FACTORIAL.grid(row=4, column=5, stick='wens', padx=5, pady=5)
FACTORIAL_ttp=CreateToolTip(FACTORIAL,'(value)!')
LOGARIFM=tk.Button(text='log', bd=5, font=('Times New Roman', 13),
                     command=lambda: add_digit('log'))
LOGARIFM.grid(row=5, column=5, stick='wens', padx=5, pady=5)
LOGARIFM_ttp=CreateToolTip(LOGARIFM,"log(value,base)")
EXPONENT=tk.Button(text='^', bd=5, font=('Times New Roman', 13),
                     command=lambda: add_digit('^'))
EXPONENT.grid(row=3, column=4, stick='wens', padx=5, pady=5)
EXPONENT_ttp=CreateToolTip(EXPONENT,'(value)^(power)')

#операции
make_operation_button('+').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=5, column=3, stick='wens', padx=5, pady=5)



#тригонометрические функции
make_trigonometry_button('sin').grid(row=2, column=(6), stick='wens', padx=5, pady=5)
make_trigonometry_button('cos').grid(row=3, column=(6), stick='wens', padx=5, pady=5)
make_trigonometry_button('tg').grid(row=4, column=(6), stick='wens', padx=5, pady=5)
make_trigonometry_button('ctg').grid(row=5, column=(6), stick='wens', padx=5, pady=5)
make_trigonometry_button('arcsin').grid(row=2, column=(7), stick='wens', padx=5, pady=5)
make_trigonometry_button('arccos').grid(row=3, column=(7), stick='wens', padx=5, pady=5)
make_trigonometry_button('arctg').grid(row=4, column=(7), stick='wens', padx=5, pady=5)
make_trigonometry_button('arcctg').grid(row=5, column=(7), stick='wens', padx=5, pady=5)

#cтатистические расчеты
make_static_button('Sum').grid(row=6, column=(4), stick='wens', padx=5, pady=5)
make_static_button('Average').grid(row=6, column=(0), columnspan=4, stick='wens', padx=5, pady=5)
make_static_button('Standart deviation').grid(row=7, column=(0),columnspan=4, stick='wens', padx=5, pady=5)


#кнопка "равно"
make_calc_button('=').grid(row=2, column=4, stick='wens', padx=5, pady=5)
#кнопка "очистить всё"
make_clear_button('C').grid(row=1, column=5, stick='wens', padx=5, pady=5)
#кнопка "удалить последний елемент"
make_clearlast_button('AC').grid(row=1, column=6, stick='wens', padx=5, pady=5)

#кнопки работы с памятью
make_memory_button('MS').grid(row=1, column=(0), stick='wens', padx=5, pady=5)
make_memory_button('MR').grid(row=1, column=(1), stick='wens', padx=5, pady=5)
make_memory_button('MC').grid(row=1, column=(2), stick='wens', padx=5, pady=5)
make_memory_button('M+').grid(row=1, column=(3), stick='wens', padx=5, pady=5)
make_memory_button('M-').grid(row=1, column=(4), stick='wens', padx=5, pady=5)

tk.Button(text='Save calculations', bd=5, font=('Times New Roman', 13), fg="black",
          command=lambda: history_button('Save calculations')).grid(row=1, column=(7), columnspan=2, stick='wens', padx=5, pady=5)
tk.Button(text='Clean the calculation history', bd=5, font=('Times New Roman', 13), fg="black",
          command=lambda: history_button('Clean the calculation history')).grid(row=6, column=(7), columnspan=2, stick='wens', padx=5, pady=5)


tk.Button(text='+File', bd=5, font=('Times New Roman', 13), fg="black",
          command=lambda: file_button()).grid(row=2, column=(8),columnspan=1, stick='wens', padx=5, pady=5)

#кнопки для работы с константами
CONSTANTS=tk.Button(text='Constants', bd=5, font=('Times New Roman', 13),fg="red",
                     command=lambda: constant_button())
CONSTANTS.grid(row=6, column=(5),columnspan=2, stick='wens', padx=5, pady=5)
CONSTANTS_ttp=CreateToolTip(CONSTANTS,'Paste constant')

ADDCONSTANTS=tk.Button(text='Add new const', bd=5, font=('Times New Roman', 13), fg="red",
                     command=lambda: add_constant_button())
ADDCONSTANTS.grid(row=7, column=(5),columnspan=2, stick='wens', padx=5, pady=5)
ADDCONSTANTS_ttp=CreateToolTip(ADDCONSTANTS,'Add constant')

#размер в ширину
win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)
win.grid_columnconfigure(5, minsize=60)
win.grid_columnconfigure(6, minsize=60)
win.grid_columnconfigure(7, minsize=80)
win.grid_columnconfigure(8, minsize=60)

#размер в высоту
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)
win.grid_rowconfigure(6, minsize=60)

win.mainloop()