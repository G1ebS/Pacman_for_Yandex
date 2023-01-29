import sys
from PyQt5.QtWidgets import QApplication
from classes.pygame_menus.start_game import start
from classes.Pyqt_menus.new_record import Records
from classes.pygame_menus.game_over_menu import game_over_screen
from classes.pygame_menus.run import run_game
from classes.Pyqt_menus.settings import Settings
from classes.Pyqt_menus.leeader_board import LeaderBoard
from classes.pygame_menus.map_editor_start import start as start_map_editor


'''
The main program in the code
'''


run = True
comand_in_game_over_menu = 'menu'
app = QApplication(sys.argv)
while run:
    if comand_in_game_over_menu == 'menu':
        comand_in_start_menu = start()
        if comand_in_start_menu == 'exit':
            break
        elif comand_in_start_menu == 'settings':
            settings = Settings()
            settings.show()
            app.exec_()
        elif comand_in_start_menu == 'leaderboard':
            leaderboard = LeaderBoard()
            leaderboard.show()
            app.exec_()
        elif comand_in_start_menu == 'editor':
            arr = start_map_editor()
            if arr:
                run_game(arr)

        elif comand_in_start_menu == 'game':
            stats = run_game()
            comand_in_game_over_menu = game_over_screen()
            if comand_in_game_over_menu == 'stop':
                break
    elif comand_in_game_over_menu == 'retry':
        stats = run_game()
        comand_in_game_over_menu = game_over_screen()
        if comand_in_game_over_menu == 'stop':
            break
    elif comand_in_game_over_menu == 'record':
        records = Records(stats)
        records.show()
        app.exec_()
        comand_in_game_over_menu = game_over_screen()
        if comand_in_game_over_menu == 'stop':
            break
