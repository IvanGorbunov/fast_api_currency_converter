from fastapi import APIRouter

from .currency.views import router as currency_router


router = APIRouter()
router.include_router(router=currency_router, prefix="/currencies")
