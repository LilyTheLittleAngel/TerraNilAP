using Data;
using Global;
using HarmonyLib;
using Model.State;
using System.Collections.Generic;
using System.Reflection;

namespace TerraNilAP;

[HarmonyPatch(typeof(CampaignStateManager), "StartMission")]
class StartMissionPatch
{
    public static void Postfix(CampaignStateManager __instance)
    {
        __instance.PlayerProfileState.metaProgressState.unlockedBuildings = new List<Model.Type>();
        var missionData = (MissionData) typeof(ProgressionState).GetField("_missionData", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(__instance.GameState.progressionState);
        missionData.toForceUnlockWhenMissionStarts = [];
        missionData.toForceUnlockWhenTier2Starts = [];
        missionData.toForceUnlockWhenTier3Starts = [];
    }
}
