import azure.functions as func
import logging
from azure.storage.blob import BlobClient
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_snow")
def http_snow(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    blob = BlobClient(account_url="https://snowsa.blob.core.windows.net",
                  container_name="setup-files",
                  blob_name="snowurls.json",
                  credential="GCaZ1lNaBC0skg69sWNKpyy2FPO6FSVqwMKnk8JFymedgw9gHV7RZM77rf6ugx0kjvRk/PQVWXJr+AStFLycrQ==")
    basicUrl=''
    blob_content=blob.download_blob().readall()   
    fileReader = json.loads(blob_content)
    for item in fileReader:  
       if item['view_name'] == 'u_apl_dv':
          basicUrl=item['basic_url']
         
    name = req.params.get('name')
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        #return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
        return func.HttpResponse(f"{basicUrl}")
    else:
        return func.HttpResponse(f"{basicUrl}")
        #return func.HttpResponse(
            # "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             #status_code=200
        # )