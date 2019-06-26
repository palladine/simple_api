def get_error_by_code(code):
    errors = {
        701: "no request method POST",
        711: "no api method",
    }
    return errors.get(code, '')