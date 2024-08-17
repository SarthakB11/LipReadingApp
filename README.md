# LipReadingApp
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SarthakB11/LipReadingApp">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Lip Reading Project</h3>

  <p align="center">
    A deep learning model for lip reading that uses 3D convolutional neural networks to process video data and predict spoken text.
    <br />
    <a href="https://github.com/SarthakB11/LipReadingApp"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SarthakB11/LipReadingApp">View Demo</a>
    ·
    <a href="https://github.com/SarthakB11/LipReadingApp/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/SarthakB11/LipReadingApp/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

![Project Screenshot](images/screenshot.png)

This project aims to develop a lip reading system using deep learning techniques. It utilizes a 3D Convolutional Neural Network (CNN) combined with Bidirectional LSTM layers to process video data and convert lip movements into text. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![TensorFlow][TensorFlow.js]][TensorFlow-url]
* [![OpenCV][OpenCV.org]][OpenCV-url]
* [![Streamlit][Streamlit]][Streamlit-url]
* [![ImageIO][ImageIO]][ImageIO-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

* Python 3.8
* Pip (Python package installer)
* Jupyter Notebook

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SarthakB11/LipReadingApp.git
   ```
2. Navigate to the project directory
  ```sh
   cd LipReadingApp
   ```
3. Create and activate a Conda environment
   ```sh
   conda create --name lipreading python=3.8
   conda activate lipreading
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- USAGE EXAMPLES -->
### Usage
1. Run the Jupyter Notebook
   Only run the Streamlit header!(to avoid training the model)
2. Running the Streamlit App: Start the Streamlit application to interactively test the model and visualize results.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- ROADMAP -->
### Roadmap

- Improve video preprocessing pipeline
- Implement more advanced model architectures
- Enhance Streamlit application features
- Expand dataset and improve training accuracy

See the [open issues](https://github.com/SarthakB11/LipReadingApp/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
### Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/SarthakB11/LipReadingApp/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=SarthakB11/LipReadingApp" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->
### License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
### Contact

sarthak Bhardwaj - [@your_twitter_handle](https://x.com/Sarthak1102) - sarthak.bhardwaj21b@iiitg.ac.in

Project Link: [https://github.com/SarthakB11/LipReadingApp](https://github.com/SarthakB11/LipReadingApp)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
### Acknowledgments

* TensorFlow
* OpenCV
* Streamlit
* ImageIO
* Matplotlib

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- MARKDOWN LINKS & IMAGES -->
[TensorFlow.js]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/
[OpenCV.org]: https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/
[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/
[ImageIO]: https://img.shields.io/badge/ImageIO-FF8C00?style=for-the-badge&logo=python&logoColor=white
[ImageIO-url]: https://imageio.readthedocs.io/
[Matplotlib]: https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white
[Matplotlib-url]: https://matplotlib.org/

