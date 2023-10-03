#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = int(input("Kilonuzu giriniz(kg): "))
print(x)

y = float(input("Boyunuzu giriniz(m): "))
print(y)


if x /(y**2) < 18.5:
     print("İdeal kilonun altındasınız!")

elif 18.5 < x /(y**2) < 24.9:
     print("İdeal kilodasınız!")

elif 25 < x /(y**2) < 29.9:
     print("İdeal kilonun üstündesiniz!")

elif 30 < x /(y**2) < 39.9:
     print("Obezsiniz!")

else:
     print("Morbid Obezsiniz!")


print("Vücut Kitle Endeksiniz Başarıyla Ölçülmüştür! Sağlıklı Günler Dileriz!")


# In[ ]:




