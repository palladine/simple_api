def get_error_by_code(code):
    errors = {
        701: "no request method POST",
        702: "no such method",

        711: "no api method",
        712: "no books id list",
    }
    return errors.get(code, '')