# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:36:32 2023

@author: HP
"""

import pandas as pd


schoolmets=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\schoolmets_names.xlsx",header=None)
# schoolmets=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\schoolmets_names.xlsx")
schoolmets.shape
schoolmets.shape[0:3,0:1]
schoolmets[0:2]
schoolmets[1:7]
collegemets=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\collegemets_names.xlsx")
schoolmets.merge(collegemets,on='name',how='inner')
schoolmets.merge(collegemets,on='name',how='outer')
schoolmets.merge(collegemets,on='name',how='left')
schoolmets.merge(collegemets,on='name',how='right')



familymembers=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\FatherFamily_members.xlsx")
mothermembers=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\motherFamily_members.xlsx")
familymembers.merge(mothermembers,on='relation',how='inner')
familymembers.merge(mothermembers,on='relation',how='outer')
familymembers.merge(mothermembers,on='relation',how='left')
familymembers.merge(mothermembers,on='relation',how='right')



dal_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\dal_items.xlsx")
veg_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\VEG_FOOD_ITEMS.xlsx")
dal_items.merge(veg_items,on='Taste',how='inner')
dal_items.merge(veg_items,on='Taste',how='outer')
dal_items.merge(veg_items,on='Taste',how='left')
dal_items.merge(veg_items,on='Taste',how='right')



soups=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\soup_items.xlsx")
fries=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\fry_items.xlsx")
soups.merge(fries,on='taste',how='inner')
soups.merge(fries,on='taste',how='outer')
soups.merge(fries,on='taste',how='left')
soups.merge(fries,on='taste',how='right')



chicken_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\Chicken_items.xlsx")
mutton_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\mutton_items.xlsx")
chicken_items.merge(mutton_items,on='taste',how='inner')
chicken_items.merge(mutton_items,on='taste',how='outer')
chicken_items.merge(mutton_items,on='taste',how='left')
chicken_items.merge(mutton_items,on='taste',how='right')



winter=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\winterseason_names.xlsx")
summer=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\summerseason_names.xlsx")
rainy=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\rainyseason_names.xlsx")
winter.merge(summer,on='season',how='inner').merge(rainy,on='season',how='inner')
winter.merge(summer,on='season',how='outer').merge(rainy,on='season',how='outer')
winter.merge(summer,on='season',how='left').merge(rainy,on='season',how='left')
winter.merge(summer,on='season',how='right').merge(rainy,on='season',how='right')



red=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\red_colour.xlsx")
white=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\whiteflowers_names.xlsx")
pink=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\pinkflowers_names.xlsx")
yellow=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\yellowflowers_names.xlsx")
red.merge(white,on='colour',how='inner').merge(pink,on='colour',how='inner').merge(yellow,on='colour',how='inner')
red.merge(white,on='colour',how='outer').merge(pink,on='colour',how='outer').merge(yellow,on='colour',how='outer')
red.merge(white,on='colour',how='left').merge(pink,on='colour',how='left').merge(yellow,on='colour',how='left')
red.merge(white,on='colour',how='right').merge(pink,on='colour',how='right').merge(yellow,on='colour',how='right')
