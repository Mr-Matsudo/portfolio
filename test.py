'''
Created on 2020/09/24

@author: madcrazy
'''
# coding: utf-8
# Your code here!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter
#from tkinter import ttk
import random
#import time
from tkinter.scrolledtext import ScrolledText






#foods=["キャベツ","にんじん","とうもろこし","ごぼう","豚肉","牛肉"]
#seasonings=["砂糖","塩","醤油","酢","みりん","酒","ケチャップ","片栗粉","小麦粉","マヨネーズ","ぽん酢"]


def crowling(foods,seasonings):
    result_window=tkinter.Tk()
    result_window.title("検索結果")

    #scroll=tkinter.Scrollbar(result_window)
    #scroll.pack(side="right",fill="y")
    textarea=ScrolledText(result_window)
    textarea.pack()
    #scroll.config(command=textarea.yview)
#print(choice_3(foods))
    options=Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(
        executable_path='./chromedriver.exe',
        chrome_options=options)

    driver.get('https://cookpad.com/')
    #time.sleep(3)
    explorer=driver.find_element_by_id("keyword")
    word=' '.join(random.sample(foods,2))
    #print(word)
    textarea.insert('end',word+"\n")
    explorer.send_keys(word)
    explorer.submit()
    #print("検索実行")
    textarea.insert('end',"検索実行"+"\n")
    #time.sleep(3)
    results =driver.find_elements_by_css_selector('a.recipe-title:link')
    #print(str(len(results)))
    results_url=[]
    dishes=[]
    for result in results:
        dishes.append(result.text)
        results_url.append(result.get_attribute('href'))
        i=0
    for result in results:
        #time.sleep(1)
        #print("移動します")
        driver.get(results_url[i])
        #time.sleep(2)
        ingredients=driver.find_elements_by_class_name('ingredient_name')
        less=[]
        all_count=0.0
        hit_count=0.0
        #print("食材数"+str(len(ingredients)))
        for ing in ingredients:
            ingredient=ing.text
            #print(ingredient+"はあるか？")
            all_count +=1                          #ingredientsの要素を抽出
            seas_be = False
            food_be = False
            for seasoning in seasonings:
                if(seasoning in ingredient):    #手持ちのseasoningにあるかどうか一つずつ確認
                    seas_be=True
                    hit_count+=1
                    #print("調味料にあった")
                    break
            if not seas_be:
                for food in foods:
                    if(food in ingredient):
                        food_be=True
                        hit_count+=1
                        #print("食材にあった")
                        break
            if not food_be and not seas_be :                     #手持ちのシーズニングになかった
                less.append(ingredient)
        #print(str(all_count))
        #print(str(hit_count))
        hit_rate=int(hit_count/all_count*100)
        #print(dishes[i])
        textarea.insert('end',dishes[i]+"\n")
        #print(results_url[i])
        textarea.insert('end',results_url[i]+"\n")
        if hit_rate == 100:
            #print("手持ちの食材でできる！")
            textarea.insert("手持ちの食材でできる"+"\n")
        else :
            #print("食材一致率："+str(hit_rate)+"％足りない食材",end="")
            textarea.insert('end',"食材一致率："+str(hit_rate)+"％足りない食材"+"\n")
            #print(less)
            textarea.insert('end',','.join(less)+"\n")
            #print()
        textarea.insert('end',"------------------"+"\n")
        i +=1
        if i>=10:
            break
        #time.sleep(2)
        driver.back()
    driver.close()
    result_window.mainloop()

#crowling(foods, seasonings)
