from tkinter import *
import tkinter.filedialog as ft
import tkinter.messagebox as tmb
import os
#opening tk
global text
root=Tk("Text Editor")
text=Text(root, wrap='word',undo=1)
root.title("Text Editor")
#displaying messagebox for help and about option
def display_about_messagebox(event=None):
	tmb.showinfo( title="About", message="This is Text Editor Made as a part of SPCC Project By Students From FRCRCE")

def display_help_messagebox(event=None):
    tmb.showinfo( "Help", "Help Book: \n Visit this site for more Information about the Text Editor", icon='question')


#highlight features

def highlight(interval=100):
	text.tag_remove("active_line", 1.0, "end")
	text.tag_add("active_line", "insert linestart", "insert lineend+1c")
	text.after(interval,toggle_highlight)

def remove_highlight():
	text.tag_remove("active_line",1.0,"end")

def toggle_highlight(event=None):
	if show_highlight.get():
		highlight()
	else:
		remove_highlight()
#highlight feature ends

#show cursor feature

def show_cursor_info_bar():
    show_cursor_info_checked = show_cursor.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
    else:
        cursor_info_bar.pack_forget()


def update_cursor_info_bar(event=None):
    row, col = text.index(INSERT).split('.')
    line_num, col_num = str(int(row)), str(int(col) + 1)  # col starts at 0
    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
    cursor_info_bar.config(text=infotext)


#show cursor feature ends	
	
#new File
def newDoc(event=None):
	root.title("Untitled")
	global file_name
	file_name = None
	content_text.delete(1.0, END)
	on_content_changed()
#saving file
def saveas(event=None):
	
	t=text.get("1.0","end-1c")
	savelocation=ft.asksaveasfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
	file1=open(savelocation,"w+")
	file1.write(t)
	global file_name
	file_name=savelocation
	root.title('{} - {}'.format(os.path.basename(savelocation), "Text Editor"))
	file1.close()
def save(event=None):
	global file_name
	if not file_name:
		save_as()
	else:
		t=text.get("1.0","end-1c")
		file1=open(file_name,"w+")
		file1.write(t)
	return "break"
def openas(event=None):
	input_file_name = ft.askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
	if input_file_name:
		global file_name
		file_name = input_file_name
		root.title('{} - {}'.format(os.path.basename(file_name), "Text Editor"))
		text.delete(1.0, END)
		file=open(input_file_name,'r')
		if file!='':
			try:
				txt=file.read()
			except:
				tmb.showwarning("Invalid","Please select a valid file to open")
			text.insert(INSERT, txt)
		else:
			pass
	on_content_changed()
	
"""
	input_file_name = ft.askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
	if input_file_name:
		global file_name
		file_name = input_file_name
		root.title('{} - {}'.format(os.path.basename(file_name), "Text Editor"))
		text.delete(1.0, END)
		file=open(input_file_name,'r')
		if file!='':
			txt=file.read()
			text.insert(INSERT, txt)
		else:
			pass
	on_content_changed()

	
	text.delete(1.0, END)
	global file_name
	openfiles=ft.askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
	file=open(openfiles,'r')
	if file!='':
		txt=file.read()
		text.insert(INSERT, txt)
		file_name=openfiles
		root.tiltle('{} -{}'.format(os.path.basename(openfiles),"Text Editor"))
	else:
		pass
	on_content_changed()
"""
#implementing cut, copy, paste, delete, selectAll, undo, redo, newFile, close, exit
def cut():
	text.event_generate("<<Cut>>")
	on_content_changed()
def copy():
    text.event_generate("<<Copy>>")
def paste():
	text.event_generate("<<Paste>>")
	on_content_changed()
def delete():
	text.event_generate("<<Delete>>")
	on_content_changed()
def selectAll():
    text.event_generate("<<SelectAll>>")
	
def undo():
	text.event_generate("<<Undo>>")
	on_content_changed()
def redo():
	text.event_generate("<<Redo>>")
	on_content_changed()
def newDoc():
	text.event_generate("<<New>>")
def close():
	text.event_generate("<<Close>>")
def exit():
	if tmb.askokcancel("Quit?", "Really quit?"):
		root.destroy()

#find option 


