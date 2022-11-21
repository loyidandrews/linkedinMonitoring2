import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#from st_aggrid import AgGrid

#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

from datetime import datetime,timedelta
import pytz
import re



st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

import time

st.sidebar.success("Choose Category")


st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",
    width=100,
)

st.title('LinkedIn Live Monitoring')
with st.expander('Monitoring Posts of CEOs from LinkedIn everyday'):
     st.write('')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)





#st.balloons()

#st.header('`streamlit_pandas_profiling`')

st.header('RWE: Andere CEOs Posts last 12 Months')



df1 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/V8A8sVT6RTvnfqub1Y0iUQ/Andere_CEOS_1.csv')
df2 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/Vx2c6OJZ59781jp9zKPViw/Andere_CEOs_2.csv')
df3 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/JUeq71McCykmR5ZrlZTJdQ/Andere_CEOs_3.csv')

frames = [df1, df2, df3]

df = pd.concat(frames)

df = df.dropna(how='any', subset=['postContent'])


df.drop(['viewCount', 'sharedJobUrl', 'error', 'repostCount'], axis=1, inplace=True)


#st.write(df.profileUrl.value_counts())



df['CEO']  = df['action']

df.loc[df.profileUrl == "https://www.linkedin.com/in/assaadrazzouk/", "CEO"] = "Assaad Razzouk"
df.loc[df.profileUrl == "https://www.linkedin.com/in/markussteilemann/", "CEO"] = "Markus Steilemann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/buschroland/", "CEO"] = "Roland Busch"
df.loc[df.profileUrl == "https://www.linkedin.com/in/bernardlooneybp/", "CEO"] = "Bernard Looney"
df.loc[df.profileUrl == "https://www.linkedin.com/in/ola-k%C3%A4llenius/", "CEO"] = "Ola Kaellenius"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martenbunnemann/detail/recent-activity/shares/", "CEO"] = "Marten Bunnemann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jocheneickholt/recent-activity/", "CEO"] = "Jochen Eickholt"
df.loc[df.profileUrl == "https://www.linkedin.com/in/leo-birnbaum-885347b0/detail/recent-activity/", "CEO"] = "Leo Birnbaum"
df.loc[df.profileUrl == "https://www.linkedin.com/in/herbertdiess/", "CEO"] = "Herbert Diess"
df.loc[df.profileUrl == "https://www.linkedin.com/in/mike-crawley-a3308a2/recent-activity/shares/", "CEO"] = "Mike Crawley"
df.loc[df.profileUrl == "https://www.linkedin.com/in/miriam-teige-66117769/recent-activity/", "CEO"] = "Miriam Teige"
df.loc[df.profileUrl == "https://www.linkedin.com/in/werner-baumann/", "CEO"] = "Werner Baumann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/katherina-reiche/detail/recent-activity/", "CEO"] = "Katherina Reiche"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jeromepecresse/?originalSubdomain=fr", "CEO"] = "Jérôme Pécresse"
df.loc[df.profileUrl == "https://www.linkedin.com/in/marc-becker-3990826/", "CEO"] = "Marc Becker"
df.loc[df.profileUrl == "https://www.linkedin.com/in/richardlutzdb/", "CEO"] = "Dr. Richard Lutz"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martin-brudermueller/detail/recent-activity/", "CEO"] = "Dr. Martin Brudermüller"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hdsohn/recent-activity/shares/", "CEO"] = "Hans-Dieter Sohn"
df.loc[df.profileUrl == "https://www.linkedin.com/in/davidcarrascosafrancis/recent-activity/shares/", "CEO"] = "David Carrascosa"
df.loc[df.profileUrl == "https://www.linkedin.com/in/juan-gutierrez-sgre/recent-activity/", "CEO"] = "Juan Gutierrez"
df.loc[df.profileUrl == "https://www.linkedin.com/in/henrik-stiesdal-064a9374/recent-activity/", "CEO"] = "Henrik Stiesdal"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hilde-merete-aasheim-b37b38203/recent-activity/shares/", "CEO"] = "Hilde Merete Aasheim"
df.loc[df.profileUrl == "https://www.linkedin.com/in/alistair-phillips-davies-14213871/recent-activity/", "CEO"] = "Alistair Phillips-Davies"
df.loc[df.profileUrl == "https://www.linkedin.com/in/annaborgvattenfall/", "CEO"] = "Anna Borg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/giles-dickson-98607229/recent-activity/", "CEO"] = "Giles Dickson"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jean-bernard-levy/", "CEO"] = "Jean-Bernard Lévy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/florian-bieberbach/recent-activity/shares/", "CEO"] = "Florian Bieberbach"



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

df['Total_Interactions'] = df['likeCount'] + df['commentCount']


df['profileImg']  = df['action']

