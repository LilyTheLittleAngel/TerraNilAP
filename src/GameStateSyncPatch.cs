using HarmonyLib;
using Model.State;

namespace TerraNilAP;

[HarmonyPatch(typeof(GameState), "ExecuteCommand")]
class GameStateSyncPatch
{
    public static void Postfix(GameState __instance)
    {
        var logic = TerraNilAP.MissionLogic.GetValueSafe(__instance.missionKey);
        if (logic != null)
        {
            logic.Update(__instance);
        }
    }
}
