# Import all of the dependencies
import streamlit as st
import os
import imageio
import tensorflow as tf
from utils import load_data, num_to_char
from modelutil import load_model

# Set the layout to the streamlit app as wide
st.set_page_config(layout='wide')

# Setup the sidebar
with st.sidebar:
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.title('LipReading')
    st.info("""
        **Tech Stack Used:**
        - **Streamlit**: ![Streamlit](https://img.shields.io/badge/Streamlit-Streamlit-ff4b4b?logo=streamlit&logoColor=white)
        - **TensorFlow**: ![TensorFlow](https://img.shields.io/badge/TensorFlow-TensorFlow-ff6f00?logo=tensorflow&logoColor=white)
        - **OpenCV**: ![OpenCV](https://img.shields.io/badge/OpenCV-OpenCV-5c3c91?logo=opencv&logoColor=white)
        - **FFmpeg**: ![FFmpeg](https://img.shields.io/badge/FFmpeg-FFmpeg-000000?logo=ffmpeg&logoColor=white)
        - **Python**: ![Python](https://img.shields.io/badge/Python-Python-306998?logo=python&logoColor=white)
    """)

st.title('LipReading App', anchor='top')
st.markdown("""
    **Welcome to the LipReading Application!** 

    This application perform lip reading from video inputs. 

    **How It Works:**
    - **Video Selection:** Choose a video from the available options.
    - **Video Rendering:** View the selected video as well as its converted form in MP4 format.
    - **Model Processing:** Watch the model process the video and make predictions.
    - **Visualization:** See how the machine learning model views the video and the output of its predictions.
    - **Prediction Decoding:** View the model's prediction in text format.

    The application demonstrates how machine learning can interpret and understand human lip movements to transcribe spoken words.
""", unsafe_allow_html=True)

# Generating a list of options or videos
options = os.listdir(os.path.join('data', 's1'))
selected_video = st.selectbox('Choose video', options, index=0, format_func=lambda x: x.split('/')[-1].replace('_', ' ').title())

# Generate two columns
col1, col2 = st.columns(2)

if options:

    # Rendering the video
    with col1:
        st.info('The video below displays the converted video in MP4 format')
        file_path = os.path.join('data', 's1', selected_video)
        os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')

        # Rendering inside of the app
        video = open('test_video.mp4', 'rb')
        video_bytes = video.read()
        st.video(video_bytes)

    with col2:
        st.info('This is the raw video data as processed by the machine learning model')
        video, annotations = load_data(tf.convert_to_tensor(file_path))
        imageio.mimsave('animation.gif', video, fps=10)
        st.image('animation.gif', width=400)

        st.info('Machine learning model output as tokens')
        model = load_model()
        yhat = model.predict(tf.expand_dims(video, axis=0))
        decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
        st.text(decoder)

        # Convert prediction to text
        st.info('Decoded prediction as readable text')
        converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
        st.text(converted_prediction)

# Custom footer
st.markdown("""
    <style>
        .footer {
            text-align: center;
            padding: 1em;
            background-color: #f1f1f1;
            border-top: 1px solid #e0e0e0;
            font-size: 12px;
            color: #555;
        }
    </style>
    <div class="footer">
        Made By Sarthak Bhardwaj
    </div>
""", unsafe_allow_html=True)
