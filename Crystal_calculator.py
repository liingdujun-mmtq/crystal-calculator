import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import END
import numpy as np
from tkinter import filedialog
import icon,base64,os
from icon import Icon

def RemoveNoNumberd(content):
    val=content
    val= ''.join([c for c in val if c in '-1234567890.e'])
    return val

def cos(x):
    return np.cos(x/180*np.pi)
def sin(x):
    return np.sin(x/180*np.pi)


def cal_d(h,k,l):
    S11=b**2*c**2*(sin(alpha))**2
    S22=a**2*c**2*(sin(beta))**2
    S33=a**2*b**2*(sin(gamma))**2
    S12=a*b*c**2*(cos(alpha)*cos(beta)-cos(gamma))
    S23=a**2*b*c*(cos(beta)*cos(gamma)-cos(alpha))
    S13=a*b**2*c*(cos(gamma)*cos(alpha)-cos(beta))
    V=a*b*c*np.sqrt(1-(cos(alpha))**2-(cos(beta))**2-(cos(gamma))**2+2*cos(alpha)*cos(beta)*cos(gamma))
    g2=(S11*h**2+S22*k**2+S33*l**2+2*S12*h*k+2*S23*k*l+2*S13*l*h)/V**2
    d=1/np.sqrt(g2)
    return [d,S11,S22,S33,S12,S13,S23,V]

def d_window():
    d_win=tk.Tk()
    d_win.title('d list')
    with open('logo_tmp.ico','wb') as tmp:
        tmp.write(base64.b64decode(Icon().img))
    d_win.iconbitmap('logo_tmp.ico')
    os.remove('logo_tmp.ico')
    #tk.Label(d_win,text="d list:").grid(row=0,column=0,columnspan=3,sticky="w")
    message=[]
    MessageBox=scrolledtext.ScrolledText(d_win, width=80,height=40)
    MessageBox.grid(row=1,column=0,columnspan=3,sticky="w")
    if alpha==90 and beta==90 and gamma==90:
        if a==b and a==c:
            for h in range(5):#立方
                for k in range(h+1):
                    for l in range(k+1):
                        if h!=0 or k!=0 or l!=0:
                            d=a/np.sqrt(h**2+k**2+l**2)
                            message.append([h,k,l,d,1/d])                            
        elif a!=b and b!=c and c!=a:  #正交         
            for h in range(5):
                for k in range(5):
                    for l in range(5):
                        if h!=0 or k!=0 or l!=0:
                            d=np.sqrt(1/(h**2/a**2+k**2/b**2+l**2/c**2))
                            message.append([h,k,l,d,1/d])

        #四方        
        elif a==b:
            for h in range(5):
                for k in range(h+1):
                    for l in range(5):
                        if h!=0 or k!=0 or l!=0:
                            d=a/np.sqrt(h**2+k**2+l**2/(c/a)**2)
                            message.append([h,k,l,d,1/d])
        elif b==c:
            for h in range(5):
                for k in range(5):
                    for l in range(k+1):
                        if h!=0 or k!=0 or l!=0:
                            d=b/np.sqrt(h**2/(a/b)**2+k**2+l**2)
                            message.append([h,k,l,d,1/d])
        elif a==c:
            for h in range(5):
                for k in range(5):
                    for l in range(h+1):
                        if h!=0 or k!=0 or l!=0:
                            d=a/np.sqrt(h**2+k**2/(b/a)**2+l**2)
                            message.append([h,k,l,d,1/d])
    else:
        for h in range(-4,5):
            for k in range(-4,5):
                for l in range(-4,5):
                    if h!=0 or k!=0 or l!=0:
                        res=cal_d(h,k,l)
                        d=res[0]
                        message.append([h,k,l,d,1/d])
        
            
    sortmessage=sorted(message,key=(lambda x:[x[3],x[0],x[1],x[2]]),reverse=True)
    outputmessage=[]
    for i in sortmessage:
        if [-i[0],-i[1],-i[2],i[3],i[4]] not in outputmessage:
            outputmessage.append(i)
    MessageBox.insert(END, "Crystal calculator by LingDuJun \n")
    MessageBox.insert(END, "================================================= \n")
    init_message="Latice: a=%.3f b=%.3f c=%.3f alpha=%.2f° beta=%.2f° gamma=%.2f° \n" %(a,b,c,alpha,beta,gamma)
    MessageBox.insert(END, init_message)
    MessageBox.insert(END, "================================================= \n")
    MessageBox.insert(END,"( h, k, l), d=      , d*=     \n")
    for i in outputmessage:
        MessageBox.insert(END,"(%2d,%2d,%2d), d= %5.3f, d*=%5.3f \n" %(i[0],i[1],i[2],i[3],i[4]))


