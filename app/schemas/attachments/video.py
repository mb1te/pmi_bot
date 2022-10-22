from pydantic import BaseModel


class Frame(BaseModel):
    height: int
    width: int
    url: str


class Cover(Frame):
    with_padding: int


class Like(BaseModel):
    count: int
    user_likes: int


class Repost(BaseModel):
    count: int
    wall_count: int
    mail_count: int
    user_reposted: int


class Video(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str
    duration: int
    image: Cover
    first_frame: list[Frame]
    date: int
    adding_date: int
    views: int
    local_views: int
    comments: int
    player: str
    platform: str
    can_add: int
    is_private: int
    access_key: str
    processing: int
    is_favorite: int
    can_comment: int
    can_edit: int
    can_like: int
    can_repost: int
    can_subscribe: int
    can_add_to_faves: int
    can_attach_link: int
    width: int
    height: int
    user_id: int
    converting: int
    added: int
    is_subscribed: int
    repeat: int
    type: str
    balance: int
    live_status: str
    live: int
    upcoming: int
    spectators: int
    likes: Like
    reposts: Repost
