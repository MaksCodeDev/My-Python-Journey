def sandwich_show(*components):
    """Выводит список компонентов бутерброда"""
    for component in components:
        print(f"описание - {component}")

sandwich_show('бекон', 'капуста', 'сыр', 'хлеб', 'помидор')

sandwich_show('сыр', 'огурец', 'масло')

sandwich_show('бекон')