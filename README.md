# Tipworthy - A Dynamic Content Recommender

Tipworthy is a text content recommender designed for users of the social media microtransaction site ChangeTip. ChangeTip users on Reddit reward interesting/creative posts or comments with micropayments. The Tipworthy algorithm looks at those tipped posts and determines user preferences. By matching these preferences against incoming documents, Tipworthy can make content recommendations in real time against new data.

# Note

This algorithm is designed and intended for ChangeTip. It is maintained here as an example of a dynamic recommender using topic modeling, but at ChangeTip's request, will not be updated as the project continues. For any questions or concerns, please feel free to email me at nimish.patil@gmail.com

# The Algorithm

Tipworthy relies on the Latent Dirichlet Allocation topic modeling algorithm. The LDA is trained against previously tipped comments to construct a set of topics. Once those topics have been built out, the LDA determines topic distributions for every tipped comment. These topic distributions are percentages of the document that match to each topic. By matching a document's topic distributions to the users that tipped the document, weighting by the amount tipped, and normalizing against the number of tipped documents, Tipworthy can construct a user affinity list for every user. This affinity list approximates the ideal topic distribution for every user. By comparing each incoming document's topic distribution using Euclidean distance, a final recommendation can be determined for every incoming document.
