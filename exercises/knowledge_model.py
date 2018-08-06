from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
   __tablename__ = 'Topics my friends want to learn'
   Knowledge_id = Column(Integer, primary_key=True)
   Topic_name = Column(String)
   Small_description= Column(String)
   Rating=Column(Integer)

   def __repr__(self):
   	return("Knowledge Topic_name: {}\n"
   		"Knowledge Small_description: {}\n"
   		"Knowledge Rating: {}").format(
   		self.Topic_name,
   		self. Small_description,
   		self.Rating)
   	print(repr(Knowledge.__table__))
    
x = Knowledge(Topic_name="Biochemistry", Small_description="the study of chemical processes within and relating to living organisms", Rating=10)
print(x)



