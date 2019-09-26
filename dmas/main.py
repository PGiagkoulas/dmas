import sys
import argparse
from cmd import Cmd
# User defined Imports ugly python import syntax >:(
sys.path.append('./')
import environment

parser = argparse.ArgumentParser(description='Run a simulation')
parser.add_argument('--n_agents', type=int, default=10, help='Give the number of agents of the network.')
parser.add_argument('--n_liars', type=int, default=1, help='Give the number of liars of the network.')
parser.add_argument('--n_experts', type=int, default=1, help='Give the number of experts of the network.')
parser.add_argument('--n_connections', type=int, default=3, help='Give the number of connections in the network.')
parser.add_argument('--n_news', type=int, default=1, help='Give the number of news in the network.')
parser.add_argument('--n_steps', type=int, default=50, help='Give the number of steps of the simulation.')

args = parser.parse_args()

def main():
    if not len(sys.argv) > 1:
        MyPrompt().cmdloop()
    else:
        network = environment.Environment(args.n_agents, args.n_liars, args.n_experts,
                                          args.n_connections, args.n_news, args.n_steps)
        network.run_simulation()


class MyPrompt(Cmd):
    prompt = 'dmas> '
    intro = """
        Welcome! The default parameter values are: \n
        n_agents: 10 
        n_liars: 1 
        n_experts: 1  
        n_connections: 3 
        n_news: 1 
        n_steps: 50 \n
        If you want to start the simulation with these values enter 'start'. 
        Otherwise change values by entering '{parameter} {value}' and then enter 'start'.
        Enter '?' for an overview over all commands.
        """

    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True

    def do_n_agents(self, inp):
        '''Change the number of agents. Must be an integer larger than 0'''
        try:
            inp = int(inp)
            if inp > 0:
                args.n_agents = inp
                print("Setting number of agents to '{}'".format(inp))
            else:
                raise ValueError
        except:
            print("Wrong input type, please enter an integer larger than 0")


    def do_n_liars(self, inp):
        '''Change the number of liars. Must be an integer larger than 0'''
        try:
            inp = int(inp)
            if inp > 0:
                args.n_liars = inp
                print("Setting number of liars to '{}'".format(inp))
            else:
                raise ValueError
        except:
            print("Wrong input type, please enter an integer larger than 0")

    def do_n_experts(self, inp):
        '''Change the number of experts. Must be an integer larger than 0'''
        try:
            inp = int(inp)
            if inp > 0:
                args.n_experts = inp
                print("Setting number of experts to '{}'".format(inp))
            else:
                raise ValueError
        except:
            print("Wrong input type, please enter an integer larger than 0")

    def do_n_connections(self, inp):
        '''Change the number of connections. Must be an integer larger than 0'''
        try:
            inp = int(inp)
            if inp > 0:
                args.n_connections = inp
                print("Setting number of connections to '{}'".format(inp))
            else:
                raise ValueError
        except:
            print("Wrong input type, please enter an integer larger than 0")

    def do_n_news(self, inp):
        '''Change the number of news. Must be an integer larger than 0'''
        try:
            inp = int(inp)
            if inp > 0:
                args.n_news = inp
                print("Setting number of news to '{}'".format(inp))
            else:
                raise ValueError
        except:
            print("Wrong input type, please enter an integer larger than 0")

    def do_n_steps(self, inp):
        '''Change the number of steps. Must be an integer larger than 0'''
        try:
            inp = int(inp)
            if inp > 0:
                args.n_steps = inp
                print("Setting number of steps to '{}'".format(inp))
            else:
                raise ValueError
        except:
            print("Wrong input type, please enter an integer larger than 0")

    def do_show_values(self, inp):
        '''Shows the current value of each parameter'''
        text = """
               The current parameter values are: \n
               n_agents: %s 
               n_liars: %s 
               n_experts: %s 
               n_connections: %s
               n_news: %s
               n_steps: %s 
               """
        print(text %(args.n_agents, args.n_liars, args.n_experts,args.n_connections, args.n_news, args.n_steps))

    def do_show_description(self, inp):
        '''Shows a description of the program and how the simulation works'''
        text = """
                This is a project on the spread of fake news in a social network created in the scope of the course 
                'Design of Multi-Agent Systems'.
                Authors: Panagiotis, Anton, Manvi, Daniel
               """
        #todo: write better description
        print(text)

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        if inp == 'c' or inp == 'start':
            network = environment.Environment(args.n_agents, args.n_liars, args.n_experts,
                                              args.n_connections, args.n_news, args.n_steps)
            network.run_simulation()
        if inp == 'show_values':
            self.do_show_values()
        if inp == 'show_description':
            self.do_show_description()

if __name__ == "__main__":
    main()