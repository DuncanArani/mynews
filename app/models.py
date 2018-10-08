class Sources:

    '''
    Class for holding sources api
    '''

    def __init__(self, id, name, descript, url, cat):

        self. id = id
        self.name = name
        self. descript = descript
        self.url = url
        self.cat = cat


class Articles:
    '''
    Class for holding articles from everything api
    '''

    def __init__(self, id, name, author, title, description, url, image, date):

        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date
