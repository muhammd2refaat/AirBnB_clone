#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, *arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program.")

    def do_EOF(self, *arg):
        """EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
