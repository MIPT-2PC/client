import connexion
import six

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server import util


def get_result():  # noqa: E501
    """returns calculated with 2PC result

    Returns the result of computation on config with A &amp; B inputs # noqa: E501


    :rtype: List[Answer]
    """
    return 'do some magic!'


def init(input_number=None, config=None):  # noqa: E501
    """Init call to start 2PC process.

    Consumes input data for this user and config location # noqa: E501

    :param input_number: 
    :type input_number: int
    :param config: 
    :type config: strstr

    :rtype: None
    """
    return 'do some magic!'
