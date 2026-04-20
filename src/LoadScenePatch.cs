using Global;
using HarmonyLib;
using WorldMap;

namespace TerraNilAP;

[HarmonyPatch(typeof(LoadingScreenManager), "LoadScene")]
class LoadScenePatch
{
    public static bool Prefix(object[] __args)
    {
        WorldMapSceneHandler.WonLastLevel = false;
        return true;
    }
}
