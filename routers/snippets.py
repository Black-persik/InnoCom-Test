from fastapi import APIRouter
from sqlalchemy import UUID

import utils.snippets as snippet_utils
from shemas import snippets as snippet_shema
from fastapi import HTTPException



router = APIRouter()

@router.post("/load-snippet", status_code=201, response_model=snippet_shema.CreateSnippet)
async def load_snippet(snippet: snippet_shema.CreateSnippet):
    return await snippet_utils.load_snippet(snippet)

@router.post("/comment_snippet", status_code=200)
async def comment_snippet(snippet: snippet_shema.CommentSnippet):
    return await snippet_utils.comment_snippet(snippet)

@router.get("/get-snippet/{user_id}/{snippet_id}", status_code=200)
async def get_snippet(snippet_id: int, user_id: str):
    return await snippet_utils.get_snippet(snippet_id, user_id)

@router.get("/get-all-snippets/{user_id}", status_code=200)
async def get_all_snippets(user_id: str):
    return await snippet_utils.get_all_user_snippets(user_id)