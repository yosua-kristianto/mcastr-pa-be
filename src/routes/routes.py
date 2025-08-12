from fastapi import APIRouter;

route = APIRouter(prefix = "/api");

from core_service.src.main.api.parking.parking_controller import ParkingController;

route.include_router(ParkingController.router, prefix="/v1/parking");