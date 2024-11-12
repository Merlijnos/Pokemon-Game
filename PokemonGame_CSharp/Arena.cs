public class Arena
{
    public Battle CurrentBattle { get; set; }
    public static int TotalRounds { get; private set; }
    public static int TotalBattles { get; private set; }

    public Arena(Battle battle)
    {
        CurrentBattle = battle;
    }

    public void StartBattle()
    {
        Console.WriteLine(CurrentBattle.FightBattle());
        TotalBattles++;
    }

    public static void UpdateScoreboard(int rounds)
    {
        TotalRounds += rounds;
    }
}
