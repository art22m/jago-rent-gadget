from fastapi import Request, HTTPException
from firebase_admin import auth


async def validate_firebase(request: Request):
    """
    Validate that the request is authenticated by Firebase Auth.
    """
    id_token = request.headers.get("Authorization")
    if not id_token:
        raise HTTPException(
            status_code=400, detail="Authorization token must be provided"
        )

    try:
        user = auth.verify_id_token(id_token)
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
