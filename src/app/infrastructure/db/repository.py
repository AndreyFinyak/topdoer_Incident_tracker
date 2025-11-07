from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.database import connection
from app.infrastructure.db.models import IncidentORM, IncidentStatus
from app.schemas import (
    IncidentCreate,
    IncidentRead,
    IncidentStatusUpdate
)


class IncidentRepository:

    @connection
    async def get_by_id_or_none(
        self,
        id: int,
        session: AsyncSession,
    ) -> IncidentRead | None:
        query = await session.execute(
            select(IncidentORM)
            .where(IncidentORM.id == id)
        )
        row = query.scalar_one_or_none()

        if row is None:
            return None

        return IncidentRead(
            id=row.id,
            body=row.body,
            status=row.status,
            source=row.source
        )

    @connection
    async def create(
        self,
        incident_dto: IncidentCreate,
        session: AsyncSession,
    ) -> IncidentRead:
        new_incedent = IncidentORM(
            body=incident_dto.body,
            source=incident_dto.source
        )
        session.add(new_incedent)

        await session.flush()
        await session.commit()
        await session.refresh(new_incedent)

        return IncidentRead(
            id=new_incedent.id,
            body=new_incedent.body,
            status=new_incedent.status,
            source=new_incedent.source
        )

    @connection
    async def update(
        self,
        id: int,
        session: AsyncSession,
        **kw
    ) -> None:
        await session.execute(
            update(IncidentORM)
            .where(IncidentORM.id == id)
            .values(
                kwargs=kw
            )
        )
        await session.commit()

        return None

    @connection
    async def update_status_by_id(
        self,
        inc: IncidentStatusUpdate,
        session: AsyncSession
    ) -> IncidentRead | None:
        await session.execute(
            update(IncidentORM)
            .where(IncidentORM.id == inc.id)
            .values(status=inc.status)
        )
        await session.commit()

        updated_obj = await session.get(IncidentORM, inc.id)
        if not updated_obj:
            return None

        return IncidentRead(
            id=updated_obj.id,
            body=updated_obj.body,
            status=updated_obj.status,
            source=updated_obj.source
        )

    @connection
    async def get_all_by_status(
        self,
        status: IncidentStatus,
        session: AsyncSession
    ) -> list[IncidentRead]:
        query = await session.execute(
            select(IncidentORM)
            .filter_by(status=status)
        )
        objs = query.scalars().all()

        result = []
        for obj in objs:
            veiw_objs = IncidentRead(
                id=obj.id,
                body=obj.body,
                status=obj.status,
                source=obj.source
            )
            result.append(veiw_objs)

        return result
