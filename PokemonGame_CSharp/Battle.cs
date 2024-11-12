public class Battle
{
    public Trainer Trainer1 { get; set; }
    public Trainer Trainer2 { get; set; }

    public Battle(Trainer trainer1, Trainer trainer2)
    {
        Trainer1 = trainer1;
        Trainer2 = trainer2;
    }

    public string FightRound()
    {
        Trainer1.ThrowPokeball();
        Trainer2.ThrowPokeball();

        var pokemon1 = Trainer1.ActivePokeball.Pokemon;
        var pokemon2 = Trainer2.ActivePokeball.Pokemon;

        if (pokemon1.Strength == pokemon2.Weakness)
        {
            Trainer2.ReturnPokemon();
            Trainer1.IncreaseCount();
            return $"{Trainer1.Name}'s {pokemon1.Nickname} wins the round!";
        }
        else if (pokemon2.Strength == pokemon1.Weakness)
        {
            Trainer1.ReturnPokemon();
            Trainer2.IncreaseCount();
            return $"{Trainer2.Name}'s {pokemon2.Nickname} wins the round!";
        }
        else
        {
            // If neither Pokemon has a strength that is the other's weakness, decide the winner based on a predefined type advantage order
            if ((pokemon1.Strength == ElementType.Fire && pokemon2.Strength == ElementType.Grass) ||
                (pokemon1.Strength == ElementType.Grass && pokemon2.Strength == ElementType.Water) ||
                (pokemon1.Strength == ElementType.Water && pokemon2.Strength == ElementType.Fire))
            {
                Trainer2.ReturnPokemon();
                return $"{Trainer1.Name}'s {pokemon1.Nickname} wins the round!";
            }
            else
            {
                Trainer1.ReturnPokemon();
                return $"{Trainer2.Name}'s {pokemon2.Nickname} wins the round!";
            }
        }
    }

  public string FightBattle()
{
    int rounds = 0;
    try
    {
        while (Trainer1.Count > 0 && Trainer2.Count > 0)
        {
            Console.WriteLine(FightRound());
            rounds++;
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }

    if (Trainer1.Count > 0 && Trainer2.Count > 0)
    {
        return $"The battle is a draw after {rounds} rounds!";
    }
    else if (Trainer1.Count == 0)
    {
        return $"{Trainer2.Name} wins the battle after {rounds} rounds!";
    }
    else
    {
        return $"{Trainer1.Name} wins the battle after {rounds} rounds!";
    }
}
}
