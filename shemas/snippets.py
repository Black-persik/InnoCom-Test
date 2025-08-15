from pydantic import BaseModel, UUID4

class Snippet(BaseModel):
    user_id: UUID4
    snippet_id: int
    language: str
    snippet_text: str

class CreateSnippet(BaseModel):
    user_id: UUID4
    language: str
    snippet_text: str

class CommentSnippet(BaseModel):
    snippet_id: int
    user_id: UUID4
    snippet_text: str

class GetSnippet(BaseModel):
    user_id: UUID4
    snippet_id: int