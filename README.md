# Guitar Automatic Playing Techniques Classification [Gaptec]
W.X.Li; J.L.Lyu; J.S.Lyu; H.Peng; Y.D.Wang; Y.D.Zhu
## Problem:
The use of various instrumental techniques is essential in instrumental performances. For guitar playing, there are
various fingering styles and playing techniques such as pull-off, hammer-on or bending.[ 1-3] Different techniques
could achieve entirely different performances. So for every novice guitar player, they may need to learn and
proficient specific playing techniques. Similar to some online autograder, a tool recording guitar playing note by
note and recognizing the matching degree of different playing techniques can undoubtedly enhance the
interactivity of guitar learning experience.[ 4] The creativity of our project is that current research mainly focus on
feature extraction with signal processing methods, while we try to adopt machine learning methods to enhance the
classification performance for more general use in future. Therefore, comparing and developing suitable machine
learning algorithm that can classify the playing techniques of guitar music accurately is one of the most crucial
technique cores we should focus on. [5]
## Hypothesis: 
Neural Networks has the best performance among all the ML methods on this topic.
## Draft of proposed solution : . [5]
1. K-nearest neighbors (Unsupervised)
(1) According to dataset, divide it into 7 classes (2) High accuracy, not sensitive to outlier
2. SVM (Supervised)
(1) Soft margin (allow some deviation) (2) Kernel (higher-dimension projection)
3. Neural Network (S & U)
(1) Layers: A single layer contains two parts, the activation part and linear transformation part.
(2) Training: Pass the x through all layers in forward pass. Pass δ through all layers in backward pass.
(3) Error: Put the test set into a forward pass then we can get the prediction by the Neural Network.
4. Decision tree (Supervised)
Make binary classification for each node, simple calculation, easy to understand and explanatory.
## Experimental Steps:
1. Deal with the data: The audio signal is pre-processed in order to reduce the dimension and pick up dominant
features for each sample. [6] For the processed dataset, use a split 80% train, 10% holdout and 10% test.
2. Build different classification models: Adopt different machine learning methods mentioned above.
3. Comparison and summary: Compare and evaluate in the aspect of algorithm accuracy and efficiency. Analyze
the comparison result and give a summary review as well as future suggestion.
Dataset:
A database consisting of 6580 clips across 7 frequently used playing techniques and 7 different tones.
Download from http://mac.citi.sinica.edu.tw/GuitarTranscription/
Proposal - Group 10 W.X.Li; J.L.Lyu; J.S.Lyu; H.Peng; Y.D.Wang; Y.D.Zhu
## Reference:
1. Barbancho, A. M., Klapuri, A., Tardón, L. J., & Barbancho, I. (2012). Automatic transcription of guitar
chords and fingering from audio. IEEE Transactions on Audio, Speech, and Language Processing, 20( 3),
915-921.
2. Scaringella, N., Zoia, G., & Mlynek, D. (2006). Automatic genre classification of music content: a survey.
IEEE Signal Processing Magazine , 23 (2), 133-141.
3. Creme, M., Burlin, C., & Lenain, R. (2016). Music genre classification.
4. Benetos, E., Dixon, S., Giannoulis, D., Kirchhoff, H., & Klapuri, A. (2013). Automatic music
transcription: challenges and future directions. Journal of Intelligent Information Systems , 41 (3), 407-434.
5. Chathuranga, Y. M. D., & Jayaratne, K. L. (2018). Automatic music genre classification of audio signals
with machine learning approaches. GSTF Journal on Computing (JoC) , 3 (2).
6. Reboursière, L., Lähdeoja, O., Drugman, T., Dupont, S., Picard-Limpens, C., & Riche, N. (2012, May).
Left and right-hand guitar playing techniques detection. In NIME .
7. Su, L., Yu, L. F., & Yang, Y. H. (2014, October). Sparse Cepstral, Phase Codes for Guitar Playing
Technique Classification. In ISMIR (pp. 9-14).
8. Murthy, Y. V., & Koolagudi, S. G. (2018). Content-Based Music Information Retrieval (CB-MIR) and Its
Applications toward the Music Industry: A Review. ACM Computing Surveys (CSUR) , 51 (3), 45.
9. Lasseck, M. (2018). Audio-based bird species identification with deep convolutional neural networks.
Working Notes of CLEF , 2018 .
10. Lartillot, O., & Toiviainen, P. (2007, September). A Matlab toolbox for musical feature extraction from
audio. In International conference on digital audio effects (pp. 237-244).
11. Nam, J., Herrera, J., Slaney, M., & Smith, J. O. (2012, October). Learning Sparse Feature Representations
for Music Annotation and Retrieval. In ISMIR (pp. 565-570).
