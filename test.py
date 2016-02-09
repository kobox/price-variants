def draw_menu(options, selected_index):
    for counter, option in enumerate(options):
        if counter == selected_index:
            print " [*] %s" % option
        else:
            print " [ ] %s" % option

options = ['Option 0', 'Option 1', 'Option 2', 'Option 3']
draw_menu(options, 2)