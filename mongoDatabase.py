from pymongo import MongoClient

# client = MongoClient()
client = MongoClient("localhost",27017)
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
db.Information.drop()
coll = db["Information"]

coll.insert([
		{"street":"1225 North King Street", "city":"Wilmington", "state":"Delaware 19801", "country":"United States" , 
			"description" : "Wilmington (Lenape: Paxahakink, Pakehakink[2]) is the largest city in the state of Delaware, United States, built on the site of Fort Christina, the first Swedish settlement in North America. It is located at the confluence of the Christina River and Brandywine River, near where the Christina flows into the Delaware River. It is the county seat of New Castle County and one of the major cities in the Delaware Valley metropolitan area. Wilmington was named by Proprietor Thomas Penn after his friend Spencer Compton, Earl of Wilmington, who was prime minister in the reign of George II of Great Britain.", 
			"image" : "1.jpg", "solution" : "Virtual Mailroom"},
		{"street":"1225 North King Street", "city":"Wilmington", "state":"Delaware 19801", "country":"United States" ,
			 "description" : "As of the 2015 United States Census estimate, the population of the city is 71,958, reflecting an increase of 1.5 from the 2010 Census.[3] The Delaware Valley metropolitan area, which includes the cities of Philadelphia, Pennsylvania, and Camden, New Jersey, had a 2015 population of 6,069,875, and a combined statistical area of 7,183,479. [4][5]", 
			 "image" : "2.jpg", "solution" : "Virtual Business Address"},
		{"street":"1225 North King Street", "city":"Wilmington", "state":"Delaware 19801", "country":"United States" ,
			 "description" : "The Renaissance Center in Detroit, Michigan, as viewed from across the Detroit River. Designed by John Portman and completed in 1977, this complex initially consisted of a five-tower rosette rising from a common base; two further towers were added in 1981. The central tower, measuring 73 floors in height, is the tallest building in Michigan. Since 1996, the complex has been owned by General Motors and used as its world headquarters; the complex also houses a shopping center, hotel, restaurants, brokerage firms, and banks.", 
			 "image" : "3.jpg", "solution" : "Mail & Packaging Forward"},
		{"street":"610 C Street", "city":"Marysville", "state":"California 95901", "country":"United States",
			"description" : "The fundamental principles by which Wikipedia operates are the five pillars. The Wikipedia community has developed many policies and guidelines to improve the encyclopedia; however, it is not a formal requirement to be familiar with them before contributing.", 
			"image" : "4.jpg", "solution" : "Virtual Mailroom"},
		{"street":"610 C Street", "city":"Marysville", "state":"California 95901", "country":"United States",
			"description" : "Marysville was established in 1872 as a trading post by James P. Comeford, but was not populated by other settlers until 1883. After the town was platted in 1885, a period of growth brought new buildings and industries to Marysville. In 1891, Marysville was incorporated and welcomed the completed Great Northern Railway. Historically, the area has subsisted on lumber and agrarian products; the growth of strawberry fields in Marysville led to the city being nicknamed the Strawberry City in the 1920s.",
			"image" : "5.jpg", "solution" : "Virtual Business Address"},
		{"street":"610 C Street", "city":"Marysville", "state":"California 95901", "country":"United States",
			"description" : "The city underwent rapid suburbanization in the 1970s and 1980s, resulting in the replacement of older buildings and businesses with chain establishments and construction of new housing. Between 1980 and 2000, the population of Marysville increased five-fold. In the early 2000s, annexations of unincorporated areas to the north and east expanded the city to over 20 square miles (52 km2) and brought the population over 60,000.", 
			"image" : "6.jpg", "solution" : "Mail & Packaging Forward"}
	])

