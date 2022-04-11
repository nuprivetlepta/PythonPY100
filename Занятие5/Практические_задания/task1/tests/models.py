
def is_win(field: list[list]) -> bool:
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for win_comb in win_combinations:
        cell_1, cell_2, cell_3 = win_comb

        cell_1 = get_cell(field,
                          row_index=cell_1_coord[0],
                          col_index=cell_1_coord[1])
        cell_2 = get_cell(field,
                          cell_2_coord[0], cell_2_coord[1])
        cell_3 = get_cell(field,
                          cell_3_coord[0], cell_3_coord[1])

        if cell_1 == cell_2 == cell_3 != EMPTY_SYMBOL:
            return True

    return False