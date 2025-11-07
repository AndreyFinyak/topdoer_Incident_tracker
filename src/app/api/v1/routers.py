from fastapi import APIRouter, Depends, HTTPException, status, Path

from app.schemas import (
    IncidentCreate,
    IncidentRead,
    IncidentStatusUpdate,
    IncidentStatus
)
from app.infrastructure.db.repository import IncidentRepository


router = APIRouter(prefix="/api/v1")


@router.post(
    "/incident/",
    response_model=IncidentRead,
    status_code=status.HTTP_201_CREATED
)
async def create_incident(
    inc: IncidentCreate = Depends(),
    inc_repo: IncidentRepository = Depends(IncidentRepository)
):
    return await inc_repo.create(inc)


@router.get("/incidents/", response_model=list[IncidentRead])
async def get_incidents_by_status(
    status: IncidentStatus,
    inc_repo: IncidentRepository = Depends(IncidentRepository)
):
    return await inc_repo.get_all_by_status(status)


@router.patch("/incidents/{incident_id}/status", response_model=IncidentRead)
async def patch_status(
    payload: IncidentStatus,
    incident_id: int = Path(..., ge=0),
    inc_repo: IncidentRepository = Depends(IncidentRepository)
):
    inc_update = IncidentStatusUpdate(
        id=incident_id,
        status=payload
    )
    respones = await inc_repo.update_status_by_id(inc_update)
    if respones is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incident with id={incident_id} not found"
        )
    return respones
