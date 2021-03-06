from naive_bayes import NaiveBayes
from generate_feature import Features
import sys

if __name__ == '__main__':
    filename = sys.argv[1]    
    distribution = "Gaussian"
    if len(sys.argv) > 2:
        distribution = sys.argv[2]
    Feature_vector = Features()
    folder = "../data/annotated_output"
    xmlfolder = "../data/tagged"    
    Feature_vector.run(folder, xmlfolder)
    NB = NaiveBayes(Feature_vector.feature_values, 0.8, distribution, True)
    NB.train()
    NB.getSummary(filename)

