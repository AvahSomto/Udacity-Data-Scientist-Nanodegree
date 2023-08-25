### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The libaries used for this project is python 3.7 and above, sklearn, keras, numpy, glob, random, sys, os, cv2, matplotlib, IPython, tqdm, the platform was Udacity Workspace. The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

For this project, I created an algorithm to identify an estimate of a canine's breed when given an image of a dog, If supplied an image of a human, the algorithm will identify the resembling dog breed.

1. What percentage of the first 100 images in human_files have a detected human face?
2. What percentage of the first 100 images in dog_files have a detected human face?
3. Should we communicate to the user that we accept human images only when they provide a clear view of a face (otherwise, we risk having 
   unneccessarily frustrated users!). Is this a reasonable expectation to pose on the user? If not, can you think of a way to detect 
   humans in images that does not necessitate an image with a clearly presented face?
4. What percentage of the images in human_files_short have a detected dog?
5. What percentage of the images in dog_files_short have a detected dog?
6. Outline the steps you took to get to your final CNN architecture and your reasoning at each step. If you chose to use the hinted 
   architecture above, describe why you think that CNN architecture should work well for the image classification task.
7. Outline the steps you took to get to your final CNN architecture and your reasoning at each step. Describe why you think the architecture is suitable for the current problem.
8. Is the output better than you expected :) ? Or worse :( ? Provide at least three possible points of improvement for your algorithm.
   

## File Descriptions <a name="files"></a>

There is only one notebook available here to showcase work related to the above questions.  The notebook is exploratory in searching through the data pertaining to the questions showcased by the notebook title.  Markdown cells were used for code clarification.  

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/@avahsomto042/unleashing-the-power-of-cnn-building-an-algorithm-for-a-dog-identification-app-ffcc3c82310d)


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Thanks to Kaggle and Udacity for the data and the starter code.
