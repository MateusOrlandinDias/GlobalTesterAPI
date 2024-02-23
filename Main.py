from fastapi import FastAPI
from Testers import servicenow

app = FastAPI()

@app.get("/sap-logon")
def sap_logon():

    return {
        "status": "full access"
        }

@app.get("/sql-server")
def sql_server():
    return {
        "status": "partial access"
        }

@app.get("/servicenow")
def servicenow():
    return {
        "status": "access pending",
        "testUi": {
            "login": "success",
            "navigatePageReports":"error"
        }
    }