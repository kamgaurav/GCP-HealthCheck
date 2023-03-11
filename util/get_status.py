import requests
from models.status_model import Status_Model

url = "https://status.cloud.google.com/incidents.json"
req = requests.get(url, verify = False)


statuses = req.json()
def Get_Status(Location: str):
    response= []
    for status in statuses:
            for i in range(len(status["most_recent_update"]["affected_locations"])):
                if status["most_recent_update"]["affected_locations"][i]["id"] == Location:
                    if status["status_impact"] == "SERVICE_DISRUPTION" or status["status_impact"] == "SERVICE_OUTAGE":
                        response += [{
                            "Service_Name": status["service_name"],
                            "Status_Impact": status["status_impact"],
                            "Description": status["external_desc"],
                            "Location": status["most_recent_update"]["affected_locations"][i]["title"],
                            "Most_Recent_Update": status["most_recent_update"]["text"],
                            "Begin": status["begin"], 
                            "End": status["end"]
                }]           
    return Status_Model(statusses=response)