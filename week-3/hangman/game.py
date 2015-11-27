class HangMan(object):
    def __init__(self, answer):
        self.answer = answer
        self.letter = ''
        self.progress= list('-' * len(answer))

    hits = ''
    misses = set([])
    max_misses = 6

    def guess(self, letter):
        self.letter = input('enter a letter: ')
        if self.letter in self.answer:
            self.hits += self.letter
        else:
            self.misses.add(self.letter)

    def update_progress(self, letter):
        for i in range(len(self.answer)):
            if letter == self.answer[i]:
                self.progress[i] = letter
        return self.progress

    def display_progress(self):
        print('You have %d guesses remaining to solve: %s' % (self.remaining(), ''.join(self.progress)))

    def remaining(self):
        return self.max_misses - len(self.misses)

    def play(self):
        while self.has_guesses() and not self.is_win():
            self.guess(self.letter)
            if self.letter in self.progress:
                print('%s is already been guessed!' % self.letter)
            self.update_progress(self.letter)
            self.display_progress()
        if self.remaining() == 0:
            print('You lose!\nThe answer was %s...' % self.answer)
        elif self.is_win():
            print('--->>>>You are awesome. You broke this unbrakeable puzzle!!!!!!!')

    def is_win(self):
        return self.progress == list(self.answer)

    def has_guesses(self):
        return self.remaining() > 0


game = HangMan('levendula')
game.play()
game.remaining()
