import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

from datetime import datetime,timedelta
import pytz
import re

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.set_page_config(layout="wide")

import time

st.sidebar.success("Select Category")


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

if st.button('Show Data'):
    st.write(df30)

#st.write(df30)
st.write(df30.shape)
#df5 = df['date'].last('24h')

st.subheader('No of Posts for each CEO from last 12 Months')
st.write(df30.CEO.value_counts())

st.header('Post from last 24 hours')



df5 = df[df['date']>=(dt.datetime.now()-dt.timedelta(hours=24))] #hours = 6,12, 24

cols = ['CEO','postContent','postUrl','likeCount','commentCount','Total_Interactions','postDate','profileUrl', 'imgUrl','profileImg','type']
df5 = df5[cols]
df5.sort_values(['Total_Interactions'], ascending=False, inplace=True)


#df5 = df5["imgUrl"].str.replace("<NA>","https://www.citypng.com/public/uploads/preview/download-horizontal-black-line-png-31631830482cvrhyz46le.png")

df5['likeCount'] = df5['likeCount'].astype(int)
df5['commentCount'] = df5['commentCount'].astype(int)
df5['Total_Interactions'] = df5['Total_Interactions'].astype(int)

df5 = df5.reset_index(drop=True)



black_image = 'https://i.imgflip.com/505yh3.png'

if st.button('Show Data for past 24 Hours'):
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




st.subheader('Total Interactions for each CEOs : last 24hours')
#x = df5.plot(kind='bar', x='CEO', y='Total_Interactions', figsize=(20,10), ylabel='View Counts')
st.bar_chart(df5, x='CEO', y='Total_Interactions',use_container_width=True)
#st.sidebar.header('Input')


st.header('Top Interacting Posts in last 24 Hours')


thumbnails = st.columns(5)

for i,c in df5.iterrows():
   with thumbnails[i]:
      

      if not pd.isnull(c['profileImg']):
         st.image(c['profileImg'], width=150)
      
      st.subheader(df5.CEO.iloc[i])
      if not pd.isnull(c['imgUrl']):
         st.image(c['imgUrl'])
      
      

      with st.expander('Post Content'):
        st.write(c['postContent']) #postContent 

      st.write('Type of Post:  ',c['type']) #totInteractions
      
      st.write('Total Interactions for this Post:  ',c['Total_Interactions']) #totInteractions

      
      st.write('Publish Date:  ',c['postDate']) #totInteractions

      with st.expander('Link to this Post'):
        st.write(c['postUrl']) #postContent 

      with st.expander('Link to  Profile'):
        st.write(c['profileUrl']) #postContent 
else if:
    st.image(
    "https://static8.depositphotos.com/1431107/919/i/600/depositphotos_9199988-stock-photo-oops-icon.jpg",
    width=180,
     )
    
    st.write('Ohh.. No Posts found in defined time range Please check after some time')








































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


  

