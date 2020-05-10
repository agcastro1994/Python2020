import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json
import time
import os.path


def main(args):
    sigo_jugando = True
    while sigo_jugando:

        layout = [[sg.Text('Elegí con qué juego querés jugar:')],
                  [sg.Text('1 - Ahorcado')],
                  [sg.Text('2 - Tic-tac-toe')],
                  [sg.Text('3 - Otello')],
                  [sg.Text('Elegí a que juego querés jugar:')],
                  [sg.Input(key='Game')],
                  [sg.Text('Escribe tu nombr de jugador')],
                  [sg.Input(key='Player')],
                  [sg.Button('Start'), sg.Exit()]]
        window = sg.Window('Juegos', layout)
        event, values = window.Read()
        now = time.strftime("%c")
        window.close()

        if event == 'Start':
            opcion = values['Game']
            if opcion == '1':
                game = 'Hangman'
                hangman.main()
            elif opcion == '2':
                game = 'Tic-Tac-Toe'
                tictactoeModificado.main()
            elif opcion == '3':
                game = 'Otello'
                reversegam.main()
            data = {}
            new_data = {now: {'Jugador': values['Player'], 'Juego': game}}
            if os.path.isfile('juegos.json'):
                with open("juegos.json", "r+") as file:
                    data = json.load(file)
                    data.update(new_data)
                    file.seek(0)
                    print(data)
                    json.dump(data, file)
            else:
                with open("juegos.json", "w") as file:
                    data.update(new_data)
                    json.dump(data, file)

        else:
            sigo_jugando = False


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
