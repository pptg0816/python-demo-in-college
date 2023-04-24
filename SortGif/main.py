import Bubble
import Quick
import DirectSelection

def RunSort(n):
    Bubble.RunBubble(n)
    DirectSelection.RunDiectSelection(n)
    Quick.RunQuick(n)


if __name__ == '__main__':
    RunSort(20)
