# Rows = [[Column(s)],...,[Column(s)]]
# Column = {"content" : "", "alignment" : ""}


def generate_ui(rows):
    max_width = 0
    for row in rows:
        current_width = 0
        for column in row:
                current_width = len(column["content"]) + 3
        if current_width > max_width:
            max_width = current_width
    
    ui_block = []
    for row in rows:
        ui_block.append(generate_row(row,max_width))
    return ui_block

def generate_row(row,width):
    column_width = width // len(row)
    output = "|"
    for column in row:
        output += generate_column(column,column_width)
    if width % len(row) != 0:
        output = output[:-1] + " |"


def generate_column(column):
    pass