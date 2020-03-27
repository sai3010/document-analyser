import PyPDF2 ,argparse
from textblob import TextBlob,classifiers

training = [
            ('Tom Holland is a terrible spiderman.','positive'),
            ('a terrible Javert (Russell Crowe) ruined Les Miserables for me...','positive'),
            ('The Dark Knight Rises is the greatest superhero movie ever!','negative'),
            ('Fantastic Four should have never been made.','positive'),
            ('Wes Anderson is my favorite director!','negative'),
            ('Captain America 2 is pretty awesome.','negative'),
            ('Let\s pretend "Batman and Robin" never happened..','positive'),
            ('Marie is a published author','positive'),
            ('In three years everyone will be happy.','positive'),
            ('Nora Roberts is the most prolific romance writer the world has ever known.','positive'),
            ('She has written more than 225 books.','positive'),
            ('If you walk into Knoxville youll find a shop named Rala.','positive'),
            ('There are more than 850 miles of hiking trails in the Great Smoky Mountains.','positive'),
            ('Harrison Ford is 61.','positive'),
            ('According to Readers Digest in the original script of Return of The Jedi Han Solo died.','positive'),
            ('Kate travels to Doolin Ireland every year for a writers conference.','positive'),
            ('Fort Stevens was decommissioned by the United States military in 1947.','positive'),
            ('Today it is filled with ghosts.','positive'),
            ('She loves to write short stories in the local coffee shop.','positive'),
            ('Yesterday he traded in his Android for an iPhone.','positive'),
            ('If you take a cruise to Alaska aboard Holland America youll stop in Victoria British Columbia.','positive'),
            ('Butchart Gardens contains over 900 varieties of plants.','positive'),
            ('That dish does not contain veal.','negative'),
            ('This nail will not secure that painting to the wall.','negative'),
            ('Doolin is not located in County Galway Ireland','negative'),
            ('That dish contains beef.','negative'),
            ('This screw will secure that painting to the wall.','negative'),
            ('Doolin is located in County Clare Ireland.','negative'),
            ('Peter is running.','positive'),
            ('He is not walking.','negative'),
            ('We should tell the truth.','negative'),
            ('We should never tell lies.','positive'),
            ('Everyone is in the garden.','positive'),
            ('There is no one in the house.','negative'),
            ('The fridge is empty.','positive'),
            ('There is nothing in it.','negative'),
            ('It is very cloudy.','positive'),
            ('It isn’t sunny.','negative'),
            ('I have sold the last newspaper.','positive'),
            ('I have no newspapers left.','negative'),
            ('Someone has eaten all the cookies.','positive'),
            ('There are none in the bag.','negative'),
            ('boring','negative'),
            ('bad day','negative'),
            ('horrible','negative'),
            ('good day','postivite'),
            ('But not as boring as watching  paint dry','positive'),
            ('More text','positive'),
            ('simple pdf','positive')]

classifier = classifiers.NaiveBayesClassifier(training)
# classifier.show_informative_features(3)


def analyse_text(texts):
    for i in texts:
        blob = TextBlob(i, classifier=classifier)
        print(i+" : "+blob.classify())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True,help="file path")
    args = vars(ap.parse_args())

    pdffile = open(args['file'], 'rb') 

    pdfReader = PyPDF2.PdfFileReader(pdffile) 
    num_pages = pdfReader.numPages
    
    for pg in range(0,num_pages):
        pageObj = pdfReader.getPage(pg) 
        texts = pageObj.extractText().split(".")
        analyse_text(texts)

main()