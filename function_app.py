import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
@app.cosmos_db_output(arg_name="documents", database_name="my-database", container_name="my-container", create_if_not_exists=True, connection="CosmosDbConnectionSetting")
def test_function(req: func.HttpRequest, documents: func.Out[func.Document]) -> func.HttpResponse:
     logging.info('Python HTTP trigger function processed a request.')
     logging.info('Python Cosmos DB trigger function processed a request.')
     name = req.params.get('name')
     if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

     if name:
        documents.set(func.Document.from_dict({"id": name}))
        return func.HttpResponse(f"Hello {name}!")
     else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400
        )