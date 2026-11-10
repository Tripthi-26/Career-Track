# CareerTrack REST API

Authentication uses the normal Flask login session.

## Applications
- GET `/api/applications`
- POST `/api/applications`
- GET `/api/applications/<id>`
- PUT `/api/applications/<id>`
- DELETE `/api/applications/<id>`

## Matching
POST `/api/match`

Example:
```json
{"resume_id":1,"job_description":"Python Flask PostgreSQL Docker REST API"}
```
