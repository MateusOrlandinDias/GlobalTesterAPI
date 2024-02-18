from fastapi import FastAPI

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
        "status": "access pending"
    }