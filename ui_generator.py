# Rows = [[Column(s)],...,[Column(s)]]
# Column = {"content" : "", "alignment" : ""}

def display_ui(ui_block):
    for line in ui_block:
        print(line)

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
    return output


def generate_column(column,width):
    padding_space = width - len(column["content"])
    padding = ""
    if column["alignment"] == "left":
        for _ in range(padding_space):
            padding += " "
        output = " " + column["content"] + padding + " |"
    if column["alignment"] == "right":
        for _ in range(padding_space):
            padding += " "
        output = " " + padding + column["content"] + " |"
    if column["alignment"] == "center":
        for _ in range(padding_space // 2):
            padding += " "
        output = " " + padding + column["content"] + padding + " |"
        if padding_space % 2 != 0:
            output = output[:-1] + " |"
    return output