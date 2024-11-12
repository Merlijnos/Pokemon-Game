public class Trainer
{
    public string Name { get; }
    public List<Pokeball> Belt { get; }
    public Pokeball ActivePokeball { get; private set; }
    public int Count { get; private set; }
    private const int NumberOfPokeballs = 6;

    public Trainer(string name)
    {
        Name = name;
        Belt = new List<Pokeball>();
        for (int i = 0; i < NumberOfPokeballs / 3; i++)
        {
            Belt.Add(new Pokeball(new Charmander($"Charmander {i + 1}")));
            Belt.Add(new Pokeball(new Squirtle($"Squirtle {i + 1}")));
            Belt.Add(new Pokeball(new Bulbasaur($"Bulbasaur {i + 1}")));
        }
        Count = Belt.Count;
    }

    public void ThrowPokeball()
    {
        var availablePokeballs = Belt.Where(p => p.Pokemon != null && p.IsActive == false).ToList();
        if (!availablePokeballs.Any())
        {
            throw new Exception("No more Pokemons in Pokeballs!");
        }

        var random = new Random();
        var randomPokeball = availablePokeballs[random.Next(availablePokeballs.Count)];

        ActivePokeball = randomPokeball;
        randomPokeball.Throw();
        Count--;
    }

    public void ReturnPokemon()
    {
        if (ActivePokeball != null && ActivePokeball.Pokemon != null)
        {
            ActivePokeball.Return();
            ActivePokeball = null;
        }
    }

    public void IncreaseCount()
    {
        Count++;
    }
}
