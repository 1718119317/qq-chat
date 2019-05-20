import tkinter
from tkinter import ttk
from client.client_socket import ClientSocket
from tkinter.messagebox import *

# from PIL import Image,ImageTk
class AddFrend(ClientSocket):
    def __init__(self,uname):
        super().__init__()
        self.uname = uname
        self.window_obj_list.append(self)
        self.root=tkinter.Tk()
    
    def show(self):
        root=self.root
        root.title("add_friend")
        root.geometry("300x600+1000+0")
        
        # im=Image.open("color.jpg")
        # img=ImageTk.PhotoImage(im)
        # imLabel=tkinter.Label(root,image=img).pack()

        frm=tkinter.Frame(root,width=300,height=600)
        frm.pack()


        self.search=tkinter.Entry(frm)
        self.search.pack(anchor='w')
        
        label_search=tkinter.Label(frm,text="搜索")
        label_search.bind("<Button-1>", self.search_by_name)
        label_search.pack(anchor='e')

        global listbox_show
        listbox_show=tkinter.Listbox(frm)
        listbox_show.pack()
        root.mainloop()

    #发送好友请求
    def send_friend_request(self):
        user_uname="zhang"
        msg = 'AF ' + self.uname + ' ' + user_uname+" 我是XXX,想添加你为好友!"
        self.sockfd.send(msg.encode())

    #发送要搜索的用户名
    def search_by_name(self,event):
        user_uname = self.search.get()
        msg = 'SU ' + self.uname + ' ' + user_uname
        self.sockfd.send(msg.encode())

    #显示好友搜索的结果,handle_response调用
    def show_search(self,res):
        for item in res:
            tkinter.Label(listbox_show, text=item).pack()



if __name__ == '__main__':
    add=AddFrend("zs")
    add.show()