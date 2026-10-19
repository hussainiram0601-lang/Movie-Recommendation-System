import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b51d44a93539bec959b2b6e30b001ae8&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return  'https://image.tmdb.org/t/p/w500/' +data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = sim[movie_index]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
    rec_movies = []
    rec_movie_pos =[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        rec_movies.append(movies.iloc[i[0]].title)
        rec_movie_pos.append(fetch_poster(movie_id))
    return rec_movies , rec_movie_pos

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
sim = pickle.load(open('sim.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "Select a Movie",
    movies['title'].values
)

if st.button("Recommend"):
    names , posters = recommend(selected_movie_name)
    col1, col2 , col3 ,  col4 , col5= st.columns(5)

    with col1:
        st.image(posters[0])
        st.header(names[0])

    with col2:
        st.image(posters[1])
        st.header(names[1])
    with col3:
        st.image(posters[2])
        st.header(names[2])
    with col4:
        st.image(posters[3])
        st.header(names[3])
    with col5:
        st.image(posters[4])
        st.header(names[4])
    import streamlit as st

    # Custom CSS for main background color
import streamlit as st

# Custom CSS for a black main background
import streamlit as st

# Apply custom dark theme CSS
st.markdown(
    """
    <style>
    /* Main App Background & Default Text Color */
    .stApp {
        background-color: #0d0d0d;
        color: #f5f5f5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Title Styling */
    .stApp h1 {
        color: #e50914; /* Netflix Red Accent */
        text-align: center;
        font-weight: 800;
        letter-spacing: 1.5px;
        margin-bottom: 25px;
        text-shadow: 0 0 10px rgba(229, 9, 20, 0.4);
    }

    /* Headers (Movie Titles above posters) */
    .stApp h2, .stApp h3 {
        color: #ffffff !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        text-align: center !important;
        margin-top: 10px !important;
        height: 2.8em; /* Kept uniform height for title wrapping */
        overflow: hidden;
    }

    /* Selectbox Label */
    div[data-baseweb="select"] > div {
        background-color: #1a1a1a !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
        color: #ffffff !important;
    }

    label[data-testid="stWidgetLabel"] {
        color: #cccccc !important;
        font-weight: 500;
    }

    /* Customizing the Recommend Button */
    div.stButton > button {
        background: linear-gradient(135deg, #e50914 0%, #b20710 100%);
        color: #ffffff;
        border: none;
        padding: 0.6rem 2rem;
        font-size: 1rem;
        font-weight: 700;
        border-radius: 8px;
        width: 100%;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.3);
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #ff1e27 0%, #e50914 100%);
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.6);
        transform: translateY(-2px);
        color: #ffffff;
    }

    /* Movie Poster Image Card Styling */
    div[data-testid="stImage"] img {
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.8);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    div[data-testid="stImage"] img:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 25px rgba(229, 9, 20, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True,
)