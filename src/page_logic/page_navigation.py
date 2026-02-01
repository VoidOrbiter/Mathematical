page_history = []

def update_ui(main_window):
    if hasattr(main_window, 'back_action'):
        main_window.back_action.setEnabled(len(page_history) > 0)

def switch_to_page(caller, target_class, record_history=True):
    main_window = caller.window()
    
    if not hasattr(main_window, 'stack'):
        return

    stack = main_window.stack
    current_widget = stack.currentWidget()
    
    if isinstance(current_widget, target_class):
        return

    for i in range(stack.count()):
        widget = stack.widget(i)
        if isinstance(widget, target_class):
            if record_history and current_widget:
                page_history.append(current_widget.__class__)
            
            stack.setCurrentWidget(widget)
            update_ui(main_window)
            return

def go_back(caller):
    if page_history:
        prev_page_class = page_history.pop()
        switch_to_page(caller, prev_page_class, record_history=False)
        
        update_ui(caller.window())

def jump_home(caller):
    global page_history
    
    from src.pages.main_menu import MainMenu
    
    page_history = []
    switch_to_page(caller, MainMenu, record_history=False)
    update_ui(caller.window())