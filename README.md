# Catch'em All: A Pokemon Type Classifier
This is a Pokemon type classifier using a TensorFlow convolutional neural network (CNN).
As it stands, this classifier is optimized to work with Generations I-VII including mega
evolutions, and future updates will add Gen VIII and Alolan Forms. 

![Gotta Catch'em All](https://i.kym-cdn.com/entries/icons/mobile/000/028/484/raw.jpg)

Given the nature of Pokemon type classification, this classification problem is largely motivated by color, 
though physical feature-mapping will likely play a role as well. Stay tuned for an updated
Jupyter notebook with filter visualizations.<br/>

The data was augmented by way of several transformations available in the sci-kit image library
to help make up for the relatively small amount of existing sampling data. Special shout-out to
Thomas Himblot for providing us with a framework for the augmentation script!

Created by: Marc Chmielewski, Andrew Sander, and Yi Chen (Duke, 2022)
