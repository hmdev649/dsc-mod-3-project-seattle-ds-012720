### Summary of the business problem:
Background:</br>
As streaming has taken over the music industry, streaming services have discovered that there is a massive market for indpendent and smaller acts.  These services have capitalized on this and made it possible for anyone to publish music to their platforms; artists do not need a label as a middle man any more to get their music distributed.  While this has made it much easier for independent acts to publish their work, you still have to pay fees in most cases to be uploaded to larger services (like Spotify and Apple Music).  This being the case, free streaming platforms like SoundCloud and Datpiff have paved the way as the home for aspiring musicians to post thier work.  </br>

Our Business Problem:</br> 
A small streaming services is having trouble manually genre-classifying this huge stream of  mp3s. They would like to free their team up to start improving the UX of their site due to the increase in traffic and need a basic model that can predict genres for these incoming songs.  There will still be enough staff overseeing the genre-classification process that they are comfortable with having to hand-examine songs that the model is 'unsure' of (ideally less than 10% of the incoming library).  The model would analyze the probabilites of predictions for each entry and if the model was less confident than a certain threshold, the file would be sent for human analysis.</br>

Our team is trying to build a predictive model to classify incoming mp3s based on various musical and meta data from these mp3s.  The susbset of [data](http://millionsongdataset.com/) we used for building this model comes from a study published by Coumbia University and a PDF containing more information on this data (how it was collected, how to interpret it) can be found [here](https://www.ee.columbia.edu/~dpwe/pubs/BertEWL11-msd.pdf). The exact features included in the subset we are working with can be found in in the project ReadMe, but generally speaking we generated our model based on musical elements such as key, tempo, time signature, duration etc. along with numeric reductions of the timbres in the audio files.  </br>

Our Model/Insights:</br>
We found that the variance within, and total average of the 12-channel frequencies in audio files were the most useful factors when predicting genre; along with the duration, and loudness of the track.  As timbre helps quantify the different tonal qualities in audio, this makes sense that differences in these measurements would help distinguish between different genres.  At present, our model is classifying unseen songs at between 88-90% accuracy.  After further looking into the prediction probabilities of our falsely-classified entries, we are seeing that theses entries typically have a high probability of belonging to a few different genres.  Plainly speaking, for the most part, our model was rarely fully convinced that a song was genre A when it was really genre B.  Rather, it was 20% sure it belonged to genre A, 10% for genre C and 5% sure for genre B, or something to that effect.  We are interpreting this clustering of a few higher probabilities as the model being 'unsure' and in the future we would like to be able impliment a system to track these files and output them for hand-labeling.</br>

Next Steps:</br> 
The next steps our team would take, given more time, would be Further optimization of our model would look possibly adding a more robust and streamlined approach for stripping the timbres, and maybe further exploration of other spectral data to incorporate.  We would also like to create an interface to input these audio files or their features, and some system to track the exact entries that the model was 'unsure' about.</br>

Stakeholders would be interested in the success of this model because of how much it would lighten employee workload. Employees would have more time to work on bug fixes, improving UX/UI, marketing and SEO, and even starting creative projects.  Along with freeing up time to work on emprovements to the organization, the company would save money by automating these previously manual tasks.







