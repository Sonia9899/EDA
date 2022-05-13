#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('orders_2016-2020_Dataset.csv')


# In[3]:


df.info()


# In[ ]:


from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='most_frequent', missing_values=np.nan)
imputer = imputer.fit(df[['Payment Date and Time Stamp','Fulfillment Date and Time Stamp']])
df[['Payment Date and Time Stamp','Fulfillment Date and Time Stamp']] = imputer.transform(df[['Payment Date and Time Stamp','Fulfillment Date and Time Stamp']])
    


# In[ ]:


imputer = SimpleImputer(strategy='most_frequent', missing_values=np.nan)
imputer = imputer.fit(df[['Tax Method', 'Coupon Code','Coupon Code Name','Billing Name','Billing Country','Billing Street Address','Billing Street Address 2','Billing City','Billing State','Billing Zip','Shipping Street Address']])
df[['Tax Method', 'Coupon Code','Coupon Code Name','Billing Name','Billing Country','Billing Street Address','Billing Street Address 2','Billing City','Billing State','Billing Zip','Shipping Street Address']] = imputer.transform(df[['Tax Method', 'Coupon Code','Coupon Code Name','Billing Name','Billing Country','Billing Street Address','Billing Street Address 2','Billing City','Billing State','Billing Zip','Shipping Street Address']])
    


# In[ ]:


imputer = SimpleImputer(strategy='most_frequent', missing_values=np.nan)
imputer = imputer.fit(df[['Shipping Street Address 2','Shipping City','Shipping State','Shipping Zip','Payment Method','Tracking #','Special Instructions','LineItem SKU','LineItem Options','LineItem Add-ons']])
df[['Shipping Street Address 2','Shipping City','Shipping State','Shipping Zip','Payment Method','Tracking #','LineItem SKU','LineItem Options','LineItem Add-ons']] = imputer.transform(df[['Shipping Street Address 2','Shipping City','Shipping State','Shipping Zip','Payment Method','Tracking #','Special Instructions','LineItem SKU','LineItem Options','LineItem Add-ons']])
    


# In[4]:


df3 = pd.read_excel("Product_details.xlsx")


# In[6]:


df['Dates'] = pd.to_datetime(df['Order Date and Time Stamp']).dt.date
df['Time'] = pd.to_datetime(df['Order Date and Time Stamp']).dt.time

df['year'] = pd.to_datetime(df1['Dates']).dt.year
df['month'] = pd.to_datetime(df1['Dates']).dt.month
df['day'] = pd.to_datetime(df1['Dates']).dt.day


# In[ ]:


menu_chosen = True

def menu():
    while menu_chosen:
        print('Enter 1 to see the analysis of Reviews given by Customers\n')
        print('Enter 2 to see the analysis of different payment methods used by the Customers\n')
        print('Enter 3 to see the analysis of Top Consumer States of India\n')
        print('Enter 4 to see the analysis of Top Consumer Cities of India\n')
        print('Enter 5 to see the analysis of Top Selling Product Categories\n')
        print('Enter 6 to see the analysis of Reviews for All Product Categories\n')
        print('Enter 7 to see the analysis of Number of Orders Per Month Per Year\n')
        print('Enter 8 to see the analysis of Reviews for Number of Orders Per Month Per Year\n')
        print('Enter 9 to see the analysis of Number of Orders Across Parts of a Day\n')
        print('Enter 10 to see the Full Report\n')
        print('Enter 11 to Exit :')
        
        
        choice = int(input("Chose menu option: "))
        if choice not in range(1,12):
            print("\n Not Valid Choice Try again \n")
        else:
            break
    return choice

choice = menu()
print("You chose menu option", choice)

       


# In[ ]:


import matplotlib.pyplot as plt
#%matplotlib inline
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# In[ ]:


