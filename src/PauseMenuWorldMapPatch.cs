using HarmonyLib;
using Menus;
using System.Reflection;
using UnityEngine.UI;

namespace TerraNilAP;

[HarmonyPatch(typeof(PauseMenu), "Show")]
class PauseMenuWorldMapPatch
{
    public static void Postfix(PauseMenu __instance)
    {
        TerraNilAP.Logger.LogInfo("Enabling WorldMap Button");
        var btn = (Button) __instance
            .GetType()
            .GetField("returnToWorldMapButton", BindingFlags.Instance | BindingFlags.NonPublic)
            .GetValue(__instance);
        btn.gameObject.SetActive(true);
    }
}
