from fastapi import APIRouter, Form, HTTPException

from app.models.user import User

router = APIRouter(prefix="/auth", tags =["auth"])

@router.post("/register")
async def register(
    username: str = Form(...), 
    password: str = Form(...), 
    device_id: str = Form(...)
):
    
    existed_device = db.query(User).filter(User.devise_id == device_id)
    if existed_device: 
        raise HTTPException(status_code=400, detail= "Устройство уже зарегистрировано")

    user = User(
    username = username,
    password = password,
    divice_id = device_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"user_id": user.id, 
            "username": user.username}


