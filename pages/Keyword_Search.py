import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

from st_aggrid import AgGrid

#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

from datetime import datetime,timedelta
import pytz
import re

from germansentiment import SentimentModel

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

import time

col1,col2= st.columns(2)

with col1:
   #st.header("A cat")
   st.image("https://storymachine.mocoapp.com/objects/accounts/a201d12e-6005-447a-b7d4-a647e88e2a4a/logo/b562c681943219ea.png", width=200)
   
with col2:
   
   st.header("Data Team Dashboard")

st.sidebar.success("Choose Category")

st.title('LinkedIn Keyword Search Monitoring')

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",
    width=100,
)


with st.expander('Monitoring Keyword Search in LinkedIn everyday'):
     st.write('')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)





#st.balloons()

#st.header('`streamlit_pandas_profiling`')

#st.header('LinkedIn Keyword Search Monitor')



df1 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/W6ABqHJigNTFHT3YtGXL5g/renewable_energy_live_monitoring.csv')
df2 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/FtuNWKMJKVUySGlR1lVmDg/live_windenergie.csv')
#df3 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/JUeq71McCykmR5ZrlZTJdQ/Andere_CEOs_3.csv')

df1.insert(len(df1.columns), 'Keyword', 'Renewable Energy')
df2.insert(len(df2.columns), 'Keyword', 'Wind Energy')

frames = [df1, df2]

df = pd.concat(frames)

df = df.dropna(how='any', subset=['textContent'])


df.drop(['connectionDegree', 'timestamp'], axis=1, inplace=True)


def getActualDate(url):

    a= re.findall(r"\d{19}", url)

    a = int(''.join(a))

    a = format(a, 'b')

    first41chars = a[:41]

    ts = int(first41chars,2)

    #tz = pytz.timezone('Europe/Paris')

    actualtime = datetime.fromtimestamp(ts/1000).strftime("%Y-%m-%d %H:%M:%S %Z")

    return actualtime

df['postDate'] = df.postUrl.apply(getActualDate)


df = df.dropna(how='any', subset=['postDate'])


import datetime as dt

#def datenow(date):
     #a = re.(datetime.now() - df.postDate.days >1:)

#df5= df
#df5['date'] =  pd.to_datetime(df5['postDate'])
df['date'] =  pd.to_datetime(df['postDate'])


df['Total Interactions'] = df['likeCount'] + df['commentCount']

st.header('Select Keyword from list to Monitor')

makes = df['Keyword'].drop_duplicates()
make_choice = st.selectbox('Select Keyword:', makes)

#st.write(make_choice)
#df30.rename(columns={'Total_Interactions': 'Total Interactions'}, inplace=True)

df_keyword = df.loc[df.Keyword == make_choice]

df_keyword = df_keyword.reset_index(drop=True)

#st.write(df_keyword.Keyword.value_counts())

df_keyword['likeCount'] = df_keyword['likeCount'].fillna(0)
df_keyword['commentCount'] = df_keyword['commentCount'].fillna(0)
df_keyword['Total Interactions'] = df_keyword['Total Interactions'].fillna(0)



#st.write(df.profileImg.value_counts())


df_keyword['likeCount'] = df_keyword['likeCount'].astype(int)
df_keyword['commentCount'] = df_keyword['commentCount'].astype(int)
df_keyword['Total Interactions'] = df_keyword['Total Interactions'].astype(int)

#st.write(df_keyword.head(50))


#df_keyword['Month'] = pd.to_datetime(df_keyword.postDate).dt.day
df_keyword.drop_duplicates(subset=['postUrl'], inplace=True)
df_keyword = df_keyword.reset_index(drop=True)

df_keyword['Hour'] = pd.to_datetime(df_keyword.postDate).dt.strftime("%H")
#st.write(df_keyword.head())
#AgGrid(df30, height=500, fit_columns_on_grid_load=True)

if st.button('Show Data'):
   st.write(df_keyword)

df30 = df_keyword[df_keyword['date']>=(dt.datetime.now()-dt.timedelta(days=1))] #hours = 6,12, 24

