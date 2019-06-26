import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
dt=pd.read_csv("data.csv")
print(dt)
reg = linear_model.Ridge()
reg.fit(dt[["Konum","AkademikYayinSayisi","AkademikYayinDerecesi","OgrenciSeviyesi","DersSaati","DonemlikStaj"]],dt.sr)
sonuc=int(reg.predict([[10,40,3,10,35,0]]))
print("\n TAHMİNİ SIRALAMA :" , sonuc)