if choice == 1:
        print('\n\n')
        print('****Analysis of Reviews given by Customers****')
        plt.figure(figsize=(45, 20))
        plt.subplot(1, 2, 1)
        df1.groupby(['PRODUCT RATING'])['PRODUCT RATING'].count().sort_values(ascending=False).plot.pie(autopct='%1.0f%%',fontsize=25);
        plt.title('Reviews of the page',fontsize=40)


# In[ ]:


plt.subplot(1, 2, 2)
        
rating_map = {'0.0 star rating':0,
              '4.0 star rating':4.0,
              '5.0 star rating':5.0,
              '4.5 star rating':4.5,
              '4.3 star rating':4.3,
              '1.0 star rating':6}

 df1['Rating_ordinal'] = df1['PRODUCT RATING'].map(rating_map)


# In[ ]:


l = df3[['Rating_ordinal']][df3['Rating_ordinal'] >= 2]
l1 = len(l)
m = df3[['Rating_ordinal']][df3['Rating_ordinal'] < 2]
m1 = len(m)
m2 = df3[['NO OF REVIEW']][df3['NO OF REVIEW'] == 0]
m_2 = len(m2)
y = []
y.append(l1)
y.append(m1)
y.append(m_2)
mylabels = ['Positive Review','Negative Review','No Reviews']
explode = [0, 0, 0.2]
plt.pie(y,labels = mylabels,autopct='%1.0f%%', textprops={'fontsize': 25},explode= explode)
plt.title('Reviews given by Customers',fontsize=40)


# In[ ]:


plt.savefig('Analysis of Reviews given by Customers.pdf')
print('\n\n')
        


# In[ ]:


elif choice == 2:
    print('\n\n')
    print('****Analysis of different payment methods used by the Customers****')
    plt.figure(figsize=(15, 8))
    sns.set_theme(style="whitegrid")
    sns.countplot('Payment Method',data=df).set_title('Payment methods used by the Customers',fontsize = 20)
        
        
     #plt.savefig('Analysis of different payment methods used by the Customers.png')
     plt.savefig('Analysis of different payment methods used by the Customers.pdf')
     # plt.savefig('Analysis of different payment methods used by the Customers.png', bbox_inches='tight')
        
        

    print('\n\n')


# In[ ]:


elif choice == 3:
    print('\n\n')
    print('****Analysis of Top Consumer States of India****')
    plt.figure(figsize=(15, 8))
    df.groupby(['Shipping State'])['LineItem Sale Price'].sum().sort_values(ascending=False).plot.bar()
    plt.title("Top Consumer States of India",fontsize=30)
        
        
    #plt.savefig('Analysis of Top Consumer States of India.png')
    plt.savefig('Analysis of Top Consumer States of India.pdf')
    #plt.savefig('Analysis of Top Consumer States of India.png', bbox_inches='tight')
        
        

    print('\n\n')


# In[ ]:


elif choice == 4:
    print('\n\n')
    print('****Analysis of Top Consumer Cities of India****')
    plt.figure(figsize=(15, 8))
    df.groupby(['Shipping City'])['LineItem Sale Price'].sum().sort_values(ascending=False).head(10).plot.bar()
    plt.title("Top Consumer Cities of India",fontsize=25)
        
     #plt.savefig('Analysis of Top Consumer Cities of India.png')
    plt.savefig('Analysis of Top Consumer Cities of India.pdf')
        #plt.savefig('Analysis of Top Consumer Cities of India.png', bbox_inches='tight')
    print('\n\n')


# In[ ]:


elif choice == 5:
    print('\n\n')
    print('****Analysis of Top Selling Product Categories****')
    plt.figure(figsize=(50, 100))
    sns.set_theme(style="whitegrid")
    df.groupby(['LineItem Name'])['LineItem Name'].count().sort_values(ascending=False).head(10).plot.bar(fontsize=25)
    plt.title("Top Selling Product Categories",fontsize=40)
      
    #plt.savefig('Analysis of Top Selling Product Categories.png')
        
    plt.savefig('Analysis of Top Selling Product Categories.pdf')
        #plt.savefig('Analysis of Top Selling Product Categories.png', bbox_inches='tight')
    print('\n\n')
        


