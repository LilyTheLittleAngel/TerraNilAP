using Global;
using HarmonyLib;
using Utils;

namespace TerraNilAP;

[HarmonyPatch(typeof(CampaignStateManager), "StartNewGameFromMenu")]
class NewGamePatch
{
    public static bool Prefix(CampaignStateManager __instance)
    {
        MonoSingleton<LoadingScreenManager>.Instance.LoadCampaignState(new LoadingScreenManager.LoadOperationData
        {
            LoadOperation = LoadingScreenManager.LoadOperation.LoadWorldMap,
            PlayerProfileState = __instance.PlayerProfileState,
            GameState = null,
            FinishedLevel = false,
            IsEndGame = false
        });
        return false;
    }
}
