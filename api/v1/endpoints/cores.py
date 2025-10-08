from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.cores_models import CoresModel
from schemas.cores_schemas import CorSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CorSchema)
async def post_cor(cor: CorSchema, db: AsyncSession = Depends(get_session)):

    nova_cor = CoresModel(nome=cor.nome, hex=cor.hex, red=cor.red, green=cor.green, blue=cor.blue)

    db.add(nova_cor)
    await db.commit()

    return nova_cor

@router.get("/", response_model=List[CorSchema])
async def get_cores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CoresModel)
        result = await session.execute(query)
        cores: List[CoresModel] = result.scalars().all()

        return cores
    
@router.get("/{cor_id}", response_model=CorSchema, status_code=status.HTTP_200_OK)
async def get_cor(cor_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CoresModel).filter(CoresModel.id == cor_id)
        result = await session.execute(query)
        cor = result.scalar_one_or_none()

        if cor:
            return cor
        else:
            raise HTTPException(details="Cor não encontrada", status_code=status.HTTP_404_NOT_FOUND)
        
@router.put("/{cor_id}", response_model=CorSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_cor(cor_id: int, cor: CorSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CoresModel).filter(CoresModel.id == cor_id)
        result = await session.execute(query)
        cor_up = result.scalar_one_or_none()

        if cor_up:
            cor_up.nome = cor.nome
            cor_up.hex = cor.hex
            cor_up.red = cor.red
            cor_up.green = cor.green
            cor_up.blue = cor.blue

            await session.commit()
            return cor_up
        else:
            raise HTTPException(details="Cor não encontrada", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{cor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cor(cor_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CoresModel).filter(CoresModel.id == cor_id)
        result = await session.execute(query)
        cor_del = result.scalar_one_or_none()

        if cor_del:
            await session.delete(cor_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(details="Cor não encontrada", status_code=status.HTTP_404_NOT_FOUND)
        