import streamlit as st

# Custom CSS for styling
custom_css = """
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
        url('https://i.imgur.com/l9HuE5j.jpeg') no-repeat center center fixed;
        background-size: cover;
        font-family: Arial, sans-serif;
        color: #ffffff;
    }
    h1 {
        color: #ffffff;
        text-align: center;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    .section {
        margin: 20px auto;
        padding: 20px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .section h2 {
        color: #ffffff;
        margin-bottom: 10px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
    }
    .section p {
        line-height: 1.6;
        font-size: 1.1rem;
    }
</style>
"""
# Apply custom CSS
st.write(custom_css, unsafe_allow_html=True)

# Header with emoji
st.markdown("<h1>🏏 Cricket Analytics Dashboard 🚀</h1>", unsafe_allow_html=True)

# Add GIF to Home Page
st.image("Images/Cricket Field GIF.gif", use_container_width=True)


st.markdown("""
<div class="section">
    <h2>About Cricket 🏏</h2>
    <p>
        Cricket is one of the most popular and widely followed sports in the world, played in various formats including Test matches, One Day Internationals (ODIs), and T20s. 🌍 
    </p>
    <p>
        The game is a thrilling battle between bat and ball, where teams compete to score the highest runs while showcasing exceptional bowling and fielding skills. 🎯⚡
    </p>
    <p>
        Cricket has a rich history, with legendary players and unforgettable moments that have captivated millions of fans globally. Whether it's the iconic Ashes series, the electrifying T20 World Cup, or the prestige of IPL, cricket continues to evolve while keeping its core spirit intact. 🏆🔥
    </p>
    <p>
        From thrilling last-over finishes to record-breaking centuries, cricket is more than just a sport—it's an emotion that unites fans worldwide! 🌟🎉
    </p>
</div>
""", unsafe_allow_html=True)

# About the App section with emoji
st.markdown("""
<div class="section">
    <h2>About the App 💡</h2>
    <p>
        Welcome to the Cricket Analytics Dashboard! 🏏 This interactive web app brings deep insights into international cricket, allowing you to analyze player statistics, compare team performances, and even predict match outcomes using advanced Machine Learning models. 🌟
    </p>
    <p>
        Whether you're a cricket enthusiast, a fantasy league player, or a data science professional, this dashboard provides valuable analytics to explore and visualize key cricket metrics dynamically. 📊✨
    </p>
</div>
""", unsafe_allow_html=True)

# About the Author section with emoji
st.markdown("""
<div class="section">
    <h2>About the Author 👨‍💻</h2>
    <p>
        Hi there! I'm Ayush Argonda, a passionate Machine Learning enthusiast 🤖 with a knack 
        for building simple yet powerful tools to make learning ML fun and accessible for 
        everyone. When I'm not coding, you can find me exploring gym 🎧ྀི, reading 📚, or 
        experimenting with new recipes 🍳.
    </p>
</div>
""", unsafe_allow_html=True)

# Skillset Section
st.markdown("""
<div class="section">
    <h2>My Skillset ✨</h2>
    <p>
        <ul>
        <li>Programming Language: Python🐍, C++ 👾, C👨🏻‍💻</li> 
        <li>Machine Learning Frameworks: Matlab📊, Scikit-learn 🖥️, Keras👨🏻‍💻, TensorFlow 🔎</li>
        <li>Data Analytics: Pandas 📊, NumPy 📈, Power BI 📉, SQL🛢️</li>
        <li>Projects: Doomsday 2D game🛡️, Sound Control system 🎙️, Crypto Price Prediction 📈</li>
        </ul>
    </p>
</div>
""", unsafe_allow_html=True)

# Connect with Me Section (Enhanced)
st.markdown("""
<div class="section" style="text-align: center;">
    <h2 style="color: #FFD700; text-shadow: 2px 2px 4px rgba(0,0,0,0.6);">🌐 Connect with Me 🚀</h2>
    <p>Let's connect and collaborate! Feel free to reach out through any of the platforms below. 💡</p>
    <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
        <a href="https://www.linkedin.com/in/ayush-argonda-48916a213/" target="_blank" 
           style="text-decoration: none; color: white; font-size: 20px; padding: 10px 15px; background: #0077B5; border-radius: 8px;">
           🔗 LinkedIn
        </a>
        <a href="https://github.com/Ayush6787" target="_blank" 
           style="text-decoration: none; color: white; font-size: 20px; padding: 10px 15px; background: #24292E; border-radius: 8px;">
           💻 GitHub
        </a>
        <a href="mailto:ayushargonda6787@gmail.com" 
           style="text-decoration: none; color: white; font-size: 20px; padding: 10px 15px; background: #D44638; border-radius: 8px;">
           📧 Email
        </a>
        <a href="https://profound-alpaca-ec7224.netlify.app/" target="_blank" 
           style="text-decoration: none; color: white; font-size: 20px; padding: 10px 15px; background: #4CAF50; border-radius: 8px;">
           🌟 Portfolio
        </a>
        <a href="https://medium.com/@ayushargonda6787" target="_blank" 
           style="text-decoration: none; color: white; font-size: 20px; padding: 10px 15px; background: #000000; border-radius: 8px;">
           📝 Medium
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