# In[ ]:


elif choice == 6:
    print('\n\n')
    print('****Analysis of Reviews for All Product Categories****')
        
    proudct_name=df3["PRODUCT NAME"]
    labels =df3["PRODUCT NAME"]

    plt.figure(figsize=(40, 40))

    plt.pie(df1['NO OF REVIEW'],autopct='%1.0f%%', pctdistance=.75, labels= proudct_name, textprops={'fontsize': 14})
    centre_circle = plt.Circle((0, 0), 0.30, fc='white' )
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('Reviews for All Product Categories',fontsize=25)
        
        


# In[ ]:


plt.savefig('Analysis of Reviews for All Product Categories.pdf')


# In[ ]:


elif choice == 7:
    print('\n\n')
    print('****Analysis of Number of Orders Per Month Per Year****')
         
    plt.figure(figsize=(15, 10))
    sns.set_theme(style="whitegrid")
    df.groupby(['month','year'])['LineItem Qty'].sum().plot.bar()
    plt.title('Number of Orders Per Month Per Year',fontsize=25)
        
        
        #plt.savefig('Analysis of Number of Orders Per Month Per Year.png')
    plt.savefig('Analysis of Number of Orders Per Month Per Year.pdf')
        #plt.savefig('Analysis of Number of Orders Per Month Per Year.png', bbox_inches='tight')
    print('\n\n')


# In[ ]:


elif choice == 9:
    print('\n\n')
    print('****Analysis of Number of Orders Across Parts of a Day****')
    
        
    sns.set_theme(style="whitegrid")
    fig = plt.figure(figsize = (30, 15))
    df.groupby(['date','month','year'])['LineItem Qty'].sum().plot.bar(color ='maroon',width = 0.4).set_title('Number of Orders Across Parts of a Day',fontsize = 30)
    plt.xlabel("Per Day")
    plt.ylabel("Total Products")
        #plt.show()
        
        
        #plt.savefig('Analysis of Number of Orders Across Parts of a Day.png')
    plt.savefig('Analysis of Number of Orders Across Parts of a Day.pdf')
        #plt.savefig('Analysis of Number of Orders Across Parts of a Day.png', bbox_inches='tight')
    print('\n\n')


# In[ ]:


