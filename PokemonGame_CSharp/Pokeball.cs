public class Pokeball
{
    public Pokemon Pokemon { get; }
    public bool IsActive { get; private set; }

    public Pokeball(Pokemon pokemon)
    {
        Pokemon = pokemon;
        IsActive = false;
    }

    public void Throw()
    {
        IsActive = true;
        Pokemon.BattleCry();
    }

    public void Return()
    {
        IsActive = false;
    }
}
