def create_section(name: str, url: str) -> dict:
    """
    Helper function to create a section dictionary.

    Parameters:
    - name (str): The name of the section.
    - url (str): The URL associated with the section.

    Returns:
    dict: Section dictionary.
    """
    return {'name': name, 'url': url}


def create_menu_item(id: int, name: str, icon: str, url: str, sections: list = None) -> dict:
    """
    Helper function to create a menu item dictionary.

    Parameters:
    - id (int): The unique identifier for the menu item.
    - name (str): The name of the menu item.
    - icon (str): The icon associated with the menu item.
    - url (str): The URL associated with the menu item.
    - sections (List[Dict[str, str]]): Optional list of sections under the menu item.

    Returns:
    dict: Menu item dictionary.
    """
    menu_item = {'id': id, 'name': name, 'icon': icon, 'url': url}
    if sections:
        menu_item['sections'] = sections
    return menu_item


def sidebar_data(active_id: int = 1) -> dict:
    """
    Generates sidebar data with optional highlighting of the active menu item.

    Parameters:
    - active_id (int): The ID of the active menu item. Default is 1.

    Returns:
    dict: Sidebar data dictionary.
    """
    data = dict(
        general=[
            create_menu_item(
                id=1, name='Dashboard', icon='bi bi-grid', url='dashboard'
            ),
            create_menu_item(
                id=2, name='Sales', icon='bi bi-speedometer2', url=None, sections=[create_section('Alert', 'dashboard')]
            ),
            create_menu_item(
                id=3, name='Product Management', icon='bi bi-cart3', url=None, sections=[create_section('Alert', 'dashboard')]
            ),
            create_menu_item(
                id=4, name='Inventory Management', icon='bi bi-shield-plus', url=None, sections=[create_section('Alert', 'dashboard')]
            ),
            create_menu_item(
                id=5, name='Customer Management', icon='bi bi-people', url=None, sections=[create_section('Alert', 'dashboard')]
            ),
            create_menu_item(
                id=6, name='Wallet', icon='bi bi-wallet2', url='dashboard'
            ),
            create_menu_item(
                id=7, name='Subscription', icon='bi bi-credit-card', url='dashboard'
            ),
            create_menu_item(
                id=8, name='Reports', icon='bi bi-journal-medical', url=None, sections=[create_section('Alert', 'dashboard')]
            ),
        ],
        pages=[
            create_menu_item(
                id=9, name='Profile', icon='bi bi-person', url='profile'
            ),
        ]
    )

    for menu_item in data['general'] + data['pages']:
        menu_item['collapsed'] = menu_item['id'] != active_id
    
    return data
