from api.models import Author, Book

def getbooks(data):
    return data

def getauthors(data):
    all_authors = Author.objects.all()

    namelst = [x.name for x in all_authors]
    idlst = [x.pk for x in all_authors]
    elements = zip(idlst, namelst)

    response = list()
    keys_response = ('id', 'name')
    for element in elements:
        response.append(dict(zip(keys_response, element)))

    return response