#find method ends

def on_content_changed(event=None):
    update_line_numbers()
#displaying number line_number_bar

def update_line_numbers(event = None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')

def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col = text.index("end").split('.')
        for i in range(1, int(row)):
            output +=  str(i)+ '\n'
    return output


#displaying number line end
"""#button.grid(row=1,column=0,sticky=W);button1.grid(row=1,column=2,sticky=W);
button.pack(side=TOP)
button1.pack(side=TOP)
"""
new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/openas.gif')
save_file_icon = PhotoImage(file='icons/saveas.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')
#icons bar

shortcut_bar = Frame(root,  height=25)
shortcut_bar.pack(expand='no', fill='x')
newFile_Button = Button(shortcut_bar, image=new_file_icon, command=newDoc)
openFile_Button = Button(shortcut_bar, image=open_file_icon, command=openas)
saveFile=Button(shortcut_bar,image=save_file_icon,command=save)
cutButton=Button(shortcut_bar,image=cut_icon,command=cut)
copyButton=Button(shortcut_bar,image=copy_icon,command=copy)
pasteButton=Button(shortcut_bar,image=paste_icon,command=paste)

newFile_Button.pack(side='left')
openFile_Button.pack(side='left')
saveFile.pack(side='left')
cutButton.pack(side='left')
copyButton.pack(side='left')
pasteButton.pack(side='left')

#icon bar ends
#Menu Bar starts
menubar = Menu(root)

#file Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=newDoc)
filemenu.add_command(label="Open", command=openas)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as...", command=saveas)
filemenu.add_command(label="Close", command=close)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)

#sub options in View option
viewmenu = Menu(menubar, tearoff=0)
show_line_number = IntVar()
show_line_number.set(1)
viewmenu.add_checkbutton(label="Show Line Number", variable=show_line_number, command=update_line_numbers)
show_cursor=  IntVar()
show_cursor.set(1)
viewmenu.add_checkbutton(label="Show Cursor Location at Bottom", variable=show_cursor,command=update_cursor_info_bar)
show_highlight = BooleanVar()
viewmenu.add_checkbutton(label="HighLight Current Line", onvalue=1, offvalue=0, variable=show_highlight, command=toggle_highlight)
viewmenu.add_command(label="Themes", command=saveas)
viewmenu.add_separator()

#creating view option
menubar.add_cascade(label="View", menu=viewmenu)
#Edit Menu 
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=undo)
editmenu.add_command(label="Redo", command=redo)
editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=cut)
editmenu.add_command(label="Copy",accelerator="Ctrl+C", command=copy)
editmenu.add_command(label="Paste",accelerator="Ctrl+V", command=paste)
editmenu.add_command(label="Delete",accelerator="del", command=delete)
editmenu.add_command(label="Select All",accelerator="Ctrl+A", command=selectAll)
editmenu.add_command(label="Find",accelerator="Ctrl+F",command=saveas)
menubar.add_cascade(label="Edit", menu=editmenu)
#Help Menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=display_help_messagebox)
helpmenu.add_command(label="About...", command=display_about_messagebox)
menubar.add_cascade(label="Help", menu=helpmenu)
#MenuBar Ends

#Line Bar
line_number_bar = Text(root, width=4, padx=3, takefocus=0, border=0,background='khaki', state='disabled', wrap='none')
line_number_bar.pack(side='left', fill='y')
"""
#ScrollBar
scroll_bar=Scrollbar(text)
#ScrollBar ends
"""
#cursor info
cursor_info_bar = Label(text, text='Line: 1 | Column: 1')
cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
#context Menu
def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)
popup_menu = Menu(text)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
    cmd = eval(i)
    popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
popup_menu.add_command(label='Select All', underline=7, command=selectAll)
text.bind('<Button-3>', show_popup_menu)
text.focus_set()




#context Menu Ends






#executing code
text.bind('<Any-KeyPress>', on_content_changed)
text.tag_configure('active_line', background='ivory2')
root.geometry('500x450')
root.config(menu=menubar)

text.pack(expand="yes", fill='both')
#scroll_bar.config(comand=text.yview)
line_number_bar.config()
#scroll_bar.pack(side='right',fill='y')
root.mainloop()