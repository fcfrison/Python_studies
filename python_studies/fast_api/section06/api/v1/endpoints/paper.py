from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.deps import get_session, get_current_user
from models.papers_model import PaperModel
from models.user_model import UserModel
from schemas.papers_schema import PaperSchema

router = APIRouter()

# POST paper
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=PaperSchema)
async def post_paper(paper:PaperSchema,
                    user:UserModel=Depends(get_current_user),
                    db:AsyncSession=Depends(get_session)):
    new_paper = PaperModel(title=paper.title,description=paper.description,
                            url=paper.url,user_id=user.id)
    db.add(new_paper) #unsert data to the db
    await db.commit() #commit 
    return new_paper # response_model is PaperSchema

# GET papers
@router.get('/',response_model=List[PaperSchema])
async def get_papers(db:AsyncSession=Depends(get_session)):
    '''
    This coroutine query all papers.
    '''
    async with db as session: # opens a db session
        query = select(PaperModel) # select all data from the table 'papers'
        result = await session.execute(query)
        papers: List[PaperModel] = result.scalars().unique().all()
        return papers

# GET paper
@router.get('/{paper_id}',response_model=PaperSchema,
            status_code=status.HTTP_200_OK)
async def get_paper(paper_id:int, db:AsyncSession=Depends(get_session)):
    '''
    This coroutine query a paper.
    '''
    async with db as session:
        query = select(PaperModel).filter(PaperModel.id==paper_id)
        result = await session.execute(query)
        paper = result.scalars().unique().one_or_none() # brings back one row or none
        if paper:
            return paper
        else:
            raise HTTPException(detail="Paper not found.",
                                status_code=status.HTTP_404_NOT_FOUND)

# PUT paper
@router.put('/{paper_id}',response_model=PaperSchema,status_code=
            status.HTTP_202_ACCEPTED)
async def put_paper(paper_id:int, paper:PaperSchema,
                    db:AsyncSession=Depends(get_session),
                    user:UserModel=Depends(get_current_user)):
    '''
    This coroutine update a paper.
    '''      
    async with db as session:
        query = select(PaperSchema).filter(PaperSchema.id==paper_id)
        result = await session.execute(query)
        paper_update = result.scalars().unique().one_or_none() # brings back one row or none
        if paper_update: # if the course was found, then update.
            if user.id!=paper_update.id:
                raise HTTPException(detail="User cannot update.",
                                status_code=status.HTTP_401_UNAUTHORIZED) 
            if paper_update.title:
                paper_update.title = paper.title
            if paper_update.description:
                paper_update.description = paper.description
            if paper_update.url:
                paper_update.url = paper.url
            await session.commit()
            return paper_update
        else:
            raise HTTPException(detail="Paper not found.",
                                status_code=status.HTTP_404_NOT_FOUND)

# DELETE paper
@router.delete('/{paper_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_paper(paper_id:int, db:AsyncSession=Depends(get_session),
                       user:UserModel=Depends(get_current_user)):
    '''
    This coroutine update a paper.
    '''      
    async with db as session:
        query = (select(PaperSchema).filter(PaperSchema.id==paper_id)
                .filter(PaperSchema.user_id==user.id))
        result = await session.execute(query)
        paper_delete = result.scalars().unique().one_or_none() # brings back one row or none
        if paper_delete: # if the course was found, then update.
            await session.delete(paper_delete)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Paper not found.",
                                status_code=status.HTTP_404_NOT_FOUND)