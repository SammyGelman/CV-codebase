# CV-codebase

Hello, if you are reading this you are most likely a prospective employeer looking to know more about the code I've written in the past.

This is a random assortment of code I've written over the last couple of years. 

The repository is broken up into a few directories. This includes the main languages I've written in: Python and Julia were used for my research and I wrote in C++ as a way to practice writing in a strongly typed language. 

There are two other small projects included. 

Simply haiku was an art project related to a twitter account I have where I have written nearly 1000 haiku. 
The idea was to use the text from the poems I had written and use them as the input for a text-to-image software. 
This was done before DALLE-2 stepped into the scene and instead I used a (in my humble opion and no judgement) slightly worse open source algorithm call VQGAN.
The text for the poems were pulled using the twitter API and various meta-data points were pulled (my friend wanted to turn the poem-image pairs into NFTs). 
Unfourtunaly the project never fully took off on the NFT end but I did gather the meta data and generated the images on a GPU. The art was enjoyed by personally and by family and friends. 

The other project was something I put together as a means to convince a company to hire me. It worked and they took me on the team with the condition to pay me in the event they secured funding. Unfortunatley the company never managed to get the funding but I very much enjoyed the work I did for them after getting hired, though that work is proprietary. 
This project was an implementation of the circle Hough Transform algorithm to recognize circles of variable sizes. 
I worte a script to generate the sample data which consisted of two dimentional matrices with a variable number of pixelated circles and rectangles of variable size and in variable location. 
I wrote a script to gauge the accuracy of the algorithm tagging the image data with the number of circles present and comparing that to the algorithms guess. I also had the system draw an outline around the edges of the circles guessed. 
The algorithm preformed at managed to successfully identify <99.8% of circles. 
