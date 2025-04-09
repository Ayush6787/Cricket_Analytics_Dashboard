🧠 Player Face Classifier & Cricket Stats Comparison
This Streamlit web application combines computer vision and data analytics to deliver a unique experience for cricket fans. Upload images of two Indian cricket players, and the app will recognize the players using facial recognition and compare their career statistics across multiple formats like Test, ODI, T20, and IPL.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Features
🔍 Face Detection & Recognition
Detects faces using Haar Cascade and classifies them using a Support Vector Classifier (SVC) trained on facial images of 28 Indian players.

📸 Image-Based Player Identification
Upload clear, frontal face images to let the model predict the player's identity.

📊 Cricket Stats Comparison
Visual comparison of:

🏏 Total runs & wickets

⚡ Strike rate vs. runs

🏆 Milestones (50s, 100s, 200s)

🧩 Match distribution across formats

📈 Interactive Charts
Stunning data visualizations using Plotly and Seaborn for an engaging experience.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📂 Dataset
📁 Final_cleaned_Cricket.csv
Contains preprocessed career statistics of 28 Indian cricket players across various formats.

📁 Face Dataset
Contains over 300 facial images per player (augmented) used for training the SVC classifier.

Player Statistics:
Sourced from RapidAPI, this dataset includes detailed cricket stats such as batting, bowling, matches, milestones, and more.

📊 209 rows x 118 columns

Player Facial Images:
Face images were also collected from RapidAPI. These images were transformed and preprocessed for machine learning.

🖼️ 8100 rows x 4097 columns (after flattening grayscale face images to vectors)



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧠 Tech Stack
Frontend: Streamlit

ML Model: Support Vector Classifier (SVC)

Face Detection: Haar Cascade (OpenCV)

Data Analysis & Viz: Pandas, NumPy, Plotly, Seaborn, Matplotlib

Model Storage: Joblib for saving/loading trained models

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📸 How to Use
Clone the repository

Install the required libraries

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py
Upload two player face images and view their comparison!

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚠️ Image Guidelines
Upload clear, front-facing facial images.

Avoid blurry, cropped, or side-angle photos for better accuracy.

📬 Author
Ayush Argonda

[🔗 LinkedIn ](https://www.linkedin.com/in/ayush-argonda-48916a213/)

[🌐 Portfolio ](https://profound-alpaca-ec7224.netlify.app/)

[📝 Medium ](https://medium.com/@ayushargonda6787)

