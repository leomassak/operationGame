from models.calc import Calc

def main() -> None:
    score: int = 0
    play(score)

def play(score: int) -> None:
    dificulty: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))
    calc: Calc = Calc(dificulty)

    print('Informe o resultado para a seguinte operação: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        score = score + 1
        print(f'Você tem {score} ponto(s)')

    continuar: int = int(input('Deseja continuar? [1 - Sim, 0 - Não] '))

    if continuar == 1:
        play(score)
    else:
        print(f'Você finalizou o jogo com {score} ponto(s)')

if __name__ == '__main__':
    main()