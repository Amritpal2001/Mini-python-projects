from wordcloud import WordCloud,STOPWORDS
from PIL import Image
import numpy

# getting .txt file in read mode
file=open(r"word cloud.txt")
# the contents of file are stored in file_contents as string
file_contents=file.read()

# function to get word cloud
def get_cloud(file_contents):

# masking the png file
    mask = numpy.array(Image.open("brain.png"))

# stopwords are sets of all those commonly used words (such as “the”, “a”, “an”, “in”). They are used to remove all these words from our text.
    stopwords = set(STOPWORDS)

# cloud object is made from WordCloud class providing all the necessary attributes
    cloud = WordCloud(mask=mask, background_color="white", stopwords=stopwords).generate(file_contents)

# Next the cloud object is converted to a png file and saved
    cloud.to_file("Word Cloud(Light).png")

# calling the get_cloud function
get_cloud(file_contents)
file.close()




