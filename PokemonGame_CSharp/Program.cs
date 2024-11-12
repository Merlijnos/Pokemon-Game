class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Welcome to the Pokemon Battle Simulator!");

        Console.Write("Please enter a name for the first Trainer: ");
        Trainer trainer1 = new Trainer(Console.ReadLine());

        Console.Write("Please enter a name for the second Trainer: ");
        Trainer trainer2 = new Trainer(Console.ReadLine());

        Battle battle = new Battle(trainer1, trainer2);
        Arena arena = new Arena(battle);
        arena.StartBattle();

        Console.Write("Type 'quit' to exit or 'restart' to start a new game: ");
        string command = Console.ReadLine();
        if (command.ToLower() == "quit")
        {
            Console.WriteLine("Thank you for playing the Pokemon Battle Simulator!");
        }
        else if (command.ToLower() == "restart")
        {
            Main(args);
        }
    }
}
