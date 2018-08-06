from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(Topic_name, Small_description, Rating):
	Knowledge_object=Knowledge(
		Topic_name=Topic_name,
		Small_description= Small_description,
		Rating= Rating)
	session.add(Knowledge_object)
	session.commit()
    
add_article("Biochemistry","the study of chemical processes within and relating to living organisms", 10)
	

def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
