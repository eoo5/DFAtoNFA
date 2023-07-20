from sys import argv

class DFA:
    def __init__(self, states, alphabet, start_state, transitions, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.transitions = transitions
        self.accept_states = accept_states

    def read_string(self, input_str):
        curr = self.start_state

        for ch in input_str:
            curr = self.transitions[curr][ch]
        if curr in self.accept_states:
            return 'Accept'
        else:
            return 'Reject'

def main():
    fname = argv[1]

    transitions = {}
    with open(fname) as f:
        lines = f.read().splitlines()

        line_number = 0

        states_line = lines[line_number]
        states = int(states_line)
        line_number += 1

        alphabet_line = lines[line_number]
        alphabet = list(alphabet_line)
        line_number += 1

        done = False
        while not done:  # Added a colon here
            transition_line = lines[line_number]
            if len(transition_line.split()) == 3:
                transition_line = transition_line.split()
                source, symbol, dest = transition_line
                if (source, symbol) in transitions:
                    transitions[(source, symbol)].append(dest)
                else:
                    transitions[(source, symbol)] = [dest]

                source = int(source)
                dest = int(dest)
                symbol = symbol.strip("'")

                if source not in transitions:
                    transitions[source] = {}

                transitions[source][symbol] = dest
                line_number += 1
            else:
                done = True

        start_state_line = lines[line_number]
        start_state = int(start_state_line)
        line_number += 1

        accept_states_line = lines[line_number]
        accept_states = list(map(int, accept_states_line.split()))
        line_number += 1

        dfa = DFA(states, alphabet, start_state, transitions, accept_states)

        inputs = lines[line_number:]
        for input_str in inputs:
            print(dfa.read_string(input_str))

if __name__ == '__main__':
    main()
