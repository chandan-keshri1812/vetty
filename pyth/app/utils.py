
def paginate(data, page_num, per_page):
    """
    Paginates the given data.
    :param data: List of items to paginate.
    :param page_num: Page number (1-based index).
    :param per_page: Number of items per page.
    :return: Paginated subset of data.
    """
    start = (page_num - 1) * per_page
    end = start + per_page
    return data[start:end]