df.loc[df.profileUrl == "https://www.linkedin.com/in/assaadrazzouk/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQHZCSQaliXdiQ/profile-displayphoto-shrink_800_800/0/1516255427468?e=2147483647&v=beta&t=eSxGSIqW9vW7rHx79J5Z7gcNrCyUGVtZEVr8-rDHh4E"

df.loc[df.profileUrl == "https://www.linkedin.com/in/markussteilemann/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQHXgF5NlZrRqQ/profile-displayphoto-shrink_400_400/0/1616592958472?e=1674086400&v=beta&t=04uxVnwfDbkTEjJAj0qy0-Le0KuSGUNLlR8ao2SqQWQ"
df.loc[df.profileUrl == "https://www.linkedin.com/in/buschroland/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQHt7A5wyfZ62Q/profile-displayphoto-shrink_400_400/0/1649329185717?e=1674086400&v=beta&t=etoCOkPNa5G9Z8b8HJ-CQLRyjzgzlvLgy-VA-uODFT8"
df.loc[df.profileUrl == "https://www.linkedin.com/in/bernardlooneybp/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQEYAcA6GHI1VQ/profile-displayphoto-shrink_400_400/0/1626105106123?e=1674086400&v=beta&t=ahiCRCiVckr2D3VhTDATY_2b9CuxJL5sfE6T427kU_g"
df.loc[df.profileUrl == "https://www.linkedin.com/in/ola-k%C3%A4llenius/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQEmslz1nw9Xcg/profile-displayphoto-shrink_400_400/0/1643731137701?e=1674086400&v=beta&t=3M-JWsoXg7r0tHbJ7RNdb7a3q8puKcCw8FJUTBF8Hzg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martenbunnemann/detail/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQEEFMfjUbmLsA/profile-displayphoto-shrink_400_400/0/1585913949824?e=1674086400&v=beta&t=fMWpbCEnskPus45UOQB8tjK65seeUL5bgboR5iMVVdY"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jocheneickholt/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/D4D03AQE7I0g99vQF7A/profile-displayphoto-shrink_400_400/0/1664128016463?e=1674086400&v=beta&t=zGoZCh7OVXmwWWYeNGjNGy6C_WN8EyYaJuq8p2nNAcQ"
df.loc[df.profileUrl == "https://www.linkedin.com/in/leo-birnbaum-885347b0/detail/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQE7yP63OXfavA/profile-displayphoto-shrink_400_400/0/1643105401117?e=1674086400&v=beta&t=8lt5v2zUGpmq279UuG5ZV122YbctFKmrXn3Rqy95bB0"
df.loc[df.profileUrl == "https://www.linkedin.com/in/herbertdiess/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQGwevkEVF9SLg/profile-displayphoto-shrink_400_400/0/1604501451969?e=1674086400&v=beta&t=KfjkItv4RipG8wTO5IG7QaMFQWe3qarjOgCLSymASiU"
df.loc[df.profileUrl == "https://www.linkedin.com/in/mike-crawley-a3308a2/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5603AQHdigGQiJWq4g/profile-displayphoto-shrink_400_400/0/1516245033117?e=1674086400&v=beta&t=W4GlchB3P4xvyjnyCIT4mGrq4mTXA6eYP2FZS5z8dSY"
df.loc[df.profileUrl == "https://www.linkedin.com/in/miriam-teige-66117769/recent-activity/", "profileImg"] = "https://profile-images.xing.com/images/e361dbb99b1048cc5b97668087ac9b59-5/miriam-teige.256x256.jpg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/werner-baumann/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5603AQGI_4YXr7uMIA/profile-displayphoto-shrink_400_400/0/1631806128361?e=1674086400&v=beta&t=EjqN-uz3hJ7qBRIQVCLbxA4C8lJCpwesaTn3RR_TUWw"
df.loc[df.profileUrl == "https://www.linkedin.com/in/katherina-reiche/detail/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQFOOt3UwR4FpQ/profile-displayphoto-shrink_400_400/0/1601888597608?e=1674086400&v=beta&t=Uvd6erXkPyYJBJoEluRZKF3fcHU7drBeCUvvwFaPUas"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jeromepecresse/?originalSubdomain=fr", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5603AQG7UwEhvr5bxw/profile-displayphoto-shrink_400_400/0/1591286963133?e=1674086400&v=beta&t=gG_d-hk4nKan7m7M8gXBnkdXtbTFk2NclmOridFbrE0"
df.loc[df.profileUrl == "https://www.linkedin.com/in/marc-becker-3990826/", "profileImg"] = "https://www.wfo-helgoland.eu/2017/files/2017/08/Dr.-Marc-Becker-e1501844444352-390x390.jpg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/richardlutzdb/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/D4E03AQG6-ESIrvZGnw/profile-displayphoto-shrink_400_400/0/1667416495067?e=1674086400&v=beta&t=yWZ-GLMN7lh7Cd5BzoJAVHYK39DKDnoY1jhqdMUy-lg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martin-brudermueller/detail/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQHjIB2XUqA9bg/profile-displayphoto-shrink_400_400/0/1616417524648?e=1674086400&v=beta&t=G7peaOsq6pl9XKOEgAeQwS8GZ6BQdBPkHdJSPQO8VEc"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hdsohn/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQFLOYyqYyLN2g/profile-displayphoto-shrink_400_400/0/1604417604865?e=1674086400&v=beta&t=5hYyozi-rYn2Abt1z7AHrP-VHw4wO0bK8BGVPIkGvgI"
df.loc[df.profileUrl == "https://www.linkedin.com/in/davidcarrascosafrancis/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5103AQGi0NnyRoRJPA/profile-displayphoto-shrink_400_400/0/1517228600139?e=1674086400&v=beta&t=mQWCKWusvkyvtELcqx6otmAp0P5s7XxRj89twgUGwJc"
df.loc[df.profileUrl == "https://www.linkedin.com/in/juan-gutierrez-sgre/recent-activity/", "profileImg"] = "https://nawindpower.com/wp-content/uploads/2020/03/Gutierrez_J-0004-scaled.jpg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/henrik-stiesdal-064a9374/recent-activity/", "profileImg"] = "https://upload.wikimedia.org/wikipedia/commons/9/99/Henrik_Stiesdal%2C_Siemens_Windpower_Division_CTO%2C_Press_Image_2012.jpg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hilde-merete-aasheim-b37b38203/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQHahchcmPw3pA/profile-displayphoto-shrink_400_400/0/1610534026461?e=1674086400&v=beta&t=vs0LmRvESXecSEVPGt3_aZhFSYuvuQHKVMdUVT2K8Ro"
df.loc[df.profileUrl == "https://www.linkedin.com/in/alistair-phillips-davies-14213871/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5603AQEGqafzcqRo2Q/profile-displayphoto-shrink_400_400/0/1612302162253?e=1674086400&v=beta&t=dl1pZ2QX-Nf5h0l17nyqaIPP8tRsRPEK3YJfSwbGQck"
df.loc[df.profileUrl == "https://www.linkedin.com/in/annaborgvattenfall/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/D4D03AQFH0lwTjUWnAw/profile-displayphoto-shrink_400_400/0/1666804754880?e=1674086400&v=beta&t=WoQB2g8S4Hk_C1xgmg-uApOgRE0vOSji8Wa9ZzhSjS0"
df.loc[df.profileUrl == "https://www.linkedin.com/in/giles-dickson-98607229/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQGhOcNb1JtCqw/profile-displayphoto-shrink_400_400/0/1645023119636?e=1674086400&v=beta&t=McqVYoA8BJK2bXyClkuytosxfjBCjYiNCGClmj_DXUc"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jean-bernard-levy/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQHrXZwpUycaZg/profile-displayphoto-shrink_400_400/0/1574177430159?e=1674086400&v=beta&t=Qxn0Bsm-BoqsWHBuezA85_LFm8YgdhpUQU0od0EUMOA"
df.loc[df.profileUrl == "https://www.linkedin.com/in/florian-bieberbach/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQFc9lmuT5toVw/profile-displayphoto-shrink_400_400/0/1627920577752?e=1674086400&v=beta&t=RnClEIBVElHEjoDDIBLhqeHXUps3DLJa_Gxr-xikvfs"







#st.write(df.profileImg.value_counts())
df30 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=365))] #hours = 6,12, 24

#AgGrid(df30, height=500, fit_columns_on_grid_load=True)

if st.button('Show Data'):
   st.write(df30)

#st.write(df30)
st.write(df30.shape)
#df5 = df['date'].last('24h')

st.subheader('No of Posts for each CEOs from last 12 Months')



#st.write(df30.CEO.value_counts())

df12 = df30['CEO'].value_counts()
st.bar_chart(df12)

number = st.number_input('How many days old data you want to see?', min_value=1, max_value=31, value=1, step=1)
#st.write('The current number is ', number)

st.header(f'Post from last {int(number)} days')



df5 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=number))] #hours = 6,12, 24

cols = ['CEO','postContent','postUrl','likeCount','commentCount','Total_Interactions','postDate','profileUrl', 'imgUrl','profileImg','type']
df5 = df5[cols]
df5.sort_values(['Total_Interactions'], ascending=False, inplace=True)


#df5 = df5["imgUrl"].str.replace("<NA>","https://www.citypng.com/public/uploads/preview/download-horizontal-black-line-png-31631830482cvrhyz46le.png")

df5['likeCount'] = df5['likeCount'].astype(int)
df5['commentCount'] = df5['commentCount'].astype(int)
df5['Total_Interactions'] = df5['Total_Interactions'].astype(int)

df5 = df5.reset_index(drop=True)



black_image = 'https://i.imgflip.com/505yh3.png'

if st.button(f'Show Data for past {int(number)} days'):
    st.write(df5)

st.write(df5.shape)
#st.write(df5)
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df5)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='CEOS_post_past24Hr.csv',
    mime='text/csv',
)






   



#st.write(a)




st.subheader(f'Total Interactions for each CEOs : last {int(number)} days')
#x = df5.plot(kind='bar', x='CEO', y='Total_Interactions', figsize=(20,10), ylabel='View Counts')
st.bar_chart(df5, x='CEO', y='Total_Interactions',use_container_width=True)
#st.sidebar.header('Input')

st.header(f'Top Interacting Posts in last {int(number)} days')


#defining three side-by-side columns

#col1, col2, col3 = st.columns(3)



num_posts = df5.shape[0]

if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df5.groupby(df5.index // 4)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                    st.subheader(frames.CEO[i])
                    
                       

                    with st.expander('Post Content'):
                         st.write(c['postContent'])  #postContent
                    st.write('Type of Post:  ',c['type']) #postType
                    st.write('Total Interactions for this Post:  ',c['Total_Interactions']) #totInteractions
                    st.write('Publish Date:  ',c['postDate']) #publishDate
                    with st.expander('Link to this Post'):
                        st.write(c['postUrl']) #linktoPost
                    with st.expander('Link to  Profile'):
                        st.write(c['profileUrl']) #linktoProfile
                    if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post')
                    
else:
     st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
     st.subheader(f'Oops... No new post found in last {int(number)} days.')
st.header('')
st.header('')
st.header('_________________________________________________________________________________________________')
st.header('')


st.header('Select CEO to see all their posts in last 1 year')

makes = df30['CEO'].drop_duplicates()
make_choice = st.selectbox('Select CEO from list:', makes)

#st.write(make_choice)
df30.rename(columns={'Total_Interactions': 'Total Interactions'}, inplace=True)

df_CEO = df30.loc[df30.CEO == make_choice]

df_CEO = df_CEO.reset_index(drop=True)


st.image(df_CEO.profileImg[0], width=200)
#st.write(df_CEO.to_html(escape=False, index=False), unsafe_allow_html=True)

df_CEO.sort_values(['postDate'], ascending=False, inplace=True)




st.subheader(f'Total Interactions for each posts of {make_choice}')

st.area_chart(df_CEO, x='postDate', y='Total Interactions',use_container_width=True)

st.subheader(f'Posts from {make_choice} in last year')



num_posts_1 = df_CEO.shape[0]

if  num_posts_1>0:
    
     #splits = np.array_split(df5,5)
     #st.image(df_CEO.profileImg[0])
     splits_1 = df_CEO.groupby(df_CEO.index // 4)
     for _, frames_1 in splits_1:
          frames_1 = frames_1.reset_index(drop=True)
          #print(frames_1.head())
          thumbnails_1 = st.columns(frames_1.shape[0])
          for i, c in frames_1.iterrows():
               with thumbnails_1[i]:

                    # if not pd.isnull(c['profileImg']):
                    #     st.image(c['profileImg'], width=150)
                    # st.subheader(frames_1.CEO[i])
                    
                       
                    st.write('Publish Date:  ',c['postDate']) #publishDate
                    if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post', width=150)
                    with st.expander('Post Content'):
                         st.write(c['postContent'])  #postContent
                    st.write('Type of Post:  ',c['type']) #postType
                    st.write('Total Interactions for this Post:  ',c['Total Interactions']) #totInteractions
                    
                    with st.expander('Link to this Post'):
                        st.write(c['postUrl']) #linktoPost
                    with st.expander('Link to  Profile'):
                        st.write(c['profileUrl']) #linktoProfile
                    
                    
else:
     
     st.write('Tut mir sehr sehr leid. No new post in last 24 hours.')









# else:
#     st.image(
#     "https://image.similarpng.com/very-thumbnail/2021/04/Sad-Emoji-face-on-transparent-background-PNG.png",
#     width=150,
#      )
    
#     st.write('Ohh.. No Posts found in defined time range Please check after some time')

  



















# #defining three side-by-side columns

# col1, col2, col3 = st.columns(3)



# #adding elements to each column, in this case- different metrics

# col1.metric("Temperature", "20 °C", "-1 °C")

# col2.metric("Cost", "$ 9200", "-8%", delta_color="inverse")

# col3.metric("Humidity", "89%", "3%")




















# st.subheader('Input CSV')
# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#   df = pd.read_csv(uploaded_file)
#   st.subheader('DataFrame')
#   st.write(df)
#   st.subheader('Descriptive Statistics')
#   st.write(df.describe())
# else:
#   st.info('☝️ Upload a CSV file')

# "


  

