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
	Topics= session.query(
		Knowledge).all()
      
	return Topics
print(query_all_articles())


def query_article_by_topic(tamara):
	Idk = session.query(
		Knowledge).filter_by(Topic_name=tamara).first()
	return Idk
print(query_article_by_topic("x"))


def delete_article_by_topic(IalsoDoNotKnow):
	session.query(Knowledge).filter_by(Topic_name=IalsoDoNotKnow).delete()
	session.commit()
#delete_article_by_topic("Biochemistry")

def delete_all_articles(Topic_name):
	session.query(Knowledge).delete()
	session.commit()
#delete_all_articles("Knowledge")

def edit_article_rating(article_title,updated_rating):
	potato_object=session.query(Knowledge).filter_by(Topic_name=article_title).first()
	potato_object.Rating=updated_rating
	session.commit()

edit_article_rating("Biochemistry",8)
print(query_all_articles())