#st.write(df30)
st.write(f'Total posts found in last Hours: ', df30.shape[0])
#df5 = df['date'].last('24h')

#st.subheader('No of Posts for each CEOs from last 12 Months')



#st.write(df30.CEO.value_counts())

st.subheader('Total Interaction getting in past hours in the day')
st.bar_chart(df30, x='Hour', y='Total Interactions')

# # date_to_monitor = st.date_input('Choose a date to see the post that created after that',value=datetime.today() - timedelta(days=1))
# # st.write(date_to_monitor)

# number = st.number_input('Select the days you want to see the posts', min_value=1, max_value=360, value=10, step=1)
# #st.write('The current number is ', number)

# st.header(f'Post from last {int(number)} days')



# df5 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=number))] #hours = 6,12, 24


# cols = ['CEO','postContent','postUrl','likeCount','commentCount','Total_Interactions','postDate','profileUrl', 'imgUrl','profileImg','type','action', 'Company']
# df5 = df5[cols]
# df5.sort_values(['Total_Interactions'], ascending=False, inplace=True)


# #df5 = df5["imgUrl"].str.replace("<NA>","https://www.citypng.com/public/uploads/preview/download-horizontal-black-line-png-31631830482cvrhyz46le.png")

# df5['likeCount'] = df5['likeCount'].astype(int)
# df5['commentCount'] = df5['commentCount'].astype(int)
# df5['Total_Interactions'] = df5['Total_Interactions'].astype(int)

# df5 = df5.reset_index(drop=True)




# if st.button(f'Show Data for past {int(number)} days'):
#     st.write(df5)

# st.write(f'Number of posts in last {int(number)} days: ', df5.shape[0])
# #st.write(df5)
# @st.cache
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')

# csv = convert_df(df5)
# st.download_button(
#     label="Download data as CSV",
#     data=csv,
#     file_name='CEOS_post_past24Hr.csv',
#     mime='text/csv',
# )






   



# #st.write(a)




# st.subheader(f'Total Interactions for each CEOs : last {int(number)} days')
# #x = df5.plot(kind='bar', x='CEO', y='Total_Interactions', figsize=(20,10), ylabel='View Counts')
# st.bar_chart(df5, x='CEO', y='Total_Interactions',use_container_width=True)
# #st.sidebar.header('Input')

st.header(f'Top Interacting 100 Posts today')
#st.write(df30.profileImgUrl.isna().sum())
df30.sort_values(['Total Interactions'], ascending=False, inplace=True)
df30 = df30.reset_index(drop=True)
#st.write(df30)
#defining three side-by-side columns

#col1, col2, col3 = st.columns(3)
df100 = df30.head(100)
#st.write(df100.shape)

num_posts = df100.shape[0]

if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df100.groupby(df100.index // 4)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImgUrl']):
                        st.image(c['profileImgUrl'], width=150)
                    if not pd.isnull(c['profileUrl']):
                        #st.image(c['profileImgUrl'], width=150)
                        st.subheader(frames.fullName[i])
                        st.write(c['title']) #postType
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Profile 🔗'):
                             st.write(c['profileUrl']) #linktoProfile
                    
                    if not pd.isnull(c['logoUrl']):
                        st.image(c['logoUrl'], width=150)
                    
                        st.subheader(c['companyName'])
                        st.write('Corporate Account')
                        st.write('👥:  ',c['followerCount'])
                        with st.expander('Post Content 📜'):
                             st.write(c['textContent'])  #postContent
                        st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                        st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                        st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                        #st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                        with st.expander('Link to this Post 📮'):
                             st.write(c['postUrl']) #linktoPost
                        with st.expander('Link to  Company Profile 🔗'):
                             st.write(c['companyUrl']) #linktoProfile
                        
                    
                    
                       

                    
                    #st.write('Type of Post 📨:  ',c['type']) #postType
                    
                    if not pd.isnull(c['postImgUrl']):
                        st.image(c['postImgUrl'])
                        st.write('Image from the Post  🗾')
                    
else:
     st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
     st.subheader(f'Oops... No new post found in last {int(number)} days.')
st.header('')
st.header('')
