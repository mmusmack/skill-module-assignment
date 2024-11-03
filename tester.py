import ui_generator

test_ui_base = [
    [{"content" : "Test UI", "alignment" : "center"}],
    [{"content" : "Left Column", "alignment" : "left"},{"content" : "Right Column", "alignment" : "right"}]
]


ui_block = ui_generator.generate_ui(test_ui_base)
ui_generator.display_ui(ui_block)