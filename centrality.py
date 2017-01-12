from neo4j.v1 import GraphDatabase, basic_auth
import csv

def calculateDegreeCentrality(session):
	degrees = session.run("MATCH (c:Deneme) RETURN c.fullName, size( (c)-[:relation_x]-() ) AS degree ORDER BY degree DESC")
	for degree in degrees:
		print degree[0],"=", degree[1]

def main(session):
	calculateDegreeCentrality(session)
	

if __name__ == '__main__':
	driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "123456"))
	session = driver.session()
	main(session)
	session.close()