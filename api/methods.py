from api.models import Author, Book


def getbooks(data):
    all_books = Book.objects.all()

    idlst = [x.pk for x in all_books]
    namelst = [x.name for x in all_books]
    authorlst = [x.author.name for x in all_books]
    yearlst = [x.year for x in all_books]

    elements = zip(idlst, namelst, authorlst, yearlst)

    response = list()
    keys_response = ('id', 'name', 'author', 'year')

    for element in elements:
        response.append(dict(zip(keys_response, element)))

    return response



def getauthors(data):
    all_authors = Author.objects.all()

    idlst = [x.pk for x in all_authors]
    namelst = [x.name for x in all_authors]

    elements = zip(idlst, namelst)

    response = list()
    keys_response = ('id', 'name')
    for element in elements:
        response.append(dict(zip(keys_response, element)))

    return response
