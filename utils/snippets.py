from models.snippets import snippets_table
from models.database import database as db
from shemas import snippets
from LLM import get_answer
async def load_snippet(snippet: snippets.CreateSnippet):
    query = (
        snippets_table.insert()
        .values(
            user_id=snippet.user_id,
            language=snippet.language,
            snippet_text=snippet.snippet_text
        )
    )
    return await db.fetch_one(query)
async def comment_snippet(snippet: snippets.CommentSnippet):
    query = (
        snippets_table.update()
        .where(
            snippets_table.c.snippet_id == snippet.snippet_id,
            snippets_table.c.user_id == snippet.user_id
        )
        .values(
            snippet_text=get_answer(snippet.snippet_text),
        )
    )
    post = await db.fetch_one(query)
    return post
async def get_snippet(snippet_id: int, user_id: str):
    query = (
        snippets_table.select()
        .where(
            snippets_table.c.snippet_id == snippet_id,
            snippets_table.c.user_id == user_id
        )
    )
    get = await db.fetch_one(query)
    return get

async def get_all_user_snippets(user_id: str):
    query = (
        snippets_table.select()
        .where(
            snippets_table.c.user_id == user_id,
        )
    )
    get = await db.fetch_one(query)
    return get










