import streamlit as st
import pickle
import pandas as pd

# Streamlit app layout customization
st.set_page_config(layout="wide")

color = 'green'
horizontal_bar = f'<hr style="border: 1px solid {color};">'
st.markdown(horizontal_bar, unsafe_allow_html=True)

st.title("Music Recommendation System")

# Define the color for the horizontal bar
color = 'green'
horizontal_bar = f'<hr style="border: 1px solid {color};">'
st.markdown(horizontal_bar, unsafe_allow_html=True)

#Main
def recommend(song):
    index = songsG[songsG['Genre'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:11]

    recommend_music = []
    for i in distances[1:11]:
        recommend_music.append(songsG.iloc[i[0]].Name)
    return recommend_music

music_genre=pickle.load(open('music_genre.pkl','rb'))
music=pickle.load(open('music.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
songsG=pickle.load(open('songsG.pkl','rb'))


selected_genre_name = st.selectbox('Select Genre', music_genre)

if st.button('Recommend'):
   recommendations= recommend(selected_genre_name)
   for i in recommendations:
    st.write(i)
#Main end


# Sidebar selection for genre
st.sidebar.title("EXPLORE!")
# Sidebar links
st.sidebar.markdown("### Top Artists of Decade")

st.sidebar.image("arijit2.jpeg")
st.sidebar.markdown("[Arijit Singh](https://en.wikipedia.org/wiki/Arijit_Singh)")
st.sidebar.image("atif.jpeg")
st.sidebar.markdown("[Atif Aslam](https://en.wikipedia.org/wiki/Atif_Aslam)")
st.sidebar.image("sonu.jpeg")
st.sidebar.markdown("[Sonu Nigam](https://en.wikipedia.org/wiki/Sonu_Nigam)")
st.sidebar.image("shreya.jpeg")
st.sidebar.markdown("[Shreya Ghoshal](https://en.wikipedia.org/wiki/Shreya_Ghoshal)")






#artist
def recommend2(song):
    index = songsA[songsA['Singer'] == song].index[0]
    distances2 = sorted(list(enumerate(similarity2[index])), reverse=True, key=lambda x: x[1])[1:11]

    recommend_song = []
    for i in distances2[1:11]:
        recommend_song.append(songsA.iloc[i[0]].Name)
        recommend_song.append(songsA.iloc[i[0]].track_href)
    return recommend_song



  


music_singer=pickle.load(open('music_singer.pkl','rb'))
music2=pickle.load(open('music2.pkl','rb'))
similarity2=pickle.load(open('similarity2.pkl','rb'))
songsA=pickle.load(open('songsA.pkl','rb'))

selected_singer_name = st.selectbox('Select Artist', music_singer)

if st.button('Recommend Songs'):
   recommendations2= recommend2(selected_singer_name)
   for i in recommendations2:
    st.write(i)



# Footer
st.markdown(
    """
    <style>
    .stFooter {
        font-size: 12px;
        color: #777;
        text-align: center;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="stFooter">Made with ❤️ by Sumitra | Music data from Kaggle</p>',
    unsafe_allow_html=True,
)