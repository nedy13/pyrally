from pyrally.models import Story, Defect
from pyrally.rally_access import get_accessor


class RallyAPIClient(object):

    def __init__(self, username, password):
        self.rally_access = get_accessor(username, password)

    def get_all_in_kanban_state(self, kanban_state):
        """
        Get all stories and defects in the given ``kanban_state``.

        :param kanban_state:
            The kanban state to search for.

        :returns:
            A dictionary containing keys for ``stories`` and ``defects``, and
            values of lists of associated ``Story`` and ``Defect`` objects.
        """
        stories = Story.get_all_in_kanban_state(kanban_state)
        defects = Defect.get_all_in_kanban_state(kanban_state)
        return {'stories': stories, 'defects': defects}

