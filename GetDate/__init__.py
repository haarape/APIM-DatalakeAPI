import logging
from datetime import date

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    today = date.today()

    return func.HttpResponse(today)

