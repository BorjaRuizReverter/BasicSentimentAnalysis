# Basic Sentiment Analysis
This repo is just to show how to apply a simple basic analysis.

The script is based on a pretrained backbone taken from keras_npl models, especifically the **BertClassifier**

This makes:
1. The script very easy to build and,
2. The processing very fast, even avoiding having to run with GPUs.

# Installation
First, make sure you are using the latest version of Python. Otherwise, download if from [here](https://www.python.org/downloads/)

Then clone this repository by open a terminal and typing:
```shell
git clone https://github.com/BorjaRuizReverter/BasicSentimentAnalysis.git
```

And move to the repository folder cloned:
```shell
cd BasicSentimentAnalysis
```

Finally, install the required packages:
```shell
pip install -r requirements.txt
```
# Run
Once all the above have been installed, run the script by typing this if the SO is Linux
```shell
python3 script.py
```
or this if it is Windows
```shell
python script.py
```