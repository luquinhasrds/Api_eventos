import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()



@pytest.mark.skip(reason="novo registro em banco de dados")
def test_insert_events():
    event = {
        "uuid": "meu-uuid-e-nois2333",
        "title": "meu-title",
        "slug": "meu-slug-aqui!221",
        "maximum_attendees": 20
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)




def test_get_event_by_id():
    event_id = "meu-uuid-e-nois21615"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
    #print(response.title)