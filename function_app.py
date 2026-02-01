import logging
import requests
import azure.functions as func
from azure.identity import DefaultAzureCredential

app = func.FunctionApp()

SUBSCRIPTION_ID = "a0d28a25-e125-4177-a7ea-3b53011e5878"
RESOURCE_GROUP = "rg-data-dev"
FACTORY_NAME = "adf-pk-data-platform-dev"
PIPELINE_NAME = "pl_raw_to_processed"

@app.event_grid_trigger(arg_name="event")
def onBlobCreated(event: func.EventGridEvent):
    logging.info("Blob created event received")

    file_name = event.subject.split("/")[-1]
    logging.info(f"Processing file: {file_name}")

    credential = DefaultAzureCredential()
    token = credential.get_token("https://management.azure.com/.default").token

    url = (
        f"https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}"
        f"/resourceGroups/{RESOURCE_GROUP}"
        f"/providers/Microsoft.DataFactory/factories/{FACTORY_NAME}"
        f"/pipelines/{PIPELINE_NAME}/createRun?api-version=2018-06-01"
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    body = {
        "parameters": {
            "fileName": file_name
        }
    }

    response = requests.post(url, headers=headers, json=body)
    logging.info(f"ADF trigger status: {response.status_code}")
