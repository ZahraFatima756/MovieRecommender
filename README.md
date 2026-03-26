# 🎬 Movie Recommendation System
*End-to-End Machine Learning Project | Content-Based Filtering*

This repository features a fully functional **Movie Recommendation Engine** that suggests films based on user preferences. 
The project demonstrates a complete ML lifecycle: from raw data cleaning and **Natural Language Processing (NLP)** to a live web deployment.

---

## 🚀 Live Demo
🔗 **[(https://www.linkedin.com/posts/zahra-fatima-07b439339_machinelearning-softwareengineering-python-ugcPost-7440445900109463552-uZ8x?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFT1sB8BJhmvtEdmMO-XCCOXbdI6g8aLVlI))**


## 🛠️ Technical Stack

**Machine Learning:** Content-Based Filtering, Cosine Similarity
**NLP:** NLTK (PorterStemmer), CountVectorizer (Bag of Words)
**Data Science:** Pandas, NumPy
**Web Framework:** Streamlit
**Environment & DevOps:** Python 3.13, Git, Pickle

---

## 📂 Project Architecture

The system uses a **Content-Based Filtering** approach, focusing on movie metadata (genres, keywords, cast, and crew) to find similarities between titles.

1. Data Preprocessing & Cleaning
* Merged multiple datasets (Credits & Movies) to create a unified data source.
* Handled missing values and dropped irrelevant features to optimize performance.
* Converted complex JSON-formatted strings into clean Python lists using `ast.literal_eval`.

2. Natural Language Processing (NLP)
* **Tags Creation:** Combined 'Overview', 'Genres', 'Keywords', 'Cast', and 'Crew' into a single "tags" column.
* **Text Normalization:** Applied **PorterStemmer** from the `NLTK` library to reduce words to their root forms (e.g., "loving" -> "love").
* **Vectorization:** Converted text tags into 5,000-dimensional vectors using `CountVectorizer`, excluding common English stop words.

3. Similarity Engine
 Implemented **Cosine Similarity** to calculate the distance between movie vectors. 
  The engine identifies the 5 movies with the smallest "angular distance" to the user's input, ensuring high-relevance recommendations.

 4. Deployment
* Serialized the similarity matrix and movie list using **Pickle** for fast loading.
* Developed an interactive UI using **Streamlit** that allows users to select a movie from a dropdown and receive instant recommendations with posters.

---

## 📈 Key Features
* ✅ **Dynamic Search:** Predictive dropdown for 5,000+ movies.
* ✅ **Poster Integration:** Fetches real-time movie posters via The Movie Database (TMDB) API.
* ✅ **Optimized Performance:** Pre-computed similarity matrix for sub-second response times.

•	LinkedIn: [www.linkedin.com/in/zahra-fatima-07b439339]
•	Other Project: [https://github.com/ZahraFatima756/Ml_Foundation]
