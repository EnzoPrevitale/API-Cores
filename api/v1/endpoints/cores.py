from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.cores_models import BandasModel
from schemas.cores_schemas import BandaSchema
from core.deps import get_session