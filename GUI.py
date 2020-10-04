'''
Created on 2020/09/25

@author: madcrazy
'''
import tkinter
from tkinter import ttk, StringVar
import test

def result():
    for i in range(len(seas_bln)):
        if len(seas_bln[i].get())>0:
            seasonings.append(seas[i])
    result_window=tkinter.Tk()
    result_window.title("検索結果")
    for name in seasonings:
        label=ttk.Label(
            result_window,
            text=name
            )
        label.pack()
    Foods=foods_entry.get().split("　")
    print(Foods)
    for name in Foods:
        label=ttk.Label(
            result_window,
            text=name
            )
        label.pack()

def explore():
    for i in range(len(seas_bln)):
        if len(seas_bln[i].get())>0:
            seasonings.append(seas[i])
    foods=foods_entry.get().split("　")
    print(seasonings)
    print(foods)
    test.crowling(foods,seasonings)

window=tkinter.Tk()
window.title("料理検索")
#window.geometry("500x120")

seas=["砂糖","塩","酢","しょうゆ","みそ","酒","みりん","ポン酢","マヨネーズ","ケチャップ","中濃ソース","胡椒","だし","レモン汁"]
seas_bln=[]
seasonings=[]

for i in range(len(seas)):
    seas_bln.append(StringVar())
    #spice=seas[i]
    Check=ttk.Checkbutton(
        window,text = seas[i],
        onvalue=seas[i], offvalue="",
        variable=seas_bln[i]
        )
    Check.pack()

foods_entry=ttk.Entry(
    window
    )
foods_entry.pack()
enter=ttk.Button(
    window,
    text="検索",
    command=lambda: explore()
    )
enter.pack()
window.mainloop()
