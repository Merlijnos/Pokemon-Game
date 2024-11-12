public enum ElementType
{
    Fire,
    Water,
    Grass
}

public abstract class Pokemon
{
    public string Nickname { get; }
    public ElementType Strength { get; }
    public ElementType Weakness { get; }

    protected Pokemon(string nickname, ElementType strength, ElementType weakness)
    {
        Nickname = nickname;
        Strength = strength;
        Weakness = weakness;
    }

    public abstract void BattleCry();
}

public class Charmander : Pokemon
{
    public Charmander(string nickname) : base(nickname, ElementType.Fire, ElementType.Water)
    {
    }

    public override void BattleCry()
    {
        Console.WriteLine($"{Nickname}!");
    }
}

public class Squirtle : Pokemon
{
    public Squirtle(string nickname) : base(nickname, ElementType.Water, ElementType.Grass)
    {
    }

    public override void BattleCry()
    {
        Console.WriteLine($"{Nickname}!");
    }
}

public class Bulbasaur : Pokemon
{
    public Bulbasaur(string nickname) : base(nickname, ElementType.Grass, ElementType.Fire)
    {
    }

    public override void BattleCry()
    {
        Console.WriteLine($"{Nickname}!");
    }
}
