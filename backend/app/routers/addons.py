from fastapi import APIRouter
router=APIRouter()
@router.get('/')
def list_addons(): return {}
