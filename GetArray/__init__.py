import logging
import json
import random
import decimal

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    itemcount = req.params.get('itemcount')
    if not itemcount:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('itemcount')

    if itemcount:
        line_items=[]
        i = 0
        while (i < int(itemcount)):

            myjson3 = {
                        'ItemCode': random.randint(1000, 9999),
                        'UnitAmount': str(decimal.Decimal(random.randrange(155, 389))/100),
                        'Quantity': random.randint(1,50)
                    }
            line_items.append(myjson3)
            i = i +1

        return func.HttpResponse(
             json.dumps(line_items),
             status_code=200
        )        
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