elif choice == 10:
    
    
    print('\n\n')
    print('****Full Report****')
        

    fig1 = plt.figure(figsize=(45, 20))
    plt.subplot(1, 2, 1)
    df1.groupby(['PRODUCT RATING'])['PRODUCT RATING'].count().sort_values(ascending=False).plot.pie(autopct='%1.0f%%',fontsize=25);
    plt.title('Reviews of the page',fontsize=40)
         
    plt.subplot(1, 2, 2)
        
    rating_map = {'0.0 star rating':0,
                  '4.0 star rating':4.0,
                  '5.0 star rating':5.0,
                  '4.5 star rating':4.5,
                  '4.3 star rating':4.3,
                  '1.0 star rating':6}

    df1['Rating_ordinal'] = df1['PRODUCT RATING'].map(rating_map)
        #df1.head(20)

    l = df1[['Rating_ordinal']][df1['Rating_ordinal'] >= 2]
    l1 = len(l)
    m = df1[['Rating_ordinal']][df1['Rating_ordinal'] < 2]
    m1 = len(m)
    m2 = df1[['NO OF REVIEW']][df1['NO OF REVIEW'] == 0]
    m_2 = len(m2)
    y = []
    y.append(l1)
    y.append(m1)
    y.append(m_2)
    mylabels = ['Positive Review','Negative Review','No Reviews']
    explode = [0, 0, 0.2]
    plt.pie(y,labels = mylabels,autopct='%1.0f%%', textprops={'fontsize': 25},explode= explode)
    plt.title('Reviews given by Customers',fontsize=40)
        
        
        #df1.groupby(['PRODUCT RATING'])['PRODUCT RATING'].count().sort_values(ascending=False).plot.pie(fontsize=18);

        
        #fig2 = plt.figure(figsize=(20, 20))
        #df1.groupby(['NO OF REVIEW'])['NO OF REVIEW'].count().sort_values(ascending=False).plot.pie(fontsize=18);
        
    fig2 = plt.figure(figsize=(20, 20))
    plt.figure(figsize=(15, 8))
    sns.set_theme(style="whitegrid")
    sns.countplot('Payment Method',data=df).set_title('Payment methods used by the Customers',fontsize = 20)
        
        
        
        #sns.set_theme(style="whitegrid")
        #sns.set(font_scale = 3)
        #sns.countplot('Payment Method',data=df)
        
        
    fig3 = plt.figure(figsize=(20, 20))
        #plt.figure(figsize=(15, 8))
    df.groupby(['Shipping State'])['LineItem Sale Price'].sum().sort_values(ascending=False).plot.bar()
    plt.title("Top Consumer States of India",fontsize=30)
        
        
        #df.groupby(['Shipping State'])['LineItem Sale Price'].sum().sort_values(ascending=False).plot.bar(fontsize=18)
        
        
        
    fig4 = plt.figure(figsize=(20, 20))
    df.groupby(['Shipping City'])['LineItem Sale Price'].sum().sort_values(ascending=False).head(10).plot.bar()
    plt.title("Top Consumer Cities of India",fontsize=25)
        
        
        #df.groupby(['Shipping City'])['LineItem Sale Price'].sum().sort_values(ascending=False).head(10).plot.bar(fontsize=18)
        
        
        
    fig5 = plt.figure(figsize=(40, 100))
        #plt.figure(figsize=(50, 100))
    sns.set_theme(style="whitegrid")
    df.groupby(['LineItem Name'])['LineItem Name'].count().sort_values(ascending=False).head(10).plot.bar(fontsize=25)
    plt.title("Top Selling Product Categories",fontsize=40)
        
        
        #df.groupby(['LineItem Name'])['LineItem Name'].count().sort_values(ascending=False).head(10).plot.bar(fontsize=18)
        
        
    fig6 = plt.figure(figsize=(40, 40))
    proudct_name=df1["PRODUCT NAME"]
    labels =df1["PRODUCT NAME"]

        #plt.figure(figsize=(40, 40))
    plt.pie(df1['NO OF REVIEW'],autopct='%1.0f%%', pctdistance=.75, labels= proudct_name, textprops={'fontsize': 14})
    centre_circle = plt.Circle((0, 0), 0.30, fc='white' )
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('Reviews for All Product Categories',fontsize=25)
        
        
        #sns.set_theme(style="whitegrid")
        #df.groupby(['month','year'])['LineItem Qty'].sum().plot.bar(fontsize=18)
        
        
    fig7 = plt.figure(figsize=(15, 10))
    sns.set_theme(style="whitegrid")
    df.groupby(['month','year'])['LineItem Qty'].sum().plot.bar()
    plt.title('Number of Orders Per Month Per Year',fontsize=25)
        
        
        
    fig8 = plt.figure(figsize=(30, 30))
        
    sns.set_theme(style="whitegrid")
        #fig = plt.figure(figsize = (30, 15))
    df.groupby(['date','month','year'])['LineItem Qty'].sum().plot.bar(color ='maroon',width = 0.4).set_title('Number of Orders Across Parts of a Day',fontsize = 30)
    plt.xlabel("Per Day")
    plt.ylabel("Total Products")
        
        
        
        #df.groupby(['date','month','year'])['LineItem Qty'].sum().plot.bar(color ='maroon',width = 0.4)
        #plt.xlabel("Per Day")
        #plt.ylabel("Total Products")
        
    def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()

    filename = "Final_report.pdf"
    save_multi_image(filename)
        
        

        
    else:
        print('\n\n')
        print("NOT A VALID OPTION")
        print('\n\n')
        
        
        
        
        
        
        

