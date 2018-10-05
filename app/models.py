class News:
    '''
     class to define news Objects
    '''

    def __init__(self, id, author, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Sources:
    
    #sources class to define source objects


    def __init__(self, id, title, description, url, category, country):
        self.id = id
        self.title = title
        self.description = description
        self.link = url
        self.type = category
        self.place = country

class Articles:
        
    #categories class to define category objects
    

    def __init__(self, id, title, description, url, urlToImage, publishedAt):
        self.id =id 
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


