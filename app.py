#
# import streamlit as st
# import pandas as pd
# import requests
# import pickle
#
# from streamlit import title
#
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#
#     data = response.json()
#     print(data)
#     return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']
#
#
#
# def recommend(movie):
#     movie_index = movies[movies['title']==movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         #fetch poster from API
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies,recommended_movies_posters
#
#
#
# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# movie = movies_dict['title'].values
# import gzip
#
#
# with gzip.open('similarity.pkl.gz', 'rb') as f:
#     similarity = pickle.load(f)
#
# st.title("Movie Recommender System")
# selected_movie_name = st.selectbox(
#     'Enter the name of your Favourite English movie',movies['title'].values
# )
# st.write("Recommending Movies for you..........")
#
# if st.button('Recommend'):
#     names,posters = recommend(selected_movie_name)
#     col1, col2, col3 ,col4, col5 = st.columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#             st.text(names[3])
#             st.image(posters[3])
#     with col5:
#             st.text(names[4])
#             st.image(posters[4])



import streamlit as st
import pandas as pd
import requests
import pickle
import gzip

# --- 1. SET BACKGROUND ---
def add_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=2000");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

# --- 2. LOGIC FUNCTIONS ---
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    try:
        data = requests.get(url, timeout=5).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# --- 3. LOAD DATA ---
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# --- 4. UI ---
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Enter the name of your Favourite English movie',
    movies['title'].values
)

if st.button('Recommend'):
    with st.spinner('Finding recommendations...'):
        names, posters = recommend(selected_movie_name)
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])