def main_window():
    root=tk.Tk()
    root.title('Crystal calculator v1.2 by LingDuJun')
    with open('logo_tmp.ico','wb') as tmp:
        tmp.write(base64.b64decode(Icon().img))
    root.iconbitmap('logo_tmp.ico')
    os.remove('logo_tmp.ico')
    # hkl
    set_hkl=tk.Frame(root)
    set_hkl.pack(anchor='w')
    tk.Label(set_hkl,text="").grid(row=0,column=0,columnspan=3,sticky="w")
    
    tk.Label(set_hkl,text="Set H1 K1 L1:").grid(row=1,column=0,columnspan=3,sticky="w")
    tk.Label(set_hkl,text="Theta:",width=8).grid(row=1,column=4,sticky="w")
    Show_theta=tk.Entry(set_hkl,textvariable=tk.StringVar(root,value="0.00"),width=10,justify='right')
    Show_theta.grid(row=1,column=5,sticky="w")

    tk.Label(set_hkl,text="H1:",width=8).grid(row=2,column=0)
    H1=tk.Entry(set_hkl,textvariable=tk.StringVar(root,value="1"),width=10,justify='right')
    H1.grid(row=2,column=1)
    tk.Label(set_hkl,text="K1:",width=8).grid(row=2,column=2)
    K1=tk.Entry(set_hkl,textvariable=tk.StringVar(root,value="0"),width=10,justify='right')
    K1.grid(row=2,column=3)
    tk.Label(set_hkl,text="L1:",width=8).grid(row=2,column=4)
    L1=tk.Entry(set_hkl,textvariable=tk.StringVar(root,value="0"),width=10,justify='right')
    L1.grid(row=2,column=5)

    tk.Label(set_hkl,text="Set H2 K2 L2:").grid(row=3,column=0,columnspan=3,sticky="w")

    tk.Label(set_hkl,text="H2:",width=8).grid(row=4,column=0)
    H2=tk.Entry(set_hkl,textvariable=tk.StringVar(root,value="1"),width=10,justify='right')
    H2.grid(row=4,column=1)
    tk.Label(set_hkl,text="K2:",width=8).grid(row=4,column=2)
    K2=tk.Entry(set_hkl,textvariable=tk.StringVar(root,value="0"),width=10,justify='right')
    K2.grid(row=4,column=3)
    tk.Label(set_hkl,text="L2:",width=8).grid(row=4,column=4)
    L2=tk.Entry(set_hkl,textvariable=tk.StringVar(root,value="0"),width=10,justify='right')
    L2.grid(row=4,column=5)
    
    tk.Label(set_hkl,text="",width=2).grid(row=4,column=6,sticky="w")
    tk.Label(set_hkl,text="").grid(row=5,column=0,columnspan=3,sticky="w")

    # abc
    set_abc=tk.Frame(root)
    set_abc.pack(anchor='w')
    tk.Label(set_abc,text="Set abcαβγ:").grid(row=1,column=0,columnspan=3,sticky="w")
    
    tk.Label(set_abc,text="a:",width=8).grid(row=2,column=0)
    A=tk.Entry(set_abc,textvariable=tk.StringVar(root,value="2.86"),width=10,justify='right')
    A.grid(row=2,column=1)
    tk.Label(set_abc,text="b:",width=8).grid(row=2,column=2)
    B=tk.Entry(set_abc,textvariable=tk.StringVar(root,value="2.86"),width=10,justify='right')
    B.grid(row=2,column=3)
    tk.Label(set_abc,text="c:",width=8).grid(row=2,column=4)
    C=tk.Entry(set_abc,textvariable=tk.StringVar(root,value="2.86"),width=10,justify='right')
    C.grid(row=2,column=5)
    tk.Label(set_abc,text="alpha:",width=8).grid(row=3,column=0)
    Alpha=tk.Entry(set_abc,textvariable=tk.StringVar(root,value="90"),width=10,justify='right')
    Alpha.grid(row=3,column=1)
    tk.Label(set_abc,text="beta:",width=8).grid(row=3,column=2)
    Beta=tk.Entry(set_abc,textvariable=tk.StringVar(root,value="90"),width=10,justify='right')
    Beta.grid(row=3,column=3)
    tk.Label(set_abc,text="gamma:",width=8).grid(row=3,column=4)
    Gamma=tk.Entry(set_abc,textvariable=tk.StringVar(root,value="90"),width=10,justify='right')
    Gamma.grid(row=3,column=5)
    tk.Label(set_abc,text="").grid(row=4,column=0,columnspan=3,sticky="w")

    def get_data():
        global a
        a=float(RemoveNoNumberd(A.get()))
        global b
        b=float(RemoveNoNumberd(B.get()))
        global c
        c=float(RemoveNoNumberd(C.get()))
        global alpha
        alpha=float(RemoveNoNumberd(Alpha.get()))
        global beta
        beta=float(RemoveNoNumberd(Beta.get()))
        global gamma
        gamma=float(RemoveNoNumberd(Gamma.get()))
        global h1
        h1=int(RemoveNoNumberd(H1.get()))
        global k1
        k1=int(RemoveNoNumberd(K1.get()))
        global l1
        l1=int(RemoveNoNumberd(L1.get()))
        global h2
        h2=int(RemoveNoNumberd(H2.get()))
        global k2
        k2=int(RemoveNoNumberd(K2.get()))
        global l2
        l2=int(RemoveNoNumberd(L2.get()))        
    def get_d():
        get_data()
        if a*b*c==0:
            messagebox.showerror(title="Error", message="Error:Wrong lattice!")
        elif alpha*beta*gamma==0:
            messagebox.showerror(title="Error", message="Error! Wrong angle!")
        else:
            d_window()
    def get_theta():
        get_data()
        if a*b*c==0:
            messagebox.showerror(title="Error", message="Error:Wrong lattice!")
        elif alpha*beta*gamma==0:
            messagebox.showerror(title="Error", message="Error! Wrong angle!")
        else:
                
            res1=cal_d(h1,k1,l1)
            res2=cal_d(h2,k2,l2)
            d1=res1[0]
            d2=res2[0]
            S11=res1[1]
            S22=res1[2]
            S33=res1[3]
            S12=res1[4]
            S13=res1[5]
            S23=res1[6]
            V=res1[7]
            cos_theta=(S11*h1*h2+S22*k1*k2+S33*l1*l2+S23*(k1*l2+k2*l1)+S13*(l1*h2+l2*h1)+S12*(h1*k2+h2*k1))*d1*d2/V**2
            theta=np.arccos(cos_theta)/np.pi*180
            Show_theta.delete(0, END)
            Show_theta.insert(0, "%4.2f°" %(theta))

    # find data from inut str
    def load_abc(input_str):
        str_split=input_str.split(' ')
        str_split=[j for j in str_split if j!='']
        output_data=float(str_split[1].replace('(','').replace(')',''))
        return output_data


    # read abc from cif
    def import_cif():
        cif_path=filedialog.askopenfilename()
        with open(cif_path) as cif_data:
            lines=cif_data.readlines()
            a=0
            b=0
            c=0
            alpha=0
            beta=0
            gamma=0
            for i in lines:
                if "_cell_length_a" in i:
                    a=load_abc(i)
                if "_cell_length_b" in i:
                    b=load_abc(i)
                if "_cell_length_c" in i:
                    c=load_abc(i)
                if "_cell_angle_alpha" in i:
                    alpha=load_abc(i)
                if "_cell_angle_beta" in i:
                    beta=load_abc(i)
                if "_cell_angle_gamma" in i:
                    gamma=load_abc(i)
        A.delete(0, END)
        A.insert(0, "%4.3f" %(a))
        B.delete(0, END)
        B.insert(0, "%4.3f" %(b))
        C.delete(0, END)
        C.insert(0, "%4.3f" %(c))
        Alpha.delete(0, END)
        Alpha.insert(0, "%4.3f" %(alpha))
        Beta.delete(0, END)
        Beta.insert(0, "%4.3f" %(beta))
        Gamma.delete(0, END)
        Gamma.insert(0, "%4.3f" %(gamma))
    
    
    #command
    Command=tk.Frame(root)
    Command.pack(anchor="c")
    

    tk.Button(Command, text = "Import cif", command = import_cif,width=15,height=3).grid(row = 0, column = 0)
    tk.Button(Command, text = "Get d-list", command = get_d,width=15,height=3).grid(row = 0, column = 1)
    tk.Label(Command,text="").grid(row=0,column=1,sticky="w")
    tk.Button(Command, text = "Get Theta", command = get_theta,width=15,height=3).grid(row = 0, column =2)
    tk.Label(Command,text="").grid(row=1,column=1,sticky="w")
    
    root.mainloop()

main_window()

