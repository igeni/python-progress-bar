from dataclasses import dataclass


class Font:
    Black = '\033[030m'
    Red = '\033[031m'
    Green = '\033[032m'
    Yellow = '\033[033m'
    Blue = '\033[034m'
    Purple = '\033[035m'
    Cyan = '\033[036m'
    LightRed = '\033[091m'
    LightGreen = '\033[092m'
    LightYellow = '\033[093m'
    LightBlue = '\033[094m'
    LightPurple = '\033[095m'
    LightCyan = '\033[096m'
    White = '\033[097m'
    Bold = '\033[1m'
    Underline = '\033[4m'
    Non = '\033[0m'


@dataclass
class FontScheme:
    Title: Font
    Bar: Font
    Percentage: Font


class ProgressBar:
    def __init__(self, title: str, bar_lenght: int = 50, bar_char: str = '#', val_max: float = 100.0, font_scheme: FontScheme = None):
        self.title = title
        self.bar_lenght = bar_lenght
        self.bar_char = bar_char
        self.val_max = val_max
        self.font_scheme = font_scheme

    def show(self, val_current: float):
        val_current = 100.0 if val_current > 100.0 else val_current
        val_current = 0.0 if val_current < 0.0 else val_current
        fnt = FontScheme(Font.White, Font.White, Font.White) if self.font_scheme is None else self.font_scheme
        pos = val_current / self.val_max
        bar = self.bar_char * int(pos * self.bar_lenght)
        bar_line = f"{bar: <{self.bar_lenght}}"
        res = f"{Font.Bold}{fnt.Title}{self.title} {Font.Non} |{fnt.Bar}{bar_line}{Font.Non}| {fnt.Percentage}{100.0 * pos:.2f}%{Font.Non}"
        print(res, end='\r')


def main():
    # print("-= Regular progress bar =-")
    pb = ProgressBar('#1')
    pb.show(17.0)
    print('\n')

    # print("-= Progress bar with unicode symbol =-")
    pb = ProgressBar('#2', bar_char='█')
    pb.show(35.0)
    print('\n')

    # print("-= Progress bar with unicode symbol =-")
    pb = ProgressBar('#3', bar_char='▷')
    pb.show(42.0)
    print('\n')

    # print('-= Colored progress bar with unicode symbols =-')
    fnts = FontScheme(Title=Font.LightPurple, Bar=Font.Yellow, Percentage=Font.LightGreen)
    pb = ProgressBar('#4', bar_char='★', font_scheme=fnts)
    pb.show(97.5)
    print('\n')


if __name__ == '__main__':
    main()
