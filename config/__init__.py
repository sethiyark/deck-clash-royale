from utils.mongo import MongoUtils

DB = MongoUtils('deckCR')

HQ_TAG = ' GQQQY9'
VIBE_TAG = ' 2YGJ8U0Q'
INDIA_ID = '57000113'
US_ID = '57000249'

API_URL = 'https://api.clashroyale.com/v1'

API_TOKEN = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjJjNDZlZjVlLTU1ZDgtNDFmNS1iODY5LWJjMjNlYmFhZDNiYSIsImlhdCI6MTUzMzMyODAwOSwic3ViIjoiZGV2ZWxvcGVyL2VhNDQyNGQ3LTkwMDQtNTUwOS04Y2FkLTMyNjJmYjI4NzhmMCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMDMuMjU1LjIyNy4xODQiXSwidHlwZSI6ImNsaWVudCJ9XX0.HOhQkbMuZo3JFY4lGQvPiDSFnhn0OPzmvJordl08HdS2EG90KbBDIeY7JT65Etrqa5ypnR2ncNb9q_pBCan9fg'

HEADERS = {
    'authorization': API_TOKEN,
    'Accept': 'application/json'
}
