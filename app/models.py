class Highlights:
    '''
    Highlights class to define highlights Objects
    '''

    def __init__(self, id, author, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Source:
    
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


