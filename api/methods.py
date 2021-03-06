from api.models import Author, Book


def getbooks(data):
    params =dict()

    all_books = Book.objects.all()
    params.update({'count': all_books.count()})

    idlst = [x.pk for x in all_books]
    namelst = [x.name for x in all_books]
    authorlst = [x.author.name for x in all_books]


    elements = zip(idlst, namelst, authorlst)

    response = list()
    keys_response = ('id', 'name', 'author')

    for element in elements:
        response.append(dict(zip(keys_response, element)))

    return response, params


def getauthors(data):
    params=dict()
    all_authors = Author.objects.all()

    params.update({'count': all_authors.count()})

    idlst = [x.pk for x in all_authors]
    namelst = [x.name for x in all_authors]

    elements = zip(idlst, namelst)

    response = list()
    keys_response = ('id', 'name')
    for element in elements:
        response.append(dict(zip(keys_response, element)))

    return response, params


def getbookinfo(data):
    # id - список
    id = data.get('id')
    if not id:
        return {'code': 712}

    params =dict()
    filter_books = Book.objects.filter(pk__in=id)

    params.update({'count': filter_books.count()})

    idlst = [x.pk for x in filter_books]
    namelst = [x.name for x in filter_books]
    authorlst = [x.author.name for x in filter_books]
    yearlst = [x.year for x in filter_books]

    elements = zip(idlst, namelst, authorlst, yearlst)

    response = list()
    keys_response = ('id', 'name', 'author', 'year')

    for element in elements:
        response.append(dict(zip(keys_response, element)))

    return response, params